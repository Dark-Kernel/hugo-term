---
Title: "create new runit service"
Published: 2023-11-05
author: Sumit Patel
description: "Create a directory with run file"
tags: ["runit"]
---



Create a directory with run file

```bash
sudo mkdir /etc/runit/sv/servdir
sudo nvim /etc/runit/sv/servdir/run
```

[--more--]

Add following contents:

```bash
#!/bin/sh -e
exec 2>&1
exec <commands>
```

Then make that file executable

```bash
sudo chmod +x /etc/sv/docker/run
```
