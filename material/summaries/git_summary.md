### Version control:
- tracks changes, collaboration, branching&merging, backup and recovery, why changes made.
- Local VC, Centralized VC, Distributed VC(git)

#### Repository
- locatoin where code, documentation, history of changes are stored and managed using VCS like git.
- **Remote repository** : stored on a remote server or cloud platform enabling collaboration and backup.

#### Origin
- default name for remote repository

#### head
- special commit reference that generally points to current checked out branch

### git clone
- creates a new directory -> initial branch checkout and track -> creates remote branch refs
- bare : no working directory, has all commits, tags, branches but no remote refs. mirror : exact replica including remote refs. 

### git add
- stage changes : mark the files you want to add in the next commit, grouping meaningful changes, buffer between working directory and repository
- we can stage multiple files and parts of code.

### git diff
- by default compares changes with head and last commit

### git commit
- save changes to repository, represents a snapshot of the project at a particular time, contains metadata(author, timestamp, commit message) 

### git push
- push to an advanced commit : need to pull or rebase changes and then commit(error : non fast forward merge)
- 
### git delete
- `git branch -d BRANCH1` deletes branch1 if it is either merged or pushed to remote
- `git push -d origin BRANCH1` deletes remote branch1 -> `git branch --unset-upstream` or `git push origin :BRANCH1` recreate.

### git stash
- used to store the uncommited (staged and unstaged) changes and revert back the working dir to head commit.    
- can create multiple stashs, apply one stash to another branch.
- to temporarily store changes when switching branches, pull latest changes from a different branch, expirementing with changes

### git fetch
- download the remote content but not alter our repository
- safer than git pull

### git merge
- fast forward merge (no new commit) and 3 way merge(new commit)
- 

### git pull
- git fetch + git merge (on head) new merge commit
- direct merge or rebase and the fast forward merge

### git rebase
- apply the advanced local commits to the tip of remote branch as it we didn't diverge
- I want my changes on top of every one else, linear project history
- commit hashes changed, don't rebase public commits

### git squash
- merge the commit with previous commit
- done using interactive rebase

### git tag
- aren't pushed with commits
- push separately

#### commands
- `git clone`
    - `git clone --depth 1 <repo>` to creates a shalow clone limiting the commit history. reduces time and disk space.
    - `git clone -b dev <repo>` Branch to checkout after cloning : If you don't want the default branch but need a specific branch. OR create a new local branch and set it to track remote branch.
    - `git clone --recurse-submodules <repo>` Needed when a repository contains sub modules 
    - `git clone --bare <repo>` Ideal for setting up remote repository that dosn't take any changes. only the `.git` is present
    - `git clone --mirror <repo>` Similar to a bare repo that will copy all references and remote configuration
    - `git clone -n <repo>` 
- `git add`
    - `git add .` - new and modified files
    - `git add -A` - all changes
    - `git add -U` - only modified and deleted files
    - `git add -p .` - stage chunks
    - `git add --dryrun`
    - `git add --intent-to-add` - add file to stage but don't stage changes.
    - `git add -f secret_file.txt` - add ignored files
- `git diff`
    - `git diff --cached PATH` - compare with staged changes
    - `git diff COMMIT1 COMMIT2`
    - `git diff BRANCH1 BRANCH2` compare tips
    - `git diff BRANCH1...BRANCH2` compare common ancestor with branch2
    - `git diff BRANCH1 BRANCH2 ./file.txt`
`git commit`
    - `git commit -a -m ""` automatically stage files and commit them
    - `git commit --ammend` change previous commit
    - `git commit --ammend --no-edit`
    - `git commit --dry-run`
    - `git commit --verbose -m ""`
    - `git commit --author="John Doe <john@example.com>" -m "Commit as John Doe"`
    - `git commit --include <file> -m "Include new file in commit"` commit staged and unstaged files together
- `git status`
- `git branch`
    - `git branch BRANCH` create a branch but not checkout
    - `git branch -a` get all branches
    - `git branch -vv` get local branches
    - `git branch -d BRANCH1`
    - `git branch --set-upstream-to=origin/BRANCH`
- `git checkout`
    - changed to `git switch` and `git restore`
    - `git checkout -b BRANCH1`
    - `git checkout RemoteBranc` create a local remotebranch and set it to track that.
    - `git checkout -- <filename>` restore the file to it's last commit
- `git stash`
    - `git stash list`
    - `git stash show`
    - `git stash pop`
    - `git stash -m "navbar1"`
    - `git stash pop --index 1`
    - `git stash clear`
    - `git stash drop 0`
    - `git stash -p` interactive stashing
- `git push`
    - `git push origin localBranch:remoteBranch`
    - `git push -u origin main`
    - `git push origin --tags`
- `git fetch`
- `git merge`
    - 
- `git rebase`
    - `git rebase <base>` base can be branch, commit hash, head reference, id
    - `git rebase -i BASE` lets you alter, squash, remove commits
- `git pull`
    - `git pull origin` fetch the specified remotes copy of current branch and merge
    - `git pull --no-commit origin`
    - `git pull --rebase origin`
    - `git pull --verbose`
    - `git config --global branch.autosetuprebase always` to set pull as rebase
- `git log`
    - `git log --pretty=oneline`

- `git show head`
- `git show --ignored`
- `git rm -r --cached`
- `git restore -- .` discard unstaged changes