#### How does the merge work?
- Find the common ancestor (merge base)
    - Last commit both branches share before diverging.
- Compares changes
    - Compares current branch, merging branch, merge base.
- Merges the changes
    - combines the changes from current branch and merging branch starting with common ancestor.
    - In case of conflict, resolve manually
    - If no conflicts, merge changes and create a merge commit.
- Result of merge
    - Merge commit has 2 commits, latest commits of two branches.

#### Why start with common ancestor and not compare the final commits?
- comparing only the latest commits ignores all the history in between and can result in missing important things or not detecting conflicts.
- Need to properly integrate changes from both sides.
- Allows git to handle parallel changes that would be impossible to detect just by comparing latest commits.
- By understanding the merge base, git can detect conflicts that might otherwise be missed, understand the context of change and avoid blindly merging code that might break, 

#### Fast forward merge
- If the branches haven't diverged and there is a linear path from the master tip to feature tip, master head now points to the feature tip.
- After doing a fast forward merge, we can delete that feature and git doesn't complain since that feature is now available through the master branch.
- If you want a merge commit even though fast forward merge is possible, say `git merge --no-ff feature1`.

> Many developers like to use fast forward merge facilitated through rebasing for small bug fixes, delete the feature and 3 way merge for longer running features


#### What happens if you merge feature branch with master branch locally and both are ahead in remote
- git only considers local branch and merges them.
- Issue occurs when we push to remote to prevent overwriting new commits.
- Correct approach: 
    - `git fetch origin` -> `git rebase origin/master` or `git pull --rebase origin master`
    - `git checkout feature1` -> `git rebase origin/master` or `git pull --rebase origin master`
    - `git merge feature` -> `git push origin master`


#### What happens after you merge feature branch with master branch
- If you keep the feature branch, the history will stay
- If you delete the feature branch, the tree will be clean
- If new commits, come feature branch will take them. but need to merge again.
- If feature branch is deleted and you add commits, then new feature branch will be created.

#### `git merge`
- Plain git merge on a local branch will try to merge the remote branch with the local branch
- This way, we will be able to push the changes.