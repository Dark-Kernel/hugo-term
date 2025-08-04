---
Title: "Pywal gradient for cava"
Published: 2023-07-24
author: Sumit Patel
description: "This can be done simply using Pywal templates"
tags: ["pywal", "cava"]
---

This can be done simply using Pywal templates

[--more--]

1. Just move your cava config to `~/.config/wal/templates/cava_config` , and then replace the colors with {color0}, {color1},... etc.

```
mv ~/.config/cava/config ~/.config/wal/templates/cava_config
```

Recommend colors : 

```
[color]
gradient = 1
gradient_count = 4
gradient_color_1 = '{color1}'
gradient_color_2 = '{color2}'
gradient_color_3 = '{color4}'
gradient_color_4 = '{color5}'
gradient_color_5 = '{color6}'
```

2. Then after you run pywal, just link your cava_config to cava/config back from ~/.cache/wal/

```
ln -s ~/.cache/wal/cava_config ~/.config/cava/config
```

And you are done.


Reference: 
[Github Issue](https://github.com/karlstav/cava/issues/340) | 
[Pywal template docs](https://github.com/dylanaraps/pywal/wiki/User-Template-Files)
