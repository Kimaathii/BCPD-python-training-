# Day 13 New Classroom Screenshot Inventory & Verbatim Extractions
**Class Date:** Monday 23 Nov 2026 (Week 3, Day 13)  
**Subject:** Modules Part 1: Imports, `sys`, `math` & `random`  
**BCPD Exam Weight:** Domain 4 · Modules & Libraries (15%)  
**Student Manual Mapping:** Day 14 · §14.1–14.6  
**Image Files Staged:** 17 JPEG files (`WhatsApp Image 2026-11-23 at 21.58.20.jpeg` to `21.58.43.jpeg`)  
**Curriculum Mapping:** Module 15 (`15-MODULES-SYS-MATH-AND-RANDOM`) & Central Exam Prep Hub (`10-EXAM-PREPARATION/`)

---

## 1. Master Slide Index & Provenance Cross-Reference

| Slide Tag | Source File(s) | Slide Title / Manual Ref | Core Topic / Code File | Target Curriculum Location |
|---|---|---|---|---|
| `[Course: D13-01]` | `21.58.20.jpeg` | Title Slide (Manual §14.1–14.6) | Week 3 Day 13 Launch (`day13.py`) | `15-MODULES-SYS-MATH-AND-RANDOM/README.md` |
| `[Course: D13-02]` | `21.58.22.jpeg` | Objectives & Agenda | 5 competencies, 10 agenda items, Lab 13.1 | `15-MODULES-SYS-MATH-AND-RANDOM/README.md` |
| `[Course: D13-03]` | `21.58.24.jpeg` | Import styles (§14.1–14.2) | 5 import styles, `sys.modules` cache | `15-MODULES-SYS-MATH-AND-RANDOM/README.md` |
| `[Course: D13-04]` | `21.58.24d.jpeg` | How Python finds modules: `sys.path` (§14.2) | `paths.py`, search order, shadowing trap | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-05]` | `21.58.25.jpeg` | Import pitfalls (§14.2) | Shadowing, Circular imports, `import *`, wrong venv | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, Traps 49–50 |
| `[Course: D13-06]` | `21.58.26h.jpeg` | The `sys` module (§14.3) | `args.py`, `sys.argv`, `sys.exit`, streams, `getsizeof` | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-07]` | `21.58.26.jpeg`, `21.58.27.jpeg` | `math`: everyday functions (§14.4) | `sqrt`, `pow`, `ceil/floor`, `trunc`, `fabs`, `factorial`, `gcd`, `isclose` | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-08]` | `21.58.27b.jpeg`, `21.58.28.jpeg` | `math`: constants, logs & trigonometry (§14.4) | `math_more.py`, constants, log bases, radians trig | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-09]` | `21.58.28v.jpeg` | More math functions (question-bank favourites) (§14.4) | `copysign`, `fabs` vs `abs`, `modf`, `fsum`, IEEE `inf`/`nan` | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, Traps 51–52 |
| `[Course: D13-10]` | `21.58.29.jpeg` | `random`: numbers & choices (§14.5) | `random_basics.py`, `randint` vs `randrange`, `choice`, `shuffle` | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-11]` | `21.58.29g.jpeg` | `random`: sampling, distributions & seeds (§14.5) | `random_more.py`, `seed`, `sample` vs `choices`, `secrets` boundary | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, `examples.py` |
| `[Course: D13-12]` | `21.58.42.jpeg` | Modules, sys & random: exam details (§14.3–14.5) | `details.py`, `sys.stdout.write` char count, `shuffle` on tuple trap | `15-MODULES-SYS-MATH-AND-RANDOM/README.md`, Traps 53–54 |
| `[Course: D13-13]` | `21.58.42v.jpeg`, `21.58.42b.jpeg` | Lab 13.1 — Dice roller & password generator (§14.6) | `dice.py`, `password.py`, CLI tool, `secrets` comparison | `15-MODULES-SYS-MATH-AND-RANDOM/exercises.py`, Solutions |
| `[Course: D13-14]` | `21.58.43.jpeg` | Knowledge check (5 questions · 5 minutes) | Official Day 13 Quiz (Q13.1–Q13.5) | `10-EXAM-PREPARATION/instructor-knowledge-checks.md` |

---

## 2. Verbatim Code & Content Transcriptions

### Slide `D13-01`: Title Slide & Opening Teaser
- **Header:** `WEEK 3 · DAY 13 · MONDAY 23 NOV 2026`
- **Topic:** `Modules Part 1: Imports, sys, math & random`
- **Goal:** *"Organise code into modules, understand how imports work, and use three essential standard modules."*
- **Exam Weight:** `Domain 4 · Modules & Libraries (15%)`
- **Manual Ref:** `Student manual: Day 14 · §14.1–14.6`
- **Code (`day13.py`):**
  ```python
  import math, random, sys

  random.seed(42)
  print(random.randint(1, 6))  # 6
  print(math.ceil(2.1))        # 3
  print(sys.platform)
  ```

---

### Slide `D13-02`: Today's Objectives & Agenda
- **Learning Outcomes:**
  1. Import modules in every style and know when to use each
  2. Explain how Python finds modules (`sys.path`) and avoid import pitfalls
  3. Use `sys` for arguments, exit codes and environment details
  4. Use `math` for rounding, powers, logs and trigonometry
  5. Use `random` correctly, including sampling and seeding
- **Agenda Breakdown:**
  - `14.1` Import styles
  - `14.2` How Python finds modules: `sys.path`
  - `14.2` Import pitfalls
  - `14.3` The `sys` module
  - `14.4` `math`: everyday functions
  - `14.4` `math`: constants, logs & trigonometry
  - `14.4` More math functions (question-bank favourites)
  - `14.5` `random`: numbers & choices
  - `14.5` `random`: sampling, distributions & seeds
  - `14.3` Modules, `sys` & `random`: exam details
  - `Lab` Lab 13.1 — Dice roller & password generator

---

### Slide `D13-03`: Import Styles (`MANUAL §14.1–14.2`)
- **Table:**
  - `import module` | `import math` | `math.sqrt(9)` | *Clear and safe — recommended*
  - `import module as alias` | `import numpy as np` | `np.array(...)` | *Standard short names*
  - `from module import name` | `from math import pi` | `pi` | *Convenient; watch for name clashes*
  - `from module import name as alias` | `from datetime import datetime as dt` | `dt.now()` | *Rename on import*
  - `from module import *` | `from math import *` | `sqrt(9)` | *Avoid: pollutes your namespace*
- **Callout:**
  > *"A module runs its top-level code only on the first import; later imports reuse the cached copy in `sys.modules`."*

---

### Slide `D13-04`: How Python Finds Modules: `sys.path` (`MANUAL §14.2`)
- **Code (`paths.py`):**
  ```python
  import sys

  for p in sys.path[:3]:
      print(p)
  # 1. folder of the running script ('' in the REPL)
  # 2. folders listed in the PYTHONPATH variable
  # 3. the standard library, then site-packages

  sys.path.append("/home/ada/my_libs")  # add at runtime
  import math
  print(math.__name__, "math" in sys.modules)  # math True
  ```
- **Key Callouts:**
  - **Search order:** `Script folder -> PYTHONPATH -> standard library -> site-packages.`
  - **Shadowing trap:** `A file named random.py or math.py in your folder hides the real module — rename it.`
  - **ModuleNotFoundError:** `The module is not in any folder on sys.path — check it is installed in this venv.`

---

### Slide `D13-05`: Import Pitfalls (`MANUAL §14.2`)
1. **Shadowing:** A file named `random.py` hides the real module: `"module random has no attribute randint"`.
2. **Circular Imports:** `a.py` imports `b.py`, which imports `a.py` -> partially initialised module. Move shared code into a third module.
3. **`import *`:** Silently overwrites names — `from math import *` replaces your own `e` or `pow`.
4. **Wrong interpreter:** `ModuleNotFoundError` for an installed package usually means a different venv is active.

---

### Slide `D13-06`: The `sys` Module (`MANUAL §14.3`)
- **Bullet points:**
  - `sys.argv` — command-line arguments; `argv[0]` is the script name
  - `sys.exit(code)` — stop the program; `0` means success, anything else an error
  - `sys.platform`, `sys.version`, `sys.version_info` — environment details
  - `sys.stdin`, `sys.stdout`, `sys.stderr` — the standard streams
  - `sys.getsizeof(obj)`, `sys.getrecursionlimit()` — runtime information
- **Code (`args.py`):**
  ```python
  import sys

  print("Script:", sys.argv[0])
  print("Args:", sys.argv[1:])
  if len(sys.argv) < 2:
      print("usage: args.py NAME", file=sys.stderr)
      sys.exit(1)
  print(f"Hello {sys.argv[1]}")

  # $ python args.py Ada 36
  # Script: args.py
  # Args: ['Ada', '36']
  # Hello Ada
  ```

---

### Slide `D13-07`: `math`: Everyday Functions (`MANUAL §14.4`)
- **Table:**
  - `math.sqrt(x)` | `math.sqrt(16)` | `4.0`
  - `math.pow(x, y)` | `math.pow(2, 3)` | `8.0 (always a float)`
  - `math.ceil(x) / math.floor(x)` | `math.ceil(-2.5), math.floor(-2.5)` | `-2, -3`
  - `math.trunc(x)` | `math.trunc(-2.7)` | `-2`
  - `math.fabs(x)` | `math.fabs(-3)` | `3.0`
  - `math.factorial(n)` | `math.factorial(5)` | `120`
  - `math.gcd(a, b)` | `math.gcd(12, 18)` | `6`
  - `math.isclose(a, b)` | `math.isclose(0.1 + 0.2, 0.3)` | `True`

---

### Slide `D13-08`: `math`: Constants, Logs & Trigonometry (`MANUAL §14.4`)
- **Code (`math_more.py`):**
  ```python
  import math
  print(math.pi)                               # 3.141592653589793
  print(round(math.log(100, 10)))              # 2
  print(math.log10(1000), math.log2(8))        # 3.0 3.0
  print(math.exp(0))                           # 1.0
  print(round(math.sin(math.pi / 2), 2))       # 1.0
  print(math.degrees(math.pi))                 # 180.0
  print(math.radians(180) == math.pi)          # True
  print(math.inf > 10 ** 100, math.isnan(math.nan)) # True True
  print(math.hypot(3, 4))                      # 5.0
  ```
- **Notes:**
  - `log(x, base)`: Natural log by default; `log10` and `log2` are more precise for those bases.
  - `Radians`: Trig functions use radians — convert with `math.radians()`.
  - `Floats`: Most results are floats; use `round()` or `isclose()` to compare.

---

### Slide `D13-09`: More Math Functions (Question-Bank Favourites) (`MANUAL §14.4`)
- **Table:**
  - `math.copysign(3, -0.0)` | `-3.0` | Size of $x$, sign of $y$
  - `math.fabs(-3) vs abs(-3)` | `3.0 vs 3` | `fabs` always returns a float
  - `math.trunc(-2.7), math.modf(2.5)` | `-2, (0.5, 2.0)` | `modf` -> `(fraction, whole part)`
  - `math.frexp(8), math.ldexp(0.5, 4)` | `(0.5, 4), 8.0` | $x = m \times 2^e$
  - `math.fsum([0.1] * 10)` | `1.0` | Exact; `a += 0.1` loop gives `0.9999999999999999`
  - `math.isfinite(math.inf), math.isinf(-math.inf)` | `False, True` | Also `math.isnan()`
  - `math.inf - math.inf` | `nan` | Undefined -> not a number
  - `math.factorial(0), math.factorial(-1)` | `1, ValueError` | A float like `5.0` -> `TypeError (3.10+)`
  - `math.log(math.e), math.log(8, 2)` | `1.0, 3.0` | No `math.logx` — use `log(x, base)`

---

### Slide `D13-10`: `random`: Numbers & Choices (`MANUAL §14.5`)
- **Bullets:**
  - `random.random() -> float in [0.0, 1.0)`
  - `random.randint(a, b) -> int in [a, b]` — both ends included
  - `random.randrange(start, stop, step) -> like range; stop excluded`
  - `random.choice(seq) -> one item`
  - `random.choices(seq, k=n) -> n items with repeats`
  - `random.shuffle(lst)` shuffles in place and returns `None`
- **Code (`random_basics.py`):**
  ```python
  import random
  random.seed(42)  # reproducible
  print(random.randint(1, 6))                   # 6
  print(random.choice(["red", "green", "blue"])) # red
  x = random.random()
  print(0 <= x < 1)                             # True
  deck = list(range(1, 6))
  print(random.shuffle(deck))                   # None
  print(sorted(deck))                           # [1, 2, 3, 4, 5]
  print(random.randrange(0, 10, 5) in (0, 5))   # True
  ```

---

### Slide `D13-11`: `random`: Sampling, Distributions & Seeds (`MANUAL §14.5`)
- **Code (`random_more.py`):**
  ```python
  import random
  random.seed(1)
  a = [random.randint(1, 100) for _ in range(3)]
  random.seed(1)
  b = [random.randint(1, 100) for _ in range(3)]
  print(a == b)                                    # True

  hand = random.sample(range(1, 50), 6)            # unique items
  print(len(set(hand)))                            # 6
  print(len(random.choices("HT", k=10)))           # 10
  u = random.uniform(1.5, 2.5)
  print(1.5 <= u <= 2.5)                           # True
  g = random.gauss(0, 1)                           # mean 0, sd 1
  print(type(g).__name__)                          # float
  ```
- **Callouts:**
  - `seed()`: Same seed -> same sequence. Essential for tests and reproducible experiments.
  - `sample vs choices`: `sample` picks unique items; `choices` allows repeats and accepts `weights=`.
  - `Not for security`: Use the `secrets` module for passwords and tokens.

---

### Slide `D13-12`: Modules, `sys` & `random`: Exam Details (`MANUAL §14.3–14.5`)
- **Bullets:**
  - Two `from` imports of the same name: the last one wins; `import *` skips `_private` names
  - `dir(module)` lists names; compiled bytecode is cached as `.pyc` in `__pycache__`
  - `sys.stdout.write()` returns the character count and adds no newline; `len() != sys.getsizeof()`
  - `random.seed()` returns `None`; `randint(a, b)` is `randrange(a, b + 1)`
  - `choice()` needs a sequence; `shuffle()` needs a mutable list
- **Code (`details.py`):**
  ```python
  import sys, random
  n = sys.stdout.write("hi\n")                         # -> hi
  print(n)                                             # -> 3
  print(len("abc"), sys.getsizeof("abc") > 3)          # -> 3 True
  print(random.seed(7))                                # -> None
  random.seed(1); a = random.randint(1, 6)
  random.seed(1); b = random.randrange(1, 7)
  print(a == b)                                        # -> True
  print(random.choice("xyz") in "xyz")                 # -> True
  try:
      random.shuffle((1, 2, 3))
  except TypeError:
      print("tuples can't be shuffled")
      # -> tuples can't be shuffled
  ```

---

### Slide `D13-13`: Lab 13.1 — Dice Roller & Password Generator (`MANUAL §14.6`)
- **Prompt:** Write a reusable module and a command-line tool built on the standard library.
  1. Create `dice.py` with `roll(n=1, sides=6)` returning a list; add a self-test under the `__main__` guard.
  2. From a second file, import it three different ways and roll two dice.
  3. Password generator: length from `sys.argv` (default 12) with letters, digits, and symbols — at least one of each.
  4. Seed `random` and show two runs match; then switch to `secrets` and explain why.
- **Code (`password.py`):**
  ```python
  import random
  import string
  import sys

  def make_password(length=12):
      pools = [string.ascii_letters,
               string.digits, "!@#$%"]
      chars = [random.choice(p) for p in pools]
      everything = "".join(pools)
      chars += random.choices(everything, k=length - 3)
      random.shuffle(chars)
      return "".join(chars)

  if __name__ == "__main__":
      args = sys.argv[1:]
      n = int(args[0]) if args else 12
      print(make_password(n))
  ```

---

### Slide `D13-14`: Knowledge Check (5 Questions · 5 Minutes)
- **Q1:** Which import style is discouraged because it pollutes the namespace?
  - A) `import math`
  - B) `from math import sqrt`
  - C) `from math import *`
  - D) `import math as m`
  - **Answer:** **C** (`from math import *`)
- **Q2:** What is `__name__` inside `app.py` when you run `python app.py`?
  - A) `'app'`
  - B) `'__main__'`
  - C) `'app.py'`
  - D) `None`
  - **Answer:** **B** (`'__main__'`)
- **Q3:** Which values can `random.randint(1, 3)` return?
  - A) 1 or 2
  - B) 0 to 3
  - C) Any float from 1 to 3
  - D) 1, 2 or 3
  - **Answer:** **D** (`1, 2 or 3`)
- **Q4:** Output of `import math; print(math.floor(-2.5))`?
  - A) -2
  - B) -3
  - C) -2.5
  - D) -3.0
  - **Answer:** **B** (`-3`)
- **Q5:** What is `sys.argv[0]`?
  - A) The script name
  - B) The first argument after the script
  - C) The Python version
  - D) The exit code
  - **Answer:** **A** (The script name)
