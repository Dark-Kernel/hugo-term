---
title: "Building a Lightweight Container System from Scratch Ft. Arch Linux"
date: 2024-10-17
draft: false
author: "Sumit Patel"
tags: ["ArchLinux", "container", "linux"] 
description: "Building a Lightweight Container System from Scratch on Arch Linux"
cover: /isSecured.jpg
---

# DIY Containers: Building a Lightweight Container System from Scratch on Arch Linux

In the world of containerization, tools like Docker and Podman reign supreme. But have you ever wondered what's happening under the hood? In this post, we'll leverage the power and flexibility of Arch Linux to build our own lightweight container system from scratch. We'll use Linux namespaces, cgroups, and some Arch-specific tools to create a basic, functional container.

## Understanding the Building Blocks

Before we dive in, let's briefly cover the key concepts:

1. **Namespaces**: These isolate system resources for a set of processes.
2. **Cgroups**: These limit, account for, and isolate resource usage (CPU, memory, disk I/O, etc.) of process groups.
3. **Chroot**: This changes the root directory for a process and its children.

## Prerequisites

Ensure you have the following packages installed:

```bash
sudo pacman -S arch-install-scripts util-linux
```

## Step 1: Creating a Root Filesystem

First, let's create a minimal Arch Linux root filesystem for our container:

```bash
mkdir arch-container
sudo pacstrap -c -d arch-container base
```

This creates a basic Arch Linux system in the `arch-container` directory.

## Step 2: Setting Up Network Namespace

We'll create a network namespace for our container:

```bash
sudo ip netns add container-ns
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth1 netns container-ns
sudo ip addr add 10.0.0.1/24 dev veth0
sudo ip link set veth0 up
sudo ip netns exec container-ns ip addr add 10.0.0.2/24 dev veth1
sudo ip netns exec container-ns ip link set veth1 up
sudo ip netns exec container-ns ip route add default via 10.0.0.1
```

These commands create a virtual ethernet pair and set up basic networking for our container.

## Step 3: Creating a Control Group

Let's create a cgroup to limit our container's resources:

```bash
sudo cgcreate -g cpu,memory:mycontainer
sudo cgset -r cpu.shares=512 mycontainer
sudo cgset -r memory.limit_in_bytes=512M mycontainer
```

This creates a cgroup named `mycontainer` with CPU and memory limits.

## Step 4: Writing the Container Script

Now, let's create a script to launch our container. Save this as `run-container.sh`:

```bash
#!/bin/bash

# Function to clean up after the container exits
cleanup() {
    ip link del veth0
    ip netns del container-ns
    cgdelete -g cpu,memory:mycontainer
}

# Set up cleanup on script exit
trap cleanup EXIT

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# Launch the container
unshare --fork --pid --net=/var/run/netns/container-ns --mount-proc \
cgexec -g cpu,memory:mycontainer \
arch-chroot arch-container /bin/bash
```

Make the script executable:

```bash
chmod +x run-container.sh
```

## Step 5: Running our Container

Now we can run our container:

```bash
sudo ./run-container.sh
```

You're now inside your homemade container! Let's verify the isolation:

```bash
# Check the network
ip addr

# Check the process tree
ps aux

# Check available memory
free -m

# Exit the container
exit
```

## Understanding What's Happening

Let's break down the key components of our container system:

1. **Filesystem Isolation**: `arch-chroot` changes the root directory, providing filesystem isolation.

2. **Network Isolation**: The `ip netns` commands create a separate network namespace, and `unshare --net` ensures the container uses this namespace.

3. **Process Isolation**: `unshare --pid --mount-proc` creates a new PID namespace and mounts a new procfs, isolating the process tree.

4. **Resource Limits**: `cgexec` ensures the container runs within the cgroup we created, enforcing resource limits.

## Enhancing our Container System

This is a basic implementation, but you could extend it in several ways:

1. **Overlay Filesystems**: Use overlay fs to make containers more efficient.
2. **User Namespaces**: Implement user namespaces for better security.
3. **Container Images**: Create a system for building and storing container images.
4. **Networking**: Implement more advanced networking features like port mapping.

## Conclusion

We've just scratched the surface of container technology, but this exercise demonstrates the power and flexibility of Linux systems like Arch. By understanding these low-level concepts, you can better appreciate tools like Docker and potentially customize them for your specific needs.

Remember, this is a educational exercise and not intended for production use. For real-world applications, stick to well-tested solutions like Docker or Podman.

In our next post, we might explore how to extend this system with more features, or perhaps dive into other unique ways to leverage Arch Linux's flexibility. Stay tuned for more advanced Arch Linux adventures!
