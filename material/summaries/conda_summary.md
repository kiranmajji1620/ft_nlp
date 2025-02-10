### anaconda vs miniconda vs conda
- anaconda : distribution of python and R for data science and ML, comes with pre installed libraries
- miniconda : minimal version of anaconda with bare minimum python and no extra libraries
- conda : core environment management and package management tool that is used by anaconda and miniconda


### Version dependency in conda
- `conda install` will find the latest version compatible with current environment configuration and installs the indirect dependencies as well
- looks in default anaconda repository. can add conda forge channel as well
- conda installs packages in a directory and each environment will symlink to that folders data reducing redundancy and duplication


### commands
- `conda update conda` 
- `conda info`
- `conda list` in active environment

#### manage environments
- `conda create --name myenv python=3.9`
- `conda activate myenv`
- `conda deactivate`
- `conda env list`
- `conda remove --name myenv --all` delete the environment and also remove all packages associated with it.

#### handling dependencies
- `conda install numpy pandas` install in current env
- `conda install -n myenv scipy` install in specific env
- `conda install -c conda-forge tensorflow scikit-learn`
- `conda update numpy` 
- `conda remove numpy` - any package installed using pip can't be removed using conda.
- `conda remove --name myenv numpy` 
- `conda search scikit-learn` 

#### export/recreate environments
- `conda list --explicit > explicit_file.txt` export all installed packages with exact packages and URLs.
    - useful for cloning environments exactly as they are
- `conda env export > environment.yml`
- `conda env create -f environment.yml`
- `conda create --name myenv --file explicit_list.txt` 

#### channels
- `conda config --add channels conda-forge`
- `conda config --show-sources` show current channels
- `conda config --remove channels conda-forge`

#### environment variables
- `conda env config vars set MY_VAR=value`
- `conda env config vars list` 

#### others
- `conda clean --all` remove cached package files and free space
- `conda info --envs` show all available environments

#### conda list vs conda list --explicit
- conda list gives only packages and versions, but explicit includes channels, build versions, systems

#### env variables
- set using env config, set using .yaml, set using actvate.d -> conda automatically deactivates

#### .yml file
- contains name, python version, channels, dependencies, env variables

### Conda resolving dependency conflicts
- Conda automatically finds a compatible set of package versions by using dependency resolution algorithms.
    - dependency solver
    - backtracking and optimization
    - strict vs flexible resolution
        - if strict resolution is enabled, conda refuses to install conflicting packages
        - if flexibility is allowed, conda may downgrad or replace some packages to satisfy dependencies.
- strict resolution is enabled by default in coda, so if there's a conflict, conda will print an error message and suggest a resolution.
- `codna install tensforflow scikit-learn --solve=libmamba` to force conda to find the best solution. libmamba is a faster dependency solver introduced in conda 22.11