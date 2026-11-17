# Output Prediction Drills (Whiteboard & Mental Execution)

> **BCPD Python Cohort 2 Certification Preparation**  
> **Purpose:** Practice manual step-by-step code execution without running the interpreter. Trace variables, pointer bindings, and control flow line-by-line.

---

## Drill 1: Bitwise Flag State Tracing `[Course: IMG-14, IMG-18, IMG-20]`

### Code Snippet:
```python
READ  = 1  # 0b001
WRITE = 2  # 0b010
EXEC  = 4  # 0b100

perms = READ | WRITE    # Line 1
perms ^= EXEC           # Line 2
perms &= ~WRITE         # Line 3

has_read = bool(perms & READ)
has_write = bool(perms & WRITE)
has_exec = bool(perms & EXEC)

print(perms, has_read, has_write, has_exec)
```

### Trace Table:
| Line | Operation | Binary Representation | Integer Value |
| :--- | :--- | :--- | :---: |
| 1 | `perms = 1 \| 2` | `0b001 \| 0b010 = 0b011` | `3` |
| 2 | `perms ^= 4` | `0b011 ^ 0b100 = 0b111` | `7` |
| 3 | `perms &= ~2` | `0b111 & ~(0b010) = 0b111 & ...11111101 = 0b101` | `5` |
| 4 | `perms & READ` | `0b101 & 0b001 = 0b001` (truthy) | `True` |
| 5 | `perms & WRITE` | `0b101 & 0b010 = 0b000` (falsy) | `False` |
| 6 | `perms & EXEC` | `0b101 & 0b100 = 0b100` (truthy) | `True` |

### Final Output:
```
5 True False True
```

---

## Drill 2: String Slicing, Methods, and Immutability `[Course: IMG-57, IMG-58, IMG-60]`

### Code Snippet:
```python
phrase = "  pyTHon-cOHOrt-2  "
cleaned = phrase.strip()
transformed = cleaned[:6].capitalize() + cleaned[6:13].lower() + cleaned[-2:]
slice_rev = transformed[::-1]

print(f"'{transformed}'")
print(f"'{slice_rev}'")
```

### Trace Table:
| Variable | Value | Length | Notes |
| :--- | :--- | :---: | :--- |
| `phrase` | `"  pyTHon-cOHOrt-2  "` | 19 | Has 2 leading spaces, 2 trailing spaces |
| `cleaned` | `"pyTHon-cOHOrt-2"` | 15 | Whitespace stripped from both sides |
| `cleaned[:6]` | `"pyTHon"` | 6 | Sliced indices 0..5 |
| `.capitalize()` | `"Python"` | 6 | Capitalizes 'P', lowercases remainder |
| `cleaned[6:13]` | `"-cOHOrt"` | 7 | Sliced indices 6..12 |
| `.lower()` | `"-cohort"` | 7 | All lowercase |
| `cleaned[-2:]` | `"-2"` | 2 | Last 2 characters |
| `transformed` | `"Python" + "-cohort" + "-2"` = `"Python-cohort-2"` | 15 | Concatenated result |
| `slice_rev` | `"2-trohoc-nohtyP"` | 15 | Complete string reversal via step `-1` |

### Final Output:
```
'Python-cohort-2'
'2-trohoc-nohtyP'
```

---

## Drill 3: Nested Matrices, Aliases, and Copies `[Course: IMG-70, IMG-74, IMG-78]`

### Code Snippet:
```python
import copy

# Structure A: Reference multiplication trap
a = [[1, 2]] * 3

# Structure B: Independent comprehension
b = [[1, 2] for _ in range(3)]

# Modifications
a[0].append(99)
b[0].append(99)

print("a:", a)
print("b:", b)
```

### Trace Table:
- For `a`: `[1, 2]` is instantiated once. Outer list stores 3 identical pointers to that single list.
  - `a[0].append(99)` modifies the inner list to `[1, 2, 99]`.
  - All 3 rows point to this same inner list.
- For `b`: List comprehension creates 3 distinct list objects in memory.
  - `b[0].append(99)` modifies only row 0.

### Final Output:
```
a: [[1, 2, 99], [1, 2, 99], [1, 2, 99]]
b: [[1, 2, 99], [1, 2], [1, 2]]
```

---

## Drill 4: Comprehension vs Generator Exhaustion `[Course: IMG-78, IMG-79]`

### Code Snippet:
```python
nums = [1, 2, 3, 4]

# Eager list
eager = [x * 10 for x in nums if x % 2 == 0]

# Lazy generator
lazy = (x * 10 for x in nums if x % 2 == 0)

run1 = list(lazy)
run2 = list(lazy)
run3 = list(eager)

print("run1:", run1)
print("run2:", run2)
print("run3:", run3)
```

### Trace Table:
- Filtering condition: `x % 2 == 0` filters `2` and `4`.
- Expression: `x * 10` produces `20, 40`.
- `eager` stores `[20, 40]` permanently in memory.
- `lazy` is a generator iterator.
  - `run1 = list(lazy)` consumes the generator. Yields `20`, then `40`. Result: `[20, 40]`.
  - `run2 = list(lazy)` attempts to consume `lazy` again. Generator is already exhausted! Result: `[]`.
  - `run3 = list(eager)` converts list to list. Result: `[20, 40]`.

### Final Output:
```
run1: [20, 40]
run2: []
run3: [20, 40]
```

---

## Drill 5: Exception Handling Flow & Finally Overrides `[Course: IMG-22, IMG-45]`

### Code Snippet:
```python
def compute(x):
    logs = []
    try:
        logs.append("try")
        val = 10 // x
        logs.append(f"val={val}")
        return logs
    except ZeroDivisionError:
        logs.append("caught_zero")
        return logs
    else:
        logs.append("else")
    finally:
        logs.append("finally")

print(compute(2))
print(compute(0))
```

### Trace Table:
- **Call 1: `compute(2)`**
  - `logs.append("try")` -> `['try']`
  - `10 // 2 = 5` (no error)
  - `logs.append("val=5")` -> `['try', 'val=5']`
  - Initiates `return logs`.
  - Python defers return to execute `finally` block!
  - In `finally`: `logs.append("finally")` -> `['try', 'val=5', 'finally']`
  - Notice `logs` is a mutable list; modifying it in `finally` modifies the returned object!
  - `else` block is skipped because `return` was triggered inside `try`.
  - Returned: `['try', 'val=5', 'finally']`
- **Call 2: `compute(0)`**
  - `logs.append("try")` -> `['try']`
  - `10 // 0` raises `ZeroDivisionError`.
  - Jumps to `except ZeroDivisionError`: `logs.append("caught_zero")` -> `['try', 'caught_zero']`
  - Initiates `return logs`.
  - Python defers return to execute `finally` block!
  - In `finally`: `logs.append("finally")` -> `['try', 'caught_zero', 'finally']`
  - Returned: `['try', 'caught_zero', 'finally']`

### Final Output:
```
['try', 'val=5', 'finally']
['try', 'caught_zero', 'finally']
```

---

## Drill 6: Dictionary Hash Collision & Set Algebra Tracing `[Course: D8-07, D8-08, D8-14]`

### Code Snippet:
```python
# Part A: Key Hash Collision
d = {1: "alpha", 1.0: "beta", True: "gamma"}

# Part B: Set Operations & Discard
s1 = {1, 2, 3}
s2 = {3, 4}
diff = s1 - s2
diff.discard(99)

# Part C: Dict Inversion
m = {"x": 10, "y": 20}
inv = dict(zip(m.values(), m))

print(len(d), d[1])
print(sorted(diff))
print(inv[10])
```

### Trace Table:
- **Part A:**
  - Python checks key `1`: `hash(1) == 1`. Stores `1: "alpha"`.
  - Next key `1.0`: `1.0 == 1` is `True` and `hash(1.0) == 1`. Same key! Overwrites value: `{1: "beta"}`.
  - Next key `True`: `True == 1` is `True` and `hash(True) == 1`. Same key! Overwrites value: `{1: "gamma"}`.
  - Total length of `d`: `1`. `d[1]` evaluates to `"gamma"`.
- **Part B:**
  - `s1 - s2 = {1, 2, 3} - {3, 4} = {1, 2}`.
  - `diff.discard(99)`: element `99` is absent; `discard()` silently succeeds without error.
  - `sorted(diff)`: `[1, 2]`.
- **Part C:**
  - `m.values()` yields `(10, 20)`. `m` yields `('x', 'y')`.
  - `zip(m.values(), m)` pairs `(10, 'x')` and `(20, 'y')`.
  - `dict(...)` creates `{10: 'x', 20: 'y'}`.
  - `inv[10]` evaluates to `'x'`.

### Final Output:
```
1 gamma
[1, 2]
x
```

---

## Drill 7: OOP Class Lookup & Property Setter Validation `[Course: D9-08, D9-10]`

### Code Snippet:
```python
class Widget:
    count = 0
    items = []

    def __init__(self, name):
        self.name = name
        Widget.count += 1
        self.items.append(name)

w1 = Widget("A")
w2 = Widget("B")
w1.count = 100

print(w1.count, w2.count, Widget.count)
print(w2.items)
```

### Trace Table:
- `Widget.count` starts at `0`. `Widget.items` starts at `[]`.
- `w1 = Widget("A")`:
  - `Widget.count` incremented to `1`.
  - `self.items.append("A")` mutates the class-level list `Widget.items` -> `['A']`.
- `w2 = Widget("B")`:
  - `Widget.count` incremented to `2`.
  - `self.items.append("B")` mutates `Widget.items` -> `['A', 'B']`.
- `w1.count = 100`:
  - Assigns `100` into instance dictionary `w1.__dict__`.
  - `w1.count` resolves from `w1.__dict__` -> `100`.
  - `w2.count` has no instance attribute `count`, so resolves from `Widget.count` -> `2`.
  - `Widget.count` remains `2`.
- `w2.items`:
  - Resolves to shared class attribute `['A', 'B']`.

### Final Output:
```
100 2 2
['A', 'B']
```

