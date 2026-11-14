# Coverage & Gap Analysis Matrix (Categories Aâ€“F)

> **Distinction Rule:** Items marked **[Course Slide]** are verified in the 79 screenshots. Items marked **[Supplementary]** are recommended additions to resolve conceptual gaps or uncaptured syllabus items; we do **not** claim to know exact official BCPD exam questions beyond what appears in your slides (`IMG-56`, `IMG-26`, `IMG-29`, `IMG-30`, `IMG-47`, `IMG-51`, `IMG-63`, `IMG-65`, and Sanfoundry sets in `IMG-31`, `IMG-49`).

---

## Category A â€” Covered Adequately `[Course Slide]`

| Topic | Source Screenshots | Target Module |
|---|---|---|
| Installing Python, REPL vs Script, `print`/`input`, `venv`/`pip` | `IMG-19`, `IMG-21`â€“`IMG-25` | `01-FOUNDATIONS-AND-ENV` |
| Arithmetic (`/`, `//`, `%`), `divmod`, `pow`, Precedence, Bitwise & Flags | `IMG-07`â€“`IMG-11`, `IMG-13`â€“`IMG-17` | `03-OPERATORS-AND-BITWISE` |
| Comparisons (`==` vs `is`), `if`/`elif`/`else`, Ternary, Short-circuit, `match-case` | `IMG-32`, `IMG-36`â€“`IMG-38` | `04-CONDITIONALS-AND-LOGIC` |
| `while`/`for`, `range`/`enumerate`/`zip`, `break`/`continue`/`pass`/`else`, Classic Programs, Traps | `IMG-39`â€“`IMG-46` | `05-LOOPS-AND-ITERATION` |
| String Methods, `split`/`join`, `%` / `str.format()` / f-strings / Format-Spec | `IMG-01`, `IMG-02`, `IMG-04`, `IMG-05`, `IMG-57`â€“`IMG-60`, `IMG-64`, `IMG-68`â€“`IMG-73`, `IMG-76` | `06-STRINGS-AND-FORMATTING` |
| List Slicing, Methods, 2D Trap, Unpacking/`deque`, Shallow vs Deep Copy | `IMG-61`, `IMG-67`, `IMG-71`, `IMG-74`, `IMG-78`, `IMG-79` | `07-LISTS-STRUCTURES-AND-COMPREHENSIONS` |

---

## Category B â€” Covered but Poorly Explained `[Course Slide + Supplementary Depth]`

| Topic | What's Missing in Slides | Why It Matters | Target Module |
|---|---|---|---|
| CPython execution pipeline (`IMG-56`) | Brief notes only + `.py` vs `.pyc` typo | Explains parse-time (`SyntaxError`) vs runtime (`ValueError`) failures | `01` |
| IEEE 754 floats & `round()` (`IMG-09, 11, 12`) | Why `0.1 + 0.2 != 0.3` and `round(2.675, 2) == 2.67` | Prevents memorization mistakes on float output MCQs | `02` |
| Two's complement `~x` (`IMG-13`) | Formula `-x - 1` stated without arbitrary-precision sign-bit reason | Beginners wrongly expect `~0b1100` -> `0b0011` (`3`) | `03` |
| Iterator protocol & generator exhaustion (`IMG-54, 55`) | `sum(gen), sum(gen) -> 91 0` without `__iter__`/`__next__` model | Crucial for predicting single-pass iterator exhaustion | `05`, `07` |
| Object-reference model & interning (`IMG-32, 64, 79`) | `is` vs `==` and aliasing shown separately without unified memory model | Connects `a = a.sort()`, `shallow` copy, and `is` traps | `02`, `07`, `09` |
| Time complexity / Big-O (`IMG-42, 43, 67`) | Labels (`O(n)`, `O(n^2)`, `pop(0) is O(n)`) without array-shift reasoning | Needed to justify `deque.popleft()` and prime `sqrt(n)` loop bound | `05`, `07` |

---

## Category C â€” Mentioned but Not Developed

- **Variables & Core Types (`Â§2.1â€“2.5`):** Mentioned in `IMG-30` Q1 & `IMG-31`; slides missing -> *include in `02`*.
- **`match-case` Bare-Name Capture Trap (`IMG-38`):** Only positive examples shown -> *include in `04`*.
- **`filter(bool, items)` (`IMG-44`):** Used without explaining lazy filter objects -> *include in `05`*.
- **Dictionaries & Sets (`IMG-54, 66`):** Used in comprehensions & `dict.get()` without foundational slides -> *include primer in `07`*.
- **`try/except` & Imports (`IMG-02, 11, 22, 45, 67, 76, 79`):** Previewed without lessons -> *bridge in `09`*.
- **Day 5 Function Topics (`IMG-75`):** 6 `extra` topics + Lab 5.1 listed on agenda, 0 slides captured -> *build `[Agenda-Mapped / Supplementary]` in `08`*.

---

## Category D & E â€” Not Covered: Foundational & Exam-Relevant `[Recommended Supplementary]`

- **D (Foundational):** Name-binding vs object mutation; `None` type & implicit `None` returns; `Sequence` vs `Iterable` vs `Mapping`; `tuple` basics including 1-element trailing comma `(5,)`.
- **E (Potentially Exam-Relevant):** Dictionaries/Sets operations & hashability; Functions/Scope (`08`); Exception hierarchy & `try/except/else/finally/raise` (`09` preview, pending Week 2â€“3 screenshots for File I/O, Modules, OOP).

---

## Category F â€” High-Yield Examination Traps (`10-EXAM-PREPARATION`)

1. `n = 1,000,000` creating tuple `(1, 0, 0)` (`IMG-09`)
2. `-2 ** 2 == -4` and right-associative `2 ** 3 ** 2 == 512` (`IMG-10`, `IMG-30`)
3. `-7 // 2 == -4`, `-7 % 3 == 2`, `-20 // 3 == -7`, `-20 % 3 == 1` (`IMG-07`, `IMG-08`)
4. `0.1 + 0.2 == 0.3` (`False`), `round(2.5) == 2`, `round(2.675, 2) == 2.67` (`IMG-09`, `IMG-11`, `IMG-12`)
5. `int("2.5")` (`ValueError`), `int(5, 2)` (`TypeError`), `09` (`SyntaxError`) (`IMG-06`, `IMG-12`)
6. `bool("0") == True`, `bool(" ") == True`, `bool([0]) == True` (`IMG-12`, `IMG-30`)
7. `0 or [] or "x"` returning `"x"` and `5 and 10` returning `10` (`IMG-37`, `IMG-47`)
8. `not 1 == 2` evaluating as `not (1 == 2)` -> `True` (`IMG-44`)
9. `a == b` vs `a is b`, `"Z" < "a"` (`True`), string interning (`IMG-32`, `IMG-64`)
10. `1 + 2 << 1 == 6` (`+` binds tighter than `<<`) & `~12 == -13` (`IMG-13`, `IMG-14`)
11. `range(n)` built once at loop start; `i += 10` overwritten next pass; `break` skips `else` (`IMG-41`, `IMG-44`)
12. `"xyzzy".lstrip("xy") == "zzy"`, `"they're".title() == "They'Re"`, `"-42".zfill(5) == "-0042"`, `"hi".center(7, "*") == "***hi**"`, `"a\tb".expandtabs(4) == "a   b"` (`IMG-60`)
13. `"class".isidentifier() == True`, `"Â½".isnumeric() == True` vs `isdigit() == False`, `"{} {0}".format(1, 2)` -> `ValueError` (`IMG-76`)
14. `sum(gen), sum(gen) -> 91 0` (exhaustion) (`IMG-54`)
15. `a = a.sort()` overwriting `a` with `None` (`IMG-71`)
16. `[[0] * 3] * 3` row aliasing & `a.copy()` sharing nested lists (`IMG-74`, `IMG-79`)
