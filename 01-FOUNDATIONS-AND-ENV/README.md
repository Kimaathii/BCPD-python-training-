# Module 01 â€” Foundations, Environment & Your First Program

> **Sources:** `IMG-19`, `IMG-21`, `IMG-22`, `IMG-23`, `IMG-24`, `IMG-25`, `IMG-26`, `IMG-27`, `IMG-28`, `IMG-29`, `IMG-56` (`Day 1 Â· MANUAL Â§1.1â€“1.23`)
> **Related Notebook Note:** [IMG-56](file:///c:/Users/kimat/Downloads/class%20screenshots/WhatsApp%20Image%202026-11-11%20at%2009.32.31.jpeg)

---

## 1. Conceptual Foundation

- **BCPD Exam Context `[Course: IMG-56]`:** The BCPD certification exam consists of **90 questions** in **120 minutes**, with a **pass mark of 70** across **7 domains**. **Domain 1 (Introduction & Setup)** accounts for **20% (18 questions)**.
- **How CPython Runs Your Code `[Course: IMG-56, IMG-26]`:**
  1. **Lexing:** Source text is split into tokens (keywords, names, operators, literals).
  2. **Parsing â†’ AST:** Tokens are arranged into an Abstract Syntax Tree. Invalid syntax (`SyntaxError`, `IndentationError`, `TabError`) stops execution right here before any line runs.
  3. **Bytecode Compilation:** The AST is compiled into platform-independent bytecode and cached as **`.pyc`** files inside **`__pycache__/`** *(note: handwritten note `IMG-56` wrote `.py in _pycache`â€”corrected here)*.
  4. **PVM Execution:** The Python Virtual Machine (PVM) executes bytecode instructions step by step.
- **Interactive Mode (REPL) vs. Script Mode `[Course: IMG-21]`:**
  - **REPL (`>>>`):** Evaluates one statement/expression at a time and automatically echoes bare expression values (`name` â†’ `'Ada'`). Exit via `exit()`, `Ctrl+Z` (Windows), or `Ctrl+D` (macOS/Linux).
  - **Script Mode (`python hello.py`):** Runs a `.py` file top-to-bottom; bare expressions produce no console output unless passed to `print()`.
- **Virtual Environments & `pip` `[Course: IMG-24, IMG-19]`:**
  - A virtual environment (`.venv`) isolates project packages so library versions do not collide across projects.
  - Running `python -m pip install <pkg>` guarantees `pip` installs into the exact Python interpreter you are executing, preventing *"installed but `ModuleNotFoundError`"* mismatches.
- **Comments, Docstrings, Indentation & PEP 8 `[Course: IMG-56, IMG-19, IMG-26]`:**
  - `#` starts a single-line comment; `"""..."""` writes a docstring `[Course: IMG-56]`.
  - Python defines code blocks with a colon (`:`) followed by consistent **4-space indentation** `[Course: IMG-19]`.
  - PEP 8 naming conventions `[Course: IMG-56, IMG-26]`: `snake_case` for variables/functions, `UPPER_CASE` for constants, `PascalCase` for classes.

---

## 2. Mental Models

- **The 4-Stage Kitchen Pipeline (CPython):**
  - *Lexing* = chopping ingredients into labeled tokens.
  - *Parsing (AST)* = checking the recipe structure (a missing `:` rejects the recipe before cooking even starts).
  - *Bytecode (`.pyc`)* = prepped meal kits stored in `__pycache__` so Python doesn't re-parse unchanged imported modules.
  - *PVM* = the chef executing each bytecode instruction.
- **`venv` as a Separate Toolbox:** Without a virtual environment, every project dumps tools into one shared garage (`global site-packages`). A `.venv` gives each project its own locked toolbox.
- **`input()` as a Sealed Envelope of Text:** No matter whether a user types `42`, `3.14`, or `hello`, `input()` always hands your program a `str` (`'42'`). You must unbox it with `int()` or `float()` before doing math.

---

## 3. Syntax and Code

### A. Console I/O (`print()` and `input()`) `[Course: IMG-22 | io_demo.py]`

**ORIGINAL CLASSROOM CODE:**
```python
print("a", "b", "c")           # -> a b c
print("a", "b", sep="-")       # -> a-b
print("Loading", end="...")
print("done")                  # -> Loading...done

age = input("Age: ")           # user types 20
print(type(age))               # <class 'str'>
age = int(age)
print(age + 1)                 # 21
```

### B. Installing, Verifying & Virtual Environments `[Course: IMG-23, IMG-24]`

```text
# Verify Python (Windows / macOS / Linux)
python --version   (or: py --version on Windows, python3 --version on macOS/Linux)

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate         # Windows
source .venv/bin/activate      # macOS / Linux

# Install, freeze, restore, deactivate
python -m pip install requests
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
deactivate
```

### C. Lab 1.1 & 1.2 (`calc.py`) `[Course: IMG-25]`

**ORIGINAL CLASSROOM CODE (`calc.py`):**
```python
# calc.py
a = float(input("First number: "))
b = float(input("Second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
```

**CORRECTED / IMPROVED CODE (`[Supplementary]` â€” guards `b == 0` and invalid numbers):**
```python
def run_safe_calculator() -> None:
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Error: please enter valid numeric values.")
        return

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b == 0:
        print("Quotient: undefined (cannot divide by zero)")
    else:
        print("Quotient:", a / b)
```
*Difference:* Original `calc.py` crashes with `ValueError` on non-numeric text (noted in `IMG-22` as handled in Week 3) and `ZeroDivisionError` when `b` is `0`. The improved version handles both cleanly.

---

## 4. Line-by-Line Explanation (`io_demo.py` & `calc.py`)

- `print("a", "b", "c")`: Passes 3 positional arguments; default `sep=" "` joins them with spaces, default `end="\n"` moves to a new line.
- `print("a", "b", sep="-")`: Overrides `sep` so `"-"` sits between items (`a-b`).
- `print("Loading", end="...")`: Replaces the trailing newline with `"..."`, so the next `print("done")` stays on the same line (`Loading...done`).
- `age = input("Age: ")`: Displays `"Age: "`, pauses for keyboard input, and binds the resulting **`str`** to `age`.
- `age = int(age)`: Converts `"20"` â†’ `20` (`int`), rebinding `age`. Without this, `age + 1` fails (`TypeError: can only concatenate str (not "int") to str`).
- `a = float(input(...))` in `calc.py`: Composes `input()` inside `float()` so the user's string is immediately converted to a floating-point number before arithmetic.

---

## 5. Code Tracing (`io_demo.py` when user types `20`)

| Step | Statement | `age` Value | `type(age)` | Console Output |
|---|---|---|---|---|
| 1 | `print("a", "b", "c")` | â€” | â€” | `a b c` |
| 2 | `print("a", "b", sep="-")` | â€” | â€” | `a-b` |
| 3 | `print("Loading", end="...")` | â€” | â€” | `Loading...` *(no newline)* |
| 4 | `print("done")` | â€” | â€” | `done` *(completes line `Loading...done`)* |
| 5 | `age = input("Age: ")` | `'20'` | `str` | Prompt `Age: ` |
| 6 | `print(type(age))` | `'20'` | `str` | `<class 'str'>` |
| 7 | `age = int(age)` | `20` | `int` | â€” |
| 8 | `print(age + 1)` | `20` | `int` | `21` |

---

## 6. Common Pitfalls `[Course: IMG-19, IMG-22, IMG-23]`

1. **`python` opens Microsoft Store / "not recognized":** Python isn't on `PATH` (or `WindowsApps` alias precedes it); use `py` on Windows or add Python to `PATH`.
2. **`ModuleNotFoundError` right after `pip install`:** `pip` belonged to a different Python interpreter than the one running your script. Always use `python -m pip install ...` inside the activated `.venv`.
3. **`IndentationError: expected an indented block`:** Nothing is indented after a `:` header (`if`, `for`, `def`). Indent consistently by 4 spaces.
4. **`TabError`:** Mixing literal Tab characters and spaces in the same block. Configure your editor to insert 4 spaces.
5. **Forgetting `input()` returns `str`:** Trying `input("Age: ") + 1` raises `TypeError`; `int("abc")` raises `ValueError`.
6. **Expecting REPL echoing inside a `.py` file:** Writing `2 + 3` on its own line in a script computes `5` and discards it; scripts need `print(2 + 3)`.

---

## 7. MCQ Examination Traps

### Instructor Slide Questions `[Course: IMG-29, IMG-26]`

1. **What does `input()` return when the user types `42`?**
   - **A. `The str '42'`** *(Correct â€” `input()` always returns a string.)*
   - B. `The int 42` *(Incorrect â€” conversion requires explicit `int()`.)*
   - C. `A float` *(Incorrect â€” requires `float()`.)*
   - D. `None` *(Incorrect â€” `print()` returns `None`, not `input()`.)*

2. **Output of `print("a", "b", sep="-", end="!")`?**
   - A. `a b!` *(Incorrect â€” ignores `sep="-"`.)*
   - **B. `a-b!`** *(Correct â€” `sep` goes between values; `end` replaces the trailing newline.)*
   - C. `a-b` *(Incorrect â€” ignores `end="!"`.)*
   - D. `ab-!` *(Incorrect â€” `sep` goes between items, not after the last item.)*

3. **Which command creates a virtual environment named `.venv`?**
   - A. `pip install venv` *(Incorrect â€” `venv` is built into the Python 3 standard library.)*
   - B. `python venv create` *(Incorrect â€” missing `-m` and invalid subcommand.)*
   - **C. `python -m venv .venv`** *(Correct â€” runs the standard-library `venv` module with target folder `.venv`.)*
   - D. `venv --new .venv` *(Incorrect â€” `venv` is not a standalone shell command.)*

4. **Before execution, CPython compiles source code into...**
   - A. `Machine code` *(Incorrect â€” CPython compiles to bytecode for the PVM, not native CPU machine code.)*
   - **B. `Bytecode`** *(Correct â€” AST compiles to `.pyc` bytecode executed by the PVM.)*
   - C. `Java bytecode` *(Incorrect â€” that belongs to the JVM/Jython, not standard CPython.)*
   - D. `Assembly` *(Incorrect â€” CPython does not emit assembly.)*

5. **Which variable name follows PEP 8?**
   - A. `TotalCount` *(Incorrect â€” `PascalCase` is for classes, not variables.)*
   - B. `totalCount` *(Incorrect â€” `camelCase` is not PEP 8 for Python variables.)*
   - C. `TOTAL-COUNT` *(Incorrect â€” `-` is subtraction, making it an invalid identifier.)*
   - **D. `total_count`** *(Correct â€” variables use lowercase `snake_case`.)*

### Exam-Style Practice `[Supplementary]`

6. **What happens if a `.py` file has a `SyntaxError` on line 10, while line 1 has `print("Start")`?**
   - A. `"Start"` prints, then `SyntaxError` is raised at line 10
   - **B. Nothing executes; `SyntaxError` is raised before line 1 runs** *(Correct â€” parsing checks the whole file into an AST before PVM execution begins.)*
   - C. `"Start"` prints and line 10 is skipped
   - D. `IndentationError` is raised instead *(Incorrect â€” indentation errors are a subclass of `SyntaxError`, only for bad indentation.)*

7. **What is the output of:**
   ```python
   x = print("Hi")
   print(x)
   ```
   - A. `Hi` then `Hi` *(Incorrect â€” `print()` writes to stdout, it does not return the printed text.)*
   - **B. `Hi` then `None`** *(Correct â€” `print()` always returns `None`.)*
   - C. `None` then `Hi` *(Incorrect â€” `print("Hi")` runs first.)*
   - D. `TypeError` *(Incorrect â€” printing `None` is valid.)*

---

## 8. Practice Exercises *(Attempt in `exercises.py` Before Checking Solutions!)*

- **Level 1 (Basic):** Print `"2026-11-12"` using `print(2026, 11, 12, sep=...)` and print `"Loading...done"` across two `print()` calls.
- **Level 2 (Application â€” Lab 1.1 & 1.2 `[Course: IMG-25]`):** Implement `greet_user()` (`Hello, <name>!`) and `safe_calculator()` handling division by zero.
- **Level 3 (Problem-Solving):** Write `format_receipt_line(item, qty, unit_price)` returning a formatted string without calling `print()` inside the helper, then print 2 lines joined on one line or separated by `" | "`.
- **Level 4 (Exam Reasoning):** Without running Python, diagnose and fix the 3 setup/syntax bugs in `broken_setup_snippets()` inside `exercises.py`.

---

## 9. Topic Mastery Checklist
- [ ] I can state the 4 CPython stages (Lexing â†’ Parsing/AST â†’ `.pyc` Bytecode in `__pycache__` â†’ PVM) and explain why `SyntaxError` prevents line 1 from running.
- [ ] I can distinguish `IndentationError`, `TabError`, `SyntaxError`, `ValueError`, and `ModuleNotFoundError`.
- [ ] I can create, activate, freeze, and deactivate a `.venv`, and explain why `python -m pip` beats bare `pip`.
- [ ] I can predict outputs of `print(..., sep=..., end=...)` and explain why `input()` requires `int()`/`float()` conversion.
- [ ] I can apply PEP 8 naming (`snake_case`, `UPPER_CASE`, `PascalCase`).
