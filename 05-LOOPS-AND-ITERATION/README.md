# Module 05 â€” Loops, Iteration, Patterns & Loop Traps

> **Sources:** `IMG-39`, `IMG-40`, `IMG-41`, `IMG-42`, `IMG-43`, `IMG-44`, `IMG-45` (steps 3â€“4), `IMG-46`, `IMG-47`, `IMG-49`, `IMG-51`, `IMG-55` (`Day 3 Â· MANUAL Â§4.1â€“4.27` & `Day 4 Â· Â§5.7`)

---

## 1. Conceptual Foundation

- **`while` Loops `[Course: IMG-39]`:**
  - Repeats while condition evaluates to `True`. Make sure loop state progresses toward `False`.
  - Counter pattern (`count -= 1`), accumulator pattern (`total += n % 10; n //= 10`), sentinel loop (`while True:` + `break`).
- **`for` Loops, Iterables & Built-in Iteration Helpers `[Course: IMG-40]`:**
  - `for item in iterable:` operates across sequences (strings, lists, tuples, ranges) and any iterable.
  - `range(stop)`, `range(start, stop)`, `range(start, stop, step)` (`stop` is always excluded; negative step counts down: `range(10, 0, -4)` â†’ `10, 6, 2`).
  - `enumerate(iterable, start=0)` yields `(index, item)` pairs without manual counter bookkeeping.
  - `zip(*iterables)` pairs items from multiple iterables and **stops at the shortest** (`zip([1, 2, 3], "ab")` yields `(1, 'a')` and `(2, 'b')`).
- **Loop Control: `break`, `continue`, `pass` & Loop `else` `[Course: IMG-41]`:**
  - `continue` skips the rest of the current iteration and jumps straight to the next pass.
  - `break` terminates the **innermost** loop immediately.
  - **Loop `else` `[Course: IMG-41, IMG-47, IMG-51]`:** Executes **only if the loop completes normally (without encountering `break`)**. A loop terminated by `break` skips its `else` block!
  - `pass` is an executable no-op placeholder required where Python syntax demands an indented statement.
- **The Iterator Protocol: `iter()`, `next()` & `StopIteration` `[Course: IMG-55]`:**
  - `it = iter(iterable)` creates an iterator tracking current position.
  - `next(it)` returns the next element, raising `StopIteration` when exhausted.
  - **Iterators are single-pass only:** a `for` loop continuing over an iterator picks up where `next()` left off; once exhausted, subsequent passes do nothing.
- **Nested Loops & Big-O Intuition `[Course: IMG-42, IMG-43]`:**
  - A single loop over $n$ items is $O(n)$ (linear); a loop inside a loop over $n$ items is $O(n^2)$ (quadratic).
  - Prime check: testing divisors only up to $\sqrt{n}$ runs in $O(\sqrt{n})$ time.
- **High-Yield Loop Traps `[Course: IMG-44, IMG-46]`:**
  - **Built once:** `for i in range(n): n = 10` evaluates `range(n)` once at loop entry; modifying `n` later has zero effect on the loop iterations (`IMG-44`).
  - **Loop variable rebinding:** `i += 10` inside the loop body is overwritten by the iterator on the very next pass (`IMG-44`).
  - **Mutating a list while iterating over it (`IMG-46`):** Deleting elements inside `for x in lst:` shifts internal indices and silently skips items. Always loop over a slice copy: `for x in lst[:]:`.
  - **Float counters (`IMG-46`):** `while x != 1.0: x += 0.1` can run forever because binary floating-point representation never hits exact `1.0`.

---

## 2. Mental Models

- **Loop `else` as a Search Guard ("If Not Found"):**
  - Think of loop `else` as: *"I searched the whole collection, never broke out early, so execute this fallback."* If `break` triggered, the search succeeded, so fallback `else` is skipped.
- **`iter()` / `next()` as a One-Way Bookmark:**
  - An iterator remembers its current index. Every `next()` moves the bookmark forward. When it reaches the back cover, it raises `StopIteration`. You cannot rewindâ€”you must buy a fresh iterator (`iter()`).
- **`range()` as a Pre-Printed Ticket Roll:**
  - When the loop starts, Python rolls out tickets `[0, 1, ..., n-1]`. Changing `n` during the loop doesn't alter the tickets already printed.

---

## 3. Syntax and Code

### A. `while` Loops `[Course: IMG-39 | while_demo.py]`

**ORIGINAL CLASSROOM CODE:**
```python
count = 3
while count > 0:
    print(count, end=" ")
    count -= 1
print("Lift-off!")          # -> 3 2 1 Lift-off!

n, total = 1234, 0
while n > 0:
    total += n % 10         # last digit
    n //= 10                # drop it
print(total)                # -> 10
```

### B. `for`, `range()`, `enumerate()`, `zip()` `[Course: IMG-40 | for_demo.py]`

**ORIGINAL CLASSROOM CODE:**
```python
print(list(range(5)))           # -> [0, 1, 2, 3, 4]
print(list(range(1, 10, 3)))    # -> [1, 4, 7]
print(list(range(10, 0, -4)))   # -> [10, 6, 2]

for i, name in enumerate(["Ada", "Bo"], start=1):
    print(i, name)
# -> 1 Ada
# -> 2 Bo

for n, ch in zip([1, 2, 3], "ab"):
    print(n, ch, end=" | ")     # -> 1 a | 2 b |
```

### C. Loop Control & `else` `[Course: IMG-41 | control.py]`

**ORIGINAL CLASSROOM CODE:**
```python
for n in range(1, 10):
    if n % 2 == 0:
        continue             # skip even numbers
    if n > 7:
        break                # leave the loop
    print(n, end=" ")
print()                      # -> 1 3 5 7

for n in [4, 6, 9]:
    if n % 2:
        print("odd found:", n)  # -> odd found: 9
        break
else:
    print("all even")        # runs only if there was no break

for _ in range(3):
    pass                     # placeholder: does nothing
```

### D. Classic Loop Programs & Time Complexity `[Course: IMG-42 | classics.py]`

**ORIGINAL CLASSROOM CODE:**
```python
n = 29
is_prime = n > 1
for d in range(2, int(n ** 0.5) + 1):   # O(sqrt(n))
    if n % d == 0:
        is_prime = False
        break
print(n, "prime?", is_prime)            # -> 29 prime? True

fact = 1
for k in range(1, 6):                   # O(n)
    fact *= k
print("5! =", fact)                     # -> 5! = 120

a, b = 0, 1
fib = []
while len(fib) < 8:                     # O(n)
    fib.append(a)
    a, b = b, a + b
print(fib)  # -> [0, 1, 1, 2, 3, 5, 8, 13]
```

### E. Patterns & Loop Traps `[Course: IMG-43, IMG-44 | patterns.py & traps.py]`

**ORIGINAL CLASSROOM CODE (`patterns.py`):**
```python
rows = 4
for i in range(1, rows + 1):
    print("*" * i)
# -> *
# -> **
# -> ***
# -> ****

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
# -> 1 2 3
# -> 2 4 6
# -> 3 6 9
```

**ORIGINAL CLASSROOM CODE (`traps.py`):**
```python
n = 3
for i in range(n):
    n = 10                  # range(3) was already built
print(i)                    # -> 2

for i in range(3):
    i += 10  # rebinding doesn't change the loop
print(i)                    # -> 12

s = "abcd"
while "c" in s:
    s = s[1:]               # shrink until "c" is gone
print(s)                    # -> d

items = ["x", "", 0, "y", None]
print(list(filter(bool, items)))   # -> ['x', 'y']
print(["no", "yes"][True])         # -> yes
print(not 1 == 2)                  # -> True
```

### F. Iterator Protocol `[Course: IMG-55 | iterate.py]`

**ORIGINAL CLASSROOM CODE:**
```python
word = "code"
it = iter(word)
print(next(it))        # -> c
print(next(it))        # -> o
for ch in it:          # continues where next() stopped
    print(ch, end="")
print()                # -> de
# calling next(it) now raises StopIteration
```

### G. Lab 3.1 & 3.2: Guessing Game `[Course: IMG-45, IMG-49 | guess.py]`

**ORIGINAL CLASSROOM CODE (`guess.py` from Slide 14):**
```python
import random

secret = random.randint(1, 20)
attempts = 0
while True:
    guess = int(input("Guess 1-20: "))
    attempts += 1
    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print(f"Got it in {attempts}!")
        break
```

**CORRECTED / HOMEWORK CODE (`[Course: IMG-49]` Summary Slide homework â€” 5-attempt limit):**
```python
def play_guessing_game_5_limit(secret: int, guesses: list[int]) -> tuple[bool, int]:
    """Summary slide homework (IMG-49): 'Finish guessing game with a 5-attempt limit'."""
    max_attempts = 5
    attempts = 0
    for guess in guesses:
        attempts += 1
        if guess == secret:
            return True, attempts
        if attempts >= max_attempts:
            break
    return False, attempts
```

---

## 4. Line-by-Line Explanation (`control.py` & `classics.py`)

- `for n in range(1, 10):`: Iterates through numbers `1` to `9`.
- `if n % 2 == 0: continue`: Skips printing even numbers (`2, 4, 6, 8`).
- `if n > 7: break`: Triggers when `n == 9`, terminating the loop before `9` is printed. Output: `1 3 5 7`.
- `for d in range(2, int(n ** 0.5) + 1):`: Tests potential divisors up to $\lfloor\sqrt{29}\rfloor = 5$. Because `29` is not divisible by 2, 3, 4, or 5, `break` never fires, leaving `is_prime = True`.
- `a, b = b, a + b`: Right-hand side evaluates `(b, a + b)` as an immutable tuple using current values before rebinding `a` and `b` simultaneously.

---

## 5. Code Tracing (`Digit Accumulator` in `while_demo.py`)

Initial state: `n = 1234`, `total = 0`.

| Iteration | `n > 0` | `n % 10` (last digit) | `total` (after `+=`) | `n //= 10` (new `n`) |
|---|---|---|---|---|
| 1 | `1234 > 0` (True) | `4` | `4` | `123` |
| 2 | `123 > 0` (True) | `3` | `7` | `12` |
| 3 | `12 > 0` (True) | `2` | `9` | `1` |
| 4 | `1 > 0` (True) | `1` | `10` | `0` |
| 5 | `0 > 0` (False) | â€” | **`10`** (Final) | `0` (Loop terminates) |

---

## 6. Common Pitfalls

1. **Expecting loop `else` to run after `break` (`IMG-41, IMG-47, IMG-51`):** `else` runs only on exhaustion without `break`.
2. **Rebinding loop variable expecting to skip steps (`IMG-44`):** Writing `i += 10` inside `for i in range(3):` does not skip numbers; the iterator sets `i` to the next value on the next pass.
3. **Mutating list during iteration (`IMG-46`):**
   ```python
   items = [1, 2, 3, 4]
   for x in items:
       if x % 2 == 0:
           items.remove(x)    # SKIPS elements!
   # Correct fix: for x in items[:]:
   ```
4. **Off-by-one in `range(start, stop)` (`IMG-46`):** `range(1, 10)` stops at `9`; write `range(1, n + 1)` to include `n`.
5. **Infinite `while` on float step (`IMG-46`):** `while x != 1.0: x += 0.1` never terminates due to float representation errors. Use integers or `<`.

---

## 7. MCQ Examination Traps

### Instructor Slide Questions `[Course: IMG-47, IMG-51]`

1. **How many times does `for i in range(2, 11, 3)` run?** `[Course: IMG-47 Q2]`
   - **A. `3`** *(Correct â€” yields `2`, `5`, `8`; `11` is excluded.)*
   - B. `4` *(Incorrect.)*
   - C. `9` *(Incorrect.)*
   - D. `2` *(Incorrect.)*

2. **When does a loop's `else` block run?** `[Course: IMG-47 Q3]`
   - A. `Always` *(Incorrect.)*
   - B. `Only after break` *(Incorrect â€” break skips else.)*
   - **C. `When the loop ends without break`** *(Correct â€” normal completion triggers else.)*
   - D. `Never on a for loop` *(Incorrect â€” both for and while support else.)*

### Exam-Style Practice `[Supplementary]`

3. **What is the output of:**
   ```python
   for i in range(3):
       if i == 1:
           break
   else:
       print("Done", end="")
   print(i)
   ```
   - A. `Done 1`
   - B. `Done 2`
   - **C. `1`** *(Correct â€” `break` skips the `else` block, and `i` retains its value `1` after loop exit.)*
   - D. `NameError`

4. **What does this print?**
   ```python
   word = "py"
   it = iter(word)
   next(it)
   print("".join(it))
   ```
   - A. `'py'`
   - **B. `'y'`** *(Correct â€” `next(it)` consumed `'p'`; subsequent iteration starts from `'y'`.)*
   - C. `''`
   - D. `StopIteration`

5. **What is the output of `list(range(10, 0, -4))`?**
   - A. `[10, 6, 2, -2]`
   - **B. `[10, 6, 2]`** *(Correct â€” stop `0` is excluded; step stops before `<= 0`.)*
   - C. `[10, 6]`
   - D. `[]`

---

## 8. Practice Exercises *(Attempt in `exercises.py` Before Checking Solutions!)*

- **Level 1 (Basic):** Implement `sum_digits(n)` using the `while n > 0` modulo/floor division pattern from `IMG-39`.
- **Level 2 (Application â€” Lab 3.2 `[Course: IMG-45, IMG-49]`):** Implement `is_prime_number(n)` in $O(\sqrt{n})$ time and `simulate_guess_game(secret, max_attempts=5, guesses=[...])`.
- **Level 3 (Problem-Solving â€” Lab 3.2 Bonus `[Course: IMG-45]`):** Implement `centered_star_pyramid(rows)` returning a list of centered rows (e.g. `['  *  ', ' *** ', '*****']`).
- **Level 4 (Exam Reasoning):** Implement `predict_loop_traps()` predicting outputs for rebinding `i += 10`, `range(10, 0, -4)`, generator/iterator resume, and `not 1 == 2`.

---

## 9. Topic Mastery Checklist
- [ ] I can trace `while` accumulator and counter patterns on paper.
- [ ] I can calculate the exact iterations of any `range(start, stop, step)` including negative steps.
- [ ] I understand the single-pass nature of `iter()`/`next()` and predict `StopIteration`.
- [ ] I know that `break` exits the innermost loop and skips loop `else`.
- [ ] I can implement $O(\sqrt{n})$ prime check, Fibonacci, and star pattern loops without reference.
- [ ] I have completed the Sanfoundry drills listed in `IMG-49` (*While & For Loops â€“ 1 to 6*).
