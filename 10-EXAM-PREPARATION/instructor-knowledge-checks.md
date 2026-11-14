# Instructor Knowledge Checks â€” Complete Classroom Quiz Bank

> **BCPD Python Cohort 2 Certification Preparation**  
> **Source Screen Mappings:** `IMG-11` (Day 1), `IMG-30` (Day 2), `IMG-50` (Day 3), `IMG-73` (Day 4)  
> **Status:** All 20 Questions Extracted, Reconstructed, and Fully Annotated.

---

## Day 1 Knowledge Check `[Course: IMG-11]`

### Question 1.1
**Which of the following describes Python?**
- A) A statically-typed, compiled language
- B) A dynamically-typed, interpreted language
- C) A low-level assembly language
- D) A machine-code language
- **Correct Answer:** **B**
- **Explanation:** Python is dynamically typed (types are checked at runtime and variables bind to objects, not fixed memory types) and interpreted (source code is compiled into bytecode and executed by the CPython virtual machine).
- **Distractor Analysis:** Option A describes C/C++ or Rust. Options C and D refer to hardware-level binary/assembly.

### Question 1.2
**What is the role of the Python Virtual Machine (PVM)?**
- A) To convert Python source code into machine code directly
- B) To execute Python bytecode (.pyc) instructions
- C) To manage computer hardware directly without an OS
- D) To format code according to PEP 8
- **Correct Answer:** **B**
- **Explanation:** The Python compiler first translates `.py` source text into platform-independent bytecode; the PVM is the runtime engine that executes those bytecode instructions.
- **Distractor Analysis:** PVM does not directly produce native machine code (unless a JIT like PyPy is used). Hardware is managed by the OS. PEP 8 is enforced by linters (flake8, black), not the runtime.

### Question 1.3
**Which command is used to create a virtual environment in Python 3?**
- A) `python -m venv myenv`
- B) `pip install virtualenv`
- C) `python --make-env myenv`
- D) `pyenv create myenv`
- **Correct Answer:** **A**
- **Explanation:** The standard library `venv` module is invoked via `python -m venv <directory>` (documented in Day 1 Lab 1, `IMG-06`).
- **Distractor Analysis:** Option B installs an external third-party tool. Option C is invalid syntax. Option D is a command from the separate `pyenv` version-management utility.

### Question 1.4
**What does PEP stand for in Python enhancement proposals?**
- A) Python Execution Protocol
- B) Python Enhancement Proposal
- C) Program Evaluation Procedure
- D) Python Extension Package
- **Correct Answer:** **B**
- **Explanation:** PEP stands for Python Enhancement Proposal, the standard design document mechanism for proposing features, processes, and style guidelines (e.g., PEP 8).

### Question 1.5
**What is the default return type of the built-in `input()` function?**
- A) `int`
- B) `float`
- C) `str`
- D) `None`
- **Correct Answer:** **C**
- **Explanation:** Regardless of user input (even if numeric characters are typed), `input()` always returns a string (`str`). Converting to numerical types requires explicit casting (e.g. `int(input())`).

---

## Day 2 Knowledge Check `[Course: IMG-30]` `[Reconstructed Key]`

> [!NOTE]
> The slide `IMG-30` displays the 5 quiz questions for Day 2, but the corresponding answer slide was omitted from the classroom deck. The answer key below has been rigorously reconstructed and verified against CPython semantics and the Day 2 syllabus.

### Question 2.1
**What is the output of `print(10 // 3, 10 % 3)`?**
- A) `3.33 1`
- B) `3 1`
- C) `3 0`
- D) `3.0 1`
- **Correct Answer:** **B** `[Reconstructed Key]`
- **Explanation:** `10 // 3` performs floor division resulting in integer `3`. `10 % 3` computes the modulo remainder resulting in integer `1`. Both operands are ints, so the results are ints.

### Question 2.2
**Which of the following values evaluates to `False` in a boolean context?**
- A) `[0]`
- B) `"False"`
- C) `()`
- D) `-1`
- **Correct Answer:** **C** `[Reconstructed Key]`
- **Explanation:** In Python, empty collections (empty tuple `()`, empty list `[]`, empty string `""`, empty dict `{}`) evaluate to `False`.
- **Distractor Analysis:** `[0]` is a non-empty list (truthy). `"False"` is a non-empty string containing 5 characters (truthy). `-1` is a non-zero integer (truthy).

### Question 2.3
**What does the expression `5 & 3` evaluate to?**
- A) `7`
- B) `1`
- C) `8`
- D) `15`
- **Correct Answer:** **B** `[Reconstructed Key]`
- **Explanation:** Bitwise AND (`&`):
  - `5 = 0b101`
  - `3 = 0b011`
  - `5 & 3 = 0b001 = 1`.
- **Distractor Analysis:** `7` would be bitwise OR (`5 | 3 = 0b111 = 7`). `8` would be addition. `15` would be multiplication.

### Question 2.4
**What is the result of `round(2.5)` and `round(3.5)` in Python 3?**
- A) `3` and `4`
- B) `2` and `4`
- C) `2` and `3`
- D) `3` and `3`
- **Correct Answer:** **B** `[Reconstructed Key]`
- **Explanation:** Python 3 implements "Round Half to Even" (Banker's Rounding) to minimize statistical bias:
  - Halfway cases round to the nearest *even* integer.
  - `2.5` rounds to `2` (even).
  - `3.5` rounds to `4` (even).

### Question 2.5
**What is the difference between `==` and `is`?**
- A) `==` compares object identity; `is` compares values
- B) `==` compares values; `is` compares object identity in memory
- C) They are completely interchangeable synonyms in Python
- D) `==` is for numbers only; `is` is for strings only
- **Correct Answer:** **B** `[Reconstructed Key]`
- **Explanation:** `==` checks value equality (calls `__eq__`), while `is` tests identity (`id(a) == id(b)`), checking whether both operands reference the identical object in memory.

---

## Day 3 Knowledge Check `[Course: IMG-50]`

### Question 3.1
**What is the output of `bool("False")`?**
- A) `False`
- B) `True`
- C) `ValueError`
- D) `None`
- **Correct Answer:** **B**
- **Explanation:** Any non-empty string in Python evaluates to `True` in a boolean context. The string `"False"` has length 5, so `bool("False")` is `True`. Only the empty string `""` evaluates to `False`.

### Question 3.2
**Which statement about the `while ... else` clause is true?**
- A) The `else` block executes whenever the condition was initially `False`.
- B) The `else` block executes only when the loop terminates normally (without hitting `break`).
- C) The `else` block executes only when `break` is encountered.
- D) `else` is invalid syntax after a `while` loop.
- **Correct Answer:** **B**
- **Explanation:** In Python, a loop's `else` block runs if and only if the loop terminates normally by exhausting the condition (for `while`) or iterable (for `for`), and is skipped if the loop exits via `break`.

### Question 3.3
**What does `range(2, 10, 3)` produce when converted to a list?**
- A) `[2, 5, 8]`
- B) `[2, 4, 6, 8, 10]`
- C) `[3, 6, 9]`
- D) `[2, 5, 8, 11]`
- **Correct Answer:** **A**
- **Explanation:** `start = 2`, `stop = 10` (exclusive), `step = 3`.
  - Step 1: `2`
  - Step 2: `2 + 3 = 5`
  - Step 3: `5 + 3 = 8`
  - Next would be `11 >= 10`, so loop stops. Result: `[2, 5, 8]`.

### Question 3.4
**What will `x = 5; print("Yes" if x > 10 else "No")` print?**
- A) `Yes`
- B) `No`
- C) `SyntaxError`
- D) `5`
- **Correct Answer:** **B**
- **Explanation:** The conditional ternary expression evaluates `condition ? true_val : false_val`. Since `x > 10` (`5 > 10`) is `False`, the `else` expression `"No"` is returned.

### Question 3.5
**What is the output of `not 0 and 5`?**
- A) `True`
- B) `5`
- C) `False`
- D) `0`
- **Correct Answer:** **B**
- **Explanation:**
  - Operator precedence: `not` has higher precedence than `and`.
  - `not 0` evaluates to boolean `True`.
  - `True and 5`: short-circuit `and` returns the first falsy operand, or the last operand if all are truthy.
  - Since `True` is truthy, Python evaluates and returns the value `5`.

---

## Day 4 Knowledge Check `[Course: IMG-73]`

### Question 4.1
**What is the output of `"python"[1:4]`?**
- A) `'pyt'`
- B) `'yth'`
- C) `'ytho'`
- D) `'pyth'`
- **Correct Answer:** **B**
- **Explanation:** Slicing is zero-based and stop-exclusive.
  - Index 0: `'p'`
  - Index 1: `'y'` (included)
  - Index 2: `'t'` (included)
  - Index 3: `'h'` (included)
  - Index 4: `'o'` (excluded)
  - Result: `'yth'`.

### Question 4.2
**What does `"hello".find("z")` return?**
- A) `False`
- B) `None`
- C) `-1`
- D) Raises `ValueError`
- **Correct Answer:** **C**
- **Explanation:** `str.find()` returns `-1` when the substring is not found. (Contrast with `str.index()`, which raises `ValueError`).

### Question 4.3
**What does `f"{42:05d}"` produce?**
- A) `'42'`
- B) `'00042'`
- C) `'42000'`
- D) `'   42'`
- **Correct Answer:** **B**
- **Explanation:** `05d` specifies formatting an integer to width 5, padded with leading zeros: `'00042'`.

### Question 4.4
**What is the result of `[x ** 2 for x in range(4) if x % 2 != 0]`?**
- A) `[0, 1, 4, 9]`
- B) `[1, 9]`
- C) `[0, 4]`
- D) `[1, 3]`
- **Correct Answer:** **B**
- **Explanation:**
  - `range(4)` generates `0, 1, 2, 3`.
  - Condition `x % 2 != 0` filters for odd numbers: `1, 3`.
  - Expression `x ** 2`: `1 ** 2 = 1`, `3 ** 2 = 9`.
  - Result: `[1, 9]`.

### Question 4.5
**What happens when `items = [1, 2, 3]; items = items.append(4)` is executed?**
- A) `items` becomes `[1, 2, 3, 4]`
- B) `items` becomes `None`
- C) Raises `AttributeError`
- D) `items` becomes `4`
- **Correct Answer:** **B**
- **Explanation:** The `list.append()` method mutates the list in place and returns `None`. Re-assigning `items = items.append(4)` overwrites `items` with `None`. (The Number One Certification Trap!)

---

## Day 5 Knowledge Check `[Course: D5-05]`

### Question 5.1
**Output of `a = [1, 2, 3]; print(a.append(4))`?**
- A) `[1, 2, 3, 4]`
- B) `4`
- C) `None`
- D) `Error`
- **Correct Answer:** **C**
- **Explanation:** `list.append()` mutates the list in-place and returns `None`. Printing the result prints `None`.
- **Distractor Analysis:** Option A confuses the in-place mutator with an expression that returns a new list. Option B confuses `.append()` with `.pop()`. Option D incorrectly assumes an exception is raised.

### Question 5.2
**Output of `print([1, 2, 3, 4, 5][-3:])`?**
- A) `[3, 4, 5]`
- B) `[1, 2, 3]`
- C) `[4, 5]`
- D) `[3]`
- **Correct Answer:** **A**
- **Explanation:** Negative index `-3` refers to the third element from the end (element `3`). Slicing with `[-3:]` extracts from index `-3` through the end of the list: `[3, 4, 5]`.

### Question 5.3
**With `a = []`, what is `a` after `b = a` and `b.append(1)`?**
- A) `[]`
- B) `[1]`
- C) `None`
- D) `[[1]]`
- **Correct Answer:** **B**
- **Explanation:** Assignment `b = a` creates an alias (both `a` and `b` reference the same list object in memory). Mutating `b.append(1)` mutates the shared list object, so `a` is `[1]`.

### Question 5.4
**What does a function return if it has no return statement?**
- A) `0`
- B) `An empty string`
- C) `It raises an error`
- D) `None`
- **Correct Answer:** **D**
- **Explanation:** In Python, functions without an explicit `return` statement (or with a bare `return`) implicitly return `None`.

### Question 5.5
**Given `def f(a, b=2): return a ** b`, what does `print(f(3), f(b=1, a=4))` show?**
- A) `6 4`
- B) `6 3`
- C) `9 4`
- D) `Error`
- **Correct Answer:** **C**
- **Explanation:**
  - Call 1: `f(3)` uses default `b=2`. Computes `3 ** 2 = 9`.
  - Call 2: `f(b=1, a=4)` uses keyword arguments. Computes `a ** b = 4 ** 1 = 4`.
  - Printed output: `9 4`.

---

## Day 6 Knowledge Check `[Course: D6-11]`

### Question 6.1
**Output of `print([x * x for x in range(5) if x % 2])`?**
- A) `[0, 4, 16]`
- B) `[0, 1, 4, 9, 16]`
- C) `[1, 3]`
- D) `[1, 9]`
- **Correct Answer:** **D**
- **Explanation:** `range(5)` yields `0, 1, 2, 3, 4`. The filter condition `x % 2` evaluates truthiness:
  - `0 % 2 = 0` (falsy)
  - `1 % 2 = 1` (truthy -> `1 * 1 = 1`)
  - `2 % 2 = 0` (falsy)
  - `3 % 2 = 1` (truthy -> `3 * 3 = 9`)
  - `4 % 2 = 0` (falsy)
  - Result: `[1, 9]`.

### Question 6.2
**Output of `print(sorted(["b", "C", "a"]))`?**
- A) `['a', 'b', 'C']`
- B) `['a', 'C', 'b']`
- C) `['b', 'C', 'a']`
- D) `['C', 'a', 'b']`
- **Correct Answer:** **D**
- **Explanation:** Python sorts strings by Unicode / ASCII code point values (`ord()`):
  - `'C'` has ordinal value `67`
  - `'a'` has ordinal value `97`
  - `'b'` has ordinal value `98`
  - Since uppercase characters have smaller ASCII values than lowercase, `'C'` precedes `'a'`, which precedes `'b'`: `['C', 'a', 'b']`.

### Question 6.3
**Inside `def f(*args):`, what type is `args`?**
- A) `list`
- B) `dict`
- C) `tuple`
- D) `set`
- **Correct Answer:** **C**
- **Explanation:** Variable positional arguments prefixed by `*` are packed into an immutable `tuple`.

### Question 6.4
**Which keyword lets an inner function rebind a variable of its enclosing function?**
- A) `global`
- B) `nonlocal`
- C) `outer`
- D) `static`
- **Correct Answer:** **B**
- **Explanation:** The `nonlocal` keyword allows re-binding variables in the nearest enclosing function scope (closures). `global` rebinds in module-level scope. `outer` and `static` are not Python scope keywords.

### Question 6.5
**What does `print((lambda x, y=3: x * y)(4))` print?**
- A) `7`
- B) `43`
- C) `Error`
- D) `12`
- **Correct Answer:** **D**
- **Explanation:** The anonymous lambda takes `x` positionally and `y` defaulting to `3`. Calling it with `4` sets `x=4`, `y=3`. The expression `x * y = 4 * 3 = 12` is returned and printed.
