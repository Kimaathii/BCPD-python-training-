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

## Day 4 Knowledge Check `[Course: IMG-73, D5-REV-05]`

> [!NOTE]
> Slide 16 of the Day 4 Strings deck (`D5-REV-05`, `WhatsApp Image 2026-11-17 at 21.28.20okl.jpeg`) provides the official classroom answer key and explanations directly from the instructor.

### Question 4.1
**What does `"hello".find("z")` return when the character is absent?**
- A) `False`
- B) `None`
- C) `-1`
- D) Raises `ValueError`
- **Correct Answer:** **C** `[Course: D5-REV-05]`
- **Official Explanation:** `find()` returns `-1` when the substring is missing; `index()` would raise `ValueError`.

### Question 4.2
**What is the result of formatting `3.14159` with specifier `%.2f` or `{:.2f}`?**
- A) `'3.14'`
- B) `'3.1'`
- C) `'3.141'`
- D) `'3.15'`
- **Correct Answer:** **A** `[Course: D5-REV-05]`
- **Official Explanation:** `.2f` rounds to two decimal places, producing `'3.14'`.

### Question 4.3
**What does `"-".join(["a", "b", "c"])` produce?**
- A) `'-a-b-c-'`
- B) `'-a-b-c'`
- C) `'a-b-c-'`
- D) `'a-b-c'`
- **Correct Answer:** **D** `[Course: D5-REV-05]`
- **Official Explanation:** The separator goes between items, not at the ends.

### Question 4.4
**What is the output of `f"{2.345:>5.1f}|"`?**
- A) `'2.345|'`
- B) `'  2.3|'`
- C) `'002.3|'`
- D) `'2.3  |'`
- **Correct Answer:** **B** `[Course: D5-REV-05]`
- **Official Explanation:** Width 5 pads on the left; 1 decimal place gives `'  2.3|'`.

### Question 4.5
**Which method call returns `True`?**
- A) `"".isalpha()`
- B) `"".isalnum()`
- C) `"A1".isalnum()`
- D) `"12 34".isdigit()`
- **Correct Answer:** **C** `[Course: D5-REV-05]`
- **Official Explanation:** `"A1"` is all letters and digits; the `is...` methods return `False` for the empty string `""` and spaces.

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

---

## Day 8 Knowledge Check: Tuples, Dictionaries & Sets `[Course: D8-01 to D8-14]`

### Question 8.1
**What is the output of `print(type((5)), type((5,)))`?**
- A) `<class 'tuple'> <class 'tuple'>`
- B) `<class 'int'> <class 'tuple'>`
- C) `<class 'int'> <class 'int'>`
- D) `TypeError`
- **Correct Answer:** **B** `[Course: D8-03]`
- **Explanation:** In Python, parentheses around a single expression without a comma are evaluated as mathematical grouping. Therefore, `(5)` is an integer. A trailing comma is required to form a single-element tuple: `(5,)`.

### Question 8.2
**What is the result of evaluating `len({1: "a", 1.0: "b"})`?**
- A) `2`
- B) `1`
- C) `0`
- D) Raises `KeyError`
- **Correct Answer:** **B** `[Course: D8-07]`
- **Explanation:** In Python, integer `1` and float `1.0` compare as equal (`1 == 1.0` is `True`) and yield identical hash values (`hash(1) == hash(1.0)`). Dictionaries key off hash and value equality, so key `1.0` overwrites key `1` in-place, leaving a dictionary of length `1`: `{1: 'b'}`.

### Question 8.3
**Given `d = dict.fromkeys("ab", [])` followed by `d["a"].append(1)`, what is `d["b"]`?**
- A) `[]`
- B) `[1]`
- C) `None`
- D) Raises `KeyError`
- **Correct Answer:** **B** `[Course: D8-05]`
- **Explanation:** `dict.fromkeys(keys, default)` associates the *exact same default object reference* with every key. Appending `1` to `d["a"]` mutates the single shared list instance, which is also accessed via `d["b"]`.

### Question 8.4
**Which statement regarding set operators versus set methods is TRUE?**
- A) Bitwise operators like `|` and `&` accept any iterable on the right-hand side.
- B) Set methods like `.union()` and `.intersection()` accept any iterable argument.
- C) `{1, 2} | [3, 4]` returns `{1, 2, 3, 4}`.
- D) `{1, 2} + {3, 4}` creates a combined set.
- **Correct Answer:** **B** `[Course: D8-14]`
- **Explanation:** Set methods (such as `s.union([3, 4])`) accept any iterable. In contrast, bitwise set operators (`|`, `&`, `-`, `^`) require both operands to be sets, otherwise raising `TypeError`. Sets do not support `+`.

### Question 8.5
**Given `c1 = Counter("aab")` and `c2 = Counter("abb")`, what is `c1 | c2`?**
- A) `Counter({'a': 3, 'b': 3})`
- B) `Counter({'a': 1, 'b': 1})`
- C) `Counter({'a': 2, 'b': 2})`
- D) `Counter({'a': 0, 'b': 0})`
- **Correct Answer:** **C** `[Course: D8-08]`
- **Explanation:** The union operator `|` on `Counter` objects computes the multiset union, which takes the **maximum** count for each key: `max(2, 1) = 2` for `'a'`, and `max(1, 2) = 2` for `'b'`, resulting in `Counter({'a': 2, 'b': 2})`. (Intersection `&` takes the minimum).

---

## Day 9 Knowledge Check: OOP Classes & Encapsulation `[Course: D9-01 to D9-11]`

### Question 9.1
**What happens when `a.species = "wolf"` is executed on an instance `a` of class `Dog` where `Dog.species = "Canis familiaris"`?**
- A) `Dog.species` is changed to `"wolf"` for all dogs.
- B) An instance attribute `species` is created on `a`; `Dog.species` remains `"Canis familiaris"`.
- C) Raises `AttributeError: read-only attribute`.
- D) Raises `TypeError`.
- **Correct Answer:** **B** `[Course: D9-08]`
- **Explanation:** Attribute assignment through an instance (`a.attr = val`) writes directly to that instance's namespace (`a.__dict__`). It shadows the class attribute for instance `a` while leaving the class-level attribute `Dog.species` unchanged.

### Question 9.2
**Given class `class Clicker: def ping(): return 1`, what occurs when calling `c = Clicker(); c.ping()`?**
- A) Returns `1`.
- B) Raises `TypeError: Clicker.ping() takes 0 positional arguments but 1 was given`.
- C) Raises `NameError: ping is not defined`.
- D) Raises `AttributeError`.
- **Correct Answer:** **B** `[Course: D9-09]`
- **Explanation:** Calling `c.ping()` passes instance `c` as the first argument automatically. Because `ping` was defined without the `self` parameter, Python raises `TypeError`.

### Question 9.3
**In the class below, why do all instances share the same `tricks` list?**
```python
class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
```
- A) Because Python lists are always global.
- B) Because `tricks` is declared at the class level, making it a shared class attribute across all instances.
- C) Because `name` was not passed to `tricks`.
- D) It does not share; each instance gets an independent copy.
- **Correct Answer:** **B** `[Course: D9-08]`
- **Explanation:** Any mutable object declared in the class body belongs to the class namespace and is shared among all instances. To give each object its own list, it must be initialized on `self` inside `__init__`: `self.tricks = []`.

### Question 9.4
**Which dunder method provides an unambiguous, developer-facing representation of an object (typically used in the REPL)?**
- A) `__str__`
- B) `__len__`
- C) `__repr__`
- D) `__name__`
- **Correct Answer:** **C** `[Course: D9-07]`
- **Explanation:** `__repr__` is intended for developers and debugging (unambiguous, ideally executable code). `__str__` is intended for readable user-facing output (`print()`).

### Question 9.5
**In Python, how is an attribute defined as `self.__balance` internally stored by the compiler to prevent accidental overrides?**
- A) It is stored in a hidden hardware register.
- B) It is name-mangled to `_ClassName__balance`.
- C) It is encrypted with AES-256 in memory.
- D) It is discarded when `__init__` completes.
- **Correct Answer:** **B** `[Course: D9-06, D9-11]`
- **Explanation:** Any identifier with two or more leading underscores (and at most one trailing underscore) undergoes private name mangling, being rewritten internally as `_ClassName__attributeName`.

