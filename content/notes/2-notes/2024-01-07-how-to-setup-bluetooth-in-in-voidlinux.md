---
Title: "How to setup bluetooth in in voidlinux"
Published: 2024-01-07
author: Sumit Patel
description: "## You need some packages first"
tags: ["voidlinux", "bluetooth"]
---


## You need some packages first

```bash
sudo xbps-install libpulseaudio bluez-alsa
```
[--more--]

## Now make some changes in bluez-alsa service `/etc/sv/bluez-alsa/run`  to add support for `A2DP` support:

```bash
#!/bin/sh
[ -r ./conf ] && . ./conf

install -d -m0755 -o _bluez_alsa -g audio /run/bluealsa
exec chpst -u _bluez_alsa:audio bluealsa -p a2dp-source -p a2dp-sink
#exec chpst -u _bluez_alsa:audio bluealsa $OPTS
```

then start it

```bash
sudo ln -s /etc/sv/bluez-alsa /var/service
```

```bash
sudo sv start bluez-alsa
```

> Make sure to stop alsa service first. `sudo sv stop alsa`. You pulseaudio should be restarted.

