---
title: "Git concepts"
date: 2023-08-13
draft: false
author: "Sumit Patel"
tags: ["git", "linux"] 
description: "Everything you need to know about git."
---


# Git 

- Branching strategies 
- Vcs reset / revert
- PR merge / branch merge
- Merge vs rebase
- Cherry pick
- git stash


> Never commit directly in master branch.


### Important branches:

1. master: The main stable branch.

2. staging: For QA team, can be sent for production. Most of the time it is same as master.

3. develop: From where developers get codes.

4. feature: To add any feature. 

    - If passed => develop ↓ 

    - If passed => staging ↓ 

    - If passed => master.



### Branching Strategies:

#### Small team strategy

* Use all important branches 
* Create features from develop/dev branch.

    - develop ↴

        → feature1

        → feature2

        → feature3 ... 

* Use hot fixes whenever needed, like for small bugs, can be done by team lead.

> hotfix: Fixing small bugs, like correction of spelling, no devs needed directly team lead can change it.


                    
#### Big team strategy

* There is change in branch name conventions like:

    - master -> prd

    - staging -> stg

    - develop -> dev 
* Use JIRA like software, to manage projects. Tasks are assigned as tickets and then status is changed according to progress.
* Integrate JIRA with github

> Jira is Issue & project tracking system, which is used by many large scale companies.

&nbsp;
---
### Git Revert & Reset


 * ##### git revert:
    Used to revert/undo a particular commit, It creates new commit of revert, and keeps original commit history.

    Example: 

    - Get commit id

        ```bash
        git log --oneline
        ```
    - Revert
        ```bash
        git revert <commit-id>
        ```

&nbsp;

---

 * ##### Git Reset: 
    It is used to undo to a particular commit but, it removes all commits history after that commit. Mostly used in case like commited security credentials and want to remove it completely from commit history.

    Example: 
    
    - If we have following log:
        ```bash
        ❯ git log --oneline
        9210da8 (HEAD -> dev) added git ignore
        e803737 no keys now
        de7aa15 Revert "added line 2"
        99c25e5 added line 2
        25d7961 (master) initial commit
        ```
    - We want to reset `de7aa15`, so we will have to use commitid of previous/below commit.
        ```bash
        git reset 99c25e5
        ```
    - So after `99c25e5` all commits will be deleted.

    <!-- ![ss](/git-reset.png) -->
    


> Don't use `git add .`, some times it might track files which is confidential and can lead to risk.


&nbsp;

---

### Git Merge

 * ##### Branch Merge:
    Git merge is used for merging two branches. 

    Example,

    - You have added some features in dev branch.
    - It is passed by QA.
    - Now to add that feature to release, you need to merge that feature in main/master/production branch.
        ```bash 
        # first switch to branch in which you want to merge.
        git checkout master

        # Then merge
        git merge dev
        ```
    - There is something called `squash` which is used to merge without commit history. 
        ```bash
        git merge dev --squash
        ```


&nbsp;

---

### Git rebase
   
It Adds commit history of other branch/remote in linear/sequence way while merging.


**Difference:** 
| Merge   | Rebase    |
|--------------- | --------------- |
| Only HEAD commit is maintained while merging | Full commit history is maintained while merging in sequence   |


   Example: 
    
   1. While pulling we can use rebase, to reconcile divergent branch.

        ```bash
        git pull origin master --rebase
        ```
   2. Rebase a particular branch.

        ```bash
        git rebase master
        ```


&nbsp;

---

### Cherry pick
Pick a particular commit from any branch and apply to master or any other branch.
In simple words apply that particular commit to current branch.

Example: 
```bash
git cherry-pick <commit-id>
```


&nbsp;

---

### Git stash 

Using this your current work is stored somewhere, not commited but tracked by git which can be loaded anytime. This is something where you can store your partial changes and commit later on.

Example: 
1. Stash 
    ```bash
    git stash
    ```

2. Apply stash to working dir
    ```bash
    git stash pop
    ```
3. List stashs

    ```bash
    git stash list
    ```
4. Apply a particular stash

    ```bash
    git stash apply stash@<list-number>
    ```

&nbsp;

So, that's it.
