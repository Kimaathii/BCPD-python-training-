# Master Guide: Comprehensions, Generators, Lambdas, `map()` & `functools`

**BCPD Certification Exam Focus:** Domain 2 (Data Structures 15%) & Domain 3 (Functions & Scope 15%)  
**Special Perspective:** JavaScript Developer Bridge & Under-The-Hood Mechanics

---

## 1. Quick Comparison for JavaScript Developers

If you come from JavaScript, Python's functional tools map directly to JS array methods and arrow functions, with critical differences in **laziness** and **syntax**:

| Concept | JavaScript Syntax | Python Syntax | Critical Difference |
|---|---|---|---|
| **Mapping** | `arr.map(x => x * 2)` | `[x * 2 for x in arr]` or `list(map(lambda x: x * 2, arr))` | Python `map()` is **lazy** (generator); JS `.map()` evaluates immediately to an array. |
| **Filtering** | `arr.filter(x => x > 0)` | `[x for x in arr if x > 0]` or `list(filter(lambda x: x > 0, arr))` | Python `filter()` is **lazy** and exhausted on first read. |
| **Reducing** | `arr.reduce((acc, x) => acc + x, 0)` | `functools.reduce(lambda acc, x: acc + x, arr, 0)` | In Python, `reduce` is in the `functools` module, not a built-in method. |
| **Anonymous Func** | `(a, b) => a + b` | `lambda a, b: a + b` | Python lambdas are strictly limited to a **single expression** (no statements or braces). |
| **Generators** | `function* gen() { yield 1; }` | `def gen(): yield 1` | Python generators also support lightweight generator expressions `(x for x in r)`. |
| **Partial Application** | `fn.bind(null, arg1)` | `functools.partial(fn, arg1)` | Creates a new callable with preset arguments. |

---

## 2. Comprehensions: Syntax, Types & The Scoping Shield

Python comprehensions provide a concise syntax for deriving new collections from existing iterables.

### A. The Three Comprehension Types

```python
# 1. List Comprehension -> returns list []
squares = [x * x for x in range(5)]
# -> [0, 1, 4, 9, 16]

# 2. Set Comprehension -> returns set {} (automatically deduplicates)
unique_lengths = {len(w) for w in ["apple", "pear", "fig", "apple"]}
# -> {3, 4, 5}

# 3. Dict Comprehension -> returns dict {key: value}
square_map = {x: x * x for x in range(3)}
# -> {0: 0, 1: 1, 2: 4}
```

### B. The Crucial "Where Does the `if` Go?" Rule

One of the most frequent BCPD syntax traps:

* **Pattern 1: Filtering (No `else`) $\rightarrow$ `if` goes at the VERY END:**
  ```python
  # Keep only positive numbers
  evens = [x for x in [1, 2, 3, 4] if x % 2 == 0]  # [2, 4]
  ```
* **Pattern 2: Transforming / Choosing Values (Ternary with `else`) $\rightarrow$ `if-else` goes BEFORE `for`:**
  ```python
  # Replace negative numbers with zero
  cleaned = [x if x > 0 else 0 for x in [3, -1, 4, -2]]  # [3, 0, 4, 0]
  ```
* **THE TRAP:** Writing `[x for x in nums if x > 0 else 0]` is an immediate **`SyntaxError`**!

### C. Nested Comprehensions & 2D Flattening

Read nested loops in comprehensions from left to right, exactly as you would write normal nested `for` statements:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Flattening 2D to 1D:
flattened = [val for row in matrix for val in row]
# Equivalent to:
# for row in matrix:
#     for val in row:
#         yield val
# -> [1, 2, 3, 4, 5, 6]
```

### D. Comprehension Scoping Shield (Python 3 Invariant)

Unlike standard `for` loops (where variables leak into the outer scope), **Python 3 comprehensions execute in their own isolated local scope**:

```python
i = 100
result = [i * 2 for i in range(5)]
print(result)  # [0, 2, 4, 6, 8]
print(i)       # 100  <-- 'i' was NOT overwritten!
```

---

## 3. Generators: Lazy Evaluation & Memory Efficiency

A generator is a stream producer that calculates values **on demand** rather than storing the entire dataset in RAM.

### A. Generator Expressions vs. List Comprehensions

Simply replace brackets `[]` with parentheses `()`:

```python
import sys

# List: Allocates 1,000,000 integers in heap RAM immediately
list_data = [x for x in range(1_000_000)]
print(sys.getsizeof(list_data))  # ~8,448,728 bytes (~8.4 MB)

# Generator Expression: Allocates zero data upfront; calculates on the fly
gen_data = (x for x in range(1_000_000))
print(sys.getsizeof(gen_data))   # ~200 bytes (constant memory!)
```

### B. Generator Functions (`yield` vs `return`)

A function containing the `yield` keyword is a **generator function**:

```python
def count_up_to(n):
    print("Generator started")
    count = 1
    while count <= n:
        yield count
        count += 1
    print("Generator finished")

g = count_up_to(3)
# Note: Calling count_up_to(3) does NOT execute the body yet! It returns a generator object.

print(next(g))  # Prints "Generator started", returns 1
print(next(g))  # Resumes after yield, returns 2
print(next(g))  # Returns 3
# print(next(g)) # Raises StopIteration and prints "Generator finished"
```

### C. The Generator One-Shot Exhaustion Trap

Generators **cannot be rewound or reused**. Once consumed, they are empty:

```python
nums = (x for x in [1, 2, 3])
print(sum(nums))  # 6
print(sum(nums))  # 0  <-- TRAP: Generator is exhausted!
```

### D. Subgenerator Delegation with `yield from`

`yield from iterable` delegates iteration directly to a sub-iterable or sub-generator:

```python
def chain_data():
    yield from [1, 2]
    yield from ("a", "b")

print(list(chain_data()))  # [1, 2, 'a', 'b']
```

---

## 4. Lambdas: Anonymous Inline Functions

A lambda is an anonymous, single-expression function constructed at runtime:

```python
# Syntax: lambda arg1, arg2, ...: expression
add = lambda x, y: x + y
print(add(3, 4))  # 7
```

### The 4 Strict Rules of Lambdas:
1. **Single Expression Only:** Lambdas cannot contain statements (`return`, `pass`, `assert`, `raise`).
2. **Implicit Return:** The result of the single expression is automatically returned.
3. **No Annotations:** Lambdas do not support PEP 484 type hints.
4. **Primary Use:** As the `key=` callable in sorting and finding extrema:
   ```python
   students = [("Ada", 95), ("Bob", 82), ("Cy", 91)]
   # Sort by grade descending:
   sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
   # -> [('Ada', 95), ('Cy', 91), ('Bob', 82)]
   ```

### The Legendary Late-Binding Closure Trap

```python
# THE EXAM BAIT
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```
* **Intuitive Guess:** `[0, 1, 2]`
* **Actual Reality:** `[2, 2, 2]`
* **Why:** The lambdas capture variable `i` by name from the enclosing scope. By the time the lambdas are called, the loop has completed and `i == 2`.
* **The Fix:** Bind `i` as a default parameter at definition time:
  ```python
  funcs = [lambda i=i: i for i in range(3)]
  print([f() for f in funcs])  # [0, 1, 2]
  ```

---

## 5. Under the Hood: Breaking Down `map()` and `filter()`

Understanding how `map()` and `filter()` work under the hood makes exam questions trivial.

### A. How `map()` Works

`map(function, iterable, ...)` applies `function` to every item in the iterable lazily:

```python
# Pure Python Equivalent of map()
def my_map(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)
```

#### Key Exam Behaviors:
1. **Returns a Map Iterator:** In Python 3, `map()` returns a lazy generator object. It has **no length** (`len(map(...))` raises `TypeError`).
2. **Multiple Iterables:** If passed multiple iterables, it passes one element from each iterable as positional arguments to `func`.
3. **Stops at Shortest:** Stops automatically as soon as the shortest iterable is exhausted:
   ```python
   a = [10, 20, 30]
   b = [1, 2]
   res = list(map(lambda x, y: x + y, a, b))
   print(res)  # [11, 22]  (30 is ignored!)
   ```

---

### B. How `filter()` Works

`filter(predicate, iterable)` yields only those elements where `predicate(item)` evaluates to truthy:

```python
# Pure Python Equivalent of filter()
def my_filter(predicate, iterable):
    for item in iterable:
        if predicate is None:
            if item:
                yield item
        elif predicate(item):
            yield item
```

#### The `filter(None, ...)` Secret Trap:
If `predicate` is passed as `None`, Python defaults to the **identity truthiness check**! It filters out all falsy values (`0`, `""`, `None`, `[]`, `False`):
```python
dirty = [0, "hello", "", None, 42, False, []]
clean = list(filter(None, dirty))
print(clean)  # ['hello', 42]
```

---

## 6. The `functools` Standard Library Suite

The `functools` module provides higher-order functions that act on or return other functions.

### A. `functools.reduce()` — Cumulative Folding

`reduce(function, iterable[, initializer])` folds an iterable down into a single cumulative scalar:

```python
from functools import reduce

# Pure Python Equivalent of reduce()
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            accum = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty iterable with no initial value")
    else:
        accum = initializer
    for item in it:
        accum = func(accum, item)
    return accum
```

#### Visualizing the Fold:
```python
# Calculate factorial of 4: 1 * 2 * 3 * 4
result = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])

# Step 1: acc = 1, x = 2 -> 1 * 2 = 2
# Step 2: acc = 2, x = 3 -> 2 * 3 = 6
# Step 3: acc = 6, x = 4 -> 6 * 4 = 24
print(result)  # 24
```

#### The Empty Iterable Trap:
* `reduce(lambda a, b: a + b, [])` $\rightarrow$ **`TypeError: reduce() of empty iterable with no initial value`**
* `reduce(lambda a, b: a + b, [], 0)` $\rightarrow$ **`0`** (Safe: initializer provided).

---

### B. `functools.partial()` — Freezing Function Arguments

`partial(func, *args, **kwargs)` creates a new callable with specific arguments pre-filled:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Freeze exponent=2 to create a specialized square function:
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27
```

---

### C. `functools.lru_cache()` — Automatic Memoization

`@lru_cache(maxsize=128)` caches the return values of expensive recursive or I/O calls based on input arguments:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Runs instantaneously in O(N) rather than taking years in O(2^N):
print(fib(50))  # 12586269025
```

---

### D. `functools.wraps()` — Decorator Metadata Preservation

When writing decorators, `@wraps(original_func)` ensures that `__name__` and `__doc__` are preserved rather than overwritten by the wrapper:

```python
from functools import wraps

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        return fn(*args, **kwargs)
    return wrapper

@my_decorator
def calculate():
    """Calculate important metrics."""
    pass

print(calculate.__name__)  # 'calculate' (NOT 'wrapper'!)
print(calculate.__doc__)   # 'Calculate important metrics.'
```

---

### E. `functools.singledispatch()` — Function Overloading Simulation

Python does not support C++/Java-style multiple `def` declarations for different types. `@singledispatch` dispatches to different implementations based on the type of the **first argument**:

```python
from functools import singledispatch

@singledispatch
def serialize(data):
    return str(data)

@serialize.register(int)
def _(data):
    return f"INT:{data}"

@serialize.register(list)
def _(data):
    return f"LIST_LEN:{len(data)}"

print(serialize("hello"))  # 'hello'
print(serialize(42))       # 'INT:42'
print(serialize([1, 2]))   # 'LIST_LEN:2'
```

---

## 7. The 7 Golden Rules for the BCPD Exam

1. **Brackets vs Parentheses:** `[x for x in r]` is a **List**; `{x for x in r}` is a **Set**; `{x: x for x in r}` is a **Dict**; `(x for x in r)` is a **Generator**.
2. **Generator Memory:** Generators take $O(1)$ constant memory and are single-pass (exhausted on read).
3. **`filter(None, iterable)`:** Strips all falsy values (`0`, `""`, `None`, `[]`).
4. **`map()` Multi-Iterable:** Pairs inputs positionally and terminates at the shortest iterable.
5. **Comprehension `if` Placement:** Filter at the end (`[x for x in l if cond]`); transform before `for` (`[a if cond else b for x in l]`).
6. **Lambda Limitation:** Strictly one expression; no statements, no `return`.
7. **Empty `reduce()`:** `reduce(fn, [])` raises `TypeError`; always supply an initializer (`0`, `""`, `[]`) if the collection might be empty.
