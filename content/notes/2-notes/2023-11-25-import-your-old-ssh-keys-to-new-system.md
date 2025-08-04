---
Title: "Import your old ssh keys to new system."
Published: 2023-11-25
author: Sumit Patel
description: "1. Place it in the right place"
tags: ["ssh"]
---

1. Place it in the right place

```bash
cp /path/to/my/key/id_rsa ~/.ssh/id_rsa
cp /path/to/my/key/id_rsa.pub ~/.ssh/id_rsa.pub
```
[--more--]



2. change permissions on file

```
sudo chmod 600 ~/.ssh/id_rsa
sudo chmod 644 ~/.ssh/id_rsa.pub
```

3. start the ssh-agent in the background

```bash
eval $(ssh-agent -s)
```

> NOTE: If your shell is `fish`, then just execute the `ssh-agent -s` and then export those printed variables.


4. Make ssh-agent to actually use the copied key

```bash
ssh-add ~/.ssh/id_rsa
```

No need to import public key.
