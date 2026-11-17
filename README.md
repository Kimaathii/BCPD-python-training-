# BCPD Python Certification — Structured Learning & Exam Prep System

Welcome to your reconstructed, exam-focused Python learning environment built from your **BCPD Cohort 2** classroom materials (`Week 1 & Week 2, Days 1–9`).

> **Preservation Guarantee:** All concepts, code snippets, and quizzes from the initial 79 classroom slides, Day 5 & 6 slides, and newly added Week 2 Day 8 & Day 9 slides (`Monday 16 Nov 2026` & `Tuesday 17 Nov 2026`) are 100% extracted, verified, and preserved with complete provenance citations.

---

## How to Study With This System

1. **Follow the Dependency Order (`01` → `12`)**, not the fragmented slide capture order.
   - Read each module's `README.md` first (conceptual foundation → mental models → original vs. corrected code → line-by-line walkthrough → step-by-step tracing → pitfalls → MCQs).
2. **Run and Modify `examples.py`** in each module (`Python 3.10+` required for `f"{x=}"`, `match-case`, and union type hints).
   - Classroom code is always preserved verbatim as `ORIGINAL CLASSROOM CODE`; fixed or guarded versions are kept separate as `CORRECTED / IMPROVED CODE`.
3. **Attempt `exercises.py` Before Checking Solutions.**
   - Every module has progressive Level 1–4 exercises. Solutions are stored separately under `10-EXAM-PREPARATION/solutions/` so you test your own reasoning first.
4. **Drill Exam Traps (`10-EXAM-PREPARATION/`).**
   - Review the instructor's Knowledge Checks (Days 1–9), output-prediction sheets, common-mistakes cheat sheet, and 40+ MCQ traps.

---

## Provenance Tags Used Everywhere

| Tag | Meaning |
|---|---|
| `[Course: IMG-XX]` | Directly verified from initial classroom deck `IMG-01`–`IMG-79` (see [Screenshot Inventory](./00-COURSE-MAP/screenshot-inventory.md)) |
| `[Course: D5-XX / D6-XX]` | Directly verified from the Day 5 & Day 6 presentation deck (see [Day 5 & 6 Inventory](./00-COURSE-MAP/day5-day6-new-inventory.md)) |
| `[Course: D8-XX / D9-XX]` | Directly verified from Week 2 Day 8 & Day 9 presentation deck (see [Day 8 & 9 Inventory](./00-COURSE-MAP/day8-day9-new-inventory.md)) |
| `[Course: D5-REV-XX]` | Directly verified from List methods, grid 2D trap, and string formatting review slides |
| `[Reconstructed Key]` | Verified answer key reconstructed where the instructor's Answers slide was missing (Day 2 Knowledge Check, `IMG-30`) |
| `[Supplementary]` | Foundational explanation, edge case, or exam-style drill added to resolve a gap or blindspot |

---

## System Map & Extraction Progress Tracker

| Module / Hub | Focus | Source Coverage | Build Status |
|---|---|---|---|
| [00-COURSE-MAP](./00-COURSE-MAP/screenshot-inventory.md) | Master inventories (`79` initial + `16` Day 5/6 + `34` Day 8/9 files), Day 1–9 outline, dependency graph | `IMG-01`–`IMG-79`, `D5-01`–`D6-11`, `D8-01`–`D9-11` | **Complete** |
| [01-FOUNDATIONS-AND-ENV](./01-FOUNDATIONS-AND-ENV/README.md) | BCPD overview, CPython pipeline, `venv`/`pip`, PEP 8, `print`/`input`, Lab 1 | Day 1 + `IMG-56` | **Complete** |
| [02-TYPES-VARIABLES-AND-TRUTHINESS](./02-TYPES-VARIABLES-AND-TRUTHINESS/README.md) | Naming, bases/conversions, floats/`round()`, truthiness, `==` vs `is` | Day 2 (`§2.1–2.8, §2.26–2.31`) + `IMG-32` | **Complete** |
| [03-OPERATORS-AND-BITWISE](./03-OPERATORS-AND-BITWISE/README.md) | Arithmetic (`/`, `//`, `%`), precedence, `:=`, bitwise & flags, Lab 2.1 | Day 2 (`§2.22–2.29`, Beyond Manual) | **Complete** |
| [04-CONDITIONALS-AND-LOGIC](./04-CONDITIONALS-AND-LOGIC/README.md) | Comparisons, `if`/`elif`/`else`, ternary, short-circuit, `match-case` | Day 3 (`§3.2–3.20`) | **Complete** |
| [05-LOOPS-AND-ITERATION](./05-LOOPS-AND-ITERATION/README.md) | `while`, `for`, `range`/`enumerate`/`zip`, `iter`/`next`, loop `else`, Big-O, traps, Lab 3 | Day 3 (`§4.1–4.27`) + `IMG-55` | **Complete** |
| [06-STRINGS-AND-FORMATTING](./06-STRINGS-AND-FORMATTING/README.md) | Literals/escapes/slicing, methods, `is...`, `%`/`format()`/f-strings, interning, Lab 4.1 | Day 2 (`§2.11–2.21`) + Day 4 (`§5.8–5.25`) + `D5-REV-02, 09` | **Complete** |
| [07-LISTS-STRUCTURES-AND-COMPREHENSIONS](./07-LISTS-STRUCTURES-AND-COMPREHENSIONS/README.md) | Lists, methods, `sorted()` vs `.sort()`, 2D trap, `combine.py`, `gotchas.py`, Big-O costs, comprehensions | Day 4 (`§5.1–5.6`), Day 5 (`§6.1–6.6`), Day 6 (`§7.1–7.5`) + `D5-REV-01, 07, 08` | **Complete** |
| [08-FUNCTIONS-AND-SCOPE](./08-FUNCTIONS-AND-SCOPE/README.md) | `def`/calls, mutable default trap, `*args`/`**kwargs`, LEGB, `nonlocal`, `map`/`filter`/`reduce`, recursion | Day 5 (`functions.py`, `defaults.py`, `varargs.py`, `scope.py`) + Day 6 (`functional.py`, `recursion.py`) | **Complete** |
| [09-SUPPLEMENTARY-BRIDGES](./09-SUPPLEMENTARY-BRIDGES/README.md) | Object-reference model, module imports, `try`/`except` Week 1–3 bridge | Previewed across `IMG-02, 11, 22, 45, 67, 76, 79` | **Complete** |
| [11-TUPLES-DICTS-AND-SETS](./11-TUPLES-DICTS-AND-SETS/README.md) | Tuples, `namedtuple`, dicts, hashability, collision trap, `Counter`/`defaultdict`, set algebra, selection matrix | Day 8 (`§8.1–8.8`, `§9.1–9.9`) + `D8-01` to `D8-14` | **Complete** |
| [12-OOP-CLASSES-AND-ENCAPSULATION](./12-OOP-CLASSES-AND-ENCAPSULATION/README.md) | Classes, `__init__`, `self`, methods, class vs instance attributes, shared mutable trap, dunders, encapsulation, `@property` | Day 9 (`§10.1–10.10`) + `D9-01` to `D9-11` | **Complete** |
| [10-EXAM-PREPARATION](./10-EXAM-PREPARATION/instructor-knowledge-checks.md) | Knowledge Checks, MCQ trap bank, output drills, mistakes cheat sheet, checklist, separated solutions | Days 1–9 Quizzes (40 MCQs) + Category F (42 Traps) + Sanfoundry map | **Complete** |

---

## Central Exam Preparation Hub Navigation

Quick access to all assessment and drill documents in `10-EXAM-PREPARATION/`:

1. [Instructor Knowledge Checks](./10-EXAM-PREPARATION/instructor-knowledge-checks.md): **All 40 classroom MCQs from Days 1–9** with verified answer keys, detailed explanations, and distractor analyses.
2. [MCQ Traps Bank](./10-EXAM-PREPARATION/mcq-traps-bank.md): **42 high-yield certification trap questions** across all syllabus domains (including `fromkeys` list trap, dict collision, set operator type errors, class attribute sharing, and name mangling).
3. [Output Prediction Drills](./10-EXAM-PREPARATION/output-prediction-drills.md): 7 whiteboard & mental trace drills with line-by-line trace tables.
4. [Sanfoundry Practice Sets](./10-EXAM-PREPARATION/sanfoundry-practice-sets.md): 7 curated problem sets referenced in instructor summaries (`IMG-31`, `IMG-49`) and Days 8 & 9.
5. [Common Mistakes Cheat Sheet](./10-EXAM-PREPARATION/common-mistakes-cheat-sheet.md): Category F 32-trap quick reference ("Don't Do This" ➔ "Do This Instead").
6. [Revision Checklist](./10-EXAM-PREPARATION/revision-checklist.md): 11-section comprehensive readiness self-assessment checklist.
7. [Separated Solutions](./10-EXAM-PREPARATION/solutions/): Clean reference implementations for all module exercises (Modules 01–09, 11, 12).

---

## Runtime & Master Verification Suite

To verify the entire curriculum system from your terminal:

```powershell
$py = "C:\Users\kimat\AppData\Local\Python\pythoncore-3.15-64\python.exe"
& $py "c:\Users\kimat\Downloads\class screenshots\BCPD-PYTHON-PREPARATION\test_all.py"
```

- **Target Python Version:** **Python 3.10+** (verified locally: **Python 3.15.2**).
- **Test Results:** **33 / 33 test suites passing (100% success rate)** across all 11 module example suites, 11 exercise suites, and 11 solution runners.
