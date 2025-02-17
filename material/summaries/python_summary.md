## Learn
- format strings

- `pass` is used as a placeholder
- `continue` is used to skip current iteration
- `break` is used to break from the innermost loop
- `/` always returns float. use `//` for int
- `f"{value:.2f}"` for precision
- `f"{value:,.2f}"` for precision and thousand commas
-  most of the times, method does an operation in place, returns none. function creates and returns new object, parameter unmodified.
- sort works only on list, sorted() works on any iterable

- Exceptions:
    - `else` : execute if no error is caught
    - `finally` : execute anyway

- strings
    - `isalpha()`
    - `lower()`, `upper()`
- Common built in exceptions:
- `BaseException` Parent of all.
- `KeyboardInterrupt`
- `Exception`
    - `ArithmeticError`
        - `ZeroDivisionError` : division by zero
    - `AssertoinError`
    - `EOFError` : ctrl + d
    - `ImportError`
        - `ModuleNotFoundError`
    - `LookupError`
        - `KeyError`
    - `NameError` : Using an undefined variable
    - `TypeError` : invalid operation between types
    - `IndexError` : Accessing an invalid index in a list
    - `KeyError` : Accessing a missing key in dict
    - `ValueError` : invalid value for an operation(int("a"))
    - `FileNotFoundError` : File not found while opening it
    - `AttributeError` : Accessing a missing attribute
    - `KeyboardInterrupt` : ctrl + c
- try should have all the error prone code, except should handle them, else should have the execution after successful try, finally should conclude.

### Python1
#### Libraries
- `sys.argv` is a list of command line arguments

#### UnitTests
- `pytest` for automating assertion and error handling
- maintain a test folder `test` with `__init__.py` and name all files to start with `test_Name` and all functions with `test_Func`.
- run `pytest test`
- can assert strings when they are returned from a function.

#### Regex


#### OOP

- class : a class is a blueprint for creating objects. It defines attributes and methods that operate on the data.
- object : instance of a class. represents a specific realization of the class with it's own data and behavior
- attributes : variables that store data inside an object
- method : functions inside a class that define an object's behavior
- `self` - represents the instance of the class and is used to access its attributes and methods. self allows the method to operate on the instance data.
- `self` automatically passes a reference to the current object that is just constructed in `__init__`, can call anything not only self
- any variable inside an object without `self.` will become a local variable scope limited by that function
- any variable initialized outside the functions will become class variables
- `__init__` - is a special method also called as constructor in python classes.
    - automatically called when an object is created. used to initialize attributes
    - avoids manually setting attributes after object creation
    - cannot have multiple init methods in a class as python does not support method overloading like c++, only last one will be used if multiple init's are used
    - use args and kwargs for variable attributes
- can use class methods for multiple constructors
- `raise` - raise errors as in `raise ValueError("Name invalid")`
- `__str__` - used to define a string representation of an object. automatically called when you use print() or str() or f"{}"on an object
- `__repr__` - debugging representation
- if we return anything other than a string from the str function, it will give typeerror
- we can access the attributes with `.` method as in `student.house = slytherin`. possibility of messing things, might overwrite the constructors initialization.
- we can structure that the user must pass through functions in order to get and set the attributes. this way, we'll be able to handle errors 
- `setter` : 
    - when python sees `student.house = ""`, it will see that user is trying to change the .house attribute. instead of allowing to do so, it will call the setter function
    - name the function exactly like the attribute
    - now, you don't have to handle the error checking in the `__init__` method, since this setter will be called even there.

- since we define our getter and setter functions with same name, collisions might occur and might lead to infinite recursion. so we must use `self._house` for the instance attributes.
- use `_house` internally to expose `house` through property methods
- `_` is a naming convention and not enforced by python, it shouldn't be accessed directly outside the class, only for internal use.
- `getter` : 
- `property` : attribute that gives more control
- we need getter and setter to have same name as their attributes since we want to allow dot notation `student.house = "hai"` to work instead of method calls
- without using properties, python will treat the method as a regular method rather than allowing other direct assignments.
- also, getter and setter methods give us more control over the attributes assignment
- since brand is already a property through getter, python expects brand.setter for setter. if we don't use so, it will overwrite the getter.
- why does init have `student.house` instead of `student._house`
    - this is because, ._house does the direct assignment without going to the setter function. saying `.house` will call the setter function and will do error checking.
- `house` is not an actual attribute, it is a property that behaves like one. it is a wrapper around `_house` and python determines whether to call the getter or setter based on how `house` is accessed. 
- `decorators` : functions that modify other functions.

#### Instance methods
- methods that can access the instance attributes, should be called using self
- a method is automatically an instance method when you define it without any property.

#### Class methods
- have a specific functionality no matter the object.
- doesn't have access to the instance that called, but still has an idea on which class has called using cls variable
- class attributes : only one copy of a variable that is shared among all instances of that class.
- `@classmethod`
- `def sort(cls, name)` python automatically passes some variable `cls` that refers to the class inside the class method.
- use a class as a container for data and functionality
- a class method can only access class variables
- when you access `self._attribute`, python will first look into instance's `__dict__` for it, if not found, it checks the class attributes, if still not found, it raises an AttributeError.

#### Class Method vs. Static Method in Python  

| Feature | **Class Method (`@classmethod`)** | **Static Method (`@staticmethod`)** |
|---------|----------------------------------|----------------------------------|
| **Tied to** | The **class** | The **class** (but no access to `cls`) |
| **First parameter** | `cls` (class reference) | No `self` or `cls` |
| **Can modify class attributes?** | ✅ Yes (`cls.attr = ...`) | ❌ No |
| **Can access instance attributes?** | ❌ No | ❌ No |
| **Decorator used** | `@classmethod` | `@staticmethod` |
| **Use case** | Modify **class-wide attributes** | Utility/helper functions related to the class |

#### Property
- Working: `print(obj.house)`
- python checks if house is a regular attribute
- if house is not found, it checks for a getter method decorated with @property or @house.setter if assignment is there
- setter and getter must go together
    - if setter with no getter -> error
    - if getter with no setter -> read only attribute

#### Public vs Protected vs Private
- no enforcing, it is just honor system, meant to be respected by everyone.
- don't touch starting with `_` and `__`. we can use, but just don't

### Inheritance
- feature that allows a class(child class) to derive properties and behaviors from another class (parent class)
- Why
    - code reusability
    - maintainability
    - extensibility
- the `super` function allows you to call a parent class method inside a child class.
- child classes can access both class attributes and instance attributes of a parent class.
    - child class automatically inherit class attributes from parent. modifying them in child doesn't affect the parent
    - child gets a copy of the class attribute.
    - instance attributes belong to individual objects
    - child classes inherit instance attributes but need to call super().init if the parent defines them in init
    - modifying class attributes -> affects other instances
    - modifying instance attributes -> affects only that instance.
- child classes cannot access the private attributes of the parent unless name mangling

### Operator Overloading
- `+` doesn't always mean addition, might mean concatenation.
- `def __add__(self, other):`
- can we add two different classes
    - technically, we can. we have to define how the addition is gonna happen between them
- we cannot do operator overloading on what ever we want.



### Et cetera
#### Sets
- `.add()`
- global : variables outside the functions
    - it's okay to read from a global variable, but not write to it.
    - trying to modify the global variables from functions, will lead to localunbound error.
    - so need to inform beforehand that this variable is global, not scoped to the local function.
    - if you declare a local variable with same name as a global variable, local will shadow the global one.
- constants :
    - keep them at the top, use capitals(don't touch this) as naming convention, but python doesn't enforce this.
- type hints: type hint variables and functions. use mypy for static checking.
    - decrease the probability of bugs.
- docstrings:
    - these describe all about your function.
    - packages available which extract all the docstrings and make documents pdfs and websites.
    - can even take tests using some other packages.
```
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
```
- argparse:
    - use `-n` for character args, `--number` for word args
```
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default = 1, help = "No of times to meow", type=int)
    args = parser.parse_args()
    print(args.n)
```
- unpacking :
    - `function(*list)`
    - works for enumerations, dictionaries
    - doesn't work with set
    - error if given more variables than required.
- can unpack using list or a dictionary
- *args
    - a function doesn't have to take a fixed no of arguments
- Maps
    ```
    uppercased = map(str.upper, words)
    print(*uppercased)
    ```
    - a map returns a map object which should be unpacked 
- List comprehension
    - `uppercased = [word.upper() for word in words]`
- Filter
    - in a map, we get one value for each value in the list but in filter, we filter out the list based on the function
    - here, function will return true or false, map returns a value.
    - include those which return true.
    - don't call function(). filter will call for us
```
gryffindors = filter(function, list)
```
- dictionary comprehension
    - list comprehension: `gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]`
    - `gryffindors = {student : "Gryffindor" for studens in students}`

- enumerate: iterate sequence by iterating the value and the index.
```
for i, student in enumerate(students):
    print(i + 1, student)
```

- Generators:
    - ability to generate values from functions 
    - what if run out of memory -> no longer works
    - use yield to return part of values
    - on each iteration, it returns a value that is appropriate for that iteration
- static method
- class method
- public, protected and private attributes and methods
- where are class variables stored, if objects are the one which occupy memory.
- inheritance
- args and kwargs