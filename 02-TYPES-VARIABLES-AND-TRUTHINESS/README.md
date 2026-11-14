# Module 02 â€” Variables, Core Data Types, Conversions & Truthiness

> **Sources:** `IMG-06`, `IMG-09`, `IMG-11` (float precision), `IMG-12`, `IMG-30` (Q1, Q5), `IMG-31`, `IMG-32` (`Day 2 Â· MANUAL Â§2.1â€“2.8, Â§2.26â€“2.31` & `Day 3 Â· Â§3.2â€“3.4`)
> **Note:** Slides `Â§2.1â€“2.5` (basic variable rules & core type overview) were missing from the folder; foundational explanations below are tagged `[Supplementary]` where reconstructed around `IMG-09`, `IMG-30`, and `IMG-31`.

---

## 1. Conceptual Foundation

- **Variables & Naming Rules `[Course: IMG-09, IMG-30, IMG-31]`:**
  - Names may contain letters, digits, and `_`, **cannot start with a digit**, are **case-sensitive**, and **cannot be Python keywords**.
  - `True`, `False`, and `None` are the **only capitalized keywords** and cannot be assigned to (`IMG-09`).
- **Variables as Name Tags (`[Supplementary]` Foundation):**
  - Python variables do not hold raw boxes of bytes like C; a variable name is a **reference (label)** bound to an **object** in memory that carries its own type (`int`, `float`, `str`, `bool`, `NoneType`, etc.).
- **Core Numeric Types & Base Literals `[Course: IMG-06]`:**
  - `int` (arbitrary precision), `float` (64-bit IEEE 754), `complex` (`1+2j`, `.imag`, `.real`, no spaces inside `complex("1+2j")`).
  - Integer literals in other bases: `0b` (binary), `0o` (octal, digits `0â€“7`), `0x` (hexadecimal). Underscores improve readability (`1_000_000`, `[Course: IMG-09]`).
  - Leading zeros on decimal integers (e.g., `09`) raise `SyntaxError` (`[Course: IMG-06]`, bottom row partially obscured by head after `09, 0...`).
- **Type Conversion, IEEE 754 Floats & Rounding `[Course: IMG-06, IMG-09, IMG-11, IMG-12]`:**
  - **Implicit:** `int + float â†’ float`; `True + 1 â†’ 2` (`bool` is a subclass of `int`).
  - **Explicit:** `int()`, `float()`, `str()`, `bool()`. Empty constructors produce defaults: `int() â†’ 0`, `float() â†’ 0.0`, `str() â†’ ''`, `bool() â†’ False` (`IMG-09`).
  - `int(3.9)` truncates toward zero (`3`), whereas `int("3.9")` raises `ValueError` (`IMG-12`). `int(s, base)` only accepts a string (`int(5, 2)` raises `TypeError`, `IMG-06`).
  - `round(x)` returns an `int`; `round(x, n)` returns a `float` (`IMG-09`). `round()` uses **banker's rounding** (round half to even: `round(2.5) â†’ 2`, `round(3.5) â†’ 4`, `IMG-12`).
  - Float precision (`[Course: IMG-11]`): `0.1 + 0.2` is `0.30000000000000004`, so `0.1 + 0.2 == 0.3` is `False`; use `math.isclose()`.
- **Truthy & Falsy Values `[Course: IMG-12]`:**
  - **Falsy (`bool(x) == False`):** `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`.
  - **Truthy:** Everything else â€” including `"0"`, `" "`, and `[0]`.
- **Value Equality (`==`) vs. Object Identity (`is`) `[Course: IMG-32]`:**
  - `==` compares **values** (`[1, 2] == [1, 2]` is `True`; `3 == 3.0` is `True`).
  - `is` checks whether two names point to the **exact same object** (`id(a) == id(b)`). Use `is` only for singletons like `None`: `if x is None:`.

---

## 2. Mental Models

- **Sticky-Note Labels vs. Houses (`==` vs. `is`):**
  - `a = [1, 2]` and `b = [1, 2]` build **two separate houses** with identical furniture (`a == b` is `True`, `a is b` is `False`).
  - `c = a` sticks a **second name tag** on the same house (`c is a` is `True`).
- **Commas Make Tuples, Not Thousands (`1,000,000`):**
  - In Python, `,` is the tuple builderâ€”so `n = 1,000,000` means `(1, 0, 0)`. Always use underscores: `1_000_000`.
- **Banker's Rounding & Binary Dust (`round(2.675, 2)`):**
  - Halfway ties go to the nearest **even** digit (`2.5 â†’ 2`, `3.5 â†’ 4`).
  - Why did `round(2.675, 2)` give `2.67` instead of `2.68`? `[Supplementary]`: In IEEE 754 binary, `2.675` is stored as `2.67499999999999982236...`, which is **strictly less** than `2.675`, so it rounds down to `2.67`!

---

## 3. Syntax and Code

### A. Number Literals, Bases & Conversions `[Course: IMG-06]`

| Expression | Result | Remember |
|---|---|---|
| `0b1010, 0o17, 0x1F` | `10, 15, 31` | Binary, octal, and hex literals |
| `bin(10), oct(8), hex(255)` | `'0b1010', '0o10', '0xff'` | Return lower-case strings |
| `int("101", 2), int("ff", 16)` | `5, 255` | Default base is `10` |
| `int(5, 2)` | `TypeError` | A base only works with a string |
| `int("2.5")` / `int(float("inf"))` | `ValueError` / `OverflowError` | Use `float()` first; infinity has no `int` |
| `float("1e3"), float(" 3.5 "), float("inf")` | `1000.0, 3.5, inf` | Spaces stripped; `inf` and `nan` allowed |
| `complex("1+2j"), (2J).imag` | `(1+2j), 2.0` | No spaces inside string; `j` or `J` |
| `09, 0...` *(obscured in `IMG-06`)* | `SyntaxError` | No leading zeros; octal digits `0â€“7` |

### B. Assignment Forms & Number Built-ins `[Course: IMG-09 | assign.py]`

**ORIGINAL CLASSROOM CODE:**
```python
a, b, c = 1, 2, 3
x = y = 0
n = 1,000,000
print(n, 1_000_000)                      # -> (1, 0, 0) 1000000
a ^= b; b ^= a; a ^= b                   # XOR swap
print(a, b)                              # -> 2 1
print(7 & 1, 8 & 1)                      # -> 1 0   (odd / even)
print(pow(2, 10, 1000), divmod(-7, 2))   # -> 24 (-4, 1)
print(round(2.5), round(2.675, 2))       # -> 2 2.67
print(int(), float(), repr(str()), bool())
# -> 0 0.0 '' False
```

**CORRECTED / PYTHONIC NOTES (`[Supplementary]`):**
```python
# Fix the comma trap:
population = 1_000_000          # int 1000000, NOT tuple (1, 0, 0)

# Prefer Pythonic tuple swap over XOR swap (works on any type, no aliasing bug):
a, b = b, a
```

### C. Type Conversion, Truthy & Falsy `[Course: IMG-12 | convert.py]`

**ORIGINAL CLASSROOM CODE:**
```python
print(3 + 2.0)                    # -> 5.0
print(int(3.9))                   # -> 3
print(int("0x1f", 16))            # -> 31
print(round(2.5), round(3.5))     # -> 2 4
print(bool(""), bool("0"))        # -> False True
print(bool([]), bool([0]))        # -> False True
print(float("1e3"))               # -> 1000.0
```

### D. Float Comparison & Identity `[Course: IMG-11, IMG-32]`

```python
import math
print(0.1 + 0.2 == 0.3)                  # -> False [IMG-11]
print(math.isclose(0.1 + 0.2, 0.3))      # -> True  [IMG-11]

a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, c is a)            # -> True False True [IMG-32]
print(3 == 3.0)                          # -> True [IMG-32]
```

---

## 4. Line-by-Line Explanation (`assign.py` & `convert.py`)

- `a, b, c = 1, 2, 3`: Sequence unpacking binds `a=1`, `b=2`, `c=3` in one statement.
- `x = y = 0`: Chained assignment binds both `x` and `y` to the same `0` object. *(Warning `[Supplementary]`: never chain mutable objects like `x = y = []`, or both share the same list!)*
- `n = 1,000,000`: Parsed as `(1, 0, 0)` because `000` in a tuple expression evaluates to `0` (`int` literal `0` is allowed, unlike `010`!).
- `a ^= b; b ^= a; a ^= b`: In-place bitwise XOR swap (`1 ^ 2 = 3`, `2 ^ 3 = 1`, `3 ^ 1 = 2`). Fails if `a` and `b` reference the same variable (`x ^= x` zeroes it out!).
- `7 & 1, 8 & 1`: Checks the lowest binary bit (`1` for odd, `0` for even).
- `pow(2, 10, 1000)`: Computes `(2 ** 10) % 1000` (`1024 % 1000 = 24`) efficiently without building giant intermediate powers.
- `int("0x1f", 16)`: With an explicit base (`16`), `int()` accepts the `"0x"` prefix (`31`). (Note: `int("0x1f")` without base `16` raises `ValueError`; `int("0x1f", 0)` auto-detects base `16`.)
- `bool("0")`, `bool([0])`: Non-empty containers/strings are always `True`, even when their single element is `0` or `"0"`.

---

## 5. Code Tracing (`XOR Swap` in `assign.py`)

Initial values: `a = 1` (`0b01`), `b = 2` (`0b10`).

| Step | Statement | `a` (binary) | `b` (binary) | Notes |
|---|---|---|---|---|
| 1 | `a ^= b` | `3` (`0b11`) | `2` (`0b10`) | `01 ^ 10 = 11` |
| 2 | `b ^= a` | `3` (`0b11`) | `1` (`0b01`) | `10 ^ 11 = 01` |
| 3 | `a ^= b` | `2` (`0b10`) | `1` (`0b01`) | `11 ^ 01 = 10` |
| 4 | `print(a, b)` | `2` | `1` | Output: `2 1` |

---

## 6. Common Pitfalls

1. **Writing `1,000,000` for one million (`IMG-09`):** Silently creates tuple `(1, 0, 0)` instead of raising an error.
2. **`int("2.5")` or `int("3.9")` (`IMG-06, IMG-12`):** `int()` parses integer strings onlyâ€”convert via `int(float("2.5"))` if truncation is intended.
3. **`int(5, 2)` (`IMG-06`):** Passing a non-string with a `base` argument raises `TypeError`.
4. **Assuming `"0"` or `" "` is falsy (`IMG-12`):** Only the **empty** string `""` is falsy.
5. **Testing floats with `==` (`IMG-11`):** `0.1 + 0.2 == 0.3` is `False`; use `math.isclose()`.
6. **Using `is` for number/string equality (`IMG-32`):** `is` tests identity, not value (`1000 is 1000` can differ from `a = 1000; b = int("1000"); a is b`).

---

## 7. MCQ Examination Traps

### Instructor Slide Questions `[Course: IMG-30 | Reconstructed Key]`
*(Note: Day 2 Answers slide was not captured; keys below are verified `[Reconstructed Key]`.)*

1. **Which is a valid variable name?** `[Course: IMG-30 Q1]`
   - A. `2nd_value` *(Incorrect â€” cannot start with a digit.)*
   - B. `my-var` *(Incorrect â€” `-` is subtraction, not allowed in identifiers.)*
   - **C. `_total`** *(Correct â€” leading underscore is valid.)*
   - D. `for` *(Incorrect â€” `for` is a reserved keyword.)*

2. **Which value is truthy?** `[Course: IMG-30 Q5]`
   - A. `0.0` *(Incorrect â€” numeric zero is falsy.)*
   - B. `""` *(Incorrect â€” empty string is falsy.)*
   - **C. `"0"`** *(Correct â€” non-empty string is truthy.)*
   - D. `None` *(Incorrect â€” `None` is falsy.)*

### Exam-Style Practice `[Supplementary]`

3. **What is the output of `n = 1,000,000; print(type(n), len(n))`?**
   - A. `<class 'int'>` followed by `TypeError`
   - **B. `<class 'tuple'> 3`** *(Correct â€” commas create the tuple `(1, 0, 0)` of length 3.)*
   - C. `<class 'int'> 7`
   - D. `SyntaxError`

4. **What does `print(round(2.5), round(3.5), int(3.9))` print?**
   - A. `3 4 4`
   - B. `2 3 3`
   - **C. `2 4 3`** *(Correct â€” banker's rounding rounds halves to nearest even (`2`, `4`); `int(3.9)` truncates to `3`.)*
   - D. `3 4 3`

5. **Which expression raises `TypeError`?**
   - A. `int("2.5")` *(Raises `ValueError`, not `TypeError`.)*
   - B. `int(float("inf"))` *(Raises `OverflowError`.)*
   - **C. `int(5, 2)`** *(Correct â€” `base` argument cannot be used with an `int` first argument.)*
   - D. `int("0x1f", 16)` *(Valid â€” returns `31`.)*

---

## 8. Practice Exercises *(Attempt in `exercises.py` Before Checking Solutions!)*

- **Level 1 (Basic):** Convert `"1010"` (binary) and `"ff"` (hex) to `int`, and `42` to binary/hex strings without the `'0b'`/`'0x'` prefix.
- **Level 2 (Application):** Write `safe_to_int(value)` handling strings like `"42"` and `"3.9"` (returning `3` via `float()` first) while returning `None` for invalid text.
- **Level 3 (Problem-Solving):** Write `classify_truthiness(items)` returning `(truthy_list, falsy_list)` preserving order without mutating `items`.
- **Level 4 (Exam Reasoning):** Write `is_nearly_equal(a, b)` using `math.isclose`, and `predict_traps()` returning expected outputs for `round(2.5)`, `round(2.675, 2)`, `bool("0")`, and `1,000,000`.

---

## 9. Topic Mastery Checklist
- [ ] I can validate Python identifier rules and identify `True`, `False`, `None` as non-assignable keywords.
- [ ] I can convert between `int`, `float`, `complex`, `bin()`, `oct()`, `hex()`, and predict `TypeError` vs `ValueError` vs `OverflowError`.
- [ ] I can explain `0.1 + 0.2 == 0.3`, banker's rounding (`round(2.5)`), and why `round(2.675, 2) == 2.67`.
- [ ] I can list all 8 falsy values and explain why `"0"` and `[0]` are truthy.
- [ ] I can explain `==` vs `is` and why `is` is reserved for singletons like `None`.
