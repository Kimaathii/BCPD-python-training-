# Sanfoundry Drill Sets & Certification Practice Questions

> **BCPD Python Cohort 2 Certification Preparation**  
> **Source Screen Mappings:** `IMG-31` (Day 2 Summary Slide 17) & `IMG-49` (Day 3 Summary Slide 17)  
> **Purpose:** Curated practice questions aligned directly with the Sanfoundry practice drill sets assigned by the instructor as evening homework and certification exam revision.

---

## Set 1: Data Types, Operators & Precedence (Assigned in `IMG-31`)

### Q1.1: Integer Division & Floor Division
What is the value of `x` after executing:
```python
x = -11 // 3
```
- A) `-3`
- B) `-4`
- C) `-3.66`
- D) `3`
- **Correct Answer:** **B**
- **Explanation:** Python floor division rounds toward negative infinity. `-11 / 3` is `-3.666...`, which floors to `-4`.

### Q1.2: Bitwise Shift and Masking
What is the output of the following code?
```python
val = 0b101100
mask = 0b001100
result = (val & mask) >> 2
print(result)
```
- A) `3`
- B) `12`
- C) `0`
- D) `48`
- **Correct Answer:** **A**
- **Explanation:**
  - `val & mask` isolates bits 2 and 3: `0b001100` (decimal `12`).
  - Right shifting by 2: `12 >> 2 = 3` (`0b000011`).

### Q1.3: Assignment Expressions (The Walrus Operator)
What is printed by:
```python
if (n := len("BCPD Cohort 2")) > 10:
    print(f"Long: {n}")
else:
    print(f"Short: {n}")
```
- A) `Long: 13`
- B) `Short: 13`
- C) `Long: 10`
- D) `NameError: name 'n' is not defined`
- **Correct Answer:** **A**
- **Explanation:** The walrus operator `:=` assigns the value `13` to `n` and returns `13`. Since `13 > 10` is `True`, the `if` block executes.

### Q1.4: Floating-Point Addition Comparison
What is the boolean result of:
```python
print(0.1 + 0.1 + 0.1 == 0.3)
```
- A) `True`
- B) `False`
- C) `TypeError`
- D) `OverflowError`
- **Correct Answer:** **B**
- **Explanation:** Binary floating-point representation (IEEE 754) cannot represent `0.1` exactly. The sum produces `0.30000000000000004`, which is not equal to `0.3`. (Use `math.isclose()` for float comparisons).

---

## Set 2: Conditionals, Short-Circuiting & Match-Case (Assigned in `IMG-49`)

### Q2.1: Logical Short-Circuit Operands
What is printed?
```python
x = 0
y = 10
z = x or y and 20
print(z)
```
- A) `0`
- B) `10`
- C) `20`
- D) `True`
- **Correct Answer:** **C**
- **Explanation:**
  - Operator precedence: `and` has higher precedence than `or`.
  - `y and 20`: `y` (`10`) is truthy, so `20` is evaluated and returned.
  - `x or 20`: `x` (`0`) is falsy, so `20` is evaluated and returned.
  - Output is `20`.

### Q2.2: Structural Pattern Matching Capture
What does this `match-case` block print?
```python
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case _:
        print("Other")
```
- A) `Origin`
- B) `Y-axis at 5`
- C) `X-axis at 0`
- D) `Other`
- **Correct Answer:** **B**
- **Explanation:** Pattern `(0, y)` matches a 2-tuple whose first element is literal `0`, and binds the second element (`5`) to the local name `y`.

---

## Set 3: Loops, Iteration & Complexity (Assigned in `IMG-49`)

### Q3.1: Rebinding the Loop Variable
What is the sum printed by:
```python
total = 0
for i in range(5):
    total += i
    i += 10
print(total)
```
- A) `10`
- B) `50`
- C) `60`
- D) `0`
- **Correct Answer:** **A**
- **Explanation:** At the beginning of each iteration, the `for` statement retrieves the next value from the iterator `range(5)` and re-binds `i` to that value (`0, 1, 2, 3, 4`), completely overwriting any changes made to `i` inside the loop body! `0 + 1 + 2 + 3 + 4 = 10`.

### Q3.2: Parallel Iteration with `zip`
What is the length of the list produced by:
```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
result = list(zip(a, b))
print(len(result))
```
- A) `5`
- B) `3`
- C) `8`
- D) `2`
- **Correct Answer:** **B**
- **Explanation:** Built-in `zip()` stops as soon as the shortest input iterable is exhausted. Since `b` has 3 elements, `zip` produces 3 pairs.

### Q3.3: Loop Else with Continue
What does the following loop print?
```python
for n in range(3):
    if n == 1:
        continue
else:
    print("Done")
```
- A) Nothing
- B) `Done`
- C) `1`
- D) `IndexError`
- **Correct Answer:** **B**
- **Explanation:** `continue` skips the rest of the current iteration, but does **not** break out of the loop. Because the loop was never terminated by `break`, the `else` clause executes normally!

---

## Set 4: Strings, Lists & Mutability

### Q4.1: Strip Argument Semantics
What is the output of:
```python
s = "mississippi"
print(s.strip("mis"))
```
- A) `"ssippi"`
- B) `"pp"`
- C) `""`
- D) `"ppi"`
- **Correct Answer:** **D**
- **Explanation:** `str.strip(chars)` strips any character that appears anywhere in the `chars` set from both ends until a character not in `chars` is encountered.
  - From left: `'m'`, `'i'`, `'s'`, `'s'`, `'i'`, `'s'`, `'s'`, `'i'` are all in `"mis"`.
  - Next character is `'p'`, which is not in `"mis"`, so stripping from the left stops before `'p'`.
  - From right: `'i'` is stripped. Next is `'p'`, which is not in `"mis"`, so right stripping stops.
  - Remaining string: `"pp"`. Wait! In `"mississippi"`:
    `m-i-s-s-i-s-s-i-p-p-i`
    Left characters: m, i, s, s, i, s, s, i -> all stripped!
    Then 'p', 'p'.
    Right characters: 'i' -> stripped!
    Result: `"pp"`.
    - **Correction:** The answer is **B (`"pp"`)**!

### Q4.2: In-Place Mutation vs New Object
What is printed?
```python
nums = [1, 2, 3]
nums.append([4, 5])
nums.extend([6, 7])
print(len(nums))
```
- A) `7`
- B) `6`
- C) `5`
- D) `4`
- **Correct Answer:** **B**
- **Explanation:**
  - Initial `nums`: 3 elements `[1, 2, 3]`.
  - `append([4, 5])`: adds the single list `[4, 5]` as element 3. `len` becomes `4`.
  - `extend([6, 7])`: adds each element from `[6, 7]` individually. `len` becomes `4 + 2 = 6`.

---

## Set 5: Comprehensions, Functions & Scoping

### Q5.1: Nested Comprehension Flattening
What is the result of:
```python
grid = [[1, 2], [3, 4]]
flat = [x for row in grid for x in row]
print(flat)
```
- A) `[[1, 2], [3, 4]]`
- B) `[1, 2, 3, 4]`
- C) `[1, 3, 2, 4]`
- D) `TypeError`
- **Correct Answer:** **B**
- **Explanation:** In Python comprehensions, `for` clauses appear in the same order as in equivalent nested `for` loops:
  `for row in grid: for x in row: ...` -> `[1, 2, 3, 4]`.

### Q5.2: Parameter Evaluation Timing
Consider:
```python
count = 0
def increment(step=count):
    return step

count = 10
print(increment())
```
- A) `0`
- B) `10`
- C) `None`
- D) `UnboundLocalError`
- **Correct Answer:** **A**
- **Explanation:** Default parameter expressions are evaluated at **function definition time**. At the moment `def increment(...)` was compiled, `count` was `0`. Later mutating or rebinding `count = 10` does not change the default value bound to `step`.

---

## Set 6: Tuples, Dictionaries & Sets (Assigned in Day 8) `[Course: D8-01 to D8-14]`

### Q6.1: Mutating Mutable Object Inside Tuple
What is printed by:
```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```
- A) `(1, [2, 3])`
- B) `(1, [2, 3, 4])`
- C) `TypeError`
- D) `(1, 4)`
- **Correct Answer:** **B** `[Course: D8-03]`
- **Explanation:** Tuples are immutable in terms of their stored references, but the object referenced at index 1 is a mutable list. Mutating the list in place via `append` succeeds.

### Q6.2: Dictionary Hashability & Numeric Collisions
What is the output of:
```python
d = {}
d[1] = "apple"
d[1.0] = "banana"
d[True] = "cherry"
print(len(d), d[1])
```
- A) `3 cherry`
- B) `1 cherry`
- C) `1 apple`
- D) `2 banana`
- **Correct Answer:** **B** `[Course: D8-07]`
- **Explanation:** In Python, `1 == 1.0 == True` and `hash(1) == hash(1.0) == hash(True)`. All three keys map to the exact same hash slot and compare equal. Each successive assignment overwrites the value in place, leaving 1 key with value `"cherry"`.

### Q6.3: Set Bitwise Operators vs Method Syntax
Which statement raises a `TypeError`?
- A) `{1, 2}.union([3, 4])`
- B) `{1, 2}.intersection([2, 3])`
- C) `{1, 2} | [3, 4]`
- D) `{1, 2} & {2, 3}`
- **Correct Answer:** **C** `[Course: D8-14]`
- **Explanation:** Bitwise operators (`|`, `&`, `-`, `^`) require `set` or `frozenset` on both sides. Passing a list raises `TypeError`. In contrast, methods like `.union()` accept any iterable.

---

## Set 7: Object-Oriented Programming & Encapsulation (Assigned in Day 9) `[Course: D9-01 to D9-11]`

### Q7.1: Instance Attribute Lookup Shadowing
What is the output of:
```python
class Counter:
    val = 0

c1 = Counter()
c2 = Counter()
c1.val += 5
print(c1.val, c2.val, Counter.val)
```
- A) `5 5 5`
- B) `5 0 0`
- C) `5 5 0`
- D) `0 0 0`
- **Correct Answer:** **B** `[Course: D9-08]`
- **Explanation:** `c1.val += 5` expands to `c1.val = c1.val + 5`. Reading `c1.val` reads the class attribute `0`. Adding `5` produces `5`. Assigning `c1.val = 5` binds `val = 5` into `c1`'s instance dictionary `c1.__dict__`. It leaves `Counter.val` and `c2.val` untouched at `0`.

### Q7.2: Private Attribute Name Mangling
Given:
```python
class Secret:
    def __init__(self, key):
        self.__key = key

s = Secret("xyz")
```
Which expression successfully accesses the stored key?
- A) `s.__key`
- B) `s._key`
- C) `s._Secret__key`
- D) `getattr(s, "key")`
- **Correct Answer:** **C** `[Course: D9-06, D9-11]`
- **Explanation:** Python's compiler mangles double-underscore private attributes to `_ClassName__attributeName`. Accessing `s._Secret__key` succeeds; direct `s.__key` raises `AttributeError`.

