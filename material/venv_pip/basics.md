## Virtual environment
- Self contained, isolated directory where you can install python packages and manage dependencies - independently of your system wide python installation and other projects.
- Mini independent python setup for each project.
- Helps avoid conflicts between different projects that may require different versions of the same package.

#### Why do you need virtual environment??
- Python isn't that great at dependency management.
- if not specific, pip will plave all the external packages that you install in a folder called site-packages/ in your base python installation.
- Avoid system pollution
    - Linux and mac come preinstalled with a version of python that the os uses for internal tasks.
    - Installing packages into global python, these packages will mix with system relevant packages. 
    - This mix up could have side effects on crucial os internal tasks
    - Also, in the event of os update, packages might get overwritten and lost.
- Sidestep dependency conflicts
    - One project might require a different version of an external library compared to another project.
    - If you have only one place to install packages, you won't be able to work with two different versions of samelibrary as you only have the latest version of package.
- Reproducibility issues:
    - To share the Dependencies relevant to your project, you have to manually go through the dependencies and know which are necessary for your project and which aren't. -> tedious and error prone.
    - Using a separate virtual environment, it'll be more straightforward to read the project requirements from your pinned dependencies.
- Dodge installation privilige lockouts
    - You may need administration priviliges on a computer to install packages into host python's site pakages directory.
    - using virtual environment, you create a new installation location within scope of user priviliges, allowing work with external packages.

#### Working
- When you create a virtual environment, it creates a folder that contains its own python binary and a separate place to install packages.
- venv reproduces the folder structure that a standard python installation creates
- This structure accounts for the location of the symlink of the python binary and the site packages directory, where python installs external packages.
- You can access python's standard library modules because your virtual environment re uses python's built ins and standard library modules from the python installation you used to create your virtual environment.
- with standard folder structure in place, python interpretor in your virtual environment can understand where all the relevant files are located.
- You activate it and then anything you install using pip or conda goes into that environment, not the system wide installation.

#### Python's venv
- venv module is part of python's standard library from python3.5
- `python3 -m venv venv1/` to create a virtual environment
- `source venv/bin/activate` to activate the venv1
- `python -m pip install <package>` to install a package in this environment
- as long as you don't close your terminal, every package that is installed will end up in this environment instead of global python site packages.
- `deactivate` to deactivate. 

### Python's virtualenv
- specifically made for creating isolated python environments
- superset of venv
    - create more quickly
    - discover installed versions  of python without needing to provide the absolute path
    - Upgrade the tool using pip
    - Extend the functionality of the tool yourself
- `virtualenv venv/` to create
- creates the isolated environment much more quicker because the tool caches platform specific application data which it can quickly read from.
- advantages of virtualenv over venv
    - Speed
    - Updates : embedded wheels, you'll receive up to date pip and setuptools without needing to connect to internet right when you first set up virtual environment


### Conda
- package and environment management tool that can replace pip and venv.
- package, dependency, environment management for any language.
- pip installs python packages within an environment, conda installs any packages within conda environments.
- in it's default configuration, conda gets its packages from repo.anaconda.com instead of the python package index.
- This alternative package index is maintained by anaconda project and is similar to pypi but not identical
- you can find other data science related packages on conda's package index written in different languages.
- coversely, ther are python packages available on pypi but not on conda repository.
- can install such packages using pip.
- conda envs are located in `conda/envs/` directory
- venv are created locally in project directory.

### Difference between conda and python venv