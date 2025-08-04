---
Title: "tmux error 'tmux.conf: no current session'"
Published: 2023-12-03
author: Sumit Patel
description: "This is because you haven't added `-g` in any of the `set` command in `tmux.conf` file."
tags: ["tmux"]
---


This is because you haven't added `-g` in any of the `set` command in `tmux.conf` file.

Reference: [Stackoverflow](https://stackoverflow.com/a/55805036)
