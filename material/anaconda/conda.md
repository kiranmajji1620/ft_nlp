### Commands

#### Managing conda
- `conda update conda` update conda to latest version
- `conda info` insatallation deatils
- `conda list` show installed packages in the active environment

#### Managing environments
- `conda create --name myenv python=3.9`
- `conda activate myenv`
- `conda deactivate`
- `conda env list`
- `conda remove --name myenv --all` delete the environment and also remove all packages associated with it.


#### Managing packages
- `conda install numpy pandas` install in current env
- `conda install -n myenv scipy` install in specific env
- `conda update numpy` 
- `conda remove numpy` - any package installed using pip can't be removed using conda.
- `conda remove --name myenv numpy` removes only numpy from myenv
- `conda search scikit-learn` search for a package in conda repositories

#### Handling dependencies 
- `conda list --explicit > explicit_file.txt` export all installed packages with exact packages and URLs.
    - useful for cloning environments exactly as they are
- `conda env export > environment.yml` export environment configuration to .yaml file
- `conda env create -f environment.yml` create an environment from .yml file

#### Channels and Package sources
- `conda config --add channels conda-forge` add a new package channel
- `conda config --show-sources` show current channels
- `conda config --remove channels conda-forge` remove a channel

#### Miscellaneous
- `conda clean --all` remove cached package files and free space
- `conda info --envs` show all available environments


#### `conda list` vs `conda list --explicit`
- `conda list` 
    - includes package name, version, build
    - not suitable for replication as it doesn't include exact channels or exact build source
    - might lead to inconsistencies as it doesn't include platform specific URLs.
- `conda list --explicit` 
    - includes exact package URL, with channel and architecture
    - Suitable for replication as it ensures exact same versions, builds and sources
- If you want reproducibility, use `conda list --explicit > explicit_list.txt` and recreate it with `conda create --name myenv --file explicit_list.txt`
- If you just need a list of installed packages, use `conda list > requirements.txt`


### Environment variables in conda
- two methods : env_vars 
#### using `conda env config vars`
- `conda env config vars set MY_VAR=value`
- `conda env config vars list` to verify the variable
- When we activate the environment, it will available, and when deactivated it is removed.
#### using `activate.d` and `deactivate.d` scripts
- conda allows you to run scripts when activating/deactivating an environment.
- you can create these scripts inside your environment directory.
- Create `activate.d` file
```
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export MY_VAR="value"' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```
- Create `deactivate.d` file
```
mkdir -p $CONDA_PREFIX/etc/conda/deactivate.d
echo 'unset MY_VAR' > $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
```
- If set using `conda env config vars` variables disappear after deactivating.
- If set using `activate.d/deactivate.d`, the unset command in deactivate.d ensures that are removed.
- If they are present in environment.yaml file, they will be activated and deactivated with environment itself.
- If manually exported `export var=value` the variable remains globally unless explicitly unset.

### Exporting a conda environment
- `conda env export > environment.yml`, it generates a YAML file that contains all the necessary information to recreate the exact same environment on another system
- **YAML file** :human readable data format that stores structured information. It is commonly used for configuration files
- A conda `environment.yml` file describes an environment including
    - environment name
    - python version
    - installed packages(with versions)
    - channels
    - environment variables
- Structure
```
name: myenv                    # Environment name
channels:                      # Package sources
  - conda-forge
  - defaults
dependencies:                   # Installed packages
  - python=3.9
  - numpy=1.23.5
  - pandas=1.5.3
  - pip:
      - tensorflow==2.10.0       # Pip-installed packages
variables:                      # Environment variables (if set)
  MY_VAR: "some_value"
```
- always export `environment.yaml` to ensure reproducibility across sytems.

### Conda resolving dependency conflicts
- A dependency conflict occurs when two or more packages require different versions of the same dependency
- eg : tensorflow requires numpy 1.2 and scikitlearn requires numpy 1.23
- conda/pip cannot install both of them in same directory => dependency conflict.
- Conda automatically finds a compatible set of package versions by using dependency resolution algorithms.
    - dependency solver
    - backtracking and optimization
    - strict vs flexible resolution
        - if strict resolution is enabled, conda refuses to install conflicting packages
        - if flexibility is allowed, conda may downgrad or replace some packages to satisfy dependencies.
- strict resolution is enabled by default in coda, so if there's a conflict, conda will print an error message and suggest a resolution.
- `codna install tensforflow scikit-learn --solve=libmamba` to force conda to find the best solution. libmamba is a faster dependency solver introduced in conda 22.11
#### Tips
- keep different projects in separate environments
- specify versions carefully `conda install numpy=1.24 tensorflow=2.10`
- use conda forge for better compatibility, some packages are better maintained on conda forge. `conda install -c conda-forge tensorflow scikit-learn`
- check dependency information before installing `conda search tensorflow --info`