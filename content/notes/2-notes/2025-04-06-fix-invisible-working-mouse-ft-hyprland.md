---
Title: "Fix: invisible working mouse Ft. Hyprland"
Published: 2025-04-06
author: Sumit Patel
description: "Just add this entry anywhere in `.config/hypr/hyprland.conf`:"
tags: ["hyprland"]
---

Just add this entry anywhere in `.config/hypr/hyprland.conf`:

```
cursor {
    no_hardware_cursors = true
}
```