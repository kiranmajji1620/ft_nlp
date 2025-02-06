### Unit testing 
- Software testing technique where individual components (functions, methods, classes) of a program are tested in isolation to ensure they work correctly.
- Helps detect bugs early
- Used to validate that each software unit performs as designed

#### Python unit test
- Built-in testing framework that provides a set of tools for testing our code's functionality in a more systematic and organized manner.
- We can create test cases, fixtures, and suites.
- Also supports test discovery, making it easy to automate test execution across a project.

### Different testing methods in Python:
- **Unittest**: Built-in, follows xUnit-style testing
  - **Cons**: Requires explicit test case setup, more verbose (requires classes)
- **Pytest**:
  - **Pros**: Easy to write and read, supports fixtures, parameterized tests, better reporting, better assertion handling, uses Python's built-in assert statements, more flexible
  - **Cons**: Needs to be installed
- **Nose2**: Successor to Nose, more feature-rich than Pytest, replaced by Pytest

- **Pytest is preferred** as it is more concise, supports fixtures, has better reporting, and doesn't require boilerplate code like unittest.

## Pytest

- Just running `pytest` on the command line detects the test files in that directory and its subdirectories.
- For this test file detection mechanism to work, there are rules for naming the test files in Pytest.
  - `test_filex` or `filex_test` for files
  - `test_function` or `testmethod` for functions or methods

#### Commands of pytest:
- `pytest` from any folder to run the tests in that directory and subdirectories.
- In file: `@pytest.mark.skip(reason="")`
- In file: `@pytest.mark.skipif(a > b, reason="")`
- `pytest -k square` to run all tests that have "square" in their name.
- `-v` for verbose mode
- Run the tests based on the category:
  - Use custom markers

### Invoking pytest
- `pytest test_mod.py` - Run tests in a module
- `pytest testing/` - Run tests in a directory
- `pytest -k 'MyClass and not method'` - Will run `TestMyClass.test_something` but not `TestMyClass.test_method`.
- `pytest tests/test_mod.py::test_func` - Run a specific test within a module
- `pytest tests/test_mod.py::TestClass` - Run all tests in a class
- `pytest tests/test_mod.py::TestClass::test_method` - Specify a specific test method
- `pytest tests/test_mod.py::test_func(x1,y2)` - Specify a specific parameterization of tests
- `pytest -m slow` - Run all tests decorated with `@pytest.mark.slow`
- `pytest -m "slow(phase=1)"` - Run tests with `@pytest.mark.slow(phase=1)`
- `pytest -v --capture=no` - Show print statements on the screen instead of capturing them elsewhere

### Write and report assertions in pytest
```python
def test_f():
    assert f() == 4
```
- If this assertion fails, you will see the return value of the function call and introspection.

#### Assertion introspection:
```python
def test_function():
    assert f() == 4
E   assert 3 == 4
        where 3 = f()
```

#### Assertion custom introspection:
```python
def test_function():
    assert f() == 4, "f should be 4."
```

#### Expected exception handling:
```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
```

### Parameterized tests
```python
import pytest

@pytest.mark.parametrize("test_input, expected_output", [
    (5, 25),
    (9, 81),
    (10, 100)
])
def test_square(test_input, expected_output):
    result = area.square(test_input)
    assert result == expected_output
```

### Temporary directories and files
- `tmp_path` provides a temporary directory unique to each test function, ensuring isolation.
- Retains contents of the last **three** pytest sessions.

#### Example:
```python
def test_write_and_read_from_file(tmp_path):
    test_data = "Hello, world!"
    temp_file_path = tmp_path / "test_file.txt"
    write_to_file(test_data, temp_file_path)
    assert temp_file_path.exists()
    data_read = read_from_file(temp_file_path)
    assert data_read == test_data
```

### `conftest.py`
- A special configuration file used by pytest to define fixtures, hooks, and plugins for multiple test files.
- Allows sharing setup and teardown logic **without** needing to import them manually.

#### Example Directory Structure:
```
project/
│── src/
│   ├── module.py
│── tests/
│   ├── test_module.py
│   ├── conftest.py  <-- Configuration file for all tests
```

#### Inside `conftest.py`:
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 25}
```

#### Inside `test_module.py`:
```python
def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 25
```

- `sample_data` is automatically available in `test_module.py` without importing it.

#### Skipping or marking tests dynamically
```python
def pytest_addoption(parser):
    parser.addoption("--skip_slow", action="store_true", default=False, help="Skip slow tests")

def pytest_collection_modifyitems(config, items):
    skip_slow = config.getoption("--skip_slow")
    for item in items:
        if "slow" in item.nodeid and skip_slow:
            item.add_marker(pytest.mark.skip(reason="Skipping slow test"))
```
- **Usage**: `pytest --skip_slow`

### Sources:
- [Parameters & Fixtures](https://medium.com/@ramanish1992/pytest-parameter-and-fixtures-13f6fdbd48c9)
- [tmp_path](https://medium.com/@mikolaj.fido/unveiling-the-power-of-tmp-path-simplify-your-testing-with-clean-and-isolated-i-o-47906da7ec80)
