---
Title: "Hyprland windows rule v2 using class"
Published: 2023-07-07
author: Sumit Patel
description: "### To set the window rule v2, we can use class, to get the class of applications that are running we can use:"
tags: ["hyprland"]
---

### To set the window rule v2, we can use class, to get the class of applications that are running we can use:

```bash
hyprctl clients
```
[--more--]
#### We can use a class with regex also, or use the exact class name using the above command:
Window Rule V1:
```toml
windowrule = workspace 2, ^(.*Brave.*)$ 
```
Window Rule V2: 
```
windowrulev2 = opacity 0.8 0.8,class:^(.*Brave.*)$
```
#### The second param is the class of brave browser or we can use the application title, as the second param instead:
Window Rule V1:
```
windowrule = workspace 2, ^(.*Brave.*)$,title:^(.*Brave.*)$
```
Window Rule V2:
```
windowrulev2 = opacity 0.8 0.8,class:^(.*Brave.*)$,title:^(.*Brave.*)$
```

<u>[Hyprland window rules docs](https://wiki.hyprland.org/Configuring/Window-Rules/)</u>

<u><b>[Reddit issue](https://www.reddit.com/r/hyprland/comments/132nhzy/is_there_any_way_to_open_and_keep_an_app_in_a/) </b></u>

