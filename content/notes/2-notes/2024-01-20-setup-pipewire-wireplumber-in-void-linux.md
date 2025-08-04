---
Title: "Setup pipewire & wireplumber in void linux"
Published: 2024-01-20
author: Sumit Patel
description: "Remove pulseaudio"
tags: ["pipwire"]
---


Remove pulseaudio
```bash
sudo xbps-remove pulseaudio pulseaudio-devel
```
[--more--]


Install dependencies

```bash
sudo xbps-install libspa-bluetooth pipewire wireplumber 
```


Reference: [Void Docs](https://docs.voidlinux.org/config/media/pipewire.html#session-management)  | [Reddit](https://www.reddit.com/r/pipewire/comments/1389b26/bluetooth_headphones_fail_to_connect_via_pipewire/)
