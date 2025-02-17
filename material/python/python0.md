### Str

```
name = "  kiran "
name = name.strip() # removes the spaces from end but not in the middle
name = name.capitalize()
name = name.title() # capitailze all words
first, last = name.split(" ")
x = float(input("what is x"))
y = float(input("what is y"))
print(x + y)
z = round(x + y)
```
- scope

- method is a function of an object.
- parameters : variable defined in a function structure
- arguments : actual value passed to the function when calling it
- variables : 
- literals : 


#### Commands
- `print(f"{z:,}")` formatting strings
- `print(f"{z:.2f}")` will round to 2 decimal places
- `5//2` for integer division
- `listA.sort()`
- 
### Control flow
- if, elif, else
- for statements
    - iterates over the items of any sequence in the order they appear
    - in a code that modifies content while iterating over the same can be tricky.
    - use .copy()
    - range : start(0), step(1), r[i] = start + step*i, returns a range object(immutable sequence of numbers)
- break and continue
    - `break` breaks the innermost enclosing `for` or `while` loop
- else belonging to loop
    - for : executed if loop finishes it's final iteration
    - while : executed after the loop's condition becomes false
    - in either kind, else is not executed if the loop is terminated by a break or exception or return
- pass :
    - busy wait for keyboard interrupt
    - create minimal class, placeholder for a function.
- match : 
    - pattern matching, "_" wild card, "|" can be used to combine
    ```
    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
    ```
#### functions:
default arguments:
- default argument values : allocation happens once : at the time of function definition, not during every function call.
- value persists across function calls like static object.
```
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # will print 5
```
- be careful with mutable objects
```
def func(val=[]):  # Default value (empty list) is created once
    val.append(1)
    print(val)

func()  # Output: [1]
func()  # Output: [1, 1] (Not a new list, same list persists!)
```
```
def func(val=None):
    if val is None:  # Create a new list each call
        val = []
    val.append(1)
    print(val)

func()  # Output: [1]
func()  # Output: [1] (New list every time)
```
keyword arguments
- `kwarg = value`
```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
can be called using
```
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
not by
```
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```
- keyword arguments must follow positional arguments
- order of keyword arguments is not important.
#### args and kwargs
- allow the function to accept an arbitrary no of positional and keyword arguments
- *args : captures extra positional arguments as a tuple
- **kwargs : captures extra keyword arguments as a dictionary
- args must appear before kwargs
- named parameters must come before kwargs
```
def demo_function(a, b, *args, x=10, y=20, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"Positional extra (args): {args}")  # Captures extra positional args as a tuple
    print(f"x = {x}, y = {y}")  # Named parameters with defaults
    print(f"Keyword extra (kwargs): {kwargs}")  # Captures extra keyword args as a dictionary
demo_function(1, 2, 3, 4, 5, x = 50, z = 100, w = 200)
a : 1, b : 2, *args : (3, 4, 5), x : 50, y : 20, **kwargs:{"z" : 100, "w" : 200}
```

#### Special Parameters
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
```
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

standard_arg(2) # works
standard_arg(arg = 2) # works
pos_only_arg(2) # works
pos_only_arg(arg = 2) # fails
kwd_only_arg(1) # fails
kwd_only_arg(arg = 1) # works
```
Combining parameters:
```
def combined_example(pos_only, /, standard, *, kwd_only):
    print("hai")
combined_example(1, 2, 3) # fails
combined_example(1, 2, kwd_only = 4) # works
combined_example(1, standard = 2, kwd_only = 3) # works
combined_example(pos_only = 1, standard = 2, kwd_only = 3) # fails
```
Collision:
```
def foo(name, **kwds):
    return 'name' in kwds
foo(1, **{'name':2}) will cause error.
    - 'name' is a positional argument. so the first value 1 is assigned to name.
    - **kwds captures all additional arguments as a dictionary
    - however name is already used as a positional parameter. so python doesn't allow it again as a keyword parameter.
def foo(name, /, **kwds): will not.
```
- use position_only if you want name of parameters not available to the user. useful if paramters have no real meaning -> enforcing the order of arguments when function is called.
- use keyword_only when names have meaning and function definition is more understandable by being explicit with names or you want to prevent users rely on position of argument being passed.
- for API, use position only if parameter's name might change in future.
Unpacking argument lists
```
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```
### Python1
- Conditionals : compare a lht to rht
- last else statement is a catch-all statement.
- match == switch, _ matches all, | (pipe)can be used as or(not in if elses)
- pythonic code : `return True if n % 2 == 0 else False`

### Loops
iteration : one cycle through the loop.
- a for loop iterates through a list of items, only works with iterables
- if a variable in for loop doesn't have any significance, represent using '_'
- a common paradigm within python is to use a while loop to validate the user input.
- `continue` : go to the next iteration of a loop.
- `break` : break out of a loop early before it has finished all iterations. 
- while lists use numbers to iterate through the list, dicts allow us to use words.
```
for student in students:
    print(student) # will print only keys
    print(students[student]) # will print values
```
- list of dictionaries
```
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
```
- use `for index, key in enumerate(list(dict.keys()))`
```
items = list(dict.items())
for i in range(len(items)):
    key, value = items[i]
```
- here, for loop iterates over keys 

### Errors and Exceptions
- Error : Syntax errors, exception errors
- exception is a runtime error that occurs during program execution, causing the program to stop unless handled properly.
- standard exception names are builtin identifiers, not reserved keywords
- `print(10/0)` ZeroDivisionError
- `print(x)` NameError(name 'x' is not defined)
- Common built in exceptions:
    - `ZeroDivisionError` : division by zero
    - `NameError` : Using an undefined variable
    - `TypeError` : invalid operation between types
    - `IndexError` : Accessing an invalid index in a list
    - `KeyError` : Accessing a missing key in dict
    - `ValueError` : invalid value for an operation(int("a"))
    - `FileNotFoundError` : File not found while opening it
    - `AttributeError` : Accessing a missing attribute
    - `KeyboardInterrupt` : ctrl + c
    - `EOFError` : ctrl + d
- use `try except` to handle errors, `else` runs when no error occurs, `finally` always runs, even if exception occurs, `raise` to trigger custom exceptions
- Try Except
```
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by 0")
```
- Working : 
    - first the try clause is executed
    - if no exception occurs, the except clause is skipped and execution of try statement is finished
    - if an exception occurs during execution of try clause, then, it its type matches the exception named after the `except` keyword, the except clause is executed, and then execution continues after the try/except block
    - if an exception occurs which does not match the exception named in the except clause, it is passed on to other try statements. if no handler is found, it is an unhandled exception and execution stops with error message.
- a class in an except clause matches exceptions which are instances of the class itself or one of its derived classes(but not the other way around)
- base class is the common base class of all exceptions.
- it's subclass Exception is the base class of all the non fatal exceptions. 
- Exceptions other than non fatal exceptions which are not subclasses of Exception are not typically handled, used to indicate that the program should terminate, include SystemExit which is raised by sys.exit()
- Exception can be used as a wildcard that catches almost everything.
- Re raise the exception
```
except Exception as err: # Exception is the base class
    raise
```
```
try:
    print(x)
except:
    print("Error:", e)
```
```
try:
    print("No errors here")
except Exception:
    print("Error occurred")
else:
    print("This runs if no exception occurs")
finally:
    print("This always runs")
```
- putting all code in try catches all exceptions and might catch unintended errors. so use `else` for safe code
- custom exceptions
```
def withdraw(amount):
    if amount > 1000:
        raise ValueError("Cannot withdraw more than 1000!")
    print("Withdraw successful")

try:
    withdraw(2000)
except ValueError as e:
    print("Error:", e)
```
- Exception chaining:
- if an unhandled exception occurs inside except section, it will have exception being handled attached to it and included in the error message.
- exception handlers also handle those that occur inside functions that are called in the try clause.
`else`
```
try:
    x = int(input("What's x"))
except ValueError:
    print("X is not a integer")
print(x)
```
- We can just write the code outside the try block like this right
    - this works if the x is integer. if it is not, it will raise a error and it is handled. But print(x) will raise a name error
    - because assignment happens from right to left, and when input is not integer, the assignment never did happen!!
```
else:
    print(x)
```
- `finally`
- if an exception is not handled by an except clause, the exception is re raised after the finally clause has been executed.
- an exceptoin could occur during execution of an except or else clause. again, the exception is re rasied after the finally clause has been executed.
- if finally clause executes a break, continue or return statement, exceptions are not raised.
- if the try statement reaches a break, continue or return statement, finally clause will execute just prior to break, continue or return statement's execution.
- if the finally includes a return statement, the returned value will be the one from finally not from try.