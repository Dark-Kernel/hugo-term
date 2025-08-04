---
Title: "Take effect of group change without logout."
Published: 2024-02-11
author: Sumit Patel
description: "Just use following command:"
tags: ["group"]
---


Just use following command:

```bash
newgrp <group>
```
[--more--]

Example: 
it is help full in case of new docker installation.

```bash
sudo usermod -aG docker $USER && newgrp docker
```