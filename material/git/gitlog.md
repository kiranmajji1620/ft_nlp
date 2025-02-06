- shows commit hashes, authors, dates, commit messages

`git log`
- shows logs in reverse chronological order

`git log --oneline`
- shows short commit hash and message

`git log --oneline --all --graph`
- shows log in oneline as a graph

`git log -p`
- show log with line by line changes

`git log --author="name"`
- filter logs of the author 

`git log --grep="keyword"`
- show commit messages for a specific keyword.

`git log --since=""` & `git log --until=""` & `git log --since="" --until=""`

`git log --stat`
- show summary of changed files in each commit

`git log --pretty=format:"%a %an"`
- customizes logs using place holders

`git log -n 5`
- display the last 5 commits

`git log --follow<file>`
- show history of a single file, even if it was renamed.

`git log -all`
- show commit of all branches

`git log --reverse`
- show commits in chronological order