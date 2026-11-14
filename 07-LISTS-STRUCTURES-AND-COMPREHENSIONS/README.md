# Module 07: Lists, Data Structures, and Comprehensions

> **BCPD Python Cohort 2 Certification Preparation**  
> **Source Screen Mappings:** `IMG-03, IMG-53, IMG-54, IMG-61, IMG-67, IMG-70, IMG-71, IMG-74, IMG-75, IMG-77, IMG-78, IMG-79` + `D6-01` to `D6-09`, `D6-11`  
> **Manual Sections:** `§6.1–6.6` (Day 5) & `§7.1–7.5` (Day 6 — Thursday 12 Nov 2026)  
> **Topic Classification:** Core Certification Subject & Domain 2 • Data Structures (15%)

---

## 1. List Fundamentals: Indexing, Slicing, and Mutability `[Course: IMG-03, IMG-53, IMG-54, IMG-61, IMG-78]`

### Creation and Heterogeneity
A Python list is an ordered, mutable sequence of object references. Lists can store mixed data types and can grow or shrink dynamically:
```python
mixed = [1, "two", 3.0, [4, 5], True]
empty = [] # or list()
```

### Indexing and Slicing
- 0-based indexing from left (`[0]`), -1-based from right (`[-1]`).
- Slices produce a new list (a shallow copy of the subrange):
  ```python
  nums = [10, 20, 30, 40, 50]
  nums[1:4]   # [20, 30, 40]
  nums[::-1]  # [50, 40, 30, 20, 10] (Reversed copy)
  ```
- **Slice Assignment (List Modification):**
  Unlike strings, lists support item and slice assignment:
  ```python
  nums = [1, 2, 3, 4]
  nums[1:3] = [20, 30, 40]  # nums is now [1, 20, 30, 40, 4]
  nums[1:4] = []            # Deletes elements: nums is now [1, 4]
  ```

---

## 2. List Methods and the `None` Return Trap `[Course: IMG-67, IMG-70, IMG-71, D6-02]`

Python distinguishes strictly between in-place mutator methods and functions that return new objects.

| Method | Description | Return Value | Complexity |
| :--- | :--- | :---: | :---: |
| `list.append(x)` | Appends `x` to end of list | `None` | $O(1)$ amortized |
| `list.extend(iterable)` | Appends all items from iterable | `None` | $O(k)$ |
| `list.insert(i, x)` | Inserts `x` before index `i` | `None` | $O(n)$ |
| `list.remove(x)` | Removes first occurrence of `x` (raises `ValueError` if absent) | `None` | $O(n)$ |
| `list.pop([i])` | Removes and returns item at index `i` (default last: `i=-1`) | **Item** | $O(1)$ for last, $O(n)$ for arbitrary |
| `list.clear()` | Removes all items | `None` | $O(n)$ |
| `list.index(x[, start[, end]])` | Returns index of first occurrence (raises `ValueError` if absent) | **int** | $O(n)$ |
| `list.count(x)` | Returns number of occurrences | **int** | $O(n)$ |
| `list.sort(key=None, reverse=False)` | Sorts the list **in place** (Timsort) | `None` | $O(n \log n)$ |
| `list.reverse()` | Reverses the elements **in place** | `None` | $O(n)$ |

> [!WARNING]
> ### The `None` Return Trap (Number One Certification Trap!)
> In-place mutators (`append`, `extend`, `sort`, `reverse`, `insert`, `clear`) return `None`.
> ```python
> items = [3, 1, 2]
> sorted_items = items.sort()  # MISTAKE! sorted_items is now None!
> print(sorted_items)          # Output: None
> print(items)                 # Output: [1, 2, 3]
> ```

### `sorted()` vs `.sort()` and Custom Key Sorting `[Course: D6-02 / Manual §7.1]`
- `sorted(iterable)` returns a **new** sorted list and works on any iterable; `list.sort()` sorts **in place** and returns `None`.
- Both accept `key=` (a callable applied to each item before comparing) and `reverse=True`.
- **Stable Sorting:** Python's Timsort algorithm is *stable*—items with equal keys retain their original relative order:
  ```python
  people = [("Bo", 25), ("Ada", 36), ("Cy", 25)]
  sorted(people, key=lambda p: p[1])
  # -> [('Bo', 25), ('Cy', 25), ('Ada', 36)]  ("Bo" stays before "Cy")
  ```
- **ASCII Case Sensitivity:** Upper-case letters sort before lower-case characters:
  ```python
  words = ["Pear", "apple", "fig"]
  sorted(words)                # -> ['Pear', 'apple', 'fig'] (ASCII 'P'=80 < 'a'=97)
  sorted(words, key=str.lower) # -> ['apple', 'fig', 'Pear'] (Case-insensitive)
  ```

---

## 3. Comparing, Combining & Flattening Lists `[Course: D6-03 / Manual §7.2]`

### Element-by-Element Comparison
Lists compare item by item from the left (lexicographically), like words in a dictionary:
```python
[1, 2, 3] < [1, 3]  # True (at index 1: 2 < 3)
[2] > [1, 9]        # True (at index 0: 2 > 1)
```

### In-Place Concatenation (`+=`) vs New List (`+`)
- `lst += [x]` mutates the list **in place** (re-uses existing object; caller sees change).
- `lst = lst + [x]` allocates a **new list** (rebinds local name; caller's object is unaffected).
```python
def grow(lst):    lst += [4]
def rebuild(lst): lst = lst + [5]

a = [1]
grow(a); rebuild(a)
print(a)  # Output: [1, 4]
```

### Flattening Nested Lists
```python
# Flattens one level using built-in sum() with an empty list start:
nested = [[1, 2], [3]]
flat = sum(nested, [])  # [1, 2, 3]
```

### Dynamic Insertion by Search
```python
nums = [5, 9]
nums.insert(nums.index(9), 7)
print(nums)  # [5, 7, 9]
```

---

## 4. What List Operations Cost: Big-O Complexity `[Course: D6-08, D6-09 / Manual §7.5]`

The instructor notes: *"Know the cost of what you call — it shows up in scenario questions."*

| Operation | Code Example | Time Complexity | Underlying Reason |
|---|---|:---:|---|
| **Index / Item Assignment** | `a[i]`, `a[i] = x` | $O(1)$ | Direct pointer arithmetic in array |
| **Append / Pop at End** | `a.append(x)`, `a.pop()` | $O(1)$ amortized | Appends to end of pre-allocated array |
| **Insert / Pop at Front** | `a.insert(0, x)`, `a.pop(0)` | $O(n)$ | Must shift all $n$ subsequent pointers |
| **Search (Membership / Index)** | `x in a`, `a.index(x)` | $O(n)$ | Linear scan from index 0 |
| **Sort** | `a.sort()`, `sorted(a)` | $O(n \log n)$ | Timsort comparison and merge passes |
| **Copy / Slice** | `a[:]`, `a.copy()` | $O(n)$ | Allocates new array and copies pointers |

> [!TIP]
> For frequent membership tests, use a `set`: `x in s` is $O(1)$ on average.

---

## 5. Multidimensional Lists and the Reference Multiplication Trap `[Course: IMG-70, IMG-74]`

When initializing a matrix or 2D grid in Python, using `*` on a list containing another list multiplies the **references**, not the contents!

### The Trap:
```python
# BROKEN: All 3 rows point to the exact same list in memory!
grid = [[0] * 3] * 3

grid[0][0] = 99
print(grid)
# Output: [[99, 0, 0], [99, 0, 0], [99, 0, 0]]  <-- All rows changed!
```

### The Correct Idiom:
Use a list comprehension to instantiate a brand-new list for every row:
```python
# CORRECT: Creates 3 distinct row objects
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 99
print(grid)
# Output: [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 6. Sequence Unpacking and Queues `[Course: IMG-70, IMG-77]`

### Basic & Extended Unpacking (PEP 3132)
```python
# Basic Unpacking
x, y, z = [1, 2, 3]

# Extended Unpacking (captures remaining elements as a list)
first, *middle, last = [10, 20, 30, 40, 50]
# first = 10, middle = [20, 30, 40], last = 50

# Unpacking into Function Arguments
print(*[1, 2, 3], sep="-")  # Output: 1-2-3
```

### Queues vs Stacks Performance
- Python lists make efficient **stacks** (LIFO): `append()` and `pop()` are $O(1)$ amortized.
- Python lists make poor **queues** (FIFO): `pop(0)` is $O(n)$ because all subsequent elements must be shifted in memory.
- For $O(1)$ FIFO queues, use `collections.deque`:
  ```python
  from collections import deque
  q = deque(["a", "b", "c"])
  q.append("d")
  item = q.popleft()  # O(1) time!
  ```

---

## 7. Aliasing, Shallow Copies, and Deep Copies `[Course: IMG-74, IMG-78, IMG-79]`

Understanding Python's object-reference model is tested heavily:

```
a = [1, [2, 3]]
b = a              # Alias: b and a point to the EXACT same object (b is a)
c = a.copy()       # Shallow copy: new outer list, shared inner lists (c is not a, but c[1] is a[1])
d = copy.deepcopy(a) # Deep copy: completely independent recursive duplication
```

---

## 8. Comprehensions & Gotchas `[Course: IMG-71, D6-04, D6-05 / Manual §7.3–7.4]`

### Syntax & Where the `if` Goes:
- **Filtering:** Trailing `if`:
  `[expr for item in iterable if condition]`
  ```python
  [n for n in [3, -1, 4, -2] if n > 0]  # [3, 4]
  ```
- **Choosing Values:** `if-else` before `for`:
  `[a if condition else b for item in iterable]`
  ```python
  [n if n > 0 else 0 for n in [3, -1, 4, -2]]  # [3, 0, 4, 0]
  # Note: [n for n in nums if n > 0 else 0] is a SyntaxError!
  ```

### Matrix Building & Transposition
```python
# 2x3 Matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 3)]
# [[1, 2, 3], [2, 4, 6]]

# Transpose 2x3 into 3x2
transpose = [[row[i] for row in matrix] for i in range(3)]
# [[1, 2], [2, 4], [3, 6]]
```

### Matrix Diagonal Extraction `[Course: D6-05]`
Given a square $n \times n$ grid:
```python
g = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

main_diag = [g[i][i] for i in range(3)]        # [1, 5, 9]
anti_diag = [g[i][2 - i] for i in range(3)]    # [3, 5, 7]
```

### Map & Join Gotchas `[Course: D6-05]`
1. **`join()` needs strings:**
   `"-".join([1, 2, 3])` -> `TypeError`. Use `"-".join(map(str, [1, 2, 3]))`.
2. **`map` is lazy and has no `len()`:**
   `m = map(str.upper, ["a", "b"])`
   `len(m)` -> `TypeError: object of type 'map' has no len()`.
   Consuming `list(m)` once exhausts it; a second `list(m)` returns `[]`.

---

## 9. Common Exam Traps & Gotchas Summary

1. **Mutator Returns `None`:** `a = [1, 2].append(3)` sets `a = None`.
2. **Matrix Reference Multiplication:** `[[0] * 3] * 3` clones rows by reference; modifying one modifies all.
3. **Generator & Map Exhaustion:** Iterators evaluate lazily and are consumed only once; subsequent calls yield empty collections.
4. **Where `if` Goes in Comprehensions:** `[x for x in xs if c]` (filter) vs `[a if c else b for x in xs]` (value choice). Trailing `if-else` is a `SyntaxError`.
5. **ASCII Case-Sensitive Sort:** Upper-case letters precede lower-case (`"Pear" < "apple"`).
6. **`pop(0)` is $O(n)$:** Use `collections.deque.popleft()` for $O(1)$ queue operations.
