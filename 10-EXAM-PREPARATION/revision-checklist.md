# Certification Revision & Readiness Checklist

> **BCPD Python Cohort 2 Certification Preparation**  
> Use this checklist for structured pre-exam self-assessment. Check off each concept only when you can explain it to another developer and write the syntax from memory.

---

## 1. Foundations, Environment & Tooling `[Module 01]`
- [ ] Understand the CPython execution pipeline: Source `.py` âž” Compiler âž” Bytecode `.pyc` âž” PVM. `[IMG-56, IMG-11]`
- [ ] Know how to create, activate, and isolate virtual environments using `python -m venv <dir>`. `[IMG-06]`
- [ ] Know how to export and install dependencies with `pip freeze > requirements.txt` and `pip install -r`.
- [ ] Memorize core PEP 8 style rules: 4-space indentation, snake_case for functions/variables, UPPER_CASE for constants, PascalCase for classes. `[IMG-09]`
- [ ] Remember that `input()` always returns a `str` and requires explicit casting for numeric operations. `[IMG-05]`

---

## 2. Types, Variables, and Truthiness `[Module 02]`
- [ ] State the 4 primitive types: `int`, `float`, `str`, `bool`. `[IMG-07]`
- [ ] Explain Python's dynamic typing and how variables are pointers to heap objects. `[IMG-15]`
- [ ] Differentiate base representations: Binary (`0b`), Octal (`0o`), Hexadecimal (`0x`). `[IMG-07]`
- [ ] Explain Banker's Rounding (Round Half to Even) and predict `round(2.5)` vs `round(3.5)`. `[IMG-10]`
- [ ] List all falsy values in Python (`0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`, `False`). `[IMG-32]`
- [ ] Distinguish `==` (value equality) from `is` (identity / same memory address). `[IMG-15]`

---

## 3. Operators, Precedence, and Bitwise `[Module 03]`
- [ ] Differentiate `/` (true float division) and `//` (floor division towards negative infinity). `[IMG-08]`
- [ ] Predict modulo with negative operands (`-17 % 5 = 3`) using `a % b = a - (a // b) * b`. `[IMG-08]`
- [ ] Master precedence traps: `-2 ** 4 = -16` (exponentiation before unary minus); `2 ** 3 ** 2 = 512` (right-associative). `[IMG-08]`
- [ ] Calculate bitwise operations mentally: `&`, `|`, `^`, `~` (`~x = -x - 1`), `<<`, `>>`. `[IMG-13, IMG-14]`
- [ ] Implement and test permission bitmasks (READ=1, WRITE=2, EXEC=4): check with `&`, toggle with `^`, clear with `&= ~`. `[IMG-18, IMG-20]`
- [ ] Use the walrus operator `:=` for assignment inside expressions. `[IMG-10]`

---

## 4. Conditionals and Logical Control `[Module 04]`
- [ ] Master short-circuit evaluation of `and` and `or`: know which operand is returned. `[IMG-32, IMG-40]`
- [ ] Write ternary conditional expressions: `val = x if condition else y`. `[IMG-36]`
- [ ] Predict chained comparisons: `1 < x < 10` is equivalent to `(1 < x) and (x < 10)`. `[IMG-36]`
- [ ] Understand structural pattern matching (`match ... case`) introduced in Python 3.10. `[IMG-38]`

---

## 5. Loops, Iteration, and Complexity `[Module 05]`
- [ ] Know how `range(start, stop, step)` operates and that `stop` is always exclusive. `[IMG-41]`
- [ ] Use `enumerate(seq, start=0)` to track index and value simultaneously without manual counters. `[IMG-44]`
- [ ] Use `zip()` to iterate through parallel sequences and know that it terminates at the shortest sequence. `[IMG-44]`
- [ ] Understand loop `else`: executes only if loop finishes normally, skipped if terminated via `break`. `[IMG-43, IMG-50]`
- [ ] Analyze time and space complexity ($O(1)$, $O(n)$, $O(n^2)$) of loops and nested loops. `[IMG-48, IMG-55]`

---

## 6. Strings, Formatting, and Text Processing `[Module 06]`
- [ ] Use 0-based and -1 based indexing, and slicing `[start:stop:step]` including reversal `[::-1]`. `[IMG-57, IMG-58]`
- [ ] Recall that slice out-of-bounds returns `""`, while direct index out-of-bounds raises `IndexError`.
- [ ] Recognize that strings are immutable and all methods (`upper()`, `replace()`, etc.) return *new* strings. `[IMG-59/64]`
- [ ] Distinguish `find()` (returns `-1`) from `index()` (raises `ValueError`). `[IMG-59/64, IMG-73]`
- [ ] Differentiate `isdecimal()`, `isdigit()`, and `isnumeric()` on fractions (`Â½`) and superscripts (`Â²`). `[IMG-76]`
- [ ] Master f-string mini-language: alignment (`<`, `>`, `^`), padding (`*^10`), currency commas (`,`), precision (`.2f`). `[IMG-68/72, IMG-73]`

---

## 7. Lists, Structures, and Comprehensions `[Module 07]`
- [ ] Identify in-place mutators returning `None` (`sort()`, `append()`, `reverse()`, `extend()`). `[IMG-67, IMG-70]`
- [ ] Avoid the 2D reference multiplication trap: never write `[[0]*3]*3`; use `[[0]*3 for _ in range(3)]`. `[IMG-70, IMG-74]`
- [ ] Use extended star unpacking: `first, *middle, last = data`. `[IMG-77]`
- [ ] Understand aliasing vs shallow copy (`copy()`) vs deep copy (`deepcopy()`). `[IMG-74, IMG-78]`
- [ ] Construct list, dict, and set comprehensions. `[IMG-71, IMG-74, IMG-78, IMG-79]`
- [ ] Explain generator expression lazy evaluation and one-shot exhaustion. `[IMG-78, IMG-79]`

---

## 8. Functions, Scope, and Parameters `[Module 08]`
- [ ] Identify and fix the mutable default argument trap (`def f(x, l=[])`). `[IMG-75]`
- [ ] Use variable arguments `*args` (tuple) and `**kwargs` (dict). `[IMG-75]`
- [ ] Understand positional-only (`/`) and keyword-only (`*`) parameter delimiters.
- [ ] Trace variable lookup through LEGB scopes (Local, Enclosing, Global, Built-in).
- [ ] Explain `global` and `nonlocal` declarations and what triggers `UnboundLocalError`.
- [ ] Write anonymous `lambda` functions for custom sorting keys.

---

## 9. Object Model, Modules, and Exceptions `[Module 09]`
- [ ] Explain small integer caching `[-5, 256]` and string interning.
- [ ] Understand how Python searches `sys.path` on `import`.
- [ ] Explain the `if __name__ == "__main__":` idiom.
- [ ] Write full exception handling suites: `try`, `except`, `else`, `finally`. `[IMG-22, IMG-45]`
- [ ] Know that `finally` runs even when `try` or `except` executes a `return`.
