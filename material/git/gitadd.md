- used to stage changes in git, meaning you mark the files that you want to include in the next commit.

### 1.Git staging area(index)
- git uses a staging area index to track which changes are ready to be committed. This acts as a buffer between working directory and repository.
- `git add` moves files from working directory to staging area.
- We can group a certain changes and commit them.

### 2. How git add works:
- `git add <file>` tells git to add changes in file to staging area.
- can stage multiple files, directories, changes.

### 3. Types of changes git add stages
- New files, Modified files, Deleted files

#### `git add file1.txt`
- stages file1

#### `git add .`
- stages all changes in current directory.

#### `git add -A`
stages all changes including new files, modified files, deletions

#### `git add -U`
- stages modified and deleted files, doesn't add new files

#### `git add -p .` or `--patch`
- interactively stage changes(hunks) -> y, n, q, a, d

#### `git add --dry-run .` or `-n`
- shows which files would be added without staging them.

#### `git add --intent-to-add`
- adds file to staging area but without staging it's contents. useful when keeping a file under version control but don't want to track changes yet.

#### `git add <directory>/`
- stages all changes within a specific directory and sub directories.

#### `git add -f secret_file.txt`
- Forces git to add ignored files(ignored by .gitignore)

#### `git add --no-all .`
- Avoids staging deletions, even if changes are tracked 