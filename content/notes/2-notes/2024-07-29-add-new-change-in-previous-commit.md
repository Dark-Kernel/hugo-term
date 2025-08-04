---
Title: "Add new change in previous commit"
Published: 2024-07-29
author: Sumit Patel
description: "1. Find the commit hash you want to edit"
tags: ["git", "rebase"]
---



1. Find the commit hash you want to edit
```
git log 
```
[--more--]

2. Start interactive rebase, adjust the number if needed
```git rebase -i HEAD~1``` 

3. In the editor, change 'pick' to 'edit' for the commit you want to modify
4. Save and close the editor

5. Add the new file
```
git add path/to/newfile 
```

6. Amend the commit to include the new file
```git commit --amend```

Save and close the commit message editor

7. Continue the rebase
```git rebase --continue``` 

8. Resolve any conflicts if necessary
    Force push to the remote repository if needed
```git push --force ```
