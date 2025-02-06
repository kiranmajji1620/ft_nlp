## git restore
- Unstage a file
    - `git restore --staged file.txt`
- Discard from unstage 
    - `git restore file.txt`
- Go to last commit stage
    - `git restore .`
- Bring the directory to the stage of a commit hash
    - `git restore --source=commithash`
    - now, stage them and commit them. => history is preserved

## git reset
- using restore, we can change the content of current directory to required commit's snapshot

## git reset --mixed <hash commit>
- commit history lost
- Changes after the last commit until the latest commit will be brought to the working directory
- Moves head and unstages the changes, the working directory remains unchanged since these are the changes that happened after the hash commit.

## git reset --soft <hash commit>
- Changes will not be discarded, will be brought to the staging area.
- The head will be brought back to that commit, Now we can commit the changes after the hash commit.
- Changes are staged

## git reset --hard
- Bring the working directory, head, commit history at the point of commit hash.

- `git reset` = `git reset --mixed`
- Undo the staged changes

#### Undo a commit
- `git reset --soft HEAD~1`
- Undo the last commit but keep changes in staging area.

#### Undo a commit and unstage the changes
- `git reset --mixed HEAD~1`
- Undo the last commit and unstage changes
- `git reset` is `git reset --mixed last commit` which will undo the staged changes and bring them to directory.

#### You made changes and want to completely throw them away
- `git reset --hard ` - discard changes and reset to the last commit.

#### Reset to a specific commit, keeping changes in the working directory
- `git reset --soft <commit hash>`

#### Reset code to a specific commit, unstage changes and keep them in working directory
- `git reset --mixed <commit hash>`

#### Reset to specific commit, discarding all changes
- `git reset --hard <commit hash>`
- All the commits made after commit hash will be discarded