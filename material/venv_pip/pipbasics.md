- Sources 
    - [create python package](https://www.freecodecamp.org/news/build-your-first-python-package/)
### Package
- Way to organize and structure code by grouping related modules into directories.
- A folder that contains an __init.py__ file and one or more python files(modules)
- Module : single python file containing reusable code
- Package : directory containing modules and a special __init.py__ file.
- Sub-Packages : Packages nested within other packages for deeper organization.

### Package Manager
- a package manager is a tool that automates the process of installing, updating, configuring and managing software packages (libraris, dependencies or applications)
- Installation, Dependency management, version control, updates and uninstallation
- Python : pip, conda
- Linux : apt, yum, pacman
- Javascript : npm, yarn
- MacOs : brew

### Software repository
- Centralized storage location where software packages, libraries or dependencies are hosted, maintained and distributed.
- Package managers use repositories to fetch and install software.
- Java : maven central, j center
- Python : Pypi, conda forge, anaconda
- Javascript : npm, yarn.

#### PyPi
- Python package index is the official repository for python packages. It allows developers to publish, distribute and install python libraries using pip.
- Features : hosts thousands of opensource packages, used with pip, supports versioning and dependency management.
- Allows multiple versions of a package to exist simultaneously, you can install any package of any version you want.
- When a package is installed, pypi ensures all required dependencies are also installed.
- `pip install pandas` to install pandas
- `pip show pandas` to see dependencies before installing
- `pip install --upgrade --no-cache-dir pandas` to resolve dependency conflicts.
- `pip install -r requirements.txt` to install consistent versions across different environments.


#### Components of a package
- Directory
- init.py : executed when package is imported. can contain code to initialize the package as well as definitions for variables, functions, classes that are accessible to other modules within the package.
- Module : contains code that can be executed or imported by other modules. A package can contain one or more modules
- subpackages : a package can contain one or more sub packages which are themselves packages that contain their own modules and subpackages.
- Setup file : defines metadata about the package : name, version, author, dependencies. used by package managers like pip to install package and it's dependencies
- Read me : provides information about package : purpose, installation and instructoins, usage examples
- License : specifies the terms under which the package can be used.

### Usage
- `pip install packagename`
- `pip install packagename==1.2`
- `pip install -r requirements.txt`
- `pip install --user package-name`
- `pip install --upgrade packagename`
- `pip install --index-url url-of-a-private-repo library_name`
- `pip uninstall packagename`
- `pip list` human readable output.
- `pip list --outdated`
- `pip freeze` generate a list of installed packages with versions for req.txt like pandas==1.2
- `pip show packagename`

### Creating and uploading a package to pypi

#### Creating a project directory
- `mkdir mypackage` : contain all the files and directories necessary for the package.
- `cd mypackage`
#### Create a package directory
- Create a new directory inside the project directory to hold the package code.
- `mkdir mypackage`
#### Create a module file
- Create a new python file to hold the package code, should have same name as package.
- `mypackage.py`
#### Write the package code
- Write package code - functions, classes, variables
#### Create a setup.py file
- setup.py should contain metadata.
#### Build the package
- `python setup.py sdist`
#### Upload the package to pypi
- `twine upload dist/*`
#### Install the package
- `pip install mypackage`

### Example
- Directory structure: 
- ![folder structure](/assets/images/Screenshot%20from%202025-02-03%2016-08-40.png)
- Write your python code in module.py
- in init.py of my_package/my_package, import all `from .module1 import great`
- Create setup.py
- Build the package `python3 setup.py sdist bdist_wheel`
- upload to pip : `twine upload dist/*` or download in local using `pip install .`
- When building the package, use `pip install -e .` this specifies python not to make a copy of the code into the python intepretor folder. instead it makes reference to the code that we are editing. So, any change we make will show up when we reload python.
- use `my_package.add()`

### Installing python packages
- Using `requirements.txt`
    - say `pip install -r requirements.txt`
    - To create a requirements.txt, Create an empty file and say `pip freeze > requirements.txt`
    - Used in setting up an environment

- Using `setup.py`
    - `pip install .` or `pip setup.py install`
    - Used in distributing and installing a package.
    - presence of which is an indiaction that the package has likely been packaged and distributed with distutils which is standard for distributing python modules.
- ![differences](/assets/images/Pasted%20image.png)

## Site packages vs Dist packages
### Site Packages
- python packages are typically installed into the site-packages directory, which is where third party packages are stored for use in environments(globally or virtual environment)
- Location : usr/local/lib/pythonX.Y/site-packages
- Location in virtual env : /path to venv/lib/python3/site-packages
- site packages is the default directory where python stores third part libraries that you install using pip or any other package manager.
### Dist packages
- a directory that is used in some linux distros like debian for storing python packages installed through system package managers like apt or yum
- similar to site packages, but is specific to linux distros and can be seen in system wide installations.

### Editable mode
- allows you to install a python package in a way that lets you modify the source code without having to re install the package everytime you make changes.
- `pip install -e .`, . can be replaced with path to the package directory.
- Working : When you install a package in editable mode, pip creates a symlink to the package's source directory in site packages directory, rather than copying the package files.
- Any changes that you make to the source code will immediately take effect without needing to re install the package.
- Ideal for active development, as it allows testing changes without interrupting workflow.

#### difference between .whl and other formats
- ![comparision](/assets/images/Pasted%20image%20(2).png)