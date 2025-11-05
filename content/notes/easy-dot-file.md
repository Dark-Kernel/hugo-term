---
Title: Easy dotfiles management
Author: Sumit Patel
---

1. Initialize empty repo at $HOME dir
```
git init --bare $HOME/.dotfiles
```

2. Use working directory of git as `$HOME`, and git dir as `.dotfiles`
```
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

3. Set git to ignore untracked files, Only for current local repo, because it's annoying.
```
config config status.showUntrackedFiles no
```

4. Here you go, check status, add your configs, commit and push
```
config status
config add .config/mpv
config commit -m "Added mpv config"
config remote add origin <link>
config push origin master
```
