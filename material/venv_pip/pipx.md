#### pip vs pipx
- pip is used to install python packages globally or within virtual environments, while pipx installs and isolate python applications in separate environments, making it ideal for managing tools that are run as standalone programs

### PIP
- standard tool used to install python libraries and packages, both globally and in virtual environment. handles the installation of dependencies and allows you to work with python packages across projects.
- packages can be installed from pypi or repos

### pipx
- tool designed to install and run python applications in isolated environments. particularly useful for managing python tools that you run as as standalone applications, rather than integrating them into a project as libraries.
- automatically creates a virtual environment for each application it installs
- designed for applications or command line tools that are installed globally and should run independently of other python packages or projects
- ensures isolation to prevent conflicts between tool versions and dependencies.
- ideal for managing tools like black, flask etc

#### when to use what
- standalone tools:
    - want to run directly from cmd
    - use pipx
    - linter(flake), flask, cli application(httpie)
- avoiding dependency conflicts:
    - use pipx
- global tools installations with isolation:
    - use pipx
- for libraries withing a project
    - use pip to manage project specific dependencies.

### How does pipx work
- when you install poetry with pipx, it creates an isolated virtual environment specifically for poetry and it installs it there.
- pipx then symlinks the poetry executable to a directory that is included in your system's path making it accessible globally.

### commands
- `pipx install poetry`
- `poetry --version`
- `pipx list`
- `pipx run poetry --version`