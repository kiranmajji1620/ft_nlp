### Poetry
- dependency resolution, package management and environment management tool
- `poetry.lock` : lock dependencies -> replicate exact environment and reproducibility, built using .toml file
- `pyproject.toml` : setup tool -> contains possible package version dependencies, build systems -> used to build .lock file
- lock file has both direct and indirect dependencies but toml file has only direct dependencies.
#### Commands
- `pipx upgrade poetry`
- `poetry config --list`
- `poetry env list`
- `poetry env use <>`
- `poetry remove -all`
- `poetry add <>==`
- `peotry add requests@latest` forced install
- `poetry remove <>`
- `poetry add --group dev black flake8 isort mypy pylint`
- `poetry add pytest --dev`
- `poetry install --without dev`
- `--all-extras` 
- `--extras <extra1> --extras <extra2>`
- `--with <optional groups>`
- `poetry lock`
- `poetry lock --no-update`
- `poetry show`
- `poetry show --tree`
- `poetry show --top-level`
- `poetry show --latest --top-level`
- `poetry install`
- `poetry update` : `poetry lock` + `poetry install`
- `poetry update --dry-run`
- `poetry update reqeusts numpy`
- `poetry self add poetry-plugin-export`
- `poetry export --output requirements.txt`
- `poetry export --output requirements.txt --with dev, test`
- `poetry export --output requirements.txt --only dev, test`
- ``

#### Virtual management
- doesn't create right away
- detect one or create one when use poetry commands, uses venv
- `poetry env use python3` - error if not compatible
- after creation `<project-name>-<base64-hash>-py<python-version>` - change location -> relocate environment -> hash code

#### Dependency management
- `poetry add <>` -> find compatible package and install -> add to .toml file -> add to .lock
- installs packages group wise, uses poetry-core not pip, installs from pypi
- manage dependencies at project level not env level like conda
- `poetry install` if .lock is there, install from there or else if .toml file changed, update .lock and install.
- group dependencies, optional dependencies, extras
- `poetry remove` remove transitive dependencies as well (absent in pip)
##### Groups
- by default `poetry install` will install all groups
- Optionals and extras(sets of optional dependencies)

### `.lock`
- will automatically update .lock from .toml when in cmd
- **dependency locking** : 
    - resolving : find compatible packages
    - pinning : put in .lock file
- if changed .toml file or to sync it : `poetry lock` -> `poetry install` 
- don't want to update dependencies then `poetry lock --no-update`

### Poetry in other directories
- use `poetry init` add details interactively
- 