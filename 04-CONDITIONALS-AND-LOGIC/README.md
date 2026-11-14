# Module 04 â€” Conditionals, Logic & Pattern Matching

> **Sources:** `IMG-32`, `IMG-33`, `IMG-34`/`IMG-35`, `IMG-36`, `IMG-37`, `IMG-38`, `IMG-45` (steps 1â€“2), `IMG-46`, `IMG-47`, `IMG-51` (`Day 3 Â· MANUAL Â§3.2â€“3.20`)

---

## 1. Conceptual Foundation

- **Comparisons & Identity `[Course: IMG-32]`:**
  - `==` compares values; `is` checks exact object identity (`id(a) == id(b)`).
  - Chained comparisons: `1 < x < 10` evaluates as `(1 < x) and (x < 10)`, with `x` evaluated only once.
  - Strings compare lexicographically by Unicode code point (`"Z" < "a"` is `True`, because `ord("Z") == 90 < ord("a") == 97`).
  - Cross-numeric equality: `3 == 3.0` is `True` (Python converts numbers across `int`/`float` before value comparison).
  - Testing singletons: always write `if x is None:`, never `if x == None:` (`IMG-32, IMG-47, IMG-51`).
- **`if`, `elif`, `else` & Ternary Operator `[Course: IMG-36]`:**
  - An `if` statement ends with `:` and controls an indented block.
  - `elif` evaluates **only if all preceding branches were `False`**; the **first `True` branch wins**, and remaining branches are skipped.
  - `else` catches anything left over.
  - Ternary conditional expression: `value_if_true if condition else value_if_false`.
- **Logical Operators & Short-Circuiting `[Course: IMG-37]`:**
  - `and` is `True` only if both operands are truthy; `or` is `True` if at least one operand is truthy; `not` inverts truthiness.
  - **Short-circuiting:** In `False and f()`, `f()` is **never called**; in `True or f()`, `f()` is never called.
  - **Return value trap `[Course: IMG-37, IMG-47]`:** `and` and `or` return **one of the operands**, not always a boolean!
    - `x or y`: returns `x` if `x` is truthy, else returns `y` (`0 or "default" â†’ 'default'`, `IMG-37`).
    - `x and y`: returns `x` if `x` is falsy, else returns `y` (`5 and 10 â†’ 10`, `IMG-37`).
  - De Morgan's laws: `not (a and b) == (not a or not b)`.
  - Built-in helpers: `any(iterable)` returns `True` if at least one item is truthy; `all(iterable)` returns `True` if all items are truthy.
- **Structural Pattern Matching (`match-case`, Python 3.10+) `[Course: IMG-38]`:**
  - Matches data structures: literals, sequences (`case ["go", direction]:`), alternatives (`case ["look" | "inspect"]:`), and wildcard `case _:`.
  - Pattern guards: `case (x, 0) if x > 0:`.
  - **No fall-through:** unlike C/Java `switch`, Python executes only the first matching `case` block without requiring `break`.

---

## 2. Mental Models

- **Short-Circuiting as an Early-Exit Security Turnstile:**
  - `and` asks: *"Did anyone fail?"* As soon as it sees a falsy operand, it stops immediately and hands back that falsy item.
  - `or` asks: *"Did anyone pass?"* As soon as it sees a truthy operand, it stops immediately and hands back that truthy item.
- **`match-case` as an Intelligent Cookie Cutter:**
  - A sequence pattern doesn't just check equalityâ€”it checks length, matches fixed positions, captures variable elements into new names (like `direction`), and tests optional guard conditions (`if x > 0`).

---

## 3. Syntax and Code

### A. Comparisons & Identity `[Course: IMG-32 | compare.py]`

**ORIGINAL CLASSROOM CODE:**
```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)     # -> True False
c = a
print(c is a)             # -> True
x = 7
print(1 < x < 10)         # -> True
print("Z" < "a")          # -> True
print(3 == 3.0)           # -> True
x = None
print(x is None)          # -> True
```

### B. `if`, `elif`, `else` & Ternary `[Course: IMG-36 | grade.py]`

**ORIGINAL CLASSROOM CODE:**
```python
score = 72
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(grade)                                  # -> B

status = "pass" if score >= 60 else "fail"
print(status)                                 # -> pass
```

### C. Logic & Short-Circuiting `[Course: IMG-37 | logic.py]`

**ORIGINAL CLASSROOM CODE:**
```python
print(True and False)              # -> False
print(0 or "default")              # -> default
print(repr("" and "x"))            # -> ''
print(5 and 10)                    # -> 10
print(any([3 > 5, 8 > 5]))         # -> True
print(all([1, 2, 0]))              # -> False
age, has_id = 20, True
print(age >= 18 and has_id)        # -> True
```

### D. `match-case` (Python 3.10+) `[Course: IMG-38 | commands.py]`

**ORIGINAL CLASSROOM CODE:**
```python
command = "go north"

match command.split():
    case ["quit"]:
        print("Bye")
    case ["go", direction]:
        print("Moving", direction)    # -> Moving north
    case ["look" | "inspect"]:
        print("You see a door")
    case _:
        print("Unknown command")

point = (3, 0)
match point:
    case (0, 0):
        print("origin")
    case (x, 0) if x > 0:
        print("on the +x axis")       # -> on the +x axis
    case _:
        print("elsewhere")
```

---

## 4. Line-by-Line Explanation (`grade.py`, `logic.py`, `commands.py`)

- `if score >= 80:`: `72 >= 80` is `False`, so block is skipped.
- `elif score >= 70:`: `72 >= 70` is `True`, so `grade = "B"` executes. Because the branch succeeded, Python skips `elif score >= 60:` and `else:` entirely.
- `status = "pass" if score >= 60 else "fail"`: Ternary evaluates condition first; `72 >= 60` is `True`, so expression yields `"pass"`.
- `0 or "default"`: `0` is falsy, so `or` evaluates and returns the second operand `"default"`.
- `5 and 10`: `5` is truthy, so `and` evaluates and returns the second operand `10`.
- `case ["go", direction]:`: Matches any 2-element list whose first item is `"go"`, binding the second item to local variable `direction` (`"north"`).

---

## 5. Code Tracing (`Short-Circuit Evaluation` in `logic.py`)

| Expression | Operand 1 | Truthiness | Evaluates Operand 2? | Return Value | Why |
|---|---|---|---|---|---|
| `True and False` | `True` | Truthy | Yes | `False` | `and` needs both truthy |
| `0 or "default"` | `0` | Falsy | Yes | `'default'` | First operand falsy, returns second |
| `"" and "x"` | `""` | Falsy | **No** (short-circuits) | `''` | First operand falsy, `and` returns it immediately |
| `5 and 10` | `5` | Truthy | Yes | `10` | First operand truthy, `and` returns second |
| `0 or [] or "x"` `[IMG-47]` | `0` (Falsy) â†’ `[]` (Falsy) | â€” | Yes | `'x'` | Reaches first truthy operand |

---

## 6. Common Pitfalls

1. **Assuming `and`/`or` return boolean `True`/`False` (`IMG-37, IMG-47`):** `0 or "x"` returns `"x"`, not `True`.
2. **Writing `if x = 5:` (`IMG-46`):** `=` is assignment, raising `SyntaxError`; equality requires `==`.
3. **Redundant boolean checks (`IMG-46`):** Writing `if flag == True:` or `if items == []:`. Write `if flag:` and `if not items:`.
4. **Bare-name capture trap in `match-case` (`[Supplementary]`):** Writing `case target:` without a guard or dot does **not** check if the value equals an outer variable `target`â€”it rebinds `target` as a catch-all match!
5. **Testing singletons with `==` (`IMG-32`):** Always write `if x is None:`.

---

## 7. MCQ Examination Traps

### Instructor Slide Questions `[Course: IMG-47, IMG-51]`

1. **Output of `print(0 or [] or "x")`?** `[Course: IMG-47 Q1]`
   - A. `0` *(Incorrect â€” `0` is falsy.)*
   - B. `[]` *(Incorrect â€” `[]` is falsy.)*
   - **C. `x`** *(Correct â€” `or` chains until the first truthy operand is found.)*
   - D. `True` *(Incorrect â€” returns the operand value, not a bool.)*

2. **Output of `x = 5; print("big" if x > 3 else "small")`?** `[Course: IMG-47 Q4]`
   - **A. `big`** *(Correct â€” `5 > 3` is `True`, so the left branch is evaluated.)*
   - B. `small` *(Incorrect.)*
   - C. `True` *(Incorrect.)*
   - D. `Error` *(Incorrect.)*

3. **Which is the recommended test for `None`?** `[Course: IMG-47 Q5]`
   - A. `x == None` *(Incorrect â€” PEP 8 discourages `==` for singletons.)*
   - **B. `x is None`** *(Correct â€” tests object identity for the `None` singleton.)*
   - C. `x = None` *(Incorrect â€” assignment statement.)*
   - D. `None in x` *(Incorrect â€” membership test.)*

### Exam-Style Practice `[Supplementary]`

4. **What is the output of `print(repr([] and "hello"))`?**
   - A. `'hello'`
   - **B. `[]`** *(Correct â€” `[]` is falsy, so `and` short-circuits and returns `[]` without evaluating `'hello'`.)*
   - C. `False`
   - D. `None`

5. **Given `score = 85`, what does this print?**
   ```python
   grade = "Pass" if score >= 60 else "Fail" if score >= 40 else "Retake"
   ```
   - **A. `'Pass'`** *(Correct â€” chained ternary evaluates first condition `score >= 60` as `True`.)*
   - B. `'Fail'`
   - C. `'Retake'`
   - D. `SyntaxError`

---

## 8. Practice Exercises *(Attempt in `exercises.py` Before Checking Solutions!)*

- **Level 1 (Basic):** Implement `fallback_username(raw_input, default="Guest")` using `or`.
- **Level 2 (Application â€” Lab 3.1 `[Course: IMG-45]`):** Implement `letter_grade(score)` returning `A/B/C/F` and `is_leap_year(year)` (divisible by 4 and not 100, or divisible by 400).
- **Level 3 (Problem-Solving):** Write `classify_command(cmd_string)` using Python 3.10+ `match-case` matching `["quit"]`, `["go", dir]`, `["take", item]`, and `_`.
- **Level 4 (Exam Reasoning):** Implement `predict_logic_results()` predicting outputs for `0 or "" or [0]`, `5 and [] and "a"`, `all([1, 2, 3])`, and `any([0, "", None])`.

---

## 9. Topic Mastery Checklist
- [ ] I can predict the exact operand returned by chained `and` and `or` expressions.
- [ ] I can write clean `if`/`elif`/`else` and ternary conditional expressions.
- [ ] I can implement leap-year and grading logic using boolean operator precedence.
- [ ] I can use Python 3.10+ `match-case` with sequences, alternatives, and guards.
- [ ] I can test singletons with `is None`.
