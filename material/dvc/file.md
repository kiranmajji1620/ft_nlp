### DVC
- in a vcs, there is a central reopsitory of code that represents the current state of project. a developer can make a copy of that project, make changes and push it. code is reviewed and then tested and production
- DVC is a set of tools and processes that tries to adapth the VCS to data.
- runs along side git.

### .dvc file
- small text file that points to your actual data files in remote storage.

#### Track files
- add your `train` and `val` to .gitignore
- save the new version of data file in a cached directory
- creates two files with `train.dvc` and `val.dvc`
- contains metadata about version of original file
- adds the data to .gitignore
- Large files go to dvc remote storage, small files like .dvc go to git. git tracks all .dvc files
- on running `dvc add train/` train goes to dvc control and .dvc goes to git control
- after dvc add, run `git add --all` to add small files to git control

#### Upload files
- not like git commit, dvc adds the data to cache during add, if you made local change, then commit so that you change cache.
- upload using dvc push
    - dvc will look through all folders to find .dvc files
    - these .dvc files tell tell DVC what data needs to be backedup, and dvc will copy them from the cache to remote storage.

#### Download files
- get .dvc files from git and then do 
- can download from cache or from remote
- (fetch to cache, and then checkout) or pull

#### MD5
- hashing function - 32 chars
- based on this hash value, dvc keeps track of which files have changed
- store only in one of cache or remote for large files.

### Share a development machine
- dvc allows a shared cache between users
- during dvc init, it will put cache in repository's .dvc/cache folder
- change that cache to another location shared by others. and move the files.
- can use links like reflinks(default) or symlinks or hardlinks

### Reproducible pipelines
- chain multiple processes together into a single execution called pipeline.
- a pipline has multiple stages and each stage contains
    - inputs(dependencies), outputs(outs), command
- a pipeline will automatically add newly created files to dvc control.
- it will be confused if we create same files so remove any existing files
- dvc stage add, give dependencies, outs, commands
- reproduce the entire workflow with `dvc repro evaluate`

### Commands
- `dvc init`
- `dvc remote add origin -d PATH`
- `dvc add data/raw/train`
- `dvc commit`
- `dvc push`
- `dvc checkout data/raw/val.dvc`
- `dvc checkout` search and checkout what's missing
- `dvc checkout --relink` check the dvc cache type, relink all the files tracked by dvc
- `dvc fetch data/raw/val.dvc` will fetch val from remote to cache
- `dvc pull` fetch + checkout
- `dvc remote data/add`
- `dvc cache dir path/to/shared_cache`
- `dvc config cache.type symlink` 
- `dvc metrics show`
- `dvc metrics show -T`
- `dvc stage add -n evalueate \ `
- `dvc status`