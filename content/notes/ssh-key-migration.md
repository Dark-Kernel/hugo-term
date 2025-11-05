
---
Title: SSH key migration
Author: Sumit Patel
---

1. Copy your files to `~/.ssh`.
```bash
cp /path/to/my/key/id_rsa ~/.ssh/id_rsa
cp /path/to/my/key/id_rsa.pub ~/.ssh/id_rsa.pub
```

2. Change permissions of files
```
sudo chmod 600 ~/.ssh/id_rsa
sudo chmod 644 ~/.ssh/id_rsa.pub
```

3. Start the ssh-agent in the background and add the key to agent
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```
> NOTE: If using `fish` shell,then just execute the `ssh-agent -s` and then export those printed vars.
> No need to import public key.
