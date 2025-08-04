---
Title: "Opencv - Could not find the Qt platform plugin 'wayland'"
Published: 2024-05-29
author: Sumit Patel
description: "Error:"
tags: ["python", "wayland"]
---

Error:
```
❯ python getcolor.py
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in "/home/stroky/testline/alemeno/lib/python3.12/site-packages/cv2/qt/plugins"
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

fish: Job 1, 'python getcolor.py' terminated by signal SIGABRT (Abort)
```

[--more--]

Solution:

```bash
❯ export QT_QPA_PLATFORM="xcb"
❯ python getcolor.py
--- success execution ---
Pixel value at (100, 50): [255 255 255]
HSV value at (100, 50): [  0   0 255]
```

Make sure `qt5-wayland` & `qt6-wayland` packages are installed


Reference:
[Stackoverflow](https://stackoverflow.com/questions/69994530/qt-qpa-plugin-could-not-find-the-qt-platform-plugin-wayland)
