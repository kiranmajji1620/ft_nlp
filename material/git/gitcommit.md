## Uses
- Switch to another branch
- Create a new branch and shift to it
- Checking out a specific comment
- Restoring files to previous state.

#### Ammend
- take stage files and stuff them to last commit
- `git commit -amend --no-edit`
    - doesn't add any extra commits, no chaning messages
    - Changes the commit hash of last commit
    - shouldn't use in a public repository
- `git commit --amend -m "new commit message"`
    - If there are no stage files, it will change the  message
    - still rewrites the commit hash

How to rewrite a past commit??

#### How to delete commits
- Higher chance of conflicts
- `git reset --hard HEAD~1`
    - remove any changes from most recent commit

- Undo last commit : `git reset --soft HEAD~1`
    - doesn't delete the changes, undo the changes

#### How to delete commits from past 
- `git rebase -i HEAD~2`
    - 