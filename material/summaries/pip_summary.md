### venv vs virtual env vs conda
- virtualenv is superset of venv, is faster and more efficient
- conda replaces pip + venv
- pip installs in any environment, conda installs in conda environments
- venvs are created locally, condas have a separate directory

### Packages
- way to organize and structure code by grouping related modules in a directorye, have __init__.py 
- directory has init, subpackages, readme, setup.py, license
- when a .py file is executed, all the files in that directory are added to sys.path file -> resolve imports
- `python3 -m tests.py` treats the file as a script instead of module and also all sub directories to sys.path

#### Package manager
- tool that automates the process of managing software packages : Installation, Dependency management, version control, updates and uninstallation
- software repository : Centralized storage location where software packages, libraries or dependencies are hosted, maintained and distributed.
- pypi : official sr of python

### Upload a packge
- `mkdir mypackage` : contain all the files and directories necessary for the package.
- `cd mypackage`
- `mkdir mypackage`
- `mypackage.py` - Write package code - functions, classes, variables
- `setup.py` should contain metadata.
- `python setup.py sdist`
- `twine upload dist/*`
- `pip install mypackage` or `pip install .` or `pip install -e .` for editable install, instead of copying to python, makes a symlink 


### Commands
- `pip install packagename`
- `pip install packagename==1.2`
- `pip install -r requirements.txt`
- `pip freeze > requirements.txt`
- `pip install --user package-name`
- `pip install --upgrade packagename`
- `pip install --no-deps` don't resolve deps    
- `pip install --index-url url-of-a-private-repo library_name`
- `pip uninstall packagename`
- `pip list` human readable output.
- `pip list --outdated`
- `pip freeze` generate a list of installed packages with versions for req.txt like pandas==1.2
- `pip show packagename`

#### setup.py vs req.txt
- req is for installing dependencies of a project
- setup is to build and distribute packages, indicates that package has been distributed with distutils

### site packages/dist packages
#### Site Packages
- python packages are typically installed into the site-packages directory, which is where third party packages are stored for use in environments(globally or virtual environment)
- Location : usr/local/lib/pythonX.Y/site-packages, Location in virtual env : /path to venv/lib/python3/site-packages
- site packages is the default directory where python stores third part libraries that you install using pip or any other package manager.
#### Dist packages
- a directory that is used in some linux distros like debian for storing python packages installed through system package managers like apt or yum
- similar to site packages, but is specific to linux distros and can be seen in system wide installations.

### .whls
- ![comparision](/material/assets/images/Pasted%20image%20(2).png)