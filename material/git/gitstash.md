- takes the uncommitted staged and unstaged changes and reverts back working dir to head commit.
- temporarily put files on side while merge rebase a branch
- can store multiple stashes in a stack
- Can create a stash from a branch and pop it to another file.
- Can have merge conflicts.


- By default git stash is only gonna track the tracked files
- Use git add.

#### `git stash`
- sets aside all the staged changes in a stack

#### `git stash list`
- list all stashes

#### `git stash show`
- show files in stash.

#### `git stash pop`
- Pop the last stash and apply them to working directory

#### `git stash -m "navbar v1"`
- Name the current stash

#### `git stash pop --index 1`
- pop index 1 stash

#### `git stash branch nav 1`
- Reincarnate index 1 stash to another branch named nav
- A new branch named nav is created.

#### `git stash clear`
- Clear entire stash

#### `git stash drop stash@{0}` or `drop 0`
- Drop that stash