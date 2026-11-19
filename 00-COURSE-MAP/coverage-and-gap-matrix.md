# Coverage & Gap Analysis Matrix (Categories A–F)

> **Distinction Rule:** Items marked **[Course Slide]** are directly verified in the presentation decks:
> - Initial 79 screenshots (`IMG-01`–`IMG-79`)
> - Day 5 & Day 6 presentation deck (`D5-01`–`D6-11`)
> - Week 2 Day 8 & Day 9 presentation deck (`D8-01`–`D9-11`, `D5-REV-01`–`D5-REV-09`)
> 
> Items marked **[Supplementary]** are recommended additions to provide architectural depth and resolve syllabus blindspots.

---

## Category A — Covered Adequately `[Course Slide]`

| Topic | Source Screenshots | Target Module | Status |
|---|---|---|:---:|
| Installing Python, REPL vs Script, `print`/`input`, `venv`/`pip` | `IMG-19`, `IMG-21`–`IMG-25` | `01-FOUNDATIONS-AND-ENV` | **100% Complete** |
| Arithmetic (`/`, `//`, `%`), `divmod`, `pow`, Precedence, Bitwise & Flags | `IMG-07`–`IMG-11`, `IMG-13`–`IMG-17` | `03-OPERATORS-AND-BITWISE` | **100% Complete** |
| Comparisons (`==` vs `is`), `if`/`elif`/`else`, Ternary, Short-circuit, `match-case` | `IMG-32`, `IMG-36`–`IMG-38` | `04-CONDITIONALS-AND-LOGIC` | **100% Complete** |
| `while`/`for`, `range`/`enumerate`/`zip`, `break`/`continue`/`pass`/`else`, Classic Programs, Traps | `IMG-39`–`IMG-46` | `05-LOOPS-AND-ITERATION` | **100% Complete** |
| String Methods, `split`/`join`, `%` / `str.format()` / f-strings / Format-Spec | `IMG-01, 02, 04, 05, 57–60, 64, 68–73, 76` + `D5-REV-02, 05, 09` | `06-STRINGS-AND-FORMATTING` | **100% Complete** |
| List Slicing, Methods, 2D Trap, Unpacking/`deque`, Sorting, Comprehensions, Big-O | `IMG-61, 67, 71, 74, 78, 79` + `D6-01`–`D6-09` + `D5-REV-01, 07, 08` | `07-LISTS-STRUCTURES-AND-COMPREHENSIONS` | **100% Complete** |
| Functions, Mutable Default Trap, `*args`/`**kwargs`, LEGB Scope, `nonlocal`, `map`/`filter`/`reduce`, Recursion | `D5-01`–`D5-04` + `D6-06, 07, 10` | `08-FUNCTIONS-AND-SCOPE` | **100% Complete** |
| Tuples, `namedtuple`, Dictionaries, Hashability, Collision Trap, `Counter`/`defaultdict`, Sets, Set Algebra | `D8-01`–`D8-14` | `11-TUPLES-DICTS-AND-SETS` | **100% Complete** |
| Classes, `__init__`, `self`, Method Chaining, Class vs Instance Attributes, Shared Mutable Trap, Dunders, Encapsulation & Mangling, `@property`, UML Class Design, Lifecycle Destructor `__del__` | `D9-01`–`D9-11` + `D9-EXT-01`–`04` | `12-OOP-CLASSES-AND-ENCAPSULATION` | **100% Complete** |
| Inheritance (IS-A), 6 Inheritance Types, `super()` & `__init__`, Method Overriding, Shared Template / Polymorphism, `isinstance`/`issubclass`, MRO (C3 Linearization), ABCs, Mixins, Dataclasses | `D10-01`–`D10-07` | `13-OOP-INHERITANCE-AND-MRO` | **100% Complete** |

---

## Category B — Covered but Strengthened with Supplemental Depth `[Course Slide + Supplementary Depth]`

| Topic | Classroom Coverage | Hardening Added | Target Module |
|---|---|---|:---:|
| CPython execution pipeline (`IMG-56`) | Brief notes + `.py` vs `.pyc` | Parse-time (`SyntaxError`) vs runtime (`ValueError`) failure timeline | `01` |
| IEEE 754 floats & `round()` (`IMG-09, 11, 12`) | Formulas shown without rounding parity | Banker's Rounding (Round-Half-To-Even) and `math.isclose()` | `02` |
| Two's complement `~x` (`IMG-13`) | Formula `~x = -x - 1` without arbitrary precision reason | Infinite sign-bit extension model | `03` |
| Iterator protocol & generator exhaustion (`IMG-54, 55`) | Traversal shown without `__iter__`/`__next__` | Single-pass exhaustion and `itertools` | `05`, `07` |
| Object-reference model & interning (`IMG-32, 64, 79`) | `is` vs `==` shown in isolation | Unified pointer model across ints, strings, lists, tuples | `02`, `07`, `09` |
| Time complexity / Big-O (`IMG-42, 43, 67`, `D6-08`) | Big-O table from class | Underlying contiguous array reallocation & pointer shifting logic | `05`, `07` |
| Function parameter ordering (`D5-03`) | `*args` and `**kwargs` shown | Strict order: positional, `*args`, keyword-only, `**kwargs` | `08` |
| Hashability & collisions (`D8-07`) | `{1: 'a', 1.0: 'b'}` collision | Underlying `hash()` equality and `__eq__()` dual requirement | `11` |
| Name mangling mechanics (`D9-06, D9-11`) | `_Account__balance` shown | Subclass namespace protection vs security misconception | `12` |

---

## Category C — Previously Missing Topics Now Fully Resolved by New Slides

- **Functions & Variable Scope:** Resolved by Day 5 & Day 6 slides (`D5-01`–`D5-04`, `D6-06`, `D6-07`, `D6-10`) -> Integrated into Module `08`.
- **List Methods Table & 2D Grid Trap:** Resolved by review slides (`D5-REV-01`, `D5-REV-07`, `D5-REV-08`) -> Integrated into Module `07`.
- **String Formatting Answers & Explanations:** Resolved by slide 16 (`D5-REV-05`) -> Integrated into Module `06` and `10-EXAM-PREPARATION`.
- **Tuples, Namedtuples, Dictionaries, Sets:** Resolved by Day 8 slides (`D8-01`–`D8-14`) -> Integrated into Module `11`.
- **OOP Classes, Instances, Attributes, Dunders, Encapsulation, Properties, UML, Lifecycle:** Resolved by Day 9 slides (`D9-01`–`D9-11`, `D9-EXT-01`–`04`) -> Integrated into Module `12`.
- **Inheritance, `super()`, MRO & C3 Linearization, Abstract Base Classes, Dataclasses:** Resolved by Day 10 slides (`D10-01`–`D10-07`) -> Integrated into Module `13`.

---

## Category D & E — Remaining Advanced Bridges (Days 11–14 Preview)

- **File I/O & Context Managers (`with open(...)`):** Standard library file operations (Week 2 Day 11+).
- **Advanced Decorators & Closures:** Previewed on Day 9 slide `D9-10` ("@property is a decorator — Day 11 shows how decorators work").
- **Package Architecture & `__init__.py`:** Multi-file packaging and distribution.

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
