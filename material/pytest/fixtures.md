### Fixtures
- In standard unittests, we will declare global variables and write setup and tear methods in case some repetitive calling of a class or a repetitive connection establishment takes place.
- fixtures are functions that set up a test environment and before a test runs and clean up after the test completes.
- Fixtures in pytest are used to set up and tear down test environments. They help manage resources like db connections, test data, temporary files etc. ensuring that each test runs in a controlled and repeatable manner
```
import pytest
@pytest.fixture
def sample_data():
    return {"name":"John", "age":30}

def test_sample(sample_data):
    assert sample_data["name"] == "John"
```
- Fixtures run once per test function which is what we don't desire when writing database connections or expensive operations.
### Fixture scope
- `function` - Default
- `class` : runs once per class
- `module` : once per module/for all tests in a file
- `session` : runs once per test session/across all test files
- Module fixtures
```
@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetting up module")
    yield
    print("\nTearing down module")

def test_one(module_fixture):
    print("Running test_one")

def test_two(module_fixture):
    print("Running test_two")
```
- Output :
```
Setting up module
Running test_one
Running test_two
Tearing down module
```
- runs once per module
- sets up resources before the first test runs and cleans up after the last test completes.
- we can use multiple fixtures for tests

#### Autouse fixtures
`@pytest.fixtures(autouse=True)`
- to make a fixture run automatically for all tests without explicitly calling it.


### Fixtures inside fixtures
```
@pytest.fixture
def base_data():
    return [1, 2, 3]

@pytest.fixture
def extended_data(base_data):
    base_data.append(4)
    return base_data

def test_extended(extended_data):
    assert extended_data == [1, 2, 3, 4]

```
- Build complex setups where one fixture relies on another.
- reuse setup logic, making test cases modular and efficient.   
- useful when tests require multiple layers of setup
    - connecting to a database
    - adding test data
    - running tests that use both.

#### Using yield for setup and teardown in dependent fixtures
- When a fixture needs setup before and cleanup after use, we ues yield.
```
@pytest.fixture
def db_connection():
    """Simulates opening and closing a database connection."""
    print("\n[SETUP] Opening database connection")
    db = {"connection": "open"}
    yield db  # Provide the database connection
    print("\n[TEARDOWN] Closing database connection")
    db["connection"] = "closed"

@pytest.fixture
def db_with_data(db_connection):
    """Populates the database with test data."""
    print("[SETUP] Adding test data to DB")
    db_connection["data"] = ["Alice", "Bob", "Charlie"]
    yield db_connection
    print("[TEARDOWN] Removing test data from DB")
    del db_connection["data"]

def test_database(db_with_data):
    assert db_with_data["connection"] == "open"
    assert db_with_data["data"] == ["Alice", "Bob", "Charlie"]

```
which will be 
```
[SETUP] Opening database connection
[SETUP] Adding test data to DB
Test runs...
[TEARDOWN] Removing test data from DB
[TEARDOWN] Closing database connection
```
- Key benifits: ensures cleanup even if test fails, encapsulates test setup in fixtures, keeping test functions clean.

#### with different scopes
- Pytest ensures they are executed in the correct order, respecting their scopes.
```
@pytest.fixture(scope="module")
def module_setup():
    print("\nSetting up module")
    yield
    print("\nTearing down module")

@pytest.fixture
def function_setup(module_setup):
    print("Setting up function")
    yield
    print("Tearing down function")

def test_one(function_setup):
    print("Running test_one")

def test_two(function_setup):
    print("Running test_two")
```
- Execution flow
```
Setting up module
Setting up function
Running test_one
Tearing down function
Setting up function
Running test_two
Tearing down function
Tearing down module
```
- module setup runs once per module, teardown happens after all tests finish.

#### Parameterized fixtures with dependencies
```
@pytest.fixture(params=["admin", "guest", "editor"])
def user_role(request):
    return request.param

@pytest.fixture
def user_db(user_role):
    """Creates a user in the database based on role."""
    print(f"\nCreating user with role: {user_role}")
    return {"username": "test_user", "role": user_role}

def test_user_permissions(user_db):
    assert user_db["role"] in ["admin", "guest", "editor"]
```
- Execution flow:
```
Creating user with role: admin
Running test_user_permissions for admin

Creating user with role: guest
Running test_user_permissions for guest

Creating user with role: editor
Running test_user_permissions for editor

```