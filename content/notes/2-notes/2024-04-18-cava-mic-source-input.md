---
Title: "Cava mic source input"
Published: 2024-04-18
author: Sumit Patel
description: "Add below section in cava config"
tags: ["Example"]
---


Add below section in cava config

get the source ID:
```bash
pactl list sources
```

[--more--]
```
[input]
method = pulse
source = 55  # source id  
```



