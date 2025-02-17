# Dictionaries
- the actual usable fraction in a dict is 1/3 not 2/3
- A dictionary doesn't hold the attributes in itself. it stores them in a hash table. 
- each entry in the hashtable contains the hashed key, actual key(for collision resolution), pointer to the value.
- the values themselves are not stored in the hash table only references to them are
    - avoids duplication, efficient memory usage, flexibility
- Why store both hashed key and actual key
    - infinite possible keys and limited hash values. so different keys might get same hash value => hash collision
    - to tell the diff entries apart, it will store the actual key.

### How dictionaries work old implementation:
- dictionary starts with 8 empty slots
- each key is hashed, and the last few bits of the hash determine where the key value pair is stored.
- if a collision occurs, place in a different slot.
- after storing 5 pairs, dictoinary doubles in size to reduce collision probability
- this leads to wasted space but ensures fast lookups by minimizing collisions.

#### LOOKUPS
- compute the hash of the key and check the expected slot
- if slot is occupied:
    - check if object is the same id(key) == id(stored key) if yes, return the value else 
    - check the hash. if hash(current key) == stored hash, then perform an equality check (key == stored_key)as multiple objects can have same hash.
    - if hashes also don't match, continue searching.
### New compact hash table implementation
- instead of allocating memory for all possible slots, python stores keys separately in insertion order.
- a separate array maintains insertion index -> order is maintained as a side effect.
#### LOOKUPS
- compute the hash of the key
- use the hash to find the index in index array
- go to that index in memory block 
- check if key matches (by id() and then hash and then ==)
- if it doesn't match, iterate over index array to check the next potential position(collision resolution).
- we do hash check after id check because two objects can have same value but stored in different memory.
- directly going to == is bad as it is slower. doing hash check confirms that if hashes don't match, reject the match. if they match check for ==.
- hash check reduces unnecessary equality comparisions.
### Dict Comprehensions
- `{country : code for code, country in dail_codes}`

#### Unpacking mappings
    ```
    def dump(*kwargs):
        return kwargs
    dump(**{'x' : 1}, 'y' = 2, **{'z' : 3})
    ```
- works when all keys are strings and unique
- duplicate keys are allowed using second ** and replace first occurence.

#### Merging mappings with |
- `d1 = d1 | d2` will change id of d1; `d1 |= d2` will do inplace

### Pattern matching with mappings
- match/case supports mapping objects
- `case {'type' : 'book', 'api' : 2, 'authors' : [*names]}`
- order of keys is irrelevant.
- in contrast to sequence patterns, mapping patterns succeed in patrial matches. even if they include an extra pair, it's okay.
- no need to capture extra items using **. **_ is forbidden because it's redundant.
**- a match succeeds only if the subject already has required keys at the top of match statement. (defaultdict d[key] in automatic handling of missing keys.)**

### Standard mapping types
- `collection.abc` provides `mapping` and `mutablemapping` abcs describing the interfaces of dicts.
- to implement a custom mapping, it is easier to extend `collections.UserDict` instead of subclassing these ABCs.
- as the c.ud and all concrete mapping classes in the standard library encapsulate the basic dict in their implementation, which is built on hash table. not the case for `collection.abc`
- limitation : keys must be hashable.

### Hashable
- an object is hashable if it's hash code`__hash__()` never changes in its lifetime and can be compared`__eq__()` to other objects .
- hashable objects which compare equal must have same hash code.
- numeric, flat immutable types str and bytes : hashable
- immutable container types : hashable
- frozen set : always hashable, tuple : hashable if all items are hashable
- user defined objects are hashable because their hash code is id() and the `__eq__()` is inherited from object class.
- if an object implements a custom `__eq__()`, then it is hashable if its `__hash__()` always returns the same hash code.
- this requires that `__eq__()` and `__hash()__` only take into account instance attributes that never change

### Common mapping methods
- basic api : dict, default dict, ordered dict(last two come from collections)
- all have similar methods
    - default dict : supports deep copy, default factory, calls `__missing__` when `__getitem__()` cannot find the key .
- `d.update(m)` : first checks whether m has a keys method and if it does, assumes it is a mapping. else, falls back to iterating m assuming items are (key, value) pairs.

### Inserting or Updating Mutable value
- d[k] raises `KeyError` when k is non existing key. alternative : `d.get(k, default)`
- better way to retrieve and update a mutable value for insertion : 
    instead of 
    ```
    o = index.get(word, [])
    o.append(l)
    index[word] = o
    ```
    use 
    ```
    index.setdefault(word, []).append(location)
    ```
    only single retrieval
- handling missing keys on any look up (not only while inserting):
### Automatic Handling of missing keys
- return made up value when a missing key is searched
    - using `defaultdict`
    - subclass dict/any mapping type and implement `__missing__()`
### defaultdict
- creates items with default values whenever a missing key is searched using d[k]
- produce a callable `default_factory` when instantiating defaultdict. it is called by `__getitem__()` whenever a missing key is passed.
- now the calling will return a reference to the empty object generated by `default_factory` 
- if no default_factory is provided, `KeyError`
- `default_factory` of a defaultdict is only invoked to provide values for `__getitem__` and not for other calls. `dd.get(k)` will still give none, `k in dd` will give False

### `__missing__`
- not defined in the dict class, but dict is aware of it.
- only triggered when `__getitem__` fails to find a key.
- subclassing dict and providing a `__missing__` method, `dict.__getitem__` will call it whenever a key is not found.
    - eg : we want a dict that can have keys as strings. if d[str(nonstr)] missing, call d[str] in the missing method.

### Inconsistent usage of `missing`
- dict subclass
    - `__missing__` called on d[k] not on `.get` or `in`
- collections.userdict subclass
    - `__missing__` is called on d[k] and `get` is also inherited which internally calls `d.__getitem__()`
- abc.mapping
    - we must implement `__getitem__` and `__missing__` is not triggered.
- abc.mapping with `__getitem__` calling `__missing__`
    - `__missing__` is triggered on d[k], d.get(k), k in d

### collections.OrderedDict
- built in dict also keeps the keys ordered since python3.6.
- used to keep code backward compatible with earlier python versions.
- dict vs ordereddict
    - equality in ordereddict also looks at order.
    - popitem() accepts which item to be popped.
    - has move_to_end() to reposition an element to last.
- regular dict was designed to be very good at mapping operations. space efficiency, iteration speed, performance of update are secondary
- ordereddict cna handle frequent reordering better than dict.

### collections.Chainmap
- holds a list of mappings that can be searched as one.
- search starts from first map in constructor call,
- doesn't copy input mapppings, only holds references. updates or insertions to it happen to the first map child.

### collections.counter
- holds an integer count for each key.
- used to count instances of hashable objects.
- `ct.counter('fasfa')` will create a counter for the elements in the string sequence
- `ct.update('dfa')` will add to the frequencies given earlier.

### shelve.shelf
- 

- ordereddict, chainmap, counter and shelf are ready to use but can also be customized by subclassing.
- userdict is intended only as a base class to be extended.
### dict vs userdict vs abc.mapping
- dict is not meant to be subclassed, stores keys and values directly in a hash table
- userdict is wrapper around dict, easier to sub class
- abc.mapping is ABC defines a read only interface, any class that implements getitem, iter and len is recognized as mapping without explicit inheritence.

### Subclassing userdict instead of dict
- dict has some implementation shortcuts that make us override methods 
- userdict does not inherit from dict. it has internal dict instance called data which will hold actual items.

## Immutable mappings
- no real one in standard library.
- `MappingProxyType` wrapper class from `types` : readonly but dynamic proxy to the original mapping.
- updates to original mapping can be seen in mapping proxy, but changes cannot be made through it.

## Dictionary views
- dict instance methods .keys(), .values(), .items() return instances of classes called dict_keys, dict_values, dict_items : read only projections of internal data structures used in the dict implementation.
- views can be iterated, can be reversed, can't use [] to get individual items from a view.
- are not built in. only used internally. cannot use them to build something from scratch.
- dict_values implement len, iter, reversed. but keys and items implement several set methods.

## Practical consequences of how dict works
- keys must be hashable objects. must implement `__eq__` and `__hash__` methods
- item access is very fast.
- key ordering is preserved from python3.6
- significant memory overhead - hash table needs to store more data per entry, and python needs to keep atleas 1/3 rows empty to remain efficient.
- python stores instance attributes in a special dict attached to each instance.
    - before 3.3 each instance had a separate dictionary storing keys and values leading to redundant storage as 2/3 table for each instance is same. same attribute (key pointer) and same hash(same key)
    - after 3.3, python shares a single hash table among multiple instances for attribute name
    - each attribute hash code and pointer is stored only once, linked to the class and the attribute are kept in parallel arrays of pointers attached to each instance.
    - each instance then only stores attribute values as an array of pointers.
    [](/material/assets/images/image%20copy%208.png)
    - the keys table is cached. the first instance and all instances after it will hold only its own value array. 
    - if an instance gets a new attribute not found in shared keys table, then this instance's dict is converted to combined table form
    - however, if this instance is the only one in its class, `__dict__` is converted back to split table.
    - if a new attribute is added later, the instance gets a separate hash table.

# Set Theory
- don't preserve order
- want to remove duplicates : use set. want to remove duplicates and preserve order : use list(dict.fromkeys(l).keys())
- set elements must be hashable
- set is not hashable => cannot create a set of sets but can create a set of frozen sets.
- `a | b`, `a & b`, `a - b`, `a ^ b`
- `a ^ b` elements in either but not in both.
- using sets makes code easier to read and removes loops and conditional logic.
- eg: use `found = len(needles & haystack)` instead of 
    ```
    for n in needles:
        if n in haystack:
            found += 1
    ```
- very efficient for membership tasks.

### Syntax
- {1}, {1, 2} works but {} doesn't. need to use `set()`
- {1, 2, 3} is faster than set([1, 2, 3])
    - latter is slower as : first fetch the set name, build a list, pass it to constructor.
    - former has a special BUILD_SET bytecode.
- frozenset must be invoked with `frozenset(range(10))`

### Set comprehensions
- `chr(90)` to get the character.

## Practical consequences of how sets work
- set elements must be hashable (must implement `__hash__` and `__eq__` methods)
- membership testing is very efficient
- heavy memory overhead -> due to hash code storage, 1/3 buckets empty compared to arrays.
- element ordering depends on insertion order. elements with same hash code differ in order based on who came first.
- elements order may change after resizing(2/3) -> elements are re inserted and different collisions may occur.

### Set Operations
- infix operators require both operands to be sets.
- remaining can work with iterables as long as they produce hashable elements.
- `a.union(b, c, d)` a must be set and in place of a or `e = {*a, *b, *c, *d}` for assignment.
- `s&z` : if s is a set and has `.__and__`, it will call it. if it doesn't have it will call `z.__rand__`

### Set Operations on dict Views
- dict_keys and dict_items impelment the special methods to support the powerful set operators &, |, -, ^.
- the return value of `d1 & d2` is a set instance.also, set operators in dictionary views are compatible with set instances.

### Internals of sets and dicts
## Hashes and equality
- hash() built in function works directly with built in types and falls back to alling __hash__ for user defined types.
- if two objects compare equal, their hash codes must be equal.
- if 1 == 1.0, then hash(1) == hash(1.0)
- hash codes should scatter around the index space as much as possible.
- similar objects should have hash codes that are similar. and non similar whould have hash codes that differ widely.
- on a 64 bit cpython, a hash code is a 64 bit number.
- there are 2^64 possible values of hash but most python types can represent many more different values.
- different hash codes mean different objects but converse not true. different objects might lead to same hash value as hash values are limited.

## Set hash tables under the hood.
- atleas 8 rows or buckets.
- [eg hash table](/material/assets/images/image%20copy%204.png)
- each bucket in a set has two fields: a 64 bit hash code and a 64 but pointer to the element value which is a python object stored elsewhere in the memory.
- buckets have a fixed size, individual buckets are accessed by offset from the start of the hash table.
- [flow chart](/material/assets/images/image%20copy%205.png)
- as elements are added, python makes sure atleast 1/3 of buckets are empty. doubling the size when needed. hash code field is initialized with -1.
- hash('mon') gives 814801924712 whose mod with 3 gives 1. and the hash code at 1 is -1. so put this in empty bucket.
- if a collision occurs at index 1, it will compare the hashes. if hashes are same -> compare values. if values are different or hashes are different, store at next index. so hash objects must implement `__eq__`
- `linear probing`incrementing the index after a collision. this can lead to clusters of occupied buckets which can degrade the performance.
- CPython counts the number of linear probes and after a certain threshold, applies a pseudo random number generator to obtain a different index from other bits of the hash code. 

## New dictionary and it's good sideeffect.
- actual usable dict storage is just 1/3 not 2/3
- key must be hashable, doesn't matter for value
- [Old dicts](/material/assets/images/image%20copy%206.png)
- New implementation : hash table : indices.
- width of buckets in indices varies as dict grows : starts with 8 bits per bucket, enough to index 128 entries. -1 for empty and -2 for deleted.
- in 64 bit, old implementation would take 192 bytes: 24 bytes per bucket 8 rows. equivalent compact dict uses 104 bytes: 96 bytes in entries(24*4) + 8 bytes in indices.
- [new alog](/material/assets/images/image%20copy%207.png)
### Algorithm
- compute the hash for 'mon' for 'mon' : 14
- compute hash(mon)%len(indices) -> 3
- put 0 at offset 3 in indices and fill the bucket at 0.
- when 5 are filled, resize to 16 bytes indices -> enough to hold 10 items.
- after doubling as needed and reaching 128 buckets filled, time comes to fill the 129th bucket. however, a signed byte is not enough to hold offsets after 128 entries.
- so the indices array is rebuilt to hold 256 16 bit buckets to hold signed integers. wide enough to represent offsets to 32768 rows in the entries table. next resizing happens at 171st addition.
- the indices array grows by doubling the no of buckets and also less often by doubling the width of each bucket to accommodate a growing no of rows in entries.