#### `git checkout feature1`
- go to feature1 if exists, error if it doesn't exists

#### `git checkout -b feature1`
- Create feature1 and go to checkout it.

#### `git checkout feature1`, feature1 exists on remote
- Create a new local feature1 and set it to track remote one.

## Git checkout => `git switch` for branch switch `git restore` for file restoration

### What happens to the changes during `git switch`?
- The switch won't happen until you stash them or commit them.
- `git checkout -f feature1` to discard the unstaged and staged changes.

## Checking out a commit
- Any new commits on this state will be orphaned, unless a new branch is created

#### `git checkout <branch name> -- <file>` for `git restore`
- Restores the file to the latest commit version of it in the branch.

#### `git checkout -- <file name>`
- Restore the file to it's last committed state
