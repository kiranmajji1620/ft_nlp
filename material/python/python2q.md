1. Dunder methods
- describe the internal functioning of the basic object operations.
- allow objects to integrate with python's built in functions, operators, iterators
- eg : `__init__`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__setitem__`, `__add__`, `__mul__`

2. str vs repr
- repr `repr(obj)` used for debugging and development. should return a precise, unambiguous string that can ideally be used to recreate the object.
- str `str(obj)` used for user friendly representation. readable description
- if str is not defined, repr is called during print(obj)
3. 
- context manager ensures database connections, files and locks are properly handled.

4. list implementations
- using [], list(), list comprehension, using []*, list(range()), collections.deque, array.array

    |  list          |  tuple         |
    |---------------|---------------|
    | Mutable       | Immutable     |
    | `[]` (Square brackets) | `()` (Parentheses) |
    | Slower        | Faster        |
    | More memory usage | Less memory usage |
    | Not hashable  | Hashable (if elements are immutable) |

6. `sorted(a, key = lambda x : x[1])` or `a.sort(key = lambda x : x[1])`

7. 

8. defaultdict, missingitem, setdefaullt
- `setdefault` : used to set a default value to the missing key. `get` will only return the default value but does not set the value.
- `__missingitem__` : is called by `__getitem__` method to handle missing keys in d[key]
- `defaultdict` : must give a callable `default_factory`. works only for `d[key]` not for `key in d` or `d.get(key)`
- 