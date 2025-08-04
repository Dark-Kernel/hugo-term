---
Title: "Easy dotfiles management"
Published: 2024-11-08
author: Sumit Patel
description: "### The easiest way to version control your dotfiles."
tags: ["git", "dotfiles"]
---

### The easiest way to version control your dotfiles.

1. Initialize empty repo at home

```
git init --bare $HOME/.dotfiles
```
[--more--]
2. Use working directory of git as `$HOME`, and git dir as `.dotfiles`
```
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

3. Only for current local repo, because it's annoying.
```
config config status.showUntrackedFiles no
```

4. Here you go, check status, add your configs, and commit.

```
config status
config add .config/mpv
config commit -m "Added mpv config"
```

5. Create repo at github/gitlab and add origin -> Push.
```
config remote add origin <link>
config push origin master
```


### Here you can use different branches for different computers, you can replicate you configuration easily on new installation - 

For using dotfiles on other device

1. Clone repo into home, if its **empty**
```
git clone --separate-git-dir=~/.myconf <link-to-repo> ~
```

2. Or clone into separate tmp dir, otherwise it **will fail if your home directory isn't empty**. Then copy your configs and remove tmp dir.
```
git clone --separate-git-dir=$HOME/.dotfiles <link-to-repo> $HOME/dotfiles-tmp
cp ~/dotfiles-tmp/.vimrc ~
rm -r ~/myconf-tmp/
```

3. Again set alias to manage dotfiles.
```
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Done!
easy peezy lemon squeezy :)


Reference: [ArchWiki](https://wiki.archlinux.org/title/Dotfiles) | [Ycombinator](https://news.ycombinator.com/item?id=11071754)

