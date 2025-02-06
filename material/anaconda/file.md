- Anaconda is a full distribution with many pre installed libraries
- Miniconda is a light weight versoin of anaconda giving freedom to install only the libraries you need
- Conda is the core package/environment management tool that both anaconda and mini conda use.
### Conda
- Conda is a package management system and environment management system. Allows to easily install, update and manage libraries and tools, as well as create isolated environments for different projects. 
- Conda works with python, R and other projects.

### Anaconda
- Distribution of python and R for scientific computing and data science.
- Includes conda but also comes with lot of additional packages as well as tools like jupyter notebook, spyder.
- Full featured distriubution that makes it easier to get started with data science tasks, since it bundles many commonly used libraries.

### Miniconda
- Minimal version of anaconda, only comes with conda, bare minimum python.
- Allows you to install only the packages you need, giving you more control over what gets installed.

### removing conda
- `rm -rf ~/miniconda3` at the home directory
- conda stores configuration files like .condarc and environment files in your home directory. remove them.
- `rm -rf ~/.condarc`
- `rm -rf ~/.conda`
- `rm -rf ~/.continuum`
- if conda is still present in your path, manually edit the path in the system environment variables.
- open `.bashrc` file and remove any lines that reference miniconda.
## important points
### conda versoin dependency
#### how conda determines the version to install
- when we say conda install, conda will install the latest compatible version of the package available in the default of specified channel for your current environment.
##### current environments dependencies
- conda will check the current environments configuration(python version, other installed packages). It will only install a version of numpy that is compatible with current environment
##### available version in channel
- Conda looks for available versions of numpy in the specified channels (usually defaults or conda-forge). It will prioritize installing the most recent stable version that works with the dependencies in your environment.
##### solving for dependencies
- Conda solves for all package dependencies when you install something. If numpy requires other specific versions of packages (like numpy-base, setuptools, etc.), it will attempt to install those too, based on compatibility.
##### pinned package versions
- If you have pinned versions of certain packages or strict dependencies in your environment (from an environment.yml file or previous installs), Conda will respect those pins and might not install the latest version of numpy if it's incompatible with other pinned versions.

#### conda activate
- when shifting to another environment, deactivate the current environment and then go, or else deactivate the current env after deactivating the future env.