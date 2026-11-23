# Topic Dependency Map & Reordering Rationale

The original classroom decks split related topics across days and occasionally previewed syntax before its prerequisites were taught. This map defines the **clean study order** used across modules `01`–`12`.

---

## 1. Visual Dependency Graph

```text
[01: Foundations & Runtime]
  │  (CPython pipeline, syntax/indentation, venv/pip, print/input)
  ▼
[02: Types, Variables & Truthiness]
  │  (Naming rules, int/float/complex/bool/None, conversions, == vs is)
  ├─────────────────────────────────────────────┐
  ▼                                              ▼
[03: Operators & Bitwise]              [06: Strings & Formatting]
  │  (/, //, %, precedence, :=, &, |, ^, ~)       ▲  (Literals, slicing, methods, formatting)
  ▼                                              │
[04: Conditionals & Logic]                       │
  │  (if/elif/else, ternary, and/or, match-case) │
  ▼                                              │
[05: Loops & Iteration] ─────────────────────────┘
  │  (while, for, range, iter/next, break/else, Big-O)
  ▼
[07: Lists, Structures & Comprehensions]
  │  (Lists, 2D trap, unpacking/deque, shallow/deep copy, comprehensions, Big-O)
  ▼
[08: Functions & Scope]
  │  (def/calls, mutable defaults, *args/**kwargs, LEGB, nonlocal, map/filter/reduce, recursion)
  ▼
[09: Supplementary Bridges]
  │  (Object-reference memory model, module imports, try/except/finally)
  ├─────────────────────────────────────────────┐
  ▼                                              ▼
[11: Tuples, Dicts & Sets]             [12: OOP Classes & Encapsulation]
  │  (Tuples, namedtuple, dicts, hashability,     │  (__init__, self, methods, class vs instance,
  │   collision trap, Counter, set algebra)       │   shared mutable trap, dunders, @property, UML)
  │                                              ▼
  │                                    [13: OOP Inheritance & MRO]
  │                                       (IS-A, super(), overriding, MRO/C3,
  │                                        isinstance vs type, ABCs, dataclasses)
  │                                              ▼
  │                                    [14: OOP Polymorphism & Design]
  │                                       (Duck typing, operator overloading,
  │                                        singledispatch, __slots__, SRP, Matrix)
  └──────────────────────┬───────────────────────┘
                         ▼
        [15: Modules, sys, math & random]
           (Import styles, sys.modules, sys.path,
            sys runtime, math favourites, random vs secrets)
                         ▼
        [10: Central Exam Preparation Hub]
           (55 MCQs, 59 Traps, 7 Drills, Solutions)
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
| **09 Supplementary Bridges** | `02`, `07`, `08` | Connects Week 1 previews (`try/except`, imports, object model) to Week 2 topics |
| **11 Tuples, Dicts & Sets** | `02` (hashability, immutability), `07` (sequences), `08` (functions) | Fast lookups, multiset counts (`Counter`), set algebra, structure selection |
| **12 OOP & Encapsulation** | `08` (functions & scope), `09` (namespaces & exception objects) | Custom data modeling, instance vs class attributes, dunders, private mangling, properties, UML design, lifecycle |
| **13 OOP Inheritance & MRO** | `12` (classes & instances) | Subclassing, parent calls (`super()`), method overriding, shared templates, MRO / C3 linearization, ABCs, dataclasses |
| **14 OOP Polymorphism & Design** | `12`, `13` | Duck typing, operator overloading (`__rmul__`), `@singledispatch`, `__slots__`, SRP, LSP, Matrix class |
| **15 Modules, sys, math & random** | `08` (functions), `12` (classes) | Import styles, `sys.modules`, `sys.path`, CLI parsing, `math` precision, `random` vs `secrets`, Lab 13.1 |
| **10 Exam Prep Hub** | `01`–`09`, `11`–`15` | Comprehensive exam readiness: 55 MCQs, 59 traps, 7 tracing drills, checklists |

---

## 3. Forward-Dependency Collisions Resolved From Slides

1. **Strings Split (`Day 2` + `Day 4`):** `IMG-05` (`§2.11–2.21`) and `IMG-04`, `IMG-57`–`IMG-64` (`§5.8–5.25`) are unified in Module `06`.
2. **Comprehensions Before Lists (`Day 4` before `Day 5`):** `IMG-54` uses lists, dicts, and sets before Day 5 teaches lists (`IMG-78`). Moving comprehensions into Module `07` after basic list mechanics removes the forward jump.
3. **Tuples, Dictionaries & Sets (`Day 8`):** Fully isolated into dedicated Module `11` with detailed coverage of `namedtuple`, hash collisions, `Counter`, and set algebra.
4. **OOP & Encapsulation (`Day 9`):** Fully established as Module `12` providing the object model foundation before Day 10–11 inheritance and polymorphism.
5. **OOP Inheritance & MRO (`Day 10`):** Structured as Module `13` covering Manual Day 11 (§11.1–11.10), resolving multiple inheritance, MRO linearization, and abstract interfaces.
6. **OOP Polymorphism & Design (`Day 11`):** Structured as Module `14` covering Manual Day 12 (§12.1–12.6) + Day 13 (§13.1–13.5), mastering dynamic polymorphism, dunder arithmetic protocols, memory-efficient slotted structures, and clean architecture.
7. **Modules Part 1: Imports, `sys`, `math` & `random` (`Day 13`):** Structured as Module `15` covering Manual Day 14 (§14.1–14.6) for Domain 4 (15% exam weight), mastering module resolution, caching, math precision, and random generation.
