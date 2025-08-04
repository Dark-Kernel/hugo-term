---
Title: "Flash image to partition, and boot with grub manual entry"
Published: 2024-11-24
author: Sumit Patel
description: "### How to flash image (.iso) to paritition"
tags: ["grub", "image", "partition"]
---
### How to flash image (.iso) to paritition

1. Create partition

```
sudo fdisk /dev/sda
```
[--more--]

2. Format partition

```
sudo mkfs.ext4 /dev/sda11
```

3. Write image to partition

```
sudo dd bs=4M if=/home/stroky/Downloads/cachyos-desktop-linux-241110.iso of=/dev/sda11 status=progress oflag=sync
```

4. Mount partition

```
sudo mount /dev/sda11 /mnt/cachyos
```

5. Check for the grub.cfg in there

```
ls /mnt/cachyos/boot/grub/
```

6. Add entry

```
sudoedit /etc/grub.d/40_custom
```

There are 3 main ways

- Direct provide path for grub.cfg: 
```
menuentry 'CachyOS Install direct' {
    set root=(hd1,gpt11)
    configfile /boot/grub/grub.cfg
    # linux ($root)/arch/boot/x86_64/vmlinuz-linux-cachyos root=/dev/sda11 ro quiet splash 
    # initrd ($root)/arch/boot/x86_64/initramfs-linux-cachyos.img
}
```

- Boot through partition:
```
menuentry 'CachyOS Install dev11' {
    set root=(hd1,gpt11)
    linux ($root)/arch/boot/x86_64/vmlinuz-linux-cachyos root=/dev/sda11 ro quiet splash cow_spacesize=10G
    initrd ($root)/arch/boot/x86_64/initramfs-linux-cachyos.img
}
```

- Boot through iso:
```
menuentry 'CachyOS Install' {
    set isofile="/home/stroky/Downloads/cachyos-desktop-linux-241110.iso"
    loopback loop $isofile
    linux (loop)/arch/boot/x86_64/vmlinuz-linux-cachyos img_dev=/dev/sda8 img_loop=$isofile earlymodules=loop cow_spacesize=10G
    initrd (loop)/arch/boot/x86_64/initramfs-linux-cachyos.img
}
```


Then finally update grub config:

```
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

> To get the hd1,gpt11 you can go to grub shell and press ls;

Reboot
