### Poetry
- poetry is a dependency management and packaging tool for python
- handles dependency resolution, pacakge management and virtual environments aimint to replace pip(poetry add), virtualenv(poetry env) and setuptools(pyproject.toml)
- uses venv, has its own package installer & dependency resolver(not pip)
#### Create a new poetry project
- `poetry new rp-poetry` creates a new folder in **flat layout**
```
rp-poetry/
│
├── rp_poetry/
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── README.md
└── pyproject.toml
```
- poetry changed (-) to an (_). the tool automatically normalizes python package names for you.
- ensures you'll be able to import them as python packages.
- to have more control over the package name, pass `poetry new rp-poetry --name realpoetry`
- using **src layout**
- `poetry new rp-poetry --src`
```
rp-poetry/
│
├── src/
│   │
│   └── rp_poetry/
│       └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── README.md
└── pyproject.toml
```
- existence of `__init__.py` will turn it into a package.

### Virtual environment
- poetry has virtual environment management.
- but it **doesn't create one right away** when you start a new project -> let you decide whether you want to manage your virtual environments yourself or let poetry handle them for you automatically.
- it will **detect a manually activated virtual environment** when you run one of the poetry comnands in project folder
- `poetry env info --path`
- If you already have an active environment, poetry confirms it'll use that env for all subsequent commands withint your project's scope.
- adding dependencies -> we'll install them into the activated environment as if with the regular pip install command. poetry would also update the necessary metadata in pyproject.toml.
- poetry **automatically creates / reuses one it created before when you run certain commands without an activated environment** in shell.
    - like when you add or remove a dependency using poetry cli.
    - prevents projects from messing ups with system wide python installation.
- it maintians a virtual environment for all the projects 
- when we run a poetry command, it will see if it has already created a virtual environment for it before. If yes, it will re use it.
- letting poetry create virtual environments on its own is the preffered way of listing dependencies in your projects.
- deactivate your conda env and now onwards peotry will take care of virtual environments.
- `poetry env use python3` specify the path to a desired python interpretor on your disk.
- If we explicitly tell which python version to use, it must satisfy **version constraint** in your pyproject.toml file. otherwise poetry will reject it with an **error** message.
- after executing the above command, poetry will create a virtual environment
#### Creation
- constructs a unique name, contains package name from pyproject.toml. 
- `<project-name>-<base64-hash>-py<python-version>`
- random string in the middle is base64 encoded **hash** value of the absolute **path leading up to your pojects parent directory**.
    - ensures that each project has its own separate virtual environment.
- ties the name of a virtual environment to your projec'ts locatoin on disk.
- If you **move the project to another folder**, poetry will detect that and **create a brand new virtual environment** behind the scenes if necessary.
- due to unique string, it can handle multiple projects with identical names and the same python version while keeping all virtual environments in one folder by default at `/.cache/pypoetry/virtualenvs/`
- `poetry config --list` reveal current poetry configuration.
- as long as you are in the folder, poetry will use the virtual environment associated with it. 
- although `poetry env list` shows an environment activated, corresponding virtual environment isn't actually activated in your shell in the traditional sense.
- Instead poetry will temporarily activate that virtual environment ina sub process when you run one of the poetry commands.
- `poetry env use <>` to switch between environments
- `poetry env remove -all`

### Declare runtime dependencies
- we can add the packages manually in pyproject.toml file but it is tedious and doesn't actually install packages into our current environment.
- running the `poetry add` will automatically update your pyproject.toml file with new dependency and install the package at the same time. 
- `poetry add requests beautifulsoup4`
- this will find the latest versions of both in pypi, install them in corresponding environment and insert the declarations in pyproject file.
```
[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp Acsany <philipp@realpython.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.31.0"
beautifulsoup4 = "^4.12.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
- **`^`** indicates that poetry is free to install any version matching the leftmost non zero digit of the version string.
- if requests library releases a new version 2.99.99, poetry will consider it an acceptable candidate but not 3.0
- `poetry add requests==2.25.1 "beautifulsoup4<4.10"`
- "" used to prevent the shell from interpreting < as a redirection parameter.
- remove any previously installed packages and downgrade their indirect or transitive dependencies to ensure compatibility.
- it'll then determine the most suitable versions of these packages, taking into account other existing constraints to resolve poetential conflicts.
#### remove dependency
- `poetry remove requests`
- it'll **remove current dependency along with its transitive dependencies**, so don't have to worry about lefover packages that are no longer needed by your project.
- advantage over **plain pip which will uninstall only individual packages**.

### Group dependencies
- allows you to keep logically related dependencies separate from your runtim dependencies.
- during development you might want linters, type checkers, testing frameworks. not needed to users.
- not available in pip
- `poetry add --group dev black flake8 isort mypy pylint`
- `poetry add --group test pytest faker`
```
[tool.poetry.group.dev.dependencies]
black = "^24.1.1"
flake8 = "^7.0.0"
isort = "^5.13.2"
mypy = "^1.8.0"
pylint = "^3.0.3"

[tool.poetry.group.test.dependencies]
pytest = "^8.0.0"
faker = "^22.6.0"
```
- not giving a group name will put the dependencies into the main group which is why you it is reserved.
#### optional dependencies
```
# ...

[tool.poetry.group.test]
optional = true

[tool.poetry.group.test.dependencies]
pytest = "^8.0.0"
faker = "^22.6.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
- Poetry won’t install dependencies belonging to such a group unless you explicitly instruct it to by using the --with option. Note that you must declare another TOML subtable to mark a group as optional because the group’s configuration is kept separately from its dependency list.
- `$ poetry add --optional mysqlclient psycopg2-binary`
- Optional dependencies are meant to be available at runtime when explicitly requested by the user during installation. It’s common to mark packages as optional when they’re platform-specific or when they provide features, such as a particular database adapter, that only some users will need.
```
mysqlclient = {version = "^2.2.1", optional = true}
psycopg2-binary = {version = "^2.9.9", optional = true}
```
#### extras
- sets of optional dependencies
```
[tool.poetry.extras]
databases = ["mysqlclient", "psycopg2-binary"]
mysql = ["mysqlclient"]
pgsql = ["psycopg2-binary"]
```
## .lock
### Install your package with poetry
- `rm poetry.lock`, `poetry env remove -all`
- clone a git repo
- go to folder, say `poetry install`
- if there is `poetry.lock`, it'll reproduce the exact same file or else, read pyprojec.toml and will resolve the set of packages satisfying the version constraints.
- you'll have new `poetry.lock` file
- **Dependency resolution** : before installing each packages, poetry figures out which version of package fulfills versoin constraints. solution may not even exist.
- won't automatically install extra sets of dependencies and optional groups of dependencies.
- `--all-extras` 
- `--extras <extra1> --extras <extra2>`
- `--with <optional groups>`
- when you install extras, only the extras specified on the cmd will be installed others will be removed.

#### Manually install
- update .toml file to contain the wanted dependency. if not sure add `requests="*"`
- run `poetry install` will not work 
- because poetry will install dependencies only from poetry.lock file
- it will use the .toml file only to sync the .lock file or if the .lock file is missing
- either delete `.lock` and run `poetry install` -> new .lock file
- or `poetry lock` -> align the two file my manually locking.
- it also recursively traverses and locks all indirect dependencies.
- in addition to resolving dependencies, it will update to the new versions if available 
- `poetry lock --no-update` only resolves new dependency versions in .lock file

#### leftover environment packages
- `poetry sync` install .lock packages and remove unused packages.
- this will not work with conda environments as poetry's environment management is venv
- might work with venv environments.

#### Dependency update
- if new version came that is compatible, do 
- delete `poetry.lock` -> `poetry install`
- `poetry lock` -> `poetry install`
- `poetry update`
- `poetry add requests@latest` to install outside versoin compatibility or manually change the .toml file

#### git commiting
- when developing an application, commit .lock file to ensure reproducibility and not resolving .toml file everytime.
- when developint a library, don't do so as you want your library to be compatible with many package version.

### Exporting
- only adds direct dependencies
- can use `pip freeze > requirements.txt`
- or add poetry plugin `poetry self add poetry-plugin-export`
- say `poetry export --output requirements.txt` and `--with dev` and `--only dev`
- extras won't be added use `--extras extra1` or `--all-extras`

### GITHUB packages
- it will clone the whole repository and adds the package as dependencies
- repo must containt .toml or .setup.py!!
- `poetry add git+https://github.com/username/repository.git` adds default master branch
- `poetry add git+https://github.com/username/repository.git#branch`
- `poetry add git+https://github.com/username/repository.git#commit`
- `poetry add git+https://github.com/username/repository.git#tag`
- can use SSH url instead if dealing with private repository
- if you just want a specific module, you still need to get the whole repository.

### Local packages
- `poetry add ./local/`

### Uninstall poetry
- `pipx uninstall poetry`