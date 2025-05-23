## An array of sequences
- standard library offers sequence types implemented in c
    - conainer sequences vs flat, mutable vs immutable

- a container sequence holds references to the objects it contains(list, tuple, deque), while a flat sequence stores teh values of its contents. 
- flats are more compact but are limited to holding primitive machine values like bytes, integers, floats.(str, bytes, array.array)

- !["image"](/material/assets/images/image%20copy%202.png)
- every python object has a header with metadata. the simplest python object float, has a value field and two meta data.
    - ob_refcnt : object's reference count
    - ob_type : a pointer to the object's type
    - ob_fval : c double holding value
- on a 64 bit, each field takes 8 bytes. that's why an array of floats is much more compact than a tuple of floats. array is a single object holding the raw values in a single contiguous memory block, while tuple consists of several objects - tuple itself and each float object.

#### Mutable vs Immutable
- mutable sequences inherit all methods from immutable sequence types and implement several additional methods
- !["collection.abc"](/material/assets/images/image%20copy%203.png)

## Lists
### List Comprehension and Generator Expressions
- quick way to build a sequence is using list comprehension(if target is a list) or a generator expression(for other kinds of sequences)
- list comprehension faster than actual lists??
- general for loop may be used to do a lots of things - pick items, sum, etc.. where as listcomp goal is always to build a new list.
- if you are not using the produced list, do not use it. esp for side effects.
- Local scope within comps and genexps
    - have a local scope to hold the variables assigned in the for clause
    - using := will have the scope until the function
    ```
    >>> x = 'ABC'
    >>> codes = [ord(x) for x in x]
    >>> x
    'ABC'
    >>> codes
    [65, 66, 67]
    >>> codes = [last := ord(c) for c in x]
    >>> last
    67
    >>> c
    Traceback (most recent call last):
    ```
- listcomp build lists from sequences or any other iterable type by filtering and transforming them. the filter and map can be composed to do the same, but readibility suffers and also, listcomp is fatser???
- to generate data for other sequence types other than a list, use genexps.
#### Generator Expressoins
- could also use listcomp, but a genexp saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.
- the are contained in () while listcomps are in []
- `array.array('I', (ord(symbol) for sybmol in symbols))`
- `tuple(ord(symbol) for symbol in symbols)`, don't have to duplicate () for a single argument
    ```
    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)
    ```
- here, the cartesion product is calculated one by one; a list with all six t shirt variations is never produced.
- if len(colors) = 1000 and len(shirts) = 1000, then we don't have to need a list that can store a million shirts.

## Tuples are not just immutable lists
- they can be used as immutable lists and also as records with no field names.
### Tuples as records:
- there is no need to create classes just to name the fields especially if we use unpacking and avoid using indexes => use tuples.

### Tuples as immutable lists
- a tuple uses less memory than a list of the same length, and it allows python to do some optimizations.
- immutability of a tuple only applies to the references contained in it. references in a tuple cannot be deleted or replaced
- but if the references point to a mutable object, then the value of tuple changes.
- tuples with mutable items can be a source of bugs. an object is hashable only if it's value cannot ever change an unhashable tuple cannot be inserted as a dict key.
- `hash(o)` will give TypeError

#### Tuples vs Lists
- python compiler generates bytecode for a tuple constant in one operation; but for a list literal, the generated bytecode pushes each element one by one as a separate datastack, and then builds the list.
-   ```
        t = (1, 2, 3)
        t2 = tuple(t)
        t == t2 # True
        l = [1, 2, 3]
        l2 = [1, 2, 3]
        l == l2 # False
    ```
    - since tuples are immutable, python does not create a new copy, it references to the same tuple but l and l2 are different objects
    - tuples won't change. so there is no risk in reusing the same object.
- tuple is allocated the exact memory space it needs. lists are allocated with room to spare for future appends.
- the refernces to the items in a tuple are stored in an array in the tuple struct, while a list holds a pointer to an array of references stored elsewhere. this is necessary because when a list grows beyond the space currently allocated, python needs to reallocate the array of refernces to make room.(CPU cache less-effective)
- tuples use almost any function that lists uses as long as they don't involve adding or removing items. except tuple lacks __reversed__ method. reversed() still works.
    - as reversed() first will look for __reversed__() and upon failure, uses a iterator to yield same items in reverse order using len and getitem

## Unpacking Sequences and Iterables
- avoids unnecessary and error-prone use of indexes to extract elements from sequences.
- works with any iterable object as data source- including iterators, which don't support index notation.
- Iterable : any object that can be looped over using for loop
    - lists, tuples, sets, dicts, strings
    - iterable has __iter__()
- Iterator : iterable that also has __next__()
    - generators, files
- Sequence : a type of iterable that supports indexing and slicing contains `__getitem__`
    - lists, tuples, strings
- unpacking works as long as the iterable yields exactly one item per variable in the receiving end, unless * is used.
- Uses
    - swapping `a, b = b, a`
    - calling a function
    ```
    t = (10, 9)
    f(*t)
    a, b = f(*t)
    ```
    - if we don't use *, python considers it as a single argument.
#### Using * to grab excess items
- `a, b, *c = range(5)` or `a, *b, c, d`
- * can be applied to only one variable, but it can appear in any position.
- can also be used when defining list, tuple, set literal, functoin calls
    ```
    def f(a, b, c, d, *rest): return a, b, c, d, rest
    f(*[1, 2], 3, *range(7)) : 1, 2, 3, 4, (5, 6)
    *range(4), 4 => (1, 2, 3, 4, 5)
    {*range(4), 4, *(5, 6, 7)} => {1, 2, 3, 4, 4, 5, 6, 7,}
    ```

### Nested Unpacking
- the target of an unpacking can use nesting as well 
    ```
    metro = [('Tokyo', 'JP', 10923, (10, 20))]
    name, _, _, (lat, lon) = metro[0]
    ```
    - by assigning the last field to a nested tuple, we unpack the cordinates.
- the target of an unpackign assignment can also be a list but is rare
- useful if you have db query that returns a single record, you can unpack and at the same time make sure ther is only one result.
- `[record] = f()` or `[[field]] = f()` will raise an error if more than one element returned from functoin
- tuples can also do the same when doing a single item unpacking. `(record, )`
- `,` is a must as it ensures that the record is a single element of a tuple. If a , is missed, it treats the record as another variable that can hold multiple elements and does not enforce single element return.

### Pattern Matching with Sequences
- key improvement of match over struct is it's de structuring - a more advaned form of unpacking.
    ```
    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)
    ```
- a sequence pattern matches the subject if the subject is a sequence and the subject and pattern have the same no of items and each corresponding item matches including nested items.
- sequence patterns can be written as tuples or lists or any combination of nested tuples or lists, makes no difference
- a sequence pattern can match instances of most actual or virtual subclasses of collections.abc.sequence with exception of str, bytes, arrays
    - list, tuple, memoryview, range, array.array, deque
- _ is the only variable that can appear more than once, is not bound to the value.
- can also bind any part of a pattern with a variable using as keyword
    - `case [name, _, _, (lat, lon) as coord]:`
- can also use type checking during runtime
    - `case [str(name), _, _, (float(lat), float(lon))]:`
    - these are not constructor calls, just typechecking during runtime.
- match starting sequence with str and ending with two floats
    - `case [str(name), *_, (float(lat), float(lon))]:`
    - using `*extra` will bind those items to extra
- should include _ to include failing matches.
- lambda function matching sequence
    - `case ['lambda', [*parms], *body] if body:`
    - ensures parms is a list even if it has one or zero elements

## SLICING
- list, tuple, str and all sequence types
#### Why slices and ranges exclude last term
    - easy to see length when only stop is given : list[:8]
    - easy to compute length using stop - start
    - easy to split using list[:7] and list[7:]
### Slice Objects
- notation a:b:c is only valid within [] when used as the indexing of subscript operator - produces a slice object: slice(a, b, c)
- seq[a:b:c] calls seq.__getitem__(slice(a, b, c))
- can call using `a = slice(0, 6)` print(seq[a])

### Multidimensional Slicing and Ellipsis
- to evaluate `a[i, j]` python calls a `a.__getitem__(i, j)`
- mds is supported in numpy.nd arrays like `a[m:n, k:l]`
- except memoryveiw, built in sequences types in python are 1D.
- (...) is an alias to Ellipsis object.
- `x[i, ...]` is shortcut for `x[i, :, :, :]` in numpy

### Assigning to slices
- not just useful to extract information from sequences, they can also be used to change mutable sequences in place.
- `l[2:5] = [20, 30]` and `del l[5:7]` 
- `l[3:8] = 100` gives error but `l[3:8] = [100]` doesn't
- when the target of the assignment is a slice, the righthand side must be an iterable object(not only sequence), even if it has just one item.

### Using + and * with sequences
- both operands of `+` must be of sqme sequence type, and neither of them is modified, but a new one is created
- to concatenate multiple copies of same sequence, use *
#### Pitfalls of using * to build lists
- `board = [['_'] * 3 for i in range(3)]` will create a list that has 3 lists and each list is a separate entity.
- `board = [['_']*3]*3` will create a list that has 3 lists and each list refers to same memory address. which is what we don't want.

#### Augmented assignment with sequences
- `+=` and `-=` behave differently based on the first operand.
- `+=`'s special methods is `__iadd__()` inplace addition. if there is no inplace, it falls back to using `__add__()`
- Mutable sequences like list, array, bytearray it is simply a.extend(b) if no iadd, it is a = a + b, the identity of object bound to a may or may not change depending on availability of iadd
- similarly `*=` is implemented using `__imul__()`
- for an immutable sequence, new sequence will be created. id will change.
- immutable sequence concat is inefficient as it creates a new one and copies all elements there. exception : string. cpython has optimized string operations allocating extra room as string concat is heavily used.
- putting a element in a list in a tuple
```
t = (1, 2, [3,4])
t[2] += [2,3]
```
- will put the elements and give an error as well.
- avoid putting mutable objects in tuples, augmented operation is not atomic operation.
### list.sort versus the sorted built - in
- list.sort will sort in place, returning none
- functions or methods that change an object in place should return None to make it clear that the receiver was changed, and no new object was created. drawback: cannot cascade calls
- built in sorted creates a new list and returns it. accepts any iterable including immutable sequences and generators.
- regardless of type of input, it always gives new list.
- both take 2 args
    - reverse : default false. if true descending order
    - key : 1 argument function that will be applied to each item to produce its sorting key, default is identity function.
- by default, strings are sorted lexographically. ascii uppercase come before lower case.

### Alternatives to lists and tuples
- lots of floating point data : array
- support removing items from opposite ends : deque
- frequently checking existence : set
#### Array
- python array is as lean as C array
- does not hold instances, but only the packed bytes representing their machine values.
- when creating an array, we provide a type code to determine the underlying c type used to store each item.
- each item will be stored in a n bytes and will not let you enter another object.
- array does not have sort function. use `a = array.array(a.typecode, sorted(a))` to rebuild the array

#### Memory views
- shared memory sequence type that lets you handle slices of arrays without copying bytes.
- memoryview.cast method lets you change the way multiple bytes are read or written as units without moving bits around.
    ```
    from array import array
    octets = array('B', range(6))
    m1 = memoryview(octets)
    m2 = m1.cast('B', [2, 3])
    m3 = m1.cast('B', [3, 2])
    ```
- three share the same memory and changing one will change others.

#### Numpy
- faster, memory efficient, vectorized math opertions, integrates well with ml and scientific computing, supports advanced operations
    - vectorized opns : low level implementations in c and simd

#### Deques
- inserting and removing at head is costly because entire list must be shifted. 