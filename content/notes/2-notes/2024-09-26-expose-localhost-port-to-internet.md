---
Title: "Expose localhost port to internet"
Published: 2024-09-26
author: Sumit Patel
description: "1. `80` is on which port to map, `5000` is the localhost port, the service we want to expose."
tags: [""]
---

1. `80` is on which port to map, `5000` is the localhost port, the service we want to expose. 

```
ssh -R 80:localhost:5000 nokey@localhost.run
```

