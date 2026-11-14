# Day 5 & Day 6 Screenshot Inventory & Analysis

> **BCPD Python Cohort 2 Certification Preparation**  
> **Batch:** 16 Newly Added Screenshots (Added 14 Nov 2026)  
> **Course Scope:** Week 1, Day 5 (Functions & Scopes) and Day 6 (List Methods, Comprehensions & Functional Tools — Thursday 12 Nov 2026)

---

## 1. Inventory & Metadata Matrix

| Image ID | Original Filename | Topic | Manual / Slide | Slide Title | Code File | Status | Notes |
|---|---|---|---|---|---|:---:|---|
| **D5-01** | `WhatsApp Image 2026-11-14 at 11.53.40.jpeg` | Day 5 — Functions | Beyond Manual / Slide 8 | Defining & calling functions | `functions.py` | Clear | `def`, docstrings (`__doc__`), implicit `None` |
| **D5-02** | `WhatsApp Image 2026-11-14 at 11.53.409ppl.jpeg` | Day 5 — Parameters | Beyond Manual / Slide 9 | The mutable default argument trap | `defaults.py` | Clear | Default evaluated ONCE at `def` time; `None` sentinel fix |
| **D5-03** | `WhatsApp Image 2026-11-14 at 11.53.39upp.jpeg` | Day 5 — Varargs | Beyond Manual / Slide 10 | `*args` and `**kwargs` | `varargs.py` | Clear | `*args` (tuple), `**kwargs` (dict), parameter ordering, call unpacking |
| **D5-04** | `WhatsApp Image 2026-11-14 at 11.53.38mk.jpeg` | Day 5 — Scoping | Beyond Manual / Slide 11 | Scope: LEGB, global & nonlocal | `scope.py` | Clear | LEGB search order, `global`, `nonlocal`, `UnboundLocalError` |
| **D5-05** | `WhatsApp Image 2026-11-14 at 11.53.37jki.jpeg` | Day 5 — Quiz | Slide 15 | Knowledge check (Day 5) | MCQs (1–5) | Clear | In-place `.append()`, slice `[-3:]`, aliasing `b = a`, `None` return, keyword call |
| **D6-01** | `WhatsApp Image 2026-11-14 at 11.53.3677.jpeg` | Day 6 — Title | Title Slide / Slide 1 | List Methods, Comprehensions & Functional Tools | `day6.py` | Clear | Week 1, Day 6 (Thursday 12 Nov 2026), Domain 2 (Data Structures 15%) |
| **D6-02** | `WhatsApp Image 2026-11-14 at 11.53.36.jpeg` | Day 6 — Sorting | Manual `§7.1` / Slide 3 | `sorted()` vs `.sort()` and the key argument | `sorting.py` | Clear | In-place `None`, stable sort, `key=str.lower`, case order (`"Pear" < "apple"`) |
| **D6-03** | `ui.jpeg` | Day 6 — Lists | Manual `§7.2` / Slide 4 | Comparing, combining & flattening lists | `combine.py` | Clear | Lexicographical compare, `+=` vs `+`, `sum(lists, [])` flatten, `*lst` unpack |
| **D6-04** | `WhatsApp Image 2026-11-14 at 11.53.35.jpeg` | Day 6 — Comprehensions | Manual `§7.3` / Slide 5 | List comprehensions | `comprehensions.py` | Clear | Filtering with trailing `if`, `if-else` before `for`, 2D grid & transpose |
| **D6-05** | `WhatsApp Image 2026-11-14 at 11.53.34.jpeg` | Day 6 — Gotchas | Manual `§7.3–7.4` / Slide 6 | map, join & comprehension gotchas | `gotchas.py` | Clear | `join` requires strings, `map` lazy/no `len()`, where `if` goes, matrix diagonals |
| **D6-06** | `WhatsApp Image 2026-11-14 at 11.53.33.jpeg` | Day 6 — Functional | Manual `§7.4` / Slide 7 | map, filter & reduce | `functional.py` | Clear | `map(func, iter)`, `filter(pred, iter)`, `functools.reduce`, multi-sequence map |
| **D6-07** | `yy.jpeg` | Day 6 — Lambdas | Manual `§7.4` / Slide 8 | lambda & functions as objects | `lambdas.py` | Clear | First-class functions, anonymous `lambda`, `key=len`, `apply(func, val)` |
| **D6-08** | `WhatsApp Image 2026-11-14 at 11.53.31.jpeg` | Day 6 — Complexity | Manual `§7.5` / Slide 9 | What list operations cost | Table | Clear | Big-O time complexity for index, append, insert(0), search, sort, copy |
| **D6-09** | `WhatsApp Image 2026-11-14 at 11.53.32.jpeg` | Day 6 — Complexity | Manual `§7.5` / Slide 9 | What list operations cost | Table | Clear | Duplicate photo of D6-08 |
| **D6-10** | `WhatsApp Image 2026-11-14 at 11.53.30.jpeg` | Day 6 — Recursion | Beyond Manual / Slide 10 | Recursion | `recursion.py` | Clear | Base case, recursive step, `RecursionError`, `sys.getrecursionlimit()` (1000) |
| **D6-11** | `WhatsApp Image 2026-11-14 at 11.53.22.jpeg` | Day 6 — Quiz | Slide 15 | Knowledge check (Day 6) | MCQs (1–5) | Clear | Comprehension odds, ASCII sort order, `*args` tuple, `nonlocal`, lambda default call |

---

## 2. Verbatim Code Extraction from Day 5 & Day 6

### Day 5: `functions.py` `[Course: D5-01]`
```python
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

def greet(name):
    print("Hi", name)  # no return

print(area(3, 4))       # -> 12
result = greet("Ada")   # -> Hi Ada
print(result)           # -> None
print(area.__doc__)     # -> Return the area of a rectangle.
```

### Day 5: `defaults.py` `[Course: D5-02]`
```python
def add_item(item, basket=[]):  # default built ONCE
    basket.append(item)
    return basket

print(add_item("apple"))  # -> ['apple']
print(add_item("pear"))   # -> ['apple', 'pear']

def add_item_safe(item, basket=None):
    if basket is None:
        basket = []             # new list on every call
    basket.append(item)
    return basket

print(add_item_safe("apple"))  # -> ['apple']
print(add_item_safe("pear"))   # -> ['pear']
```

### Day 5: `varargs.py` `[Course: D5-03]`
```python
def total(*args):
    return sum(args)

def profile(name, **kwargs):
    print(name, kwargs)

print(total(1, 2, 3))                       # -> 6
print(total())                              # -> 0
profile("Ada", age=36, lang="py")           # -> Ada {'age': 36, 'lang': 'py'}
nums = [4, 5]
print(total(*nums))                         # -> 9
opts = {"age": 20}
profile("Bo", **opts)                       # -> Bo {'age': 20}
```

### Day 5: `scope.py` `[Course: D5-04]`
```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "changed"
    inner()
    return x

print(outer())  # -> changed
print(x)        # -> global

count = 0
def bump():
    global count
    count += 1

bump()
bump()
print(count)    # -> 2
```

---

### Day 6: `sorting.py` `[Course: D6-02]`
```python
nums = [5, 2, 9, 1]
print(sorted(nums), nums)  # -> [1, 2, 5, 9] [5, 2, 9, 1]
print(nums.sort())         # -> None
print(nums)                # -> [1, 2, 5, 9]

words = ["Pear", "apple", "fig"]
print(sorted(words))                     # -> ['Pear', 'apple', 'fig'] (ASCII: 'P'=80 < 'a'=97)
print(sorted(words, key=str.lower))      # -> ['apple', 'fig', 'Pear']

people = [("Bo", 25), ("Ada", 36), ("Cy", 25)]
print(sorted(people, key=lambda p: p[1])) # -> [('Bo', 25), ('Cy', 25), ('Ada', 36)] (Stable sort!)
```

### Day 6: `combine.py` `[Course: D6-03]`
```python
print([1, 2, 3] < [1, 3], [2] > [1, 9])  # -> True True (Lexicographical element-by-element)

def grow(lst):
    lst += [4]            # in place: caller sees it

def rebuild(lst):
    lst = lst + [5]       # new list: caller doesn't

a = [1]
grow(a)
rebuild(a)
print(a)                  # -> [1, 4]

print(sum([[1, 2], [3]], []))  # -> [1, 2, 3] (Flattens one level using sum with empty list start)

z = zip("ab", [1, 2, 3])
print(type(z).__name__ == "zip")  # -> True (Iterator, stops at shortest input)

print(*[1, 2, 3], sep="-")        # -> 1-2-3 (Unpacking into arguments)

nums = [5, 9]
nums.insert(nums.index(9), 7)
print(nums)                       # -> [5, 7, 9]
```

### Day 6: `comprehensions.py` `[Course: D6-04]`
```python
nums = [3, -1, 4, -2]
print([n * 2 for n in nums])                  # -> [6, -2, 8, -4]
print([n for n in nums if n > 0])             # -> [3, 4]
print([n if n > 0 else 0 for n in nums])      # -> [3, 0, 4, 0]

print([(x, y) for x in "ab" for y in (1, 2)]) # -> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

matrix = [[i * j for j in range(1, 4)] for i in range(1, 3)]
print(matrix)                                 # -> [[1, 2, 3], [2, 4, 6]]

transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)                              # -> [[1, 2], [2, 4], [3, 6]]
```

### Day 6: `gotchas.py` `[Course: D6-05]`
```python
nums = [1, 2, 3]
# "-".join(nums)                              # -> TypeError: expected str instance
print("-".join(map(str, nums)))               # -> 1-2-3

m = map(str.upper, ["a", "b"])
# len(m)                                      # -> TypeError: object of type 'map' has no len()
print(list(m), list(m))                       # -> ['A', 'B'] [] (Map is lazy & consumed only once!)

print(list(map(list, ["ab", "c"])))           # -> [['a', 'b'], ['c']]

out = [print(n, end=" ") for n in "xy"]       # -> prints 'x y '
print(out)                                    # -> [None, None]

print([n if n > 1 else 0 for n in nums])      # -> [0, 2, 3]
# [n for n in nums if n > 1 else 0]           # -> SyntaxError

g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([g[i][i] for i in range(3)])            # -> [1, 5, 9] (Main diagonal)
print([g[i][2 - i] for i in range(3)])        # -> [3, 5, 7] (Anti-diagonal)
```

### Day 6: `functional.py` & `lambdas.py` `[Course: D6-06, D6-07]`
```python
from functools import reduce

nums = [1, 2, 3, 4]
print(list(map(lambda n: n ** 2, nums)))                   # -> [1, 4, 9, 16]
print(list(filter(lambda n: n % 2, nums)))                 # -> [1, 3]
print(reduce(lambda a, b: a * b, nums))                    # -> 24
print(list(map(str, nums)))                                # -> ['1', '2', '3', '4']
print(list(map(lambda a, b: a + b, [1, 2], [10, 20, 30]))) # -> [11, 22]

# Lambdas
square = lambda x: x * x
print(square(6))                                           # -> 36

def apply(func, value):
    return func(value)

print(apply(str.upper, "hi"))                              # -> HI
print(apply(lambda n: n + 1, 9))                           # -> 10

words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                              # -> ['fig', 'kiwi', 'banana']
print(max(words, key=len))                                 # -> banana
```

### Day 6: `recursion.py` `[Course: D6-10]`
```python
import sys

def factorial(n):
    if n <= 1:
        return 1  # base case
    return n * factorial(n - 1)

def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

def digit_sum(n):
    return n if n < 10 else n % 10 + digit_sum(n // 10)

print(factorial(5))         # -> 120
print(fib(10))              # -> 55
print(digit_sum(1234))      # -> 10
print(sys.getrecursionlimit()) # -> 1000
```
