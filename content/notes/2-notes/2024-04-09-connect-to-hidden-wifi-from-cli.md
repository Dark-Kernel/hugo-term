---
Title: "connect to hidden wifi from cli"
Published: 2024-04-09
author: Sumit Patel
description: "1. Install `iwd` for `iwctl`"
tags: ["wifi"]
---

1. Install `iwd` for `iwctl`

```bash
sudo pacman -S iwd
```
[--more--]
2. iwctl
3. Enter following info

"station <wlan> connect-hidden <"network name">" 

e.g
```
> station wlan0 connec-hidden "<SSID>"
```


Reference : [Reddit](https://www.reddit.com/r/archlinux/comments/10uhl9f/connect_to_a_hidden_wifi/)
| [stackexchange](https://unix.stackexchange.com/questions/664646/connecting-to-a-hidden-wi-fi-network-arch-linux)
