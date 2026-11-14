# Topic Dependency Map & Reordering Rationale

The original classroom decks split related topics across days and occasionally previewed syntax before its prerequisites were taught. This map defines the **clean study order** used across modules `01`â€“`09`.

---

## 1. Visual Dependency Graph

```text
[01: Foundations & Runtime]
  â”‚  (CPython pipeline, syntax/indentation, venv/pip, print/input)
  â–¼
[02: Types, Variables & Truthiness]
  â”‚  (Naming rules, int/float/complex/bool/None, conversions, == vs is)
  â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â–¼                                              â–¼
[03: Operators & Bitwise]              [06: Strings & Formatting]
  â”‚  (/, //, %, precedence, :=, &, |, ^, ~)       â–²  (Literals, slicing, methods, formatting)
  â–¼                                              â”‚
[04: Conditionals & Logic]                       â”‚
  â”‚  (if/elif/else, ternary, and/or, match-case) â”‚
  â–¼                                              â”‚
[05: Loops & Iteration] â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
  â”‚  (while, for, range, iter/next, break/else, Big-O)
  â–¼
[07: Lists, Structures & Comprehensions]
  â”‚  (Lists, 2D trap, unpacking/deque, shallow/deep copy, comprehensions, generators)
  â–¼
[08: Functions & Scope]  â—„â”€â”€ (Day 5 Agenda `extra` + Lab 5.1)
  â”‚
  â–¼
[09: Supplementary Bridges]
     (Object-reference memory model, module imports, try/except preview)
```

---

## 2. Module-by-Module Prerequisites

| Module | Must Understand First | Unlocks |
|---|---|---|
| **01 Foundations** | None | Running scripts safely, reading tracebacks (`SyntaxError`/`IndentationError`/`TabError`), `input()` returning `str` |
| **02 Types & Truthiness** | `01` (`input()`, `print()`) | Numeric conversions, truthy/falsy rules, `==` vs `is` before conditionals |
| **03 Operators & Bitwise** | `02` (numeric types, `bool`, literals) | Expression evaluation order, negative `//`/`%`, bitwise flags/masks |
| **04 Conditionals & Logic** | `02` (truthiness, `is`), `03` (comparisons, precedence) | Branching, short-circuit defaults, `match-case` |
| **05 Loops & Iteration** | `04` (boolean conditions, `break` logic) | Iteration patterns, `iter()`/`next()`, Big-O, loop traps |
| **06 Strings & Formatting** | `02` (indexing/immutability), `05` (iterating characters) | Text parsing, validation, `%`/`.format()`/f-string formatting |
| **07 Lists & Comprehensions** | `02` (`==` vs `is`), `05` (`for` loops & `iter`), `06` (slicing) | Mutability, aliasing/copying, list/dict/set comprehensions, lazy generators |
| **08 Functions & Scope** | `04` (early returns), `07` (mutable lists & aliasing) | Reusable functions, mutable-default trap, LEGB, object-reference passing |
| **09 Supplementary Bridges** | `02`, `07`, `08` | Connects Week 1 previews (`try/except`, imports, object model) to Week 2â€“3 topics |

---

## 3. Forward-Dependency Collisions Resolved From Slides

1. **Strings Split (`Day 2` + `Day 4`):** `IMG-05` (`Â§2.11â€“2.21`) and `IMG-04`, `IMG-57`â€“`IMG-64` (`Â§5.8â€“5.25`) are unified in Module `06`.
2. **Comprehensions Before Lists (`Day 4` before `Day 5`):** `IMG-54` uses lists, dicts, and sets before Day 5 teaches lists (`IMG-78`). Moving comprehensions into Module `07` after basic list mechanics removes the forward jump.
3. **Previewed Syntax Explained Early/Bridged:**
   - `Day 1` (`IMG-22`) previews f-strings & `ValueError` ("Week 3").
   - `Day 2` (`IMG-07`) uses `if (n := len("hello")) > 3:` before `if` statements.
   - `Day 3` (`IMG-44`) uses `list(filter(bool, items))` and `lst[:]` before lists/slicing.
   - `Day 4` (`IMG-76`) uses `try/except ValueError:` and `IMG-66` uses `dict.get(word, word)` before exceptions or dictionaries.
   - `Day 5` (`IMG-67`) uses `from collections import deque` without an imports lesson.
