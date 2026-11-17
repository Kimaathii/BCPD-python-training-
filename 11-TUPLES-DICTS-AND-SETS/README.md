# Module 11: Tuples, Dictionaries & Sets

> **BCPD Python Certification — Domain 2: Data Structures (15%)**  
> **Student Manual Reference:** Day 8 (§8.1–8.8) + Day 9 (§9.1–9.9)  
> **Classroom Source Slides:** `D8-01` to `D8-14` (Week 2 • Day 8: Monday 16 Nov 2026)  
> **Core Theme:** *Pick the right container: immutable records, fast key lookups, and unique collections.*

---

## 1. Tuples & Records (`§8.1–8.3`)

### 1.1 Tuple Basics & Characteristics `[Course: D8-03]`
Tuples are **ordered**, **heterogeneous**, and **immutable** sequences.
- Defined using parentheses `(1, 2, 3)` or simply comma-separated values `1, 2, 3`.
- An empty tuple is written as `()`.
- **The Single-Item Comma Trap**:
  A single value in parentheses `(5)` is simply an integer `5` evaluated in parentheses (`type((5)) == int`). To create a 1-element tuple, a trailing comma is **mandatory**: `(5,)` or `5,` (`type((5,)) == tuple`).
- **Tuple Methods**: Because tuples are immutable, they possess only **two** methods:
  - `.count(value)`: counts occurrences of `value`.
  - `.index(value)`: returns the index of the first occurrence; raises `ValueError` if absent.
- **Mutability Inside Immutability**:
  While the tuple structure itself cannot be modified (cannot add, delete, or reassign elements), if a tuple contains a mutable object (such as a `list`), that nested object can still be mutated in place!

```python
# ORIGINAL CLASSROOM CODE [Course: D8-03]
t = (1, 2, 3)
print(type((5)), type((5,)))       # -> <class 'int'> <class 'tuple'>
print(t[1:], t * 2)               # -> (2, 3) (1, 2, 3, 1, 2, 3)
print(t.count(2), t.index(3))     # -> 1 2

# t[0] = 9 raises TypeError: 'tuple' object does not support item assignment
x = ([1], 2)
x[0].append(5)
print(x)                          # -> ([1, 5], 2)
print(len(()), tuple("ab"))       # -> 0 ('a', 'b')
```

### 1.2 Packing, Unpacking & Multiple Return Values `[Course: D8-04]`
- **Packing**: Values separated by commas automatically pack into a tuple: `point = 3, 4`.
- **Unpacking**: Assigning a tuple to variables unpacks them positionally: `x, y = point`.
- **Multiple Return Values**: When a Python function returns multiple expressions separated by commas (`return min(nums), max(nums)`), it really returns a **single tuple**.
- **Count Mismatch Trap**: Unpacking requires exact length matching. If counts differ, Python raises `ValueError: too many values to unpack (expected 2, got 3)` or `ValueError: not enough values to unpack`.
- **Star Unpacking**: `first, *middle, last = (1, 2, 3, 4, 5)` assigns `first=1`, `middle=[2, 3, 4]` (a list), `last=5`.

### 1.3 `collections.namedtuple` `[Course: D8-04]`
For lightweight records with readable field names without the overhead of a full class:
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p[1], p)               # -> 1 2 Point(x=1, y=2)
```
- Accessed by attribute name (`p.x`) or numerical index (`p[0]`).
- Immutable: `p.x = 10` raises `AttributeError: can't set attribute`.
- Memory efficient: retains the compact C-struct memory footprint of plain tuples.

---

## 2. Dictionaries: Keys, Hashability & Lookups (`§8.4–8.6`)

### 2.1 Dictionary Architecture & Hashability `[Course: D8-07]`
A dictionary (`dict`) is an associative array mapping unique keys to values.
- **Insertion Order**: Since Python 3.7 (guaranteed in language spec), dictionaries strictly preserve **insertion order**.
- **Hashability Requirement**: Keys must be **hashable**:
  - An object is hashable if it has a hash value that never changes during its lifetime (`__hash__()`), and can be compared to other objects (`__eq__()`).
  - **Hashable Types**: `str`, `int`, `float`, `tuple` (if all elements are hashable), `frozenset`, `bytes`.
  - **Unhashable Types**: `list`, `dict`, `set` (raises `TypeError: unhashable type: 'list'`).
- **Numeric Hash & Equality Collision Trap**:
  In Python, `1 == 1.0` is `True` and `hash(1) == hash(1.0)`. Therefore, `{1: "a", 1.0: "b"}` treats `1.0` and `1` as the **exact same key**! The existing key `1` has its value overwritten with `'b'`, producing `{1: 'b'}`!

```python
# ORIGINAL CLASSROOM CODE [Course: D8-07]
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

### 2.2 Dictionary Methods Table `[Course: D8-05, D8-06]`

| Method | Example (`d = {"a": 1}`) | Result / Effect |
|---|---|---|
| `keys()`, `values()`, `items()` | `list(d.items())` | `[('a', 1)]` — Dynamic live view objects |
| `get(k[, default])` | `d.get("z", 0)` | `0` (Returns default without adding to dict; default is `None`) |
| `pop(k[, default])` | `d.pop("a")` | `1`, and key `"a"` is removed; raises `KeyError` if absent and no default |
| `popitem()` | `d.popitem()` | Removes and returns the **last inserted** `(key, value)` pair (LIFO) |
| `update(other)` | `d.update(b=2)` | Adds or overwrites keys from another dict or key-value iterable |
| `setdefault(k, v)` | `d.setdefault("c", [])` | Returns existing value; if `k` missing, sets `d[k] = v` and returns `v` |
| `dict.fromkeys(seq, v)` | `dict.fromkeys("ab", 0)` | `{'a': 0, 'b': 0}` |
| `copy()` / `clear()` | `d.copy()` | Shallow copy / empties the dict |

> [!WARNING]
> **The `dict.fromkeys("ab", [])` Shared List Trap `[Course: D8-05]`**  
> When providing a mutable default object (like `[]` or `{}`) to `dict.fromkeys()`, the **exact same instance** is shared across every key:
> ```python
> d = dict.fromkeys("ab", [])
> d["a"].append(1)
> print(d)  # -> {'a': [1], 'b': [1]}  (BOTH keys mutated!)
> ```
> This is the dictionary analog of the nested list trap `[[0] * 3] * 3`. To create independent lists, use a dictionary comprehension: `{k: [] for k in "ab"}`.

### 2.3 Dictionary & Tuple Edge Cases `[Course: D8-08, D8-09]`
- **Equality Ignores Order**: `{"x": 1, "y": 2} == {"y": 2, "x": 1}` evaluates to `True`.
- **Relational Comparison Raises `TypeError`**: In Python 3, `d1 < d2` raises `TypeError: '<' not supported between instances of 'dict' and 'dict'`.
- **Dictionary Sorting**: `sorted(d)` sorts and returns the **keys** as a list: `sorted({"b": 1, "a": 2}) -> ['a', 'b']`.
- **Truthiness of Empty Dict**: `all({})` evaluates to `True` (vacuous truth: no element is falsy).
- **Inverting a Dictionary**: `dict(zip(d.values(), d))` or `{v: k for k, v in d.items()}`.
- **Tuple Lexicographical Comparison**: `(1, 2) < (1, 3)` evaluates to `True` (element-by-element comparison from index 0).

---

## 3. Specialized Collections: `Counter` & `defaultdict` (`§9.3`)

### 3.1 `collections.Counter` `[Course: D8-01, D8-08, D8-10]`
`Counter` is a dictionary subclass designed for counting hashable objects:
- Missing keys return `0` instead of raising `KeyError`.
- `.most_common(n)`: returns the $n$ most frequent elements and their counts as `[(elem, count), ...]`.
- **Counter Set-like Arithmetic**:
  - `c1 | c2`: Union — takes the **maximum** count for each key: `Counter("aab") | Counter("abb") -> Counter({'a': 2, 'b': 2})`.
  - `c1 & c2`: Intersection — takes the **minimum** count for each key: `Counter("aab") & Counter("abb") -> Counter({'a': 1, 'b': 1})`.
  - `c1 + c2`: Adds counts together.
  - `c1 - c2`: Subtracts counts (keeps only positive counts).

### 3.2 `collections.defaultdict` `[Course: D8-08, D8-10]`
`defaultdict` calls a factory function (e.g. `list`, `int`, `set`) whenever a key is accessed that does not currently exist:
- `defaultdict(int)`: missing keys initialize to `int()` (`0`).
- `defaultdict(list)`: missing keys initialize to `list()` (`[]`).
- `defaultdict(str)`: missing keys initialize to `str()` (`""`).

```python
# ORIGINAL CLASSROOM CODE [Course: D8-10]
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

### 3.3 Also Know for Certification `[Course: D8-10]`
- `collections.OrderedDict`: remembers insertion order (historically essential before 3.7); retains unique methods like `.move_to_end(key, last=True)`.
- `collections.ChainMap`: groups multiple dictionaries into a single updatable view, searching through them sequentially.

---

## 4. Sets & Set Algebra (`§9.4–§9.7`)

### 4.1 Set Fundamentals `[Course: D8-11]`
A `set` is an **unordered** collection of **unique**, **hashable** elements.
- Syntax: `{1, 2, 3}` or `set(iterable)`.
- **Empty Set Trap**: `{}` creates an **empty dictionary**, NOT a set! You MUST use `set()` to create an empty set.
- **Fast Membership**: Average $O(1)$ time complexity for `in` checks (backed by hash tables).
- **Mutators**:
  - `.add(x)`: adds element `x`.
  - `.discard(x)`: removes `x` if present; does **not** raise an error if absent.
  - `.remove(x)`: removes `x`; raises `KeyError` if absent!
  - `.pop()`: removes and returns an *arbitrary* element; raises `KeyError` if empty.

```python
# ORIGINAL CLASSROOM CODE [Course: D8-11]
s = {3, 1, 3, 2}
print(len(s))                                 # -> 3
print(type({}), type(set()))                  # -> <class 'dict'> <class 'set'>
s.add(4)
s.discard(10)                                 # no error
print(sorted(s))                              # -> [1, 2, 3, 4]
print(sorted(set("banana")))                  # -> ['a', 'b', 'n']
# s[0] raises TypeError: 'set' object is not subscriptable
# s.remove(10) raises KeyError: 10
```

### 4.2 Mathematical Set Algebra `[Course: D8-12]`

Given `a = {1, 2, 3}` and `b = {3, 4}`:

| Operation | Operator Syntax | Method Syntax | Result | Description |
|---|:---:|---|:---:|---|
| **Union** | `a \| b` | `a.union(b)` | `{1, 2, 3, 4}` | Elements in either `a` or `b` |
| **Intersection** | `a & b` | `a.intersection(b)` | `{3}` | Elements in both `a` and `b` |
| **Difference** | `a - b` | `a.difference(b)` | `{1, 2}` | Elements in `a` but not `b` |
| **Symmetric Diff** | `a ^ b` | `a.symmetric_difference(b)` | `{1, 2, 4}` | Elements in `a` or `b`, but not both |
| **Subset** | `a <= b` | `a.issubset(b)` | `False` | All elements of `a` are in `b` |
| **Proper Subset** | `a < b` | — | `False` | `a <= b` and `a != b` |
| **Superset** | `a >= b` | `a.issuperset(b)` | `False` | All elements of `b` are in `a` |
| **Disjoint** | — | `a.isdisjoint({9})` | `True` | No elements in common |
| **Immutable Set** | `frozenset(a)` | Hashable | `frozenset({1, 2, 3})` | Can be used as dict keys or set members |

### 4.3 Set Traps & Certification Exam Traps `[Course: D8-14]`

1. **Operator vs Method Type Trap**:
   - Bitwise set operators (`|`, `&`, `-`, `^`) require **both operands to be sets**.
     `{1} | [2, 3]` raises `TypeError: unsupported operand type(s) for |: 'set' and 'list'`.
   - Set methods (`union`, `intersection`, etc.) accept **any iterable**:
     `{1}.union([2, 3])` succeeds and returns `{1, 2, 3}`!
2. **Unsupported `+` and `*` Operators**:
   - Unlike lists and strings, sets do **not** support concatenation (`+`) or repetition (`*`):
     `{1} + {2}` -> `TypeError: unsupported operand type(s) for +: 'set' and 'set'`.
     `{1} * 2` -> `TypeError: unsupported operand type(s) for *: 'set' and 'int'`.
3. **Empty Collection Truthiness**:
   - `all(set())` evaluates to `True` (vacuous truth: no element is falsy).
   - `any(set())` evaluates to `False`.
4. **Nested Sets & Hashability**:
   - `{[1, 2]}` raises `TypeError: unhashable type: 'list'`.
   - `{{1}}` raises `TypeError: unhashable type: 'set'`.
   - To store a set inside a set, wrap it in `frozenset`: `{frozenset({1, 2}), frozenset({3})}`.

---

## 5. Choosing the Right Data Structure (`§9.9`) `[Course: D8-13]`

| Type | Ordered | Mutable | Duplicates | Best For |
|---|:---:|:---:|:---:|---|
| **`list`** | Yes | Yes | Yes | Sequences you add to, remove from, and sort |
| **`tuple`** | Yes | No | Yes | Fixed records, dict keys, multiple return values |
| **`dict`** | Insertion | Yes | Unique keys | Looking values up by key |
| **`set`** | No | Yes | No | Uniqueness and fast average $O(1)$ membership tests |
| **`frozenset`** | No | No | No | A hashable set (dict key or set member) |

---

## 6. Summary of Certification Gotchas

1. `(5)` is an `int`, while `(5,)` is a `tuple`.
2. `dict.fromkeys("ab", [])` creates **one shared list** referenced by all keys.
3. `{1: "a", 1.0: "b"}` collapses into `{1: "b"}` because `1 == 1.0` and `hash(1) == hash(1.0)`.
4. Set operators require sets on both sides (`s | [1]` raises `TypeError`), whereas methods accept any iterable (`s.union([1])` works).
5. Mutating methods (`s.add()`, `s.update()`, `d.update()`) return `None`.
6. `frozenset` is the only set type that can be placed inside another set or used as a dictionary key.
