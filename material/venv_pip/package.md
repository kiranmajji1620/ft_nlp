### Python package
- A python package is essentially a folder that contains python files and is marked as a package by the presence of `__init__.py`
- This special file tells python that the directory should be treated as a package, allowing you to use import statements to reference modules inside that directory

#### sys.path
- sys.path is a list in python that contains directories where python looks for modules when you use import statements.
- These directories include
    - directory of currently executing script
    - directories specified in the pythonpath env variable
    - standard library directories
- when we run a python script, python needs to know where to search for the module or package you are importing.
- when we run a script directly `python3 test_area.py`, python only adds the current directory to sys.path. If the source folder as in `import area from source` is not in this directory, python won't find it by default.
- But when running pytest, pytest automatically adds the project root to sys.path before running the tests, which lets python find source even if it's not in the current directory.

### Does python remove something from sys.path after execution?
- does not remove automatically after exection
- how ever, it is populated based on the current working directory, pythonpath and other conditions. It will persist for the lifetime of the python process. 
- Once the python process terminates, modifications are removed.

### Running a module as a script
- `python3 test_area.py` won't work from tests directory as it requires an import from source directory
- in parent directory, run `python3 -m tests.test_area`, it will treat test_area as a script instead of a module and will also add the parent directories (folder1) to sys.path 