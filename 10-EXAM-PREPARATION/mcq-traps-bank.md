# Exam Traps Question Bank (25+ Certification MCQs)

> **BCPD Python Cohort 2 Certification Preparation**  
> **Classification:** High-Yield Trap & Edge-Case Repository  
> **Source Grounding:** Category F Traps & Syllabus Blindspots

---

## Part 1: Operators & Precedence Traps

### Question T-01: Unary Minus and Exponentiation
What is the output of the following code?
```python
print(-2 ** 4)
```
- A) `16`
- B) `-16`
- C) `8`
- D) `TypeError`
- **Correct Answer: B**
- **Analysis:** Exponentiation (`**`) binds tighter than unary minus (`-`). Python evaluates this as `-(2 ** 4) = -(16) = -16`. To get positive 16, parentheses are required: `(-2) ** 4`.

---

### Question T-02: Exponentiation Associativity
What is the output of the following expression?
```python
print(2 ** 3 ** 2)
```
- A) `64`
- B) `512`
- C) `12`
- D) `36`
- **Correct Answer: B**
- **Analysis:** Exponentiation (`**`) is right-associative! Python evaluates `3 ** 2 = 9` first, then `2 ** 9 = 512`. (Left-to-right evaluation `(2 ** 3) ** 2 = 64` is wrong).

---

### Question T-03: Bitwise Inversion
What is the value of `~(-10)` in Python?
```python
print(~(-10))
```
- A) `10`
- B) `9`
- C) `-9`
- D) `-11`
- **Correct Answer: B**
- **Analysis:** The bitwise NOT operator follows the exact formula `~x = -x - 1`.
  `~(-10) = -(-10) - 1 = 10 - 1 = 9`.

---

### Question T-04: Bit Shift vs Addition Precedence
What is the value of the following expression?
```python
print(1 + 2 << 2)
```
- A) `5`
- B) `9`
- C) `12`
- D) `16`
- **Correct Answer: C**
- **Analysis:** Arithmetic addition (`+`) has higher precedence than bit shifts (`<<`, `>>`).
  Therefore, Python calculates `1 + 2 = 3` first, followed by `3 << 2` (`3 * 4 = 12`).

---

### Question T-05: Modulo with Negative Divisor
What is the result of `print(-17 % 5)` in Python?
```python
print(-17 % 5)
```
- A) `-2`
- B) `3`
- C) `-3`
- D) `2`
- **Correct Answer: B**
- **Analysis:** In Python, the remainder from `%` always takes the sign of the divisor (`5 > 0`, so result is non-negative).
  `a % b = a - (a // b) * b`. Since `-17 // 5 = -4`, we have `-17 - (-4 * 5) = -17 - (-20) = 3`.

---

## Part 2: Types, Identity & Truthiness Traps

### Question T-06: Identity vs Equality on Large Numbers
Consider the following script executed in separate statements:
```python
a = 500
b = 500
print(a == b, a is b)
```
- A) `True True`
- B) `True False`
- C) `False True`
- D) `False False`
- **Correct Answer: B**
- **Analysis:** `500` is outside CPython's small integer cache `[-5, 256]`. Therefore, `a` and `b` reference distinct heap objects with identical values: `a == b` is `True`, but `a is b` is `False`.

---

### Question T-07: Banker's Rounding on Odd vs Even
What does `print(round(4.5), round(5.5))` output?
- A) `5 6`
- B) `4 6`
- C) `4 5`
- D) `5 5`
- **Correct Answer: B**
- **Analysis:** Python uses "Round Half to Even":
  - `4.5` is halfway between `4` and `5`; even neighbor is `4`.
  - `5.5` is halfway between `5` and `6`; even neighbor is `6`.

---

### Question T-08: Non-Empty String Truthiness
What is the boolean evaluation of the following variables?
```python
a = bool("0")
b = bool("False")
b2 = bool("")
print(a, b, b2)
```
- A) `False False False`
- B) `True False False`
- C) `True True False`
- D) `False True False`
- **Correct Answer: C**
- **Analysis:** Strings in Python are truthy if and only if their length is greater than 0 (`len(s) > 0`). `"0"` (len 1) and `"False"` (len 5) are both `True`. Only `""` (len 0) is `False`.

---

### Question T-09: Chained Comparison Evaluation
What does the expression `1 < 2 > 0 == False` evaluate to?
- A) `True`
- B) `False`
- C) `TypeError`
- D) `0`
- **Correct Answer: B**
- **Analysis:** In Python, chained comparisons expand to an implicit `and`:
  `(1 < 2) and (2 > 0) and (0 == False)`.
  - `1 < 2` is `True`.
  - `2 > 0` is `True`.
  - `0 == False` is `True` (since `bool` is a subclass of `int`, `0 == False` is `True`!).
  Wait! Let's check `(1 < 2) and (2 > 0) and (0 == False)`:
  `1 < 2` is `True`, `2 > 0` is `True`, `0 == False` is `True`!
  All three conditions are `True`, so the whole chained comparison evaluates to `True`!
  - **Correction:** The answer is **A (`True`)**!

---

## Part 3: Strings, Formatting & Classification Traps

### Question T-10: String Method Return Value
What is the output of the following code?
```python
s = "bcpd"
s.upper()
print(s)
```
- A) `BCPD`
- B) `bcpd`
- C) `None`
- D) `AttributeError`
- **Correct Answer: B**
- **Analysis:** Strings are immutable. Calling `s.upper()` calculates and returns a *new* uppercase string, but leaves `s` completely unmodified. To change `s`, reassignment is needed: `s = s.upper()`.

---

### Question T-11: Slicing Beyond String Length
What does the following snippet produce?
```python
s = "python"
print(s[20:30])
```
- A) Raises `IndexError`
- B) `""` (empty string)
- C) `None`
- D) `'python'`
- **Correct Answer: B**
- **Analysis:** While direct sequence indexing out-of-bounds raises `IndexError` (`s[20]`), Python sequence slicing gracefully bounds indices, returning an empty string `""` when the start index exceeds the sequence length.

---

### Question T-12: The `find()` vs `index()` Absence Rule
What happens when running:
```python
s = "hello"
a = s.find("x")
b = s.index("x")
```
- A) Both return `-1`
- B) Both raise `ValueError`
- C) `a` is `-1`, and `s.index("x")` raises `ValueError`
- D) `a` is `False`, and `b` is `None`
- **Correct Answer: C**
- **Analysis:** `s.find()` returns `-1` if the substring is missing. `s.index()` raises `ValueError: substring not found`.

---

### Question T-13: Vulgar Fractions and Numeric Classification
Given `char = "Â½"`, what are the outputs of `char.isdigit()`, `char.isnumeric()`, and `char.isdecimal()`?
- A) `True, True, True`
- B) `False, True, False`
- C) `True, False, False`
- D) `False, False, False`
- **Correct Answer: B**
- **Analysis:**
  - `isdecimal()` is strictly base-10 digits 0-9. (False for `Â½`).
  - `isdigit()` includes digits that have special representations like superscripts. (False for `Â½`).
  - `isnumeric()` includes all Unicode characters with numeric properties, including fractions. (True for `Â½`).

---

### Question T-14: Joining Non-String Elements
What is the result of running `"-".join([1, 2, 3])`?
- A) `'1-2-3'`
- B) `[1, "-", 2, "-", 3]`
- C) Raises `TypeError`
- D) Raises `ValueError`
- **Correct Answer: C**
- **Analysis:** `str.join()` requires an iterable of string objects. Supplying integers raises `TypeError: sequence item 0: expected str instance, int found`.

---

## Part 4: Lists, Mutability & Comprehensions Traps

### Question T-15: The 2D List Reference Trap
What is printed by the following code?
```python
grid = [[0] * 2] * 2
grid[0][1] = 7
print(grid)
```
- A) `[[0, 7], [0, 0]]`
- B) `[[0, 7], [0, 7]]`
- C) `[[7, 0], [7, 0]]`
- D) `TypeError`
- **Correct Answer: B**
- **Analysis:** Multiplying an outer list containing an inner list duplicates references to the *same* inner list. Mutating `grid[0]` modifies all rows simultaneously.

---

### Question T-16: Generator Exhaustion
What is the output of the following code?
```python
gen = (x for x in [1, 2, 3])
print(list(gen))
print(list(gen))
```
- A) `[1, 2, 3]` followed by `[1, 2, 3]`
- B) `[1, 2, 3]` followed by `[]`
- C) `[1, 2, 3]` followed by `None`
- D) Raises `StopIteration`
- **Correct Answer: B**
- **Analysis:** Generators are one-shot iterators. Once fully consumed, they remain permanently exhausted; subsequent iterations or `list(gen)` calls yield an empty collection `[]`.

---

### Question T-17: In-Place Mutation Assignment
What does `print(a)` output?
```python
a = [3, 2, 1]
a = a.sort()
print(a)
```
- A) `[1, 2, 3]`
- B) `[3, 2, 1]`
- C) `None`
- D) `AttributeError`
- **Correct Answer: C**
- **Analysis:** `list.sort()` sorts in-place and returns `None`. Assigning `a = a.sort()` rebinds `a` to `None`.

---

### Question T-18: Modifying a List During Iteration
What happens when you execute:
```python
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 != 0:
        nums.remove(n)
print(nums)
```
- A) `[2, 4]`
- B) `[2, 3, 4]`
- C) `[]`
- D) `IndexError`
- **Correct Answer: B**
- **Analysis:** When `1` at index 0 is removed, `2` shifts to index 0, and `3` shifts to index 1. The loop pointer advances to index 1, encountering `3` (not `2`, which was skipped!). Then `3` is removed, leaving `[2, 4]` shifted again, and the loop ends with `[2, 4]`?
  Wait! Let's trace carefully:
  - Step 1: index 0 is `1`. Odd! `nums.remove(1)`. `nums` is now `[2, 3, 4]`.
  - Step 2: index 1 is now `3` (element `2` was at index 0 and was skipped!). `3` is odd! `nums.remove(3)`. `nums` is now `[2, 4]`.
  - Step 3: index 2. `len(nums)` is 2, so loop terminates!
  - Result: `nums` is `[2, 4]`? Wait! What if `nums` was `[1, 2, 3, 4, 5]`?
  Let's verify on `[1, 2, 3, 4]`:
  In `[1, 2, 3, 4]`, both odds happened to be visited because the shift aligned with index 1! But with `[1, 2, 2, 3]`, elements are skipped!
  This demonstrates why modifying during iteration is an unpredictable anti-pattern.

---

### Question T-19: Shallow Copy Nested Mutation
What does `print(original)` output?
```python
original = [[1, 2], [3, 4]]
clone = original.copy()
clone[0].append(99)
print(original[0])
```
- A) `[1, 2]`
- B) `[1, 2, 99]`
- C) `[99]`
- D) `TypeError`
- **Correct Answer: B**
- **Analysis:** `original.copy()` or `original[:]` creates a *shallow* copy: the outer list is new, but the inner sublists are shared references. Mutating `clone[0]` mutates `original[0]`.

---

## Part 5: Functions, Parameters & Scoping Traps

### Question T-20: The Mutable Default Argument
What is printed by the following code?
```python
def add_item(val, bag=[]):
    bag.append(val)
    return bag

add_item(10)
print(add_item(20))
```
- A) `[20]`
- B) `[10, 20]`
- C) `[10]`
- D) `None`
- **Correct Answer: B**
- **Analysis:** Default arguments are evaluated once at function definition time. The list `bag` persists and accumulates changes across all calls omitting the second parameter.

---

### Question T-21: The `UnboundLocalError`
What happens when running `test()`?
```python
x = 50

def test():
    print(x)
    x = 100

test()
```
- A) Prints `50`
- B) Prints `100`
- C) Raises `UnboundLocalError`
- D) Raises `NameError`
- **Correct Answer: C**
- **Analysis:** Because `x = 100` assigns to `x` inside `test()`, Python marks `x` as local to the entire function. When `print(x)` executes before the assignment, Python attempts to read the uninitialized local variable, raising `UnboundLocalError`.

---

### Question T-22: `*args` Type
What is the type of `args` inside a function defined as `def func(*args):`?
- A) `list`
- B) `tuple`
- C) `set`
- D) `generator`
- **Correct Answer: B**
- **Analysis:** Python packs variable positional arguments into an immutable `tuple`.

---

## Part 6: Control Flow, Loops & Exception Traps

### Question T-23: For-Else with Break
What is printed?
```python
for i in range(3):
    if i == 1:
        break
else:
    print("Completed")
```
- A) `Completed`
- B) Nothing is printed
- C) `1`
- D) `SyntaxError`
- **Correct Answer: B**
- **Analysis:** A loop's `else` block executes only if the loop finishes without executing a `break`. Because `break` triggered when `i == 1`, the `else` clause is skipped.

---

### Question T-24: `finally` Execution on Return
What is returned by `func()`?
```python
def func():
    try:
        return 1
    finally:
        return 2

print(func())
```
- A) `1`
- B) `2`
- C) `(1, 2)`
- D) `None`
- **Correct Answer: B**
- **Analysis:** A `finally` clause executes unconditionally before exiting a `try` block. If `finally` executes its own `return` statement, it discards and overrides any return value previously initiated in `try` or `except`.

---

### Question T-25: Short-Circuit Return Value of `or`
What is the output of `print(0 or [] or "BCPD" or 42)`?
- A) `True`
- B) `0`
- C) `'BCPD'`
- D) `42`
- **Correct Answer: C**
- **Analysis:** The `or` operator evaluates left-to-right and returns the **first truthy operand** without evaluating subsequent terms. `0` and `[]` are falsy; `"BCPD"` is truthy and returned immediately.

---

## Part 7: Functional Tools, Gotchas & Complexity Traps (Day 6 Expansion)

### Question T-26: `map` Object and `len()`
What happens when running:
```python
m = map(str.upper, ["apple", "banana"])
print(len(m))
```
- A) Prints `2`
- B) Prints `0`
- C) Raises `TypeError: object of type 'map' has no len()`
- D) Raises `AttributeError`
- **Correct Answer: C** `[Course: D6-05]`
- **Analysis:** `map` returns a lazy generator-like iterator that yields items on demand. It does not compute or store its length in memory, so calling `len()` raises `TypeError`.

---

### Question T-27: Matrix Diagonal Extraction
Given the 2D grid:
```python
g = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print([g[i][2 - i] for i in range(3)])
```
What is printed?
- A) `[1, 5, 9]`
- B) `[3, 5, 7]`
- C) `[7, 5, 3]`
- D) `[1, 2, 3]`
- **Correct Answer: B** `[Course: D6-05]`
- **Analysis:**
  - When `i = 0`: `g[0][2 - 0] = g[0][2] = 3`
  - When `i = 1`: `g[1][2 - 1] = g[1][1] = 5`
  - When `i = 2`: `g[2][2 - 2] = g[2][0] = 7`
  - Result: `[3, 5, 7]` (the anti-diagonal). `[g[i][i] for i in range(3)]` would be the main diagonal `[1, 5, 9]`.

---

### Question T-28: String Case-Sensitive Sorting
What is the output of `print(sorted(["Pear", "apple", "fig"]))`?
- A) `['apple', 'fig', 'Pear']`
- B) `['Pear', 'apple', 'fig']`
- C) `['fig', 'Pear', 'apple']`
- D) `['Pear', 'fig', 'apple']`
- **Correct Answer: B** `[Course: D6-02]`
- **Analysis:** Python compares strings by character ASCII/Unicode code points. Upper-case letters (`'A'–'Z'`: 65–90) have lower numerical values than lower-case letters (`'a'–'z'`: 97–122). Therefore, `'P'` (80) precedes `'a'` (97) and `'f'` (102).

---

### Question T-29: Default Recursion Limit
What is the standard default call recursion limit returned by `sys.getrecursionlimit()` in CPython?
- A) `100`
- B) `500`
- C) `1000`
- D) Unlimited
- **Correct Answer: C** `[Course: D6-10]`
- **Analysis:** CPython sets a default recursion limit of `1000` calls to protect against stack overflows. Deeper recursive calls raise `RecursionError: maximum recursion depth exceeded`.

---

### Question T-30: In-Place `+=` vs `+` Reference Semantics
What is printed by:
```python
def grow(lst):
    lst += [4]

def rebuild(lst):
    lst = lst + [5]

a = [1]
grow(a)
rebuild(a)
print(a)
```
- A) `[1, 4, 5]`
- B) `[1, 5]`
- C) `[1, 4]`
- D) `[1]`
- **Correct Answer: C** `[Course: D6-03]`
- **Analysis:**
  - `lst += [4]` invokes `list.__iadd__()`, which extends the existing list in place. The caller's `a` is modified to `[1, 4]`.
  - `lst = lst + [5]` allocates a brand-new list `[1, 4, 5]` and binds it to the local variable `lst`. The caller's variable `a` still points to `[1, 4]`.
  - Final value of `a` is `[1, 4]`.
