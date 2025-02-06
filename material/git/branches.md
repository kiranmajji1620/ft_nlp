#### Create a new branch
- Creat a new branch `git branch <branch name>`
- Go to that branch `git checkout <branch name>`
- Create and go to that branch `git checkout -b <branch name>`  



### Remote Tracking Branches
- These track the latest commits in the remote repositories branches.




#### How to switch to feature1 branch from main branch
- When cloned, your local branch is created as the copy of remote repo's main branch and it tracks the remote changes. meaning git pull and git push work 
- If you want to work on feature1 branch instead of main branch, 
    - create a new local branch `git checkout -b feature1 origin/feature1`
    - This means that we created a local branch named feature1 which tracks the remote branch origin/feature1.
    - Now, stay in local feature1 branch and git pull and git push work seamlessly.
    - git push origin feature1


#### How to push a branch to remote repository
- Stay in the local branch feature1, say `git push origin feature1`
- Will create the feature1 in remote repo and then push the local feature1 commits to remote feature1.
- Still, local and remote aren't connected.


#### what happens during `git push origin master` while staying on feature1?    
- If master isn't updated, Even though you are staying and working in feature1, `git push origin master` pushes the old state of master ignoring the changes in feature1, remote master remains unchanged.
- will throw an error if local repo doesn't have any master branch.
- If remote master has new commits, that aren't there in local master, git will reject the push.


#### What happens if remote branch is ahead of local branch you still push?
- Git will reject the push to prevent overwriting remote changes.
- Fix1
    - `git pull origin master --rebase`
    - Saves local changes in a buffer.
    - Updates local master to match the latest remote master.
    - Re applies the saved commits on the updated master.
    - The `--rebase` option applies your local commits on top of the latest remote changes.
    - If there are any conflicts, you need to resolve.
    - `git push origin master`
    - This keeps history linear without any merge commit.

- Fix2
    - `git pull origin master`
    - Here, git fetches remote changes and merges them with local master.
    - If conflict occurs, git asks to resolve them manually and commit these changes. anyway has a merge commit.
    - Now, git push origin main.


#### What happens if your current branch is not tracking any remote branch.
- It throws an error for `git push` as there is no remote repository to track.
- To mention where to push, say `git push origin feature9` 
- To link the remote branch to local branch after pushing as well, `git push -u origin feature9`
- To link them separately, say `git branch --set-upstream-to=origin/feature9`, make sure that remote branch exists prehand.


#### Get all the    branches
- `git branch -a`
#### Get local branhes
- `git branch -vv`


#### Delete a local branch
- `git branch -d feature1` or `--delete`
- only deletes the branch if it has already been fully merged into the remote or another branch.
 
- `git branch -D feature1` or `--delete --force`
- Deletes the branch irrespective of delete status.

#### Delete a remote branch
- `git push --delete origin feature1` or `-d`   
- Deletes the remote branch. Now, the local branch that is tracking the deleted remote branch needs a separate upstream
- `git branch --unset-upstream`
or 
- `git push origin :feature1`