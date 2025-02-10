## Virtual environment
- Self contained, isolated directory where you can install python packages and manage dependencies - independently of your system wide python installation and other projects.
- Mini independent python setup for each project.
- Helps avoid conflicts between different projects that may require different versions of the same package.

#### Why do you need virtual environment??
- Python isn't that great at dependency management.
- pip might mess up system packages
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

### Pip vs Conda vs Poetry for Dependency management
- Pip : backtracking algorithm, installs packages incrementally 
    - download metadata for all dependencies, tries different versions until all constraints are satisfied, install resolved versions
    - dependency resolution happens during installation, making it less efficient
- Conda : SAT solver
    - ensures conflict free environment before installing anything.
    - fetch all dependencies -> constraint solving algorithm
    - prevents broken environments by resolving dependencies beforehand
- Poetry : Dependency graph resolver
    - similar to conda, resolve dependencies before installing and updates
    - ensures deterministic builds with .lock
- reproducibility is manual in pip, good in conda, excellent in poetry
- cause poetry ensures exact same package versions, including transitive dependencies, across all systems as it focuses only on python packages and their versions.
- conda takes different builds for same versions depending on time, os, system, channel