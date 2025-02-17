## Python 1

script : single file of code meant to be executed
package : collection of modules in a directory, contians `__init__.py`
module : single file of code meant to be imported
library : a collection of modules and packages that provide a functionality
### Libraries

#### Random
- `coin = random.choice(["heads" ,"tails"])`, does the math prob based on no of items in list.
- `number = random.randint(1, 10)`, including end points
- `random.shuffle(cards)`

#### Statistics
- `statistics.mean([100, 90])`

#### Command line arguments
- `sys.argv` - list of arguments.
- `sys.exit()` - exit current program
- handle indexerrors

#### API calls
- `response = requests.get("LINK", args)`
- `response.json()` and `json.dumps(response.json, indent = 2)` for clear output.

### Unit Tests
- we can test our code by handling assertions.
```
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")

if __name__ == "__main__":
    main()
```
- we can let pytest do our work
```
from calculator import square
def test_square(): 
    assert square(1) == 1
    assert square(2) == 4
```
- can test the errors as well
```
with pytests.raises(TypeError):
    'cat'*'cat'
```
- to test a string, return string from a function instead of outputting it