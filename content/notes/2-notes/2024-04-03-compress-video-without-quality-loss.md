---
Title: "Compress video without quality loss"
Published: 2024-04-03
author: Sumit Patel
description: "```bash"
tags: ["ffmpeg"]
---



```bash
ffmpeg -i <input file>  -vcodec libx265 -crf 28 <output file>
```

