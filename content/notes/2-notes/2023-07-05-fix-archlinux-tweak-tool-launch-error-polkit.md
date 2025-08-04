---
Title: "Fix `archlinux-tweak-tool` launch error `polkit`"
Published: 2023-07-05
author: Sumit Patel
description: "The error is because the polkit authentication agent helper is not running."
tags: ["fix"]
---

The error is because the polkit authentication agent helper is not running. 
> The GUI window which asks for password

We can use any polkit helper like `polkit-gnome` or any other [--more--]

#### To fix this error execute below command on another terminal, or add it to your window manager script or at startup
```
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
```

### This will fix the issue.
