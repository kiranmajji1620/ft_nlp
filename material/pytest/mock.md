## Mock
- mocking is a technique allows you to isolate a piece of code being tested from its dependencies so that the test can focus on the code under test in isolation.
- Achieved by replacing the dependencies with mock objects that simulate the behaviour of the real objects
- helps to isolate bugs, improve test coverage in unit testing.
- mockito : java, unittest.mock & pytest : python, moq : .net

### Benifits of mocking
- Shorter feedback loop
    - precious development time is wasted during api calls as it depends on external server.
    - preset what you expect the api to return and test quicker.
- Reduce     on external server

### Mocking in pytest
- **Note** : Mock an item in the unit test or where the class is initialised, rather than just defined.
- The `pytest-mock` plugin provides a mocker fixture that can be used to create mock objects and patch functions.
- The `mocker` fixture is an instance of mockfixture class which is a subclass of the unittest.mock module
- `mocker.patch` - patch a function or method
- `mocker.patch.object` - patch a method of an object
- `mocker.patch.multiple` - patch multiple functions
- `mocker.patch.dict` - patch a dictionary
- `mocker.patch.stopall` - stop all patches
- `mocker.patch.stop` - stop a specific patch

#### Mock a constant or a variable
#### Mock a function : Create or remove file
- mock_examples/file_handler.py
```
import os

def create_file(filename: str) -> None:
    """
    Function to create a file
    :param filename: Name of the file to create
    :return: None
    """
    with open(f"{filename}", "w") as f:
        f.write("hello")

def remove_file(filename: str) -> None:
    """
    Function to remove a file
    :param filename: Name of the file to remove
    :return: None
    """
    os.remove(filename)
```

- tests/test_file_handler.py
```
import os
from mock_examples.file_handler import create_file, remove_file


def test_create_file():
    """
    Function to test make file
    """
    create_file(filename="delete_me.txt")
    assert os.path.isfile("delete_me.txt")

def test_remove_file():
    """
    Function to test remove file
    """
    create_file(filename="delete_me.txt")
    remove_file(filename="delete_me.txt")
    assert not os.path.isfile("delete_me.txt")
```
- This is risky as we don't want to mess with local file system, not to mention we can use `tmp_path`
- tests/test_file_handler.py
```
def test_create_file_with_mock(mocker):
    """
    Function to test make file with mock
    """
    filename = "delete_me.txt"

    # Mock the 'open' function call to return a file object.
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    # Call the function that creates the file.
    create_file(filename)

    # Assert that the 'open' function was called with the expected arguments.
    mock_file.assert_called_once_with(filename, "w")

    # Assert that the file was written to with the expected text.
    mock_file().write.assert_called_once_with("hello")
```

#### Mock an external REST API
- mock_examples/api.py
```
from typing import Dict
import requests

def get_weather(city: str) -> Dict:
    """
    Function to get weather
    :return: Response from the API
    """
    response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    return response.json()

```

- tests/test_api.py
```
from mock_examples.api import get_weather


def test_get_weather():
    """
    Function to test get weather
    """
    response = get_weather(city="London")
    assert type(response) is dict
```
- This test is dependent on the external API and may fail if the API is down, changes or rate limits you.

- tests/mock_api.py
```
def test_get_weather_mocked(mocker):
    mock_data = {
        "temperature": "+7 °C",
        "wind": "13 km/h",
        "description": "Partly cloudy",
        "forecast": [
            {"day": "1", "temperature": "+10 °C", "wind": "13 km/h"},
            {"day": "2", "temperature": "+6 °C", "wind": "26 km/h"},
            {"day": "3", "temperature": "+15 °C", "wind": "21 km/h"},
        ],
    }

    # Create a mock response object with a .json() method that returns the mock data
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data

    # Patch 'requests.get' to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    # Call the function
    result = get_weather(city="London")

    # Assertions to check if the returned data is as expected
    assert result == mock_data
    assert type(result) is dict
    assert result["temperature"] == "+7 °C"
```
- Similarly we can mock a class as well

### When should you mock?
- It's a good idea to mock when you want to test a single module in isolation and avoid external dependencies
- When you want to test the functionality of the system, you need to test the real connections -> don't mock
- Unit Testing : Mock where necessary
- Integration Testing : Don't mock, use real connections.