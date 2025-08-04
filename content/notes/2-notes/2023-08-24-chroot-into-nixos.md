---
Title: "Chroot into nixos"
Published: 2023-08-24
author: Sumit Patel
description: "1. Mount the file system containing the NixOS to chroot into at `/mnt` or any other directory, using e.g."
tags: ["nixos"]
---

1. Mount the file system containing the NixOS to chroot into at `/mnt` or any other directory, using e.g.

```bash
sudo mount /dev/sda10 /mnt/nixx/
```
[--more--]

2. Mount the host system's Linux run-time api file systems inside the mount, then populate /run using the activate script and chroot inside, starting a bash shell

```bash
sudo mount -o bind /dev /mnt/nixx/dev/
sudo mount -o bind /proc /mnt/nixx/proc/
sudo mount -o bind /sys /mnt/nixx/sys/
sudo chroot /mnt/nixx /nix/var/nix/profiles/system/activate
sudo chroot /mnt/nixx/ /run/current-system/sw/bin/bash
```


Reference: [NixOS Wiki](https://nixos.wiki/wiki/Change_root)
