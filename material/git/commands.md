### [Git clone](https://git-scm.com/docs/git-clone "git clone")
- Used to copy a repository from remote source to local machine.
- `git clone <reponame>` basic command to clone a repo.
- Completely isolated environment from the remote repository.

## What happens during git clone?
#### Cloning a repository

- Git creates a new directory where the content will be cloned.
- All the data from the source repository is fetched.
- A remote tracking branch is created for each branch in cloned repo. 
    - These remote tracking branches are to track the branches of remote repository
    - These stay in refs/remotes/origin/* like origin/main, origin/dev, origin/branch9.
    - They are not local repositories they are read only references to the state of the remote repository.  
    - Can be viewed using `git branch --remotes` 

#### Initial Branch Checkout

- After cloning, git automatically creates and checks out a local branch that corresponds to active branch in remote repo.
- If remote's active branch is main, git will create a local branch also named main and set it to track the remote branch origin/main 
- Now, running `git pull` will fetch and merge updates from origin/main.
- running `git push` will push changes to origin/main.
#### Fetching and pulling updates

- `git fetch` retrieves updates for all remote tracking branches
- `git pull` not only fetches these updates but also merges the changes from the remote branch(origin/main) into local branch(main)

#### Default configuration

- references to the remote repository branches are stored under `refs/remotes/origin`. these are remote tracking branches.
- Local repository might have `refs/remotes/origin/main` or `refs/remotes/origin/dev`.
- Configuration variables `remote.origin.url` and `remote.origin.fetch` are intitialized in `.git/config` file 

- Common sub commands
    - `git clone --depth 1 <repo>` to creates a shalow clone limiting the commit history. reduces time and disk space.
    - `git clone -b dev <repo>` Branch to checkout after cloning : If you don't want the default branch but need a specific branch.
    - `git clone --recurse-submodules <repo>` Needed when a repository contains sub modules 
    - `git clone --bare <repo>` Ideal for setting up remote repository that dosn't take any changes. only the `.git` is present
    - `git clone --mirror <repo>` Similar to a bare repo that will copy all references and remote configuration
    - `git clone -n <repo>` 


#### Git bare vs Git mirror
Git bare:  
- contains only meta data(.git) and doesn't have a working directory.
- used as a central repository for collaboration.
- Includes all branches, commits and tags. Does not include remote tracking branches, Does not configure remotes.

Git mirror:
- Exact replica of source repository includes all branches, tags, all references, remote tracking branches, remote configurations.