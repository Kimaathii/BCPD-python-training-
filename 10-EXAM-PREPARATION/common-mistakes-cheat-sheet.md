# Category F: Common Mistakes & Exam Traps Cheat Sheet

> **BCPD Python Cohort 2 Certification Preparation**  
> **Source Grounding:** Category F Trap Analysis (`00-COURSE-MAP/coverage-and-gap-matrix.md`)  
> **Format:** Quick-reference tables ("Don't Do This" âž” "Do This Instead")

---

## 1. Syntax, Types & Input Traps

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T01** | `age = input("Age: ")`<br>`if age > 18:` | `input()` returns `str`. Comparing `str > int` raises `TypeError`. | `age = int(input("Age: "))` | `IMG-05, IMG-11` |
| **T02** | Expecting `round(2.5) == 3` | Python 3 uses Banker's Rounding (Round Half to Even): `2.5` rounds to `2`. | Expect even integers on `.5` boundaries (`round(3.5) == 4`). | `IMG-10, IMG-30` |
| **T03** | Using `is` for value equality:<br>`if user_name is "admin":` | `is` tests memory identity, which fails for non-interned dynamically computed values. | `if user_name == "admin":` (always use `==` for values; reserve `is` for `None`). | `IMG-15, IMG-30` |
| **T04** | Assuming `"False"` is falsy:<br>`if bool("False"):` | Non-empty strings are always truthy regardless of content. | Compare explicitly: `flag = (user_str.lower() == "true")`. | `IMG-32, IMG-50` |

---

## 2. Operators & Precedence Traps

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T05** | Assuming `-2 ** 4 == 16` | Exponentiation binds tighter than unary minus: `-(2 ** 4) == -16`. | `(-2) ** 4` if exponentiating negative base. | `IMG-08, IMG-30` |
| **T06** | Assuming `2 ** 3 ** 2 == 64` | `**` is right-associative: evaluated as `2 ** (3 ** 2) == 2 ** 9 == 512`. | Explicitly parenthesize `(2 ** 3) ** 2` if left-to-right is intended. | `IMG-08, IMG-30` |
| **T07** | Expecting `~5 == -5` | Bitwise NOT formula in two's complement is `~x == -x - 1`. `~5 == -6`. | Use `-x` for negation, `~x` only for bitmasks. | `IMG-13, IMG-14` |
| **T08** | Expecting `-17 % 5 == -2` | Remainder `%` in Python takes the sign of divisor: `-17 % 5 == 3`. | Remember `a % b = a - (a // b) * b`. | `IMG-08, IMG-30` |
| **T09** | Assuming logical `and`/`or` return booleans | Python logical operators return the deciding operand itself: `0 or 5` returns `5`. | Wrap with `bool(0 or 5)` if strict `True`/`False` is required. | `IMG-32, IMG-40` |

---

## 3. Strings & Formatting Traps

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T10** | In-place string method assumption:<br>`s = "hello"; s.upper()` | Strings are immutable; `s.upper()` returns a new string and leaves `s` unchanged. | Reassign: `s = s.upper()` | `IMG-57, IMG-58` |
| **T11** | Catching missing substrings with `index()` without `try` | `str.index("x")` raises `ValueError` if absent. | Use `str.find("x") != -1` or `if "x" in s:`. | `IMG-59/64, IMG-73` |
| **T12** | Joining integer lists directly:<br>`"-".join([1, 2, 3])` | `str.join()` raises `TypeError` if any element in the iterable is not a `str`. | `"-".join(str(x) for x in [1, 2, 3])` | `IMG-62/65, IMG-70` |
| **T13** | Believing `"Â½".isdigit() == True` | Fractions like `Â½` are numeric (`isnumeric() == True`), but not digits (`isdigit() == False`). | Use `isnumeric()` for general numerals or `isdecimal()` for strict 0â€“9. | `IMG-76` |

---

## 4. Lists, Structures & Functions Traps

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T14** | Overwriting with in-place sort:<br>`data = data.sort()` | `sort()`, `append()`, `reverse()` mutate in place and return `None`. | Use `data.sort()` alone, or `data = sorted(data)`. | `IMG-67, IMG-70, IMG-73` |
| **T15** | 2D matrix multiplication:<br>`grid = [[0] * 3] * 3` | Duplicates pointers to the same inner list; modifying `grid[0][0]` changes all rows. | `grid = [[0] * 3 for _ in range(3)]` | `IMG-70, IMG-74` |
| **T16** | Re-iterating a consumed generator:<br>`g = (x for x in r); sum(g); sum(g)` | Generators evaluate lazily and exhaust on first traversal; second run yields 0. | Convert to `list` first if multiple traversals are needed: `data = list(g)`. | `IMG-78, IMG-79` |
| **T17** | Modifying a list during iteration:<br>`for x in lst: lst.remove(x)` | Deleting elements shifts remaining indices left, causing subsequent elements to be skipped. | Iterate over a copy: `for x in lst[:]:` or use a list comprehension. | `IMG-46, IMG-70` |
| **T18** | Mutable default parameter:<br>`def f(x, acc=[]): acc.append(x)` | Default object is instantiated once at function definition and shared across all calls. | `def f(x, acc=None): if acc is None: acc = []` | `IMG-75, D5-02` |

---

## 5. Tuples, Dictionaries & Sets Traps (Day 8)

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T19** | Single-item tuple comma omission:<br>`t = (5)` | Parentheses without a trailing comma evaluate as integer grouping: `type((5)) is int`. | Add trailing comma: `t = (5,)` or `t = 5,`. | `D8-03` |
| **T20** | Attempting to mutate tuple elements:<br>`t = (1, 2); t[0] = 9` | Tuples are immutable and do not support item assignment. | Convert to list first: `l = list(t); l[0] = 9; t = tuple(l)`. | `D8-03` |
| **T21** | Mutating list nested inside tuple:<br>`t = ([1], 2); t[0].append(5)` | The tuple binding is immutable, but the nested list object is mutable and modified in place! | Use nested tuples if complete immutability is required: `t = ((1,), 2)`. | `D8-03` |
| **T22** | `dict.fromkeys("ab", [])` list trap | The same single list object is shared across all keys; mutating one key alters all! | Use dict comprehension: `{k: [] for k in "ab"}`. | `D8-05` |
| **T23** | Numeric key collision in dicts:<br>`d = {1: "a", 1.0: "b"}` | `1 == 1.0` is `True` and `hash(1) == hash(1.0)`; key `1.0` overwrites key `1` in place! | Keep key types strictly distinct if numerical differentiation is required. | `D8-07` |
| **T24** | Creating an empty set with `{}` | `{}` creates an empty dictionary (`dict`), NOT a set. | Use `set()` to instantiate an empty set. | `D8-11` |
| **T25** | Set bitwise operators on non-sets:<br>`s = {1, 2} \| [3, 4]` | Bitwise set operators (`\|`, `&`, `-`, `^`) require sets on both sides and raise `TypeError`. | Use method syntax: `s.union([3, 4])` (accepts any iterable). | `D8-14` |
| **T26** | Attempting set concatenation:<br>`s = {1, 2} + {3}` | Sets do not support sequence concatenation (`+`) or repetition (`*`); raises `TypeError`. | Use `s \| {3}` or `s.add(3)`. | `D8-14` |
| **T27** | Expecting empty `all()` to be False:<br>`all(set())` | Vacuous truth: `all()` returns `True` if no element is falsy, so `all(set()) is True`. | Check non-emptiness explicitly: `bool(s) and all(s)`. | `D8-14` |

---

## 6. Object-Oriented Programming Traps (Day 9)

| # | Trap / Anti-Pattern | Why It Breaks | Do This Instead | Course Citation |
|---|---|---|---|---|
| **T28** | Shared mutable class attribute:<br>`class Dog: tricks = []` | Attributes declared in class body are shared across all instances; mutating in one modifies all. | Initialize mutable attributes inside `__init__`: `self.tricks = []`. | `D9-08` |
| **T29** | Forgetting `self` in method definition:<br>`def click(): pass` | Calling `obj.click()` passes `self` automatically, raising `TypeError: takes 0 args but 1 given`. | Always write `def click(self, ...):`. | `D9-09` |
| **T30** | Direct private attribute access:<br>`print(obj.__balance)` | Double leading underscore name-mangles attribute to `_ClassName__balance`; raises `AttributeError`. | Provide a public getter via `@property` or access via `obj._ClassName__balance`. | `D9-06, D9-11` |
| **T31** | Assigning to a read-only property:<br>`t.fahrenheit = 100` | A `@property` without a corresponding `@<name>.setter` raises `AttributeError: can't set attribute`. | Define a `@fahrenheit.setter` method or set the underlying state (`celsius`). | `D9-10` |
| **T32** | Expecting instance assignment to update class:<br>`a = Dog(); a.species = "wolf"` | Instance assignment creates a local attribute in `a.__dict__`, masking but not touching `Dog.species`. | Mutate class directly if global change is intended: `Dog.species = "wolf"`. | `D9-08` |

