#### `git push`
- Used to upload local repository content to the remote repository.
- when you run `git push`, it will push the changes of the current working branch to its corresponding upstream branch in the remote repository.
- doesn't work if local and remote branches have different names.
- For eg, if we are on local branch feature1 which is tracking origin/feature1, `git push` will push the local commits from feature1 to origin/feature1.
- `git push` from local repository is equivalent to merging a branch in remote repository.

## Details When you run `git push origin <branch>`
- Check if the remote repository is accessible?
- Compare local and remote branch history.
    - git checks if remote has new commits that local doesn't have
- case 1 : Now new commits on remote
    - Fast forward push -> simply update with your changes.
    - push succeeds.
- case 2 : New commits in remote
    - Git rejects the push to avoid overwriting new changes
    - You must first fetch and merge or rebase before pushing.
- case 3 : Forced push
    - If you want to overwrite the remote branch with local changes, use `git push --force origin main`
    - Deletes the latest commits on remote.
- case 4 : Conflicts a merge attempt:
    - git doesn't check for conflicts during a push.
    - conflicts only occur during pull.
- push rejects if remote has new commits (standard rejection for non fast forward)
- force with lease allows you to force pus hif the remote has not been changed since you last fetched, protecting against accidental overwrites.

#### What happens if current local branch is not tracking anything?
- `git push` will throw an error and asks you to specify the remote and branch.
- Can specify the remote branch to be pushed by saying `git push origin localbranch:feature9`
- Now, we have pushed to feature9 branch but still the current local branch is not tracking the feature9. So, next time `git push` still won't work.
- can fix this by saying `git push -u origin feature9` or linking the current local branch to a remote branch and say `git push`

#### `git push origin feature1`
- This should actually be `local branch`: `remote branch` so, when you say a single word like feature1, it will assume local branch and remote branch are feature1. If you have a local branch named feature1 which is not linked to any remote branch, it will create a remote branch with same name and push to it.
- If there is no local branch with name feature1, but there is a remote branch with same name, it will throw error.

#### `git push origin feature1:feature99`
- push the ref`feature1` to update the `feature99`
- If feature1 doesn't exist, it will throw error
- If feature99 doesn't exist, it will create it in remote repository.
- If feature99 exists, it will push to feature99

#### What happens on running `git push` from different branch
- Git will push changes from that branch to its upstream counterpart on the remote reposoitory.

#### What happens on running `git push origin feature2` from feature1
- Commits on feature2 will be uploaded to it's upstream counterpart

#### `git push origin branch`
- Pushes to branch. updates if exists, else , creates new one 

#### `git push --all`
- Pushes all local branches to the remote.

#### `git push origin --tags`
- Pushes all local tags to the remote.

#### `git push -u origin <branch>`
- Push and set upstream.

#### `git push --force` or `git push --force origin main`
- Overwrites remote branch history.

#### `git push --force-with-lease`
- Force pushes only if no new commits are there on remote repo.

#### `git push --delete origin <branch>`
- Removes the branch from remote repository.
- The local 

#### `git push --dry-run origin main`
- Simulates the push without making any changes

#### `git push --signed`
- Pushes commits only if they are signed.

#### `git push --mirror origin`
- mirror flag synchronizes everything between the local and remote repositories, overwrites the remote repository to match the local repository.
- delete any remote branches that do not exist locally
- Used when migrating a repository.

#### `git push --atomic origin feature fix-bug`
- Either push both feature and fixbug or else none.

#### What happens if you push to a repository where you don't have write access
- permission denied to username

#### How to undo a git push
- Either go back 1 commit in local branch and do a forced write
- `git reset --hard --HEAD-1` -> `git push --force-with-lease`
or 
- Revert the commit
- `git revert <commit-hash>`
- git push origin main


