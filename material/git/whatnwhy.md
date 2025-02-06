# Version Control Basics

### What is VC?
software tools that help in recording changes made to files by keeping track of modification done in the code.


### Why VC?
- A software product is developed by several devs and each dev has a separate element to work upon.
- A VCS helps devs to efficiently communicate and track all the changes that have been made to the source code along with who made and what changes were made.
- A separate branch is created for every contributor and changes are merged when green siganlled.
- We can always omit the new changes and restore the older version if necessary.

### What is git
- global information tracker, git is a version control system that helps developers to track and manage changes to code.s

### Repository
- can be thought of as a database of changes, contains all the edits and historical versions(snapshots) of the project.

Types of Version control systems:  
- Local VCS
    - keeps patch sets(difference between files) in a special format on disk.
    - By adding up all the patches, it can then recreate file at anypoint of time
- Centralized VCS
    - Contains only one repository globally and every user needs to commit to see the changes.
    - Need to update to see the changes.
    - Single point of failure.
- Distributed VCS
    - Each user has their own repository
    - Committed changes will reflect on your own copy. 
    - Need to push to make them visible globally.
    - Commit -> Push -> Pull -> Update.


### Why version control
- Multiple people can work simultaneously on a single project.
- Integrates  the work that is done by differrent mems of team.
- Can easily roll back if mistakes are done.
- Possible to undo specific changes without losing the updates made meanwhile. (git revert)


### What is git head
- head is a special commit reference that generally points to the currently checked out commit.

### detached head
- When we checkout a commit, the head will point to that commit and not to the latest commit.
- Any new commits will be lost unless we make a separate branch from that commit.

- `git reset --hard HEAD~2` to move back head 2 commits back ward and discard the changes from the later commits.

`git show head`
- show the latest commit

`git checkout -- .`
- reset to the last committed state

## gitignore
- secret.txt -> ignore this
- *.log ignore all log files
- /node_modules/ -> ignore this directory
- .env !.env.example -> ignore all env files but not this one
- log/ ignore files in sub directory
- *.txt !imp.txt -> ignore all txt files except for imp.txt
-

- If you create .gitignore after some files have been tracked, git will not remove those already tracked files
- `git rm -r cached` -> this will remove all files from index. now re add only the non ignored files.
- `git status --ignored` -> shows the ignored files.