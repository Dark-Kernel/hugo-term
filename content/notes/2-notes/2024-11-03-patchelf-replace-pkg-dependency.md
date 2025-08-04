---
Title: "patchelf, replace pkg dependency"
Published: 2024-11-03
author: Sumit Patel
description: "Replace the required dependency error in packages."
tags: ["nvim", "libmsgpackc.so.2"]
---

Replace the required dependency error in packages.

Error:

```
nvim: error while loading shared libraries: libmsgpackc.so.2: cannot open shared object file: No such file or directory
```
[--more--]
Solution: 

[image 1730633405.jpg]

```pacman -S patchelf```

``` patchelf --replace-needed libmsgpackc.so.2 libmsgpack-c.so.2 $(command -v nvim)```


Reference: [Reddit](https://www.reddit.com/r/termux/comments/1fl4wo8/comment/lo15lw1/)
