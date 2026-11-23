# Module 15: Modules Part 1 — Imports, `sys`, `math` & `random`

Welcome to **Module 15** of the BCPD Python Certification curriculum. This module marks the beginning of **Week 3** and directly covers **Domain 4: Modules & Libraries (15% of the certification exam)**, mapped to **Student Manual Day 14 (§14.1–14.6)**.

---

## 1. Domain 4 Certification Overview & Objectives

In the BCPD certification, Domain 4 evaluates your ability to structure modular programs, control execution flow via system hooks, apply mathematical precision, and work safely with pseudo-random and secure random generation.

```
       BCPD Certification Exam Breakdown
┌───────────────────────────────────────────────┐
│ Domain 1: Basics & Foundations         (15%)  │
│ Domain 2: Data Types & Control Flow    (30%)  │
│ Domain 3: Object-Oriented Programming  (25%)  │
│ Domain 4: Modules & Standard Libraries (15%) ◄── THIS MODULE
│ Domain 5: Exceptions & File I/O        (15%)  │
└───────────────────────────────────────────────┘
```

### Classroom Competency Checklist `[Course: D13-02]`
1. **Import Styles:** Import modules using all 5 syntactic styles and explain when to select each.
2. **Module Resolution (`sys.path`):** Trace module discovery, understand bytecode caching (`.pyc`), and prevent shadowing.
3. **The `sys` Module:** Parse CLI arguments (`sys.argv`), control exit codes (`sys.exit`), and inspect system resources.
4. **The `math` Module:** Apply IEEE 754 floating-point operations, truncation, logarithms, trigonometric radians, and exact summation (`math.fsum`).
5. **The `random` Module:** Manage PRNG state (`seed`), distinguish inclusive vs exclusive boundaries (`randint` vs `randrange`), sample with/without replacement (`choices` vs `sample`), and enforce cryptographic security boundaries (`random` vs `secrets`).

---

## 2. Module System & Import Styles `[Course: D13-03]`

A Python module is simply a `.py` file containing functions, classes, and executable statements. Python provides five distinct syntax styles for importing modules:

| Style | Syntax Example | Usage in Code | Exam Characteristics & Best Practice |
|---|---|---|---|
| **Direct Import** | `import math` | `math.sqrt(9)` | **Clear & safe (Recommended).** Prevents name collisions by keeping symbols inside their namespace. |
| **Module Alias** | `import numpy as np` | `np.array([1, 2])` | **Standard short alias.** Used for common libraries (`np`, `pd`, `plt`). |
| **Direct Symbol** | `from math import pi, sqrt` | `sqrt(9)`, `pi` | **Convenient.** Watch out for local variable collisions that overwrite imported names. |
| **Symbol Alias** | `from datetime import datetime as dt` | `dt.now()` | **Rename on import.** Resolves name clashes or shortens verbose class names. |
| **Star Import** | `from math import *` | `sqrt(9)` | **Strongly Discouraged.** Pollutes namespace, hides provenance, and silently shadows built-ins. |

### CPython Import Lifecycle: `sys.modules` Caching `[Course: D13-03, D13-04]`
When Python encounters an `import foo` statement:
1. Python checks `sys.modules` (an internal dictionary mapping module names to loaded module objects).
2. **First Import:** If `foo` is not in `sys.modules`, CPython finds the file, compiles it to bytecode (`__pycache__/*.pyc`), creates a new module namespace, and **runs all top-level statements from line 1 to the end**.
3. **Subsequent Imports:** If `foo` is already present in `sys.modules`, CPython **reuses the cached reference immediately**. Top-level code is **NEVER executed twice** during a single Python runtime session.

```python
import sys
import math

# top-level check
print("math" in sys.modules)  # True
print(math.__name__)           # "math"
```

### The `if __name__ == "__main__":` Idiom `[Course: D13-13, D13-14]`
- When a file is executed directly (e.g. `python app.py`), CPython sets its special global variable `__name__ = "__main__"`.
- When a file is imported as a module (e.g. `import app`), CPython sets `__name__ = "app"`.
- This guard enables a file to serve dual roles: a **reusable library** when imported, and a **standalone runnable script/test harness** when executed directly.

---

## 3. How Python Finds Modules: `sys.path` & Resolution `[Course: D13-04, D13-12]`

CPython resolves module imports by searching the directories in `sys.path` in exact chronological sequence:

```
                    sys.path Search Order
┌─────────────────────────────────────────────────────────────┐
│ 1. Current directory of running script ('' in REPL)         │
│                              │                              │
│                              ▼                              │
│ 2. Folders listed in PYTHONPATH environment variable        │
│                              │                              │
│                              ▼                              │
│ 3. Standard Library directory (e.g. /usr/lib/python3.x)     │
│                              │                              │
│                              ▼                              │
│ 4. site-packages (Installed 3rd-party packages in venv)     │
└─────────────────────────────────────────────────────────────┘
```

### Dynamic Path Mutation
`sys.path` is an ordinary Python list of directory strings. You can inspect and modify it at runtime:
```python
import sys

# Inspect search roots
for p in sys.path[:3]:
    print(p)

# Dynamically add custom module library
sys.path.append("/path/to/my_libs")
```

### Bytecode Caching & Private Exports `[Course: D13-12]`
- **Bytecode Caching:** When a `.py` file is imported, CPython automatically writes compiled bytecode to `__pycache__/<name>.cpython-<version>.pyc` to accelerate subsequent startup times.
- **Introspection with `dir()`:** `dir(module)` returns a sorted list of all attributes and functions in that module namespace.
- **Private Names (`_`) in Star Imports:** If a module defines a function `def _helper():`, running `from module import *` **skips** `_helper`. Names prefixed with a leading underscore are treated as private to star imports (unless explicitly overridden in `__all__`).

---

## 4. The 4 Major Import Pitfalls `[Course: D13-05]`

In the BCPD exam, module questions frequently present broken import scenarios. You must identify which of the 4 classic pitfalls is occurring:

```
                      The 4 Import Pitfalls
  ┌─────────────────────────────────────────────────────────┐
  │ 1. SHADOWING TRAP                                       │
  │    Naming a local file random.py or math.py masks stdlib│
  │    -> AttributeError: module random has no attribute... │
  ├─────────────────────────────────────────────────────────┤
  │ 2. CIRCULAR IMPORTS                                     │
  │    module_a imports module_b; module_b imports module_a│
  │    -> ImportError: cannot import name from partially... │
  ├─────────────────────────────────────────────────────────┤
  │ 3. STAR IMPORT POLLUTION                                │
  │    from math import * overwrites built-in pow or vars   │
  │    -> Silently alters calculation outcomes             │
  ├─────────────────────────────────────────────────────────┤
  │ 4. VIRTUAL ENVIRONMENT / INTERPRETER MISMATCH           │
  │    Package installed in global Python, script runs in   │
  │    venv -> ModuleNotFoundError                          │
  └─────────────────────────────────────────────────────────┘
```

1. **Shadowing Trap:** If you save a file named `math.py` in your project directory and run `import math`, Python finds your local file first (step 1 of `sys.path`) instead of the standard library module. When you subsequently attempt `math.sqrt()`, Python raises `AttributeError: module 'math' has no attribute 'sqrt'`.
2. **Circular Imports:** When Module A imports Module B at top-level before defining its symbols, and Module B simultaneously imports Module A, CPython halts with `ImportError: cannot import name ... from partially initialized module`. **Remedy:** Move shared logic to a 3rd module or defer imports inside functions.
3. **Star Import Collision:** `from math import *` injects `math.e` (float `2.718...`) and `math.pow` directly into your namespace, overwriting any prior variable named `e` or the built-in 3-argument modular exponentiation function `pow(base, exp, mod)`.
4. **Interpreter Mismatch:** `ModuleNotFoundError: No module named 'xyz'` occurs when a package was installed under one interpreter while the script is running under another. Always verify `sys.executable`.

---

## 5. The `sys` Module & Runtime System Hooks `[Course: D13-06, D13-12]`

The `sys` module provides variables and functions that interact directly with the CPython interpreter runtime.

### CLI Arguments: `sys.argv` `[Course: D13-06, D13-14]`
- `sys.argv` is a `list[str]` containing arguments passed from the command line.
- **Rule 1:** `sys.argv[0]` is **always** the script name or path (e.g. `'args.py'`).
- **Rule 2:** `sys.argv[1:]` contains all subsequent CLI tokens.
- **Rule 3:** All elements in `sys.argv` are strings (`str`), even if digits were passed. You must convert them explicitly: `int(sys.argv[1])`.

```python
import sys

if len(sys.argv) < 2:
    print("usage: args.py <name>", file=sys.stderr)
    sys.exit(1)

print(f"Hello {sys.argv[1]}")
```

### Process Exit: `sys.exit(code)`
- `sys.exit(0)` indicates successful process termination.
- `sys.exit(1)` (or any non-zero integer) signals an error status code to the host OS.
- Internally, `sys.exit()` raises the `SystemExit` exception, allowing `try...finally` blocks to execute cleanup handlers before the process dies.

### Standard Streams: `stdin`, `stdout`, `stderr` `[Course: D13-06, D13-12]`
- `sys.stdout.write("hi\n")`: Writes raw text directly to standard output.
  - **Exam Trap:** `sys.stdout.write()` **returns the integer character count written** (`3`) and does **not** append an automatic newline (unlike `print()` which returns `None` and appends `\n`).
- `sys.stderr`: Used for diagnostic, debug, and error messages: `print("Error occurred", file=sys.stderr)`.

### System Introspection
- `sys.platform`: Returns the host platform identifier (`'win32'`, `'linux'`, `'darwin'`).
- `sys.version_info`: A named tuple containing major, minor, and micro versions (e.g. `(3, 15, 2, 'final', 0)`).
- `sys.getsizeof(obj)`: Returns the memory allocated for an object in bytes.
  - **Exam Trap:** `len("abc") == 3` (3 characters), but `sys.getsizeof("abc") >= 52` bytes due to CPython's `PyASCIIObject` memory header structure!
- `sys.getrecursionlimit()`: Returns the maximum call stack depth (default `1000`).

---

## 6. The `math` Module: Precision & Question-Bank Favourites `[Course: D13-07, D13-08, D13-09]`

The `math` module delivers C-standard floating-point operations.

### A. Rounding & Truncation Comparison Table

| Function | Call Example | Result | Type | Exact Behavior |
|---|---|---|---|---|
| `math.floor(x)` | `math.floor(-2.5)` | `-3` | `int` | Rounds **down** towards $-\infty$. |
| `math.ceil(x)` | `math.ceil(-2.5)` | `-2` | `int` | Rounds **up** towards $+\infty$. |
| `math.trunc(x)` | `math.trunc(-2.7)` | `-2` | `int` | Truncates fractional part towards $0$. |
| `round(x)` | `round(-2.5)` | `-2` | `int` | Banker's rounding (rounds to nearest **even** integer). |
| `math.modf(x)` | `math.modf(2.5)` | `(0.5, 2.0)` | `tuple[float, float]` | Returns `(fractional_part, integer_part)`. Both floats! |

### B. High-Yield Question-Bank Favourites `[Course: D13-09]`

```python
import math

# 1. math.pow vs **
print(math.pow(2, 3))       # 8.0 (math.pow ALWAYS returns a float!)
print(2 ** 3)               # 8   (** returns an int for integer operands)

# 2. math.fabs vs abs
print(math.fabs(-3))        # 3.0 (fabs ALWAYS returns a float!)
print(abs(-3))              # 3   (built-in abs preserves operand type)

# 3. math.copysign
# Magnitude of x, sign of y (supports signed negative zero -0.0)
print(math.copysign(3, -0.0))  # -3.0

# 4. math.fsum: Precision summation
naive_sum = sum([0.1] * 10)     # 0.9999999999999999 (IEEE 754 precision loss)
exact_sum = math.fsum([0.1] * 10) # 1.0 (Exact full-precision tracking)

# 5. Trigonometry expects Radians
print(math.sin(math.pi / 2))    # 1.0
print(math.degrees(math.pi))    # 180.0
print(math.radians(180) == math.pi) # True

# 6. Logarithms
print(math.log(math.e))         # 1.0 (natural log ln by default)
print(math.log(8, 2))           # 3.0 (log base 2)
print(math.log10(1000))         # 3.0 (specialized base-10)
print(math.log2(8))             # 3.0 (specialized base-2)

# 7. Factorial boundaries
print(math.factorial(0))        # 1 (0! == 1)
# math.factorial(-1) -> ValueError: factorial() not defined for negative values
# math.factorial(5.0) -> TypeError in Python 3.10+ (requires integer argument)

# 8. Floating-point infinity and NaN
print(math.isinf(math.inf))     # True
print(math.isnan(math.nan))     # True
print(math.inf - math.inf)      # nan (indeterminate form)
```

---

## 7. The `random` Module, PRNG & Security Boundaries `[Course: D13-10, D13-11]`

Python's `random` module uses the **Mersenne Twister** algorithm (period $2^{19937}-1$) to generate pseudo-random numbers.

### Number & Sequence Generators `[Course: D13-10]`
- `random.random()`: Generates float in range $[0.0, 1.0)$ ($0.0$ inclusive, $1.0$ exclusive).
- `random.randint(a, b)`: Generates integer in range $[a, b]$ (**both $a$ and $b$ are inclusive**).
- `random.randrange(start, stop[, step])`: Generates integer from `range(start, stop, step)`. **Stop is excluded**.
  - Note: `random.randint(a, b)` is functionally equivalent to `random.randrange(a, b + 1)`.
- `random.uniform(a, b)`: Generates uniform float in range $[a, b]$.
- `random.gauss(mu, sigma)`: Generates Gaussian (normal) distribution float.

### Sampling: `choice`, `choices`, and `sample` `[Course: D13-10, D13-11]`

| Function | Signature | Replacement? | Returns | Behavior |
|---|---|---|---|---|
| `random.choice(seq)` | `(seq)` | N/A | Single element | Picks 1 random item from a non-empty sequence. |
| `random.choices(seq, k=n, weights=...)` | `(seq, k=1)` | **With replacement** | `list` of $k$ items | Items **can duplicate**; accepts optional probability weights. |
| `random.sample(population, k=n)` | `(pop, k)` | **Without replacement** | `list` of $k$ items | Items are **strictly unique**; raises `ValueError` if $k > \text{len}(pop)$. |
| `random.shuffle(lst)` | `(lst)` | In-place | `None` | Mutates list in-place. **Raises `TypeError` on immutable sequences (tuples/strings).** |

### Seeding Determinism & Cryptographic Boundary `[Course: D13-11]`
```python
import random
import secrets

# Determinism: Same seed -> Identical sequence
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(3)]

random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(3)]
assert seq1 == seq2  # True! Reproducible for simulations and tests

# CRITICAL SECURITY BOUNDARY:
# The random module is completely deterministic and NOT cryptographically secure.
# Never use random for passwords, authentication tokens, API keys, or cryptography!
# Use the secrets module instead:
secure_token = secrets.token_hex(16)
secure_char = secrets.choice("ABCDEF123456")
```

---

## 8. Classroom Lab 13.1 — Dice Roller & Password Generator `[Course: D13-13]`

In Lab 13.1, you build two tools showcasing modularity and standard library integration:

### 1. `dice.py` Reusable Module
```python
"""
dice.py: Reusable dice rolling library with self-test execution guard.
"""
import random

def roll(n=1, sides=6):
    """Roll n dice with specified number of sides."""
    if n < 1 or sides < 2:
        raise ValueError("Must roll at least 1 die with at least 2 sides.")
    return [random.randint(1, sides) for _ in range(n)]

if __name__ == "__main__":
    # Self-test harness runs only when directly executed
    random.seed(42)
    sample_roll = roll(3, 6)
    print(f"Self-test roll(3, 6): {sample_roll}")
    assert len(sample_roll) == 3
    assert all(1 <= d <= 6 for d in sample_roll)
    print("dice.py self-test passed!")
```

### 2. `password.py` Command-Line Tool
```python
"""
password.py: CLI Password Generator built on sys, random, and string.
"""
import random
import string
import sys

def make_password(length=12):
    """Generate a password with guaranteed letter, digit, and symbol."""
    if length < 3:
        raise ValueError("Password length must be at least 3.")
    pools = [string.ascii_letters, string.digits, "!@#$%"]
    chars = [random.choice(p) for p in pools]  # Guarantee at least 1 of each
    everything = "".join(pools)
    chars += random.choices(everything, k=length - 3)
    random.shuffle(chars)  # In-place shuffle
    return "".join(chars)

if __name__ == "__main__":
    args = sys.argv[1:]
    n = int(args[0]) if args else 12
    print(make_password(n))
```

---

## 9. Exam Traps & Pitfalls Radar (Domain 4)

| Trap # | Code Snippet | What You Might Expect | Actual CPython Outcome | Core Principle |
|---|---|---|---|---|
| **Trap 49** | `import math`<br>Naming file `math.py` in cwd | Loads standard `math` | `AttributeError: module 'math' has no attribute 'sqrt'` | **Shadowing Trap:** `sys.path[0]` is current working directory. |
| **Trap 50** | `from math import *`<br>`pow(2, 3, 5)` | Computes $2^3 \pmod 5 = 3$ | `TypeError: pow() takes 2 positional arguments` | **Star Import Pollution:** `math.pow` overwrites built-in 3-arg `pow()`. |
| **Trap 51** | `math.floor(-2.5)` | `-2` | `-3` | **Negative Floor Trap:** Floored division and `floor()` always go towards $-\infty$. |
| **Trap 52** | `math.pow(2, 3)` | `8` (`int`) | `8.0` (`float`) | **Float Return Trap:** `math.pow()` **always** converts operands to C doubles and returns `float`. |
| **Trap 53** | `random.randint(1, 5)` | 1, 2, 3, or 4 | 1, 2, 3, 4, **or 5** | **Inclusive End Trap:** Unlike `range()` and `randrange()`, `randint` includes upper bound! |
| **Trap 54** | `t = (1, 2, 3)`<br>`random.shuffle(t)` | Returns shuffled tuple | `TypeError: 'tuple' object does not support item assignment` | **In-Place Mutation Trap:** `random.shuffle()` requires a mutable sequence (`list`). |

---

## 10. Official Day 13 Knowledge Check Review `[Course: D13-14]`

### Q1. Which import style is discouraged because it pollutes the namespace?
- A) `import math`
- B) `from math import sqrt`
- C) `from math import *`
- D) `import math as m`
- **Correct Answer: C (`from math import *`)**
- *Distractor Analysis:* A, B, and D cleanly isolate symbols or bring in specific names. Star import dumps all public module symbols into global scope.

### Q2. What is `__name__` inside `app.py` when you run `python app.py`?
- A) `'app'`
- B) `'__main__'`
- C) `'app.py'`
- D) `None`
- **Correct Answer: B (`'__main__'`)**
- *Distractor Analysis:* The entry-point script is always designated as `'__main__'`. Only imported modules receive their module stem name (`'app'`).

### Q3. Which values can `random.randint(1, 3)` return?
- A) `1 or 2`
- B) `0 to 3`
- C) `Any float from 1 to 3`
- D) `1, 2 or 3`
- **Correct Answer: D (`1, 2 or 3`)**
- *Distractor Analysis:* `randint(a, b)` includes both endpoints $a$ and $b$. Option A confuses `randint` with `range(1, 3)` / `randrange(1, 3)`.

### Q4. Output of `import math; print(math.floor(-2.5))`?
- A) `-2`
- B) `-3`
- C) `-2.5`
- D) `-3.0`
- **Correct Answer: B (`-3`)**
- *Distractor Analysis:* `floor` rounds towards negative infinity, so $-2.5 \to -3$. Truncation (`math.trunc(-2.5)`) would produce `-2`. Furthermore, `floor()` returns an `int` in Python 3, eliminating options C and D.

### Q5. What is `sys.argv[0]`?
- A) The script name
- B) The first argument after the script
- C) The Python version
- D) The exit code
- **Correct Answer: A (The script name)**
- *Distractor Analysis:* `sys.argv[0]` is the script invocation token itself. `sys.argv[1]` is the first user-supplied argument.
