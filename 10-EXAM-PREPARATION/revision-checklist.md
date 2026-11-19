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

---

## 10. Tuples, Dictionaries & Sets `[Module 11]`
- [ ] Understand tuple immutability and know that a single-item tuple requires a comma: `(5,)`. `[D8-03]`
- [ ] Explain mutability inside immutability: mutating a list nested inside a tuple `([1], 2)`. `[D8-03]`
- [ ] Define and use `collections.namedtuple` for lightweight, readable immutable records. `[D8-04]`
- [ ] Understand multiple return values as implicit tuples and avoid unpacking count mismatches. `[D8-04]`
- [ ] State dictionary key requirements: keys must be **hashable** (immutable: `str`, `int`, `float`, `tuple`, `frozenset`). `[D8-07]`
- [ ] Predict the `{1: 'a', 1.0: 'b'}` numeric key collision: equal values and hashes overwrite the key in-place. `[D8-07]`
- [ ] Identify the `dict.fromkeys("ab", [])` shared mutable list trap. `[D8-05]`
- [ ] Use dictionary methods: `get()`, `pop()`, `popitem()` (LIFO), `update()`, and `setdefault()`. `[D8-05]`
- [ ] Know that dictionary equality ignores key ordering: `{"a": 1, "b": 2} == {"b": 2, "a": 1}` is `True`. `[D8-08]`
- [ ] Perform multiset operations with `collections.Counter`: `|` takes maximum count, `&` takes minimum count. `[D8-08, D8-10]`
- [ ] Use `collections.defaultdict` with factory callables (`int`, `list`, `set`) to handle missing keys. `[D8-10]`
- [ ] Remember that `{}` creates an empty dictionary, while `set()` creates an empty set. `[D8-11]`
- [ ] Distinguish `remove()` (raises `KeyError` if absent) from `discard()` (silent no-op). `[D8-11]`
- [ ] Perform set algebra: Union `|`, Intersection `&`, Difference `-`, Symmetric Difference `^`, Subsets `<` and `<=`. `[D8-12]`
- [ ] Recall that set operators require sets on both sides, while set methods accept any iterable. `[D8-14]`
- [ ] Know that sets do not support `+` or `*`, and that `all(set())` evaluates to `True`. `[D8-14]`
- [ ] Explain `frozenset` as an immutable, hashable set suitable for dictionary keys or set members. `[D8-12, D8-13]`

---

## 11. Object-Oriented Programming & Encapsulation `[Module 12]`
- [ ] Differentiate between Class (blueprint) and Object (instance). `[D9-04]`
- [ ] Read and draw UML class diagrams: PascalCase class name, `-` private attributes/methods, `+` public methods. `[D9-EXT-01]`
- [ ] Follow 4-step class design workflow: 1. Name class, 2. List attributes (`-`), 3. List methods (`+`), 4. Code & test (`__init__` first). `[D9-EXT-01]`
- [ ] Write PascalCase class definitions with `__init__` constructors. `[D9-05]`
- [ ] Understand the explicit `self` parameter and how `obj.method()` translates to `Class.method(obj)`. `[D9-05, D9-09]`
- [ ] Recognize that omitting `self` in an instance method signature raises `TypeError` when called on an instance. `[D9-09]`
- [ ] Implement method chaining by returning `self` from mutator methods. `[D9-09]`
- [ ] Trace attribute lookup order: instance dictionary `obj.__dict__` first, then class dictionary `type(obj).__dict__`. `[D9-08]`
- [ ] Explain instance attribute masking: `a.species = "wolf"` creates an instance attribute without touching `Dog.species`. `[D9-08]`
- [ ] Identify and resolve the **shared mutable class attribute trap** (`tricks = []` declared in class body). `[D9-08]`
- [ ] Implement core dunder methods: `__str__` (readable/user), `__repr__` (unambiguous/developer), `__eq__` (value equality), `__len__`. `[D9-07]`
- [ ] Distinguish protected attributes (`_x` convention) from private name-mangled attributes (`__x` becomes `_ClassName__x`). `[D9-06, D9-11]`
- [ ] Know that `__balance` raises `AttributeError` on direct external access, but `_Account__balance` accesses the attribute. `[D9-06, D9-11]`
- [ ] Use `@property` to create getter methods, `@<name>.setter` for data validation, and recognize read-only property `AttributeError` on write. `[D9-10]`
- [ ] Use dynamic attribute functions: `setattr()`, `getattr()`, `hasattr()`, `delattr()`, and `vars(obj)`. `[D9-EXT-02]`
- [ ] Explain the object lifecycle and destructor `__del__(self)`: runs when reference count drops to 0; `del obj` removes the variable name, not necessarily the object immediately. `[D9-EXT-02]`
- [ ] Build Lab 9.1 `BankAccount` with owner, private balance property, validation, and inter-account transfers. `[D9-EXT-03]`

---

## 12. OOP Inheritance & the MRO `[Module 13]`
- [ ] Understand class inheritance syntax: `class Dog(Animal):` for true IS-A relationships. `[D10-01, D10-03]`
- [ ] Know that all Python classes implicitly inherit from `object`. `[D10-03]`
- [ ] Categorize the 5 types of inheritance: Single, Multilevel, Hierarchical, Multiple, and Hybrid (Diamond). `[D10-04]`
- [ ] Inspect inheritance hierarchies using `cls.__mro__`, `cls.mro()`, `cls.__bases__`, and `issubclass()`. `[D10-04, D10-07]`
- [ ] Always call `super().__init__(*args)` in child initializers to avoid `AttributeError` on uninitialized parent fields. `[D10-05]`
- [ ] Extend parent method logic using `super().method(...)` rather than copying code. `[D10-05]`
- [ ] Implement method overriding and the Shared Template Pattern (where a base method like `__str__` calls `self.area()` polymorphically). `[D10-06]`
- [ ] Distinguish `isinstance(obj, Class)` (checks entire inheritance chain) from `type(obj) is Class` (exact match only). `[D10-07]`
- [ ] Explain why `isinstance(True, int)` is `True` while `type(True) is int` is `False`. `[D10-07]`
- [ ] Explain the C3 Linearization algorithm and how Python deterministically resolves the Diamond problem. `[D10-04]`
- [ ] Understand that private attributes (`__attr`) are independently mangled per class (`_Parent__attr` vs `_Child__attr`) and cannot be accidentally overridden by subclasses. `[D10-05]`
- [ ] Define abstract interfaces using `abc.ABC` and `@abstractmethod`, and recognize `TypeError` when an incomplete subclass is instantiated. `[D10-02]`
- [ ] Apply Mixin classes for reusable capability without identity or persistent instance state. `[D10-02]`
- [ ] Implement `@dataclass` for clean data containers with automatic `__init__`, `__repr__`, `__eq__`, and `frozen=True` immutability. `[D10-02]`
- [ ] Avoid the dataclass mutable default error by using `field(default_factory=list)`. `[D10-02]`

