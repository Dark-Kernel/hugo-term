---
Title: "Combine audio & video of different length"
Published: 2024-06-24
author: Sumit Patel
description: "1. Long audio & shortvideo:"
tags: ["ffmpeg"]
---


1. Long audio & shortvideo:

```bash
ffmpeg -i Downloads/pooja_updated.mp4 -i aum.opus -map 0:v:0 -map 1:a:0 -c:v copy -shortest -y output3.mp4
```
[--more--]

2. Long video & short audio:

```bash
ffmpeg -stream_loop -1 -i Downloads/pooja.mp4 -i aum.opus -shortest -map 0:v:0 -map 1:a:0 -y output-pooja.mp4
```
