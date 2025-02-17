### Data model
-  A Data Model a set of rules that define how objects behave in python. includes special methods like dunder methods that allow objects to interact with built in functions, operators, language features
    - everything is an object
    - dunder methods control behaviour
    - custom objects can behave like built ins.
- unlike c or java, python doesn't work with primitive or non primitive data types. everything whether it be int, float, string or list, is represented by objects or relationships between objects.
- data modelling : process of creating data models using the syntax and environment of the python programming language is called data modelling in python.

#### Identity of an object
- every object has an identity which can never change once it is created. think like address
- `id()` returns the virtual memory address

#### Type of an object
- type of an object is the name of the class to which the object belongs.
- `type()` -> operations allowed on that object, set of values the object can hold.

#### Value of an object
- data that is stored for that object. value an object can hold is decided on the basis of the type of object.
- type, values cannot change : immutable objects(numbers, strings, tuples, sets)
```
#Let's create a varible with string value
s = "Hevo"
print("Variable value: ",s)
print("Identity of s: ",id(s))

Variable value:  Hevo
Identity of s:  1397871732528

s = "Data" #Change value of varibale 's'
print("Variable value: ",s)
print("Identity of s: ",id(s))

Variable value:  Data
Identity of s:  1397836021296
```

### Special methods
- describe the internal functoining of the basic object operations.
- allows objects to implement, support and interact with basic language constructs such as iteration, object creation, destruction, atribute access etc.

### Data model
- defines how python's core features like sequences, functions, iterators and classes work and interact as a framework
- python interpretor invokes special methods to perform basic object operations, often triggered by special syntax.
- we implement special methods when we want our objects to support and interact with fundamental language constructs like:
    - collections, attribute access, iteration, operator overloading, function and method invocation, string representation, object creation and destruction, context management

use of special methods:
- users don't have to memorize arbitrary method names like .size(), .length() for standard operations
- easier to benifit from rich python standard library and avoid reinventing the wheel like random.choice function.
    - implementing getitem and len, allows our class to behave as a sequence, allowing random to work
- our deck has `__getitem__` we used for indexing =>
    - it supports slicing
    - it is also iterable
        - works because, for loop first tries to call `__iter__()`, upon it's missing and `__getitem__()` is present, it will call get[0], get[1].. until index error is raised

- eventhough frenchDeck implicitly inherits from the object class, most of its functionality is not inherited, but comes from leveraging the data model and composition.
- by implementing len and getitem, we allow it to behave like a standard python sequence performing slicing, iteration and using standard library functions. they delegete all work to a list object ._cards
- special methods are meant to be called by the interpretor not us.
- when using `len()` for built in types, interpretor takes a shortcut. python variable sized collections written in c have size field in a struct. retrieve it's value which is faster.
- do not call special methods other than init, built in function types, operators are are faster than method calls.

#### Uses of Special methods
- emulating numeric types
- string representation of objects
- boolean value of an object
- implementing collections

### Emulating numeric types
- when doing + or * using __add__ or __mul__, do not modify either operand. just read them and create new objects.

### String representation
- use !r like in return f'{self.x!r}' to invoke repr() for the internal instead of str()
- `__repr__` is called by the `repr` built in to get the string representation of the object for inspection, without one, we see `<Vector object at xxx>`
- the string returned by __repr__ should be unambiguous and if possible, shoud match the source code necessary to re create the represented object.
- __str__ is called by str() built in and implicitly used by print function. should return a string suitable for display to end users.

### Boolean value of a custom type
- although python has bool type, it accepts any object in a boolean context : if while expression, and or operand
- by default user defined instances are truthy, unless `__bool__` or `__len__` is implemented.
- first calls `bool` and then `len`

### Collection API
#### ABC
- abstract base class in pyton is a class that defines a common interface for a group of related classes but cannot be instantiated directly, provides a blueprint for subclasses to follow.
- specify methods that subclasses must implement
- ![image](/material/assets/images/image%20copy.png)
- top ABCs have a special single method
- ABC collection unifies the 3 interfaces every collection must implement(iterable for iteration, sized for len, container for in)
- Python does not require concrete classes to actually inherit from any of these ABCs. any class that impelements __len__ satisfies the sized interface. but does not inherit the sized class.
    - cause python uses duck typing. if an object implements the required methods, it works even without inheritance.

- only sequence is reversible as it allows arbitrary ordering. mappings and sets do not.
- from 3.7, dict is ordered based on key.
- all special methods in set ABC implement infix operators. eg, A&B computes intersection.

#### Why len is not a method
- len(x) runs very fast when x is an instance of built in type. getting value from a field in a C struct. this should run fast since len is a basic operation in a collection.
- len is still a method for our custom objects.

## Summary:
- by implementing special methods, your objects can behave like the built in types, enabling the expressing coding style community considers pythonic
- a basic requirement of a python object is to provide usable string representations of itself. `__repr__` for debugging and logging and `__str__` for presentation to users.
- emulating sequences is the most common uses of special methods.
- thanks to operator overloading python offers a rich selection of numeric types, from built ins to decimal, fraction all supporting infix arithmetic operators.