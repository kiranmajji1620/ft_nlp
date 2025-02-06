### Temporary directories and files
- this fixture provides a temporary directory unique to each test function, offering a clean and isolated environment for testing file operations, mocking dependencies, and more.
- Reatains the contents of last 3 pytest sessions.

#### Seamless management of temporary Resources
- `tmp_path` able to seamlessly manage temporary files and directories for each test function.
- pytest automatically creates a unique temporary directory before the test begins and cleans it up after the test completes. This eliminates the need for manual cleaup operations and ensures a clean and isolated environment for each test run.

#### Isolation and avoidance of sideeffects
- by providing a dedicated temporary directory for each test function, tmp_path helps isolate tests from each other, preventing side effects and interference between tests. 
- isolation is crucial for maintaining test determinism and reliability, especially in complex test suites where dependencies may overlap.

#### Flexibility in test data generation
- tmp_path offers flexibility in generating test data on-the-fly within the temporary directory. Whether you need to create temporary files, directories, or even complex directory structures, tmp_path makes it easy to generate custom test data tailored to your specific testing needs. 
- This flexibility enables you to simulate diverse testing scenarios and edge cases with ease.

#### Integration with parameterization
- tmp_path seamlessly integrates with parametrized tests, enabling you to generate and manage temporary resources dynamically based on the test parameters. 
- This combination of features enhances the expressiveness and flexibility of your test suite, allowing you to cover a wide range of test scenarios efficiently.

- Example 
```
def write_to_file(data, file_path):
    with open(file_path, 'w') as f:
        f.write(data)

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def test_write_and_read_from_file(tmp_path):
    # Define test data
    test_data = "Hello, world!"
    
    # Create a temporary file path within the temporary directory
    temp_file_path = tmp_path / "test_file.txt"
    
    # Call the function under test to write data to the temporary file
    write_to_file(test_data, temp_file_path)
    
    # Assert that the file was created in the temporary directory
    assert temp_file_path.exists()
    
    # Call the function under test to read data from the temporary file
    data_read = read_from_file(temp_file_path)
    
    # Assert that the data read from the file matches the test data
    assert data_read == test_data
```
- the file and directory automatically get deleted after the test.
#### Understanding the path of `tmp_path`
- when tmp_path is used, pytest creates a unique temporary directory for each test inside the system's temp location
- `/tmp/pytest-of-user/pytest-0/test_tmp_path_location0`
- We can create multiple files inside `tmp_path`
- Each test gets a separate and clean workspace
- Creating sub directories:
```
def test_subdirectory(tmp_path):
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()  # Create subdirectory

    file_in_subdir = sub_dir / "nested_file.txt"
    file_in_subdir.write_text("Inside a subdirectory")

    assert file_in_subdir.read_text() == "Inside a subdirectory"
```
#### `tmp_path_factory`
- `tmp_path_factory` for shared temporary directories
- unlike `tmp_path` which is function scoped, `tmp_path_factory` allows creating temporary directories shared across multiple tests.
- useful when multiple tests need access to the same directory.
```
import pytest

@pytest.fixture(scope="session")
def shared_tmp_dir(tmp_path_factory):
    """Creates a shared directory for multiple tests."""
    return tmp_path_factory.mktemp("shared")

def test_shared_1(shared_tmp_dir):
    file = shared_tmp_dir / "common_file.txt"
    file.write_text("Shared Data")
    assert file.read_text() == "Shared Data"

def test_shared_2(shared_tmp_dir):
    file = shared_tmp_dir / "common_file.txt"
    assert file.read_text() == "Shared Data"

```