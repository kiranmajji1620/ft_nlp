### PYTEST

- fixtures, mocks, parameterized tests, tmp_env file
### FIxtures
- reusable setup function that provides resources to testing funcitons
- helps maintain cleaner, more maintainable tests.
- auto use, yield  
- Fixture scope
- `function` - Default
- `class` : runs once per class
- `module` : once per module/for all tests in a file
- `session` : runs once per test session/across all test files

### tmp file
- manage temporary resources
- created for individual test
- can create directories for multiple tests using scope texture

### Mock
- isolate a piece of code from external resources so that our test focuses on our code
- create a mocker fixture and patch functions

- unit testing : mock when necessary
- integration testing : don't mock

### conftest.py
- configuration file that allows you to write shared fixtures, hooks