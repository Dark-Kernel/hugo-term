---
Title: "Fix mpv lags system while playing yt video"
Published: 2024-05-30
author: Sumit Patel
description: "There are different ways:"
tags: ["mpv"]
---

There are different ways:

1. Using resample
```
mpv -vo=gpu --video-sync=display-resample -hwdec=auto "https://www.youtube.com/watch?v=ENxwig2JOKo"
```
[--more--]

2. Use yt-dlp
```
mpv -ytdl-raw-options='format="mp4,best[height<1081]"' -vo=gpu --video-sync=display-resample "https://www.youtube.com/watch?v=ys5MqjzPTag"
```


References: 
[ArchLinux Forum](https://bbs.archlinux.org/viewtopic.php?id=283397) | [Reddit](https://www.reddit.com/r/mpv/comments/m6uv5b/video_lagging_on_mpv/)
