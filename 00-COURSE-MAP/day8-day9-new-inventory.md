# Day 8 & Day 9 Screenshot Inventory & Analysis

> **BCPD Python Cohort 2 Certification Preparation**  
> **Batch:** 34 Newly Added Screenshots (Added 17 Nov 2026)  
> **Course Scope:** 
> - **Week 2 • Day 8 (Monday 16 Nov 2026):** Tuples, Dictionaries & Sets (Manual §8.1–8.8 + §9.1–9.9; Domain 2: Data Structures, 15%)
> - **Week 2 • Day 9 (Tuesday 17 Nov 2026):** OOP Part 1: Classes, Objects & Encapsulation (Manual §10.1–10.10; Domain 3: Object-Oriented Programming, 15%)
> - **Review / Supplemental Slides:** List methods, 2D grid trap, string formatting styles, f-strings, and classroom quiz answers.

---

## 1. Inventory & Metadata Matrix

| Image ID | Original Filename | Topic | Manual / Slide | Slide Title | Code File | Status | Notes |
|---|---|---|---|---|---|:---:|---|
| **D8-01** | `WhatsApp Image 2026-11-17 at 21.28.15.jpeg` | Day 8 — Title | Title Slide / Slide 1 | Tuples, Dictionaries & Sets | `day8.py` | Clear | Week 2 • Day 8 (Monday 16 Nov 2026); Domain 2 (Data Structures 15%); `Counter.most_common(1)` |
| **D8-02** | `WhatsApp Image 2026-11-17 at 21.28.15kli.jpeg` | Day 8 — Agenda | Objectives & Agenda / Slide 2 | Today's objectives & agenda | — | Clear | Tuples, packing/unpacking, dicts, dict methods, edge cases, comprehensions, Counter/defaultdict, sets, set algebra, Lab 8.1 |
| **D8-03** | `WhatsApp Image 2026-11-17 at 21.28.16uyt.jpeg` | Day 8 — Tuples | Manual §8.1–8.2 | Tuples | `tuples.py` | Clear | Single-item comma `(5,)`, `count()`, `index()`, immutable error, mutable element in tuple mutation |
| **D8-04** | `WhatsApp Image 2026-11-17 at 21.28.16optr.jpeg` | Day 8 — Unpacking | Manual §8.1, 8.3 | Packing, unpacking & named tuples | `records.py` | Clear | Packing `3, 4`, unpacking `x, y`, `min_max()` returns tuple, `ValueError` count mismatch, `namedtuple` |
| **D8-05** | `WhatsApp Image 2026-11-17 at 21.28.16kytr.jpeg` | Day 8 — Dict Methods | Manual §8.5–8.6 | Dictionary methods | Table | Clear | Table of dict methods: `keys()`, `values()`, `items()`, `get()`, `pop()`, `popitem()`, `update()`, `setdefault()`, `fromkeys()`, `dict.fromkeys("ab", [])` trap |
| **D8-06** | `WhatsApp Image 2026-11-17 at 21.28.17potw.jpeg` | Day 8 — Dict Methods | Manual §8.5–8.6 | Dictionary methods | Table | Clear | Duplicate/alternative angle of D8-05 |
| **D8-07** | `WhatsApp Image 2026-11-17 at 21.28.17piw.jpeg` | Day 8 — Dict Lookups | Manual §8.4–8.5 | Dictionaries: keys & lookups | `dicts.py` | Clear | Hashable keys, insertion order (3.7+), `d[k]` vs `get()`, `in` checks keys, `{1: 'a', 1.0: 'b'}` key collision |
| **D8-08** | `WhatsApp Image 2026-11-17 at 21.28.18asd.jpeg` | Day 8 — Dict/Tuple Edge Cases | Manual §8.5–8.6 | Dictionary & tuple edge cases | `edge_cases.py` | Clear | `popitem()`, dict equality ignores order, `sorted(d)`, `all({}) is True`, dict inversion, `Counter` union/intersection, `defaultdict`, tuple compare |
| **D8-09** | `WhatsApp Image 2026-11-17 at 21.28.18lb.jpeg` | Day 8 — Dict/Tuple Edge Cases | Manual §8.5–8.6 | Dictionary & tuple edge cases | `edge_cases.py` | Clear | Duplicate/alternative angle of D8-08 |
| **D8-10** | `WhatsApp Image 2026-11-17 at 21.28.21jjm.jpeg` | Day 8 — Collections | Manual §9.3 | collections: Counter & defaultdict | `collections_demo.py` | Clear | `Counter` word frequency, `most_common(2)`, missing key counts as 0, `defaultdict(list)` grouping, `OrderedDict`, `ChainMap` |
| **D8-11** | `WhatsApp Image 2026-11-17 at 21.28.22m.jpeg` | Day 8 — Sets | Manual §9.4 | Sets: unique & unordered | `sets.py` | Clear | `{1, 2}` vs `set()`, `{}` is dict, hashable items, `remove()` vs `discard()`, `pop()`, O(1) membership |
| **D8-12** | `WhatsApp Image 2026-11-17 at 21.28.22mn.jpeg` | Day 8 — Set Algebra | Manual §9.5 | Set algebra | Table | Clear | Union `\|`, intersection `&`, difference `-`, symmetric difference `^`, subset `<=`, `isdisjoint()`, `frozenset` |
| **D8-13** | `WhatsApp Image 2026-11-17 at 21.28.23mnb.jpeg` | Day 8 — Structure Selection | Manual §9.9 | Choosing the right structure | Table | Clear | Decision matrix: list, tuple, dict, set, frozenset (Ordered, Mutable, Duplicates, Best for) |
| **D8-14** | `WhatsApp Image 2026-11-17 at 21.28.23.jpeg` | Day 8 — Set Traps | Manual §9.6–9.7 | More set operations & set traps | Table | Clear | `{1, 2} < {1, 2, 3}`, `{1}+{2}` TypeError, `update(iterable)`, `\|` operator vs `.union()` iterable, `all(set()) is True`, mutable item TypeError |
| **D9-01** | `WhatsApp Image 2026-11-17 at 21.28.25.jpeg` | Day 9 — Title | Title Slide / Slide 1 | OOP Part 1: Classes, Objects & Encapsulation | `day9.py` | Clear | Week 2 • Day 9 (Tuesday 17 Nov 2026); Domain 3 (OOP 15%); `Account` class with `__init__` and `self.__balance` |
| **D9-02** | `WhatsApp Image 2026-11-17 at 21.28.26.jpeg` | Day 9 — Agenda | Objectives & Agenda / Slide 2 | Today's objectives & agenda | — | Clear | Agenda: 10.1 Why OOP?, 10.2 `__init__` & self, 10.4 Instance methods, 10.5 Class vs instance attributes, 10.6 Dunders, 10.7 Encapsulation, 10.8 @property, 10.4 Inspecting objects, Lab 9.1 |
| **D9-03** | `WhatsApp Image 2026-11-17 at 21.28.26nnmm.jpeg` | Day 9 — Agenda | Objectives & Agenda / Slide 2 | Today's objectives & agenda | — | Clear | Duplicate/alternative angle of D9-02 |
| **D9-04** | `WhatsApp Image 2026-11-17 at 21.28.27kl.jpeg` | Day 9 — OOP Overview | Manual §10.1 | Why object-oriented programming? | Four cards | Clear | Definitions: Class (blueprint), Object (instance), Encapsulation (guard internals), Coming next (Inheritance & polymorphism) |
| **D9-05** | `WhatsApp Image 2026-11-17 at 21.28.28vb.jpeg` | Day 9 — Class Definition | Manual §10.2–10.3 | Defining a class: `__init__` and self | `account.py` | Clear | PascalCase naming, `__init__` runs automatically, `self` is current object, `BankAccount("Ada", 100)`, `type(acct).__name__` |
| **D9-06** | `WhatsApp Image 2026-11-17 at 21.28.29mn.jpeg` | Day 9 — Encapsulation | Manual §10.7 | Encapsulation: protected & private | `private.py` | Clear | `_owner` protected (convention), `__balance` private (mangled to `_Account__balance`), input validation, `AttributeError` on `acc.__balance` |
| **D9-07** | `WhatsApp Image 2026-11-17 at 21.28.30mk.jpeg` | Day 9 — Dunder Methods | Manual §10.6 | Dunder (magic) methods | `book.py` | Clear | `__str__` (readable), `__repr__` (unambiguous), `__eq__` (value equality vs `is`), `__len__` (length of object) |
| **D9-08** | `WhatsApp Image 2026-11-17 at 21.28.3089.jpeg` | Day 9 — Attributes | Manual §10.5 | Class attributes vs instance attributes | `dogs.py` | Clear | Lookup order (instance first, then class), assigning via instance masks class, **shared mutable trap** (`tricks = []` shared by all instances!) |
| **D9-09** | `WhatsApp Image 2026-11-17 at 21.28.30.jpeg` | Day 9 — Instance Methods | Manual §10.4 | Instance methods & method calls | `counter.py` | Clear | `obj.method()` passes self automatically, forgetting self raises `TypeError`, returning `self` enables method chaining, `Clicker.click(c)` |
| **D9-10** | `WhatsApp Image 2026-11-17 at 21.28.30nn.jpeg` | Day 9 — Properties | Manual §10.8 | @property: getters, setters & read-only | `temperature.py` | Clear | `@property` getter, `@celsius.setter` with validation (`< -273.15`), read-only property without setter raises `AttributeError` on assignment |
| **D9-11** | `WhatsApp Image 2026-11-17 at 21.28.31kl.jpeg` | Day 9 — Access Matrix | Manual §10.7 | Encapsulation: who can access what | Table | Clear | Access table: `x` (public), `_x` (protected), `__x` (private/mangled), `__x__` (dunder/special) across inside class, subclass, and outside |
| **D5-REV-01** | `WhatsApp Image 2026-11-17 at 21.28.19vv.jpeg` | Review — List Methods | Manual §6.4–6.5 | List methods | Table | Clear | Methods: `append`, `extend`, `insert`, `remove`, `pop`, `index`/`count`, `sort`/`reverse`, `copy`/`clear`. Callout: `a = a.sort()` returns `None` trap! |
| **D5-REV-02** | `WhatsApp Image 2026-11-17 at 21.28.19lkj.jpeg` | Review — f-strings | Manual §5.18 | f-strings (Python 3.6+) | `fstrings.py` | Clear | `f"{expr}"`, format specifiers, `f"{x=}"` (3.8+), conversions `!r` and `!s`, `datetime` format specifiers |
| **D5-REV-03** | `WhatsApp Image 2026-11-17 at 21.28.19zx.jpeg` | Review — List Methods | Manual §6.4–6.5 | List methods | Table | Clear | Duplicate/angle of D5-REV-01 |
| **D5-REV-04** | `WhatsApp Image 2026-11-17 at 21.28.20mn.jpeg` | Review — f-strings | Manual §5.18 | f-strings (Python 3.6+) | `fstrings.py` | Clear | Duplicate/angle of D5-REV-02 |
| **D5-REV-05** | `WhatsApp Image 2026-11-17 at 21.28.20okl.jpeg` | Review — Strings Quiz | Slide 16 | Answers & explanations | Table | Clear | Official answer key: `# 1 C -1`, `# 2 A 3.14`, `# 3 D 'a-b-c'`, `# 4 B 2.3\|`, `# 5 C "A1".isalnum()` |
| **D5-REV-06** | `WhatsApp Image 2026-11-17 at 21.28.20hh.jpeg` | Review — Strings Quiz | Slide 16 | Answers & explanations | Table | Clear | Duplicate of D5-REV-05 |
| **D5-REV-07** | `WhatsApp Image 2026-11-17 at 21.28.21kk.jpeg` | Review — List Indexing | Manual §6.1–6.3 | Lists: creation, indexing & slicing | `lists.py` | Clear | Negative indexing, step slicing `[::2]`, slice assignment `items[1:3] = ["X"]`, list concatenation and repetition |
| **D5-REV-08** | `WhatsApp Image 2026-11-17 at 21.28.21jj.jpeg` | Review — 2D Grid Trap | Manual §6.6 | Nested lists & the 2D trap | `grid.py` | Clear | `grid[row][col]`, `bad = [[0] * 3] * 3` reference duplication trap vs `good = [[0] * 3 for _ in range(3)]` fix |
| **D5-REV-09** | `WhatsApp Image 2026-11-17 at 21.28.21kl.jpeg` | Review — Old Formatting | Manual §5.16–5.17 | Formatting with % and str.format() | `old_styles.py` | Clear | `%s`, `%d`, `%.2f`, `str.format()` positional `{0}` and named `{n}`, doubling `{{literal}}` braces |

---

## 2. Verbatim Code Extraction: Day 8 (Tuples, Dicts & Sets)

### Day 8 Title Snippet: `day8.py` `[Course: D8-01]`
```python
from collections import Counter
words = "to be or not to be".split()
print(Counter(words).most_common(1))
# [('to', 2)]
```

### Day 8: `tuples.py` `[Course: D8-03]`
```python
t = (1, 2, 3)
print(type((5)), type((5,)))       # -> <class 'int'> <class 'tuple'>
print(t[1:], t * 2)               # -> (2, 3) (1, 2, 3, 1, 2, 3)
print(t.count(2), t.index(3))     # -> 1 2
# t[0] = 9 TypeError: immutable
x = ([1], 2)
x[0].append(5)
print(x)                          # -> ([1, 5], 2)
print(len(()), tuple("ab"))       # -> 0 ('a', 'b')
```

### Day 8: `records.py` `[Course: D8-04]`
```python
point = 3, 4                      # packing
x, y = point                      # unpacking
print(x + y)                      # -> 7

def min_max(nums):
    return min(nums), max(nums)   # returns one tuple

lo, hi = min_max([7, 2, 9])
print(lo, hi)                     # -> 2 9

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p[1], p)               # -> 1 2 Point(x=1, y=2)
```

### Day 8: `dicts.py` `[Course: D8-07]`
```python
ages = {"Ada": 36, "Bo": 25}
ages["Cy"] = 30                   # add
ages["Bo"] = 26                   # update
print(ages)                       # -> {'Ada': 36, 'Bo': 26, 'Cy': 30}
print(ages.get("Zed"))            # -> None
print(ages.get("Zed", 0))         # -> 0
print("Ada" in ages, 36 in ages)  # -> True False
del ages["Cy"]
print(len(ages))                  # -> 2
print({1: "a", 1.0: "b"})         # -> {1: 'b'}
```

### Day 8: Dictionary Methods Table `[Course: D8-05, D8-06]`
```python
# With d = {"a": 1}
list(d.items())                   # -> [('a', 1)] - live view objects
d.get("z", 0)                     # -> 0
d.pop("a")                        # -> 1, and the key is removed
d.popitem()                       # Removes the last inserted pair
d.update(b=2)                     # Adds or overwrites keys
d.setdefault("c", [])             # Returns the value; inserts [] if missing
dict.fromkeys("ab", 0)            # -> {'a': 0, 'b': 0}
d.copy()                          # Shallow copy
d.clear()                         # Empty the dict

# CRITICAL TRAP:
# dict.fromkeys("ab", []) shares ONE list between all keys — the same trap as [[0] * 3] * 3.
```

### Day 8: `edge_cases.py` `[Course: D8-08, D8-09]`
```python
d = {"a": 1, "b": 2}
d["c"] = 3
print(d.popitem())                            # -> ('c', 3)
print({"x": 1, "y": 2} == {"y": 2, "x": 1})   # -> True
print(sorted({"b": 1, "a": 2}), all({}))      # -> ['a', 'b'] True
print(dict(zip(d.values(), d)))               # -> {1: 'a', 2: 'b'}

from collections import Counter, defaultdict
c1, c2 = Counter("aab"), Counter("abb")
print(c1 | c2)                                # -> Counter({'a': 2, 'b': 2})
print(c1 & c2)                                # -> Counter({'a': 1, 'b': 1})
print(defaultdict(int)["x"], repr(defaultdict(str)["y"])) # -> 0 ''
print((1, 2) < (1, 3), sum((1, 2), 10))       # -> True 13
print(sorted((3, 1, 2)))                      # -> [1, 2, 3]
```

### Day 8: `collections_demo.py` `[Course: D8-10]`
```python
from collections import Counter, defaultdict

words = "the cat and the hat and the bat".split()
counts = Counter(words)
print(counts["the"])                          # -> 3
print(counts.most_common(2))                  # -> [('the', 3), ('and', 2)]
print(counts["dog"])                          # -> 0 (no KeyError)

by_letter = defaultdict(list)
for w in ["apple", "avocado", "banana"]:
    by_letter[w[0]].append(w)
print(dict(by_letter))                        # -> {'a': ['apple', 'avocado'], 'b': ['banana']}
```

### Day 8: `sets.py` `[Course: D8-11]`
```python
s = {3, 1, 3, 2}
print(len(s))                                 # -> 3
print(type({}), type(set()))                  # -> <class 'dict'> <class 'set'>
s.add(4)
s.discard(10)                                 # no error
print(sorted(s))                              # -> [1, 2, 3, 4]
print(sorted(set("banana")))                  # -> ['a', 'b', 'n']
# s[0] TypeError: not subscriptable
# s.remove(10) KeyError
```

### Day 8: Set Algebra & Traps `[Course: D8-12, D8-14]`
```python
a = {1, 2, 3}
b = {3, 4}

print(a | b)                                  # -> {1, 2, 3, 4} (Union)
print(a & b)                                  # -> {3} (Intersection)
print(a - b)                                  # -> {1, 2} (Difference)
print(a ^ b)                                  # -> {1, 2, 4} (Symmetric difference)
print({1, 2} <= a)                            # -> True (Subset)
print({1, 2} < {1, 2, 3})                     # -> True (Proper subset)
print(a.isdisjoint({9}))                      # -> True

# Set traps & edge cases:
# {1} + {2} -> TypeError: unsupported operand type(s) for +: 'set' and 'set'
# {1} * 2   -> TypeError: unsupported operand type(s) for *: 'set' and 'int'
# {1} | [2, 3] -> TypeError: unsupported operand type(s) for |: 'set' and 'list'
# {1}.union([2, 3]) -> {1, 2, 3} (methods accept ANY iterable)
# all(set()) -> True (vacuous truth)
# {[1, 2]} -> TypeError: unhashable type: 'list' (use frozenset inside sets)
```

### Day 8: Container Selection Matrix `[Course: D8-13]`
| Type | Ordered | Mutable | Duplicates | Best For |
|---|:---:|:---:|:---:|---|
| `list` | Yes | Yes | Yes | Sequences you add to, remove from, and sort |
| `tuple` | Yes | No | Yes | Fixed records, dict keys, multiple return values |
| `dict` | Insertion | Yes | Unique keys | Looking values up by key |
| `set` | No | Yes | No | Uniqueness and fast average $O(1)$ membership tests |
| `frozenset` | No | No | No | A hashable set (dict key or set member) |

---

## 3. Verbatim Code Extraction: Day 9 (OOP Part 1)

### Day 9 Title Snippet: `day9.py` `[Course: D9-01]`
```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

acct = Account("Ada")
```

### Day 9: `account.py` `[Course: D9-05]`
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acct = BankAccount("Ada", 100)
print(acct.owner, acct.balance)       # -> Ada 100
print(acct.deposit(50))               # -> 150
print(type(acct).__name__)            # -> BankAccount
```

### Day 9: `counter.py` `[Course: D9-09]`
```python
class Clicker:
    def __init__(self):
        self.count = 0

    def click(self, step=1):
        self.count += step
        return self                   # enables chaining

c = Clicker()
c.click().click(5)
print(c.count)                        # -> 6
Clicker.click(c)                      # same as c.click()
print(c.count)                        # -> 7
```

### Day 9: `dogs.py` `[Course: D9-08]`
```python
class Dog:
    species = "Canis familiaris"      # class attribute: shared
    tricks = []                       # shared mutable: a trap!

    def __init__(self, name):
        self.name = name              # instance attribute

a, b = Dog("Rex"), Dog("Fido")
a.tricks.append("sit")
print(b.tricks)                       # -> ['sit']
a.species = "wolf"                    # creates an instance attribute
print(a.species, b.species)           # -> wolf Canis familiaris
print(Dog.species)                    # -> Canis familiaris
```

### Day 9: `book.py` `[Course: D9-07]`
```python
class Book:
    def __init__(self, title, pages):
        self.title, self.pages = title, pages

    def __str__(self):
        return f"{self.title} ({self.pages}p)"

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"

    def __eq__(self, other):
        return self.title == other.title

    def __len__(self):
        return self.pages

b = Book("Dune", 412)
print(b)                              # -> Dune (412p)
print(repr(b))                        # -> Book('Dune', 412)
print(len(b), b == Book("Dune", 1))   # -> 412 True
```

### Day 9: `private.py` `[Course: D9-06]`
```python
class Account:
    def __init__(self, balance):
        self._owner = "Ada"           # protected
        self.__balance = balance      # private (mangled)

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

acc = Account(100)
print(acc.withdraw(30))               # -> 70
print(acc._Account__balance)          # -> 70
print(acc._owner)                     # -> Ada
# acc.__balance AttributeError
```

### Day 9: Encapsulation Access Matrix `[Course: D9-11]`
| Identifier | Kind | Inside Class | In Subclass | From Outside |
|---|---|:---:|:---:|---|
| `x` | Public | `✓ self.x` | `✓ self.x` | `✓ obj.x` |
| `_x` | Protected (convention) | `✓ self._x` | `✓ self._x` | Works, but you shouldn't |
| `__x` | Private (name-mangled) | `✓ self.__x` | `✗ stored as _Parent__x` | `✗ AttributeError`; `obj._Cls__x` works |
| `__x__` | Special (dunder) | Not mangled | `✓` | `✓ obj.__x__` |

### Day 9: `temperature.py` `[Course: D9-10]`
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius        # runs the setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):             # read-only
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
t.celsius = 30
print(t.celsius, t.fahrenheit)        # -> 30 86.0
```

---

## 4. Verbatim Code Extraction: Review Slides

### `lists.py` `[Course: D5-REV-07]`
```python
items = ["a", "b", "c", "d", "e"]
print(items[1], items[-1])       # -> b e
print(items[1:4])                # -> ['b', 'c', 'd']
print(items[::2])                # -> ['a', 'c', 'e']
print(items[::-1][:2])           # -> ['e', 'd']
items[0] = "A"
items[1:3] = ["X"]               # slice assignment
print(items)                     # -> ['A', 'X', 'd', 'e']
print(list("hey"), len(items))   # -> ['h', 'e', 'y'] 4
print([1, 2] + [3], [0] * 3)     # -> [1, 2, 3] [0, 0, 0]
```

### `grid.py` `[Course: D5-REV-08]`
```python
grid = [[1, 2, 3], [4, 5, 6]]
print(grid[1][2])                # -> 6
for row in grid:
    print(sum(row), end=" ")     # -> 6 15
print()

bad = [[0] * 3] * 3              # 3 references to ONE row
bad[0][0] = 1
print(bad)                       # -> [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

good = [[0] * 3 for _ in range(3)] # 3 separate rows
good[0][0] = 1
print(good)                      # -> [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### `old_styles.py` `[Course: D5-REV-09]`
```python
name, age, pi = "Ada", 36, 3.14159
print("%s is %d" % (name, age))                 # -> Ada is 36
print("Pi is %.2f" % pi)                        # -> Pi is 3.14
print("[%5d]" % 42)                             # -> [   42]
print("{} and {}".format("x", "y"))             # -> x and y
print("{1} {0}".format("a", "b"))               # -> b a
print("{n} scored {s}".format(n="Bo", s=9))     # -> Bo scored 9
print("{{literal}}".format())                   # -> {literal}
```

### `fstrings.py` `[Course: D5-REV-02, D5-REV-04]`
```python
name, price, x = "ada", 1234.5, 5
print(f"Hi {name.title()}!")                    # -> Hi Ada!
print(f"Total: {price:.2f}")                    # -> Total: 1234.50
print(f"{price:,.1f}")                          # -> 1,234.5
print(f"{x=}")                                  # -> x=5
print(f"{name!r}")                              # -> 'ada'
print(f"{x * 2 + 1}")                           # -> 11

from datetime import date
d = date(2026, 10, 26)
print(f"{d:%d %b %Y}")                          # -> 26 Oct 2026
```

### Knowledge Check Answers & Explanations `[Course: D5-REV-05, D5-REV-06]`
| # | Answer | Why |
|---|---|---|
| **1** | `C -1` | `find()` returns `-1` when the substring is missing; `index()` would raise. |
| **2** | `A 3.14` | `.2f` rounds to two decimal places. |
| **3** | `D 'a-b-c'` | The separator goes between items, not at the ends. |
| **4** | `B  2.3\|` | Width 5 pads on the left; 1 decimal place gives `2.3`. |
| **5** | `C "A1".isalnum()` | `"A1"` is all letters and digits; the `is...` methods are `False` for `""`. |
