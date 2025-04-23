---
title: "DIY Containers: Building a Lightweight Container System from Scratch on Linux"
date: 2025-04-23
draft: false
author: "Sumit Patel"
tags: ["containers", "linux"] 
description: "We are going to implement a minimal container system from scratch on Linux"
cover: "/container-from-scratch.png"
---

In today's cloud-native world, containers have revolutionized how we deploy and manage applications. While Docker and Kubernetes dominate the landscape, understanding what's happening under the hood can be valuable. This blog post will guide you through building a minimalist container system from scratch using Linux's namespaces and other kernel features.

## What Are Containers, Really?

At their core, containers are just processes running with isolation features provided by the Linux kernel. Unlike virtual machines, containers don't need a separate OS kernel - they share the host's kernel while maintaining isolation through several key technologies:

- **Namespaces**: Provide isolation for system resources
- **Control Groups (cgroups)**: Limit and account for resource usage
- **Chroot**: Change the root directory for a process
- **Mount Points**: Control what filesystems are visible

## Before we begin

Before jumping to the code, you need a filesystem for your container. You can create one from a base distribution:

```bash
# Create a directory for your rootfs
mkdir -p mycontainer/rootfs

# Use debootstrap to create a minimal Debian system
sudo debootstrap --variant=minbase bullseye containers/mycontainerr/rootfs

# OR Download the Arch Linux rootfs
curl -O https://mirrors.edge.kernel.org/archlinux/iso/latest/archlinux-bootstrap-x86_64.tar.zst
sudo tar xf archlinux-bootstrap-x86_64.tar.zst -C mycontainer/rootfs --strip-components=1 

# OR Alpine (Lightweight)
wget https://dl-cdn.alpinelinux.org/alpine/v3.14/releases/x86_64/alpine-minirootfs-3.14.0-x86_64.tar.gz
tar -xzf alpine-minirootfs-3.14.0-x86_64.tar.gz -C containers/mycontainerr/rootfs
```

The `rootfs` is a directory containing the root filesystem of our container. It contains the necessary files and directories to run a basic system.

## Let's begin

We'll start with the necessary includes and definitions, yes we are doing it in c :)

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mount.h>
#include <sys/wait.h>
#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>

#define STACK_SIZE (1024 * 1024)
static char child_stack[STACK_SIZE];

char *child_args[] = { "/bin/sh", NULL };
```

These includes provide access to necessary system calls for creating our container. We also define a stack size for our container process and set up the default command to run inside our container (`/bin/sh`).
If you know docker that last line should be familiar to you.

## Creating the Container Process

Next, we need to define what happens inside our container. The `child_main` function will be executed inside the container namespace:

```c
int child_main(void *arg) {
    // Set container hostname
    sethostname("minicontainer", 10);
    
    // ... more container setup to come
    
    return 1;
}
```

### Setting the Hostname

The first step in our container setup is to set a hostname. This is important because it helps identify the container environment:

```c
sethostname("minicontainer", 10);
```

This sets the hostname to "container" with a maximum length of 10 characters. The hostname is isolated because we're using the `CLONE_NEWUTS` namespace flag when creating the container.

### Changing Root Directory

Now, we need to isolate the filesystem by changing the root directory using `chroot()`:

```c
if (chroot("/path/to/mycontainer/rootfs") != 0 || chdir("/") != 0) {
    perror("chroot/chdir");
    return 1;
}
```

This changes the root directory to "/path/to/mycontainer/rootfs" and let us in there. After changing the root, we also change the current directory to the new root with `chdir("/")`.
If you still wonder what roofs directory is then you can think it as a OS image.

### Setting Up /proc Filesystem

To ensure our container has access to process information (the thing we do using `ps` command), we need to mount a `/proc` filesystem:

```c
// Make sure /proc exists
mkdir("/proc", 0555);

// Mount /proc
if (mount("proc", "/proc", "proc", 0, "") != 0) {
    perror("mount /proc");
    return 1;
}
```

First, we create the `/proc` directory with appropriate permissions (if it doesn't already exist). Then we mount the proc filesystem, which gives processes in the container access to information about running processes within **their namespace**.
This namespace creates the isolation.

### Executing the Container Command

Finally, we execute the command that will run inside our container:

```c
// Execute shell
execv(child_args[0], child_args);
perror("exec");
return 1;
```

This replaces the current process with the specified command (by default, `/bin/sh`). If the `execv` call fails, we print an error and return.

## Setting Up the Main Function

Now let's look at the main function that will create our container:

```c
int main(int argc, char *argv[]) {
    
    int flags = CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET | SIGCHLD;
    printf("Launching container...\n");

    // ... container creation code to come
    
    return 0;
}
```

### Defining Namespace Flags

Now we define the namespace flags that will determine what isolation features our container will have, read it again:

```c
int flags = CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET | SIGCHLD;
```

Each flag provides different isolation:

- `CLONE_NEWUTS`: Isolates hostname and domain name
- `CLONE_NEWPID`: Gives the container its own process ID namespace
- `CLONE_NEWNS`: Creates a new mount namespace
- `CLONE_NEWNET`: Isolates the network stack
- `SIGCHLD`: Signal to send when child terminates

### Creating the Container Process

Finally, we create the container process using the `clone()` system call:

```c
pid_t pid = clone(child_main, child_stack + STACK_SIZE, flags, NULL);
if (pid < 0) {
    perror("clone");
    return 1;
}

waitpid(pid, NULL, 0);
```

The `clone()` system call creates a new process that runs the `child_main` function with the specified namespace flags. We pass it the stack we defined earlier and wait for the container process to finish with `waitpid()`.

Now our container is ready to go!



{{< code language="c" title="container.c" id="1">}}
#define _GNU_SOURCE
#include <sched.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define STACK_SIZE (1024 * 1024)
static char child_stack[STACK_SIZE];

char *child_args[] = {"/bin/sh", NULL};

int child_main(void *arg) {
  // Set container hostname
  sethostname("minicontainer", 10);

  if (chroot("/home/stroky/.local/codes/Dockers/custom_container/containers/"
             "mycontainerr/rootfs") != 0 ||
      chdir("/") != 0) {
    perror("chroot/chdir");
    return 1;
  }

  mkdir("/proc", 0555);

  // Mount /proc
  if (mount("proc", "/proc", "proc", 0, "") != 0) {
    perror("mount /proc");
    return 1;
  }
  // Execute shell
  execv(child_args[0], child_args);
  perror("exec");
  return 1;

  return 1;
}

int main(int argc, char *argv[]) {

  int flags = CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET | SIGCHLD;
  printf("Launching container...\n");
  pid_t pid = clone(child_main, child_stack + STACK_SIZE, flags, NULL);
  if (pid < 0) {
    perror("clone");
    return 1;
  }

  waitpid(pid, NULL, 0);
  return 0;
}

{{< /code >}}

## Building and Running the Container

Compile the code:

```bash
gcc -o container container.c
```

Run it:

```bash
sudo ./container
```

You should now be in a shell inside your container with its own isolated environment!

```
❯ sudo ./container
Launching container...
sh-5.2#
sh-5.2# ls
bin   dev  home  lib64	opt   root  sbin  sys  usr  version
boot  etc  lib	 mnt	proc  run   srv   tmp  var
sh-5.2#
```

## What this container provides?

Our minimal container provides:

1. **Process Isolation**: Processes inside the container can't see processes outside
2. **Filesystem Isolation**: The container has its own root filesystem
3. **Hostname Isolation**: The container has its own hostname
4. **Network Isolation**: The container has its own network namespace


Now, this is a minimalist implementation, but a production-grade container systems also include:

1. cgroup support to limit CPU and memory usage
2. Implementation of user namespace isolation (`CLONE_NEWUSER`)
3. Bridge network interface for container connectivity
4. Support for mounting volumes from the host

## Conclusion

Building a container system from scratch helps in understanding what's going on under the hood. Though our implementation is basic, it reflects the core that underlie all container systems, including Docker and containerd.

The Linux kernel provides all the building blocks we need like namespaces, chroot, and mount points - to create isolated environments for running applications.

So that's it.

