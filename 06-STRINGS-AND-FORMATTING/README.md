# Module 06: Strings, Text Processing, and String Formatting

> **BCPD Python Cohort 2 Certification Preparation**  
> **Source Screen Mappings:** `IMG-01, IMG-02, IMG-04, IMG-05, IMG-50, IMG-52, IMG-57, IMG-58, IMG-59/64, IMG-60, IMG-62/65, IMG-63, IMG-66, IMG-68/72, IMG-69, IMG-73, IMG-76`  
> **Topic Classification:** Core Certification Subject (Day 3 Afternoon & Day 4 Morning)

---

## 1. String Literals, Quoting, Escapes, and Slicing `[Course: IMG-01, IMG-02, IMG-52, IMG-57, IMG-58]`

### String Literals and Quoting
Strings in Python are sequences of Unicode characters. Python supports single (`'...'`), double (`"..."`), and triple quotes (`'''...'''` or `"""..."""`):
- Single and double quotes are functionally identical; choose one style to embed the other without escaping: `"It's Python!"` or `'He said "Hello"'`.
- Triple quotes preserve literal newlines and indentation, commonly used for multiline strings and docstrings.
- Raw strings (`r"..."` or `r'...'`) suppress escape sequence interpretation (e.g., `r"C:\test\new"` treats `\t` and `\n` as literal characters). Note that a raw string cannot end with an odd number of backslashes.

### Escape Sequences
Common escape sequences include:
- `\n`: Linefeed (ASCII 10)
- `\t`: Horizontal tab (ASCII 9)
- `\\`: Literal backslash
- `\'` / `\"`: Literal single / double quote
- `\r`: Carriage return

### Slicing and Indexing `[Course: IMG-57, IMG-58]`
Python sequences use 0-based indexing from the left and -1-based indexing from the right:
```python
s = "PYTHON"
#  Index:   0   1   2   3   4   5
# -Index:  -6  -5  -4  -3  -2  -1
#  Char:    P   Y   T   H   O   N
```

**Slice Syntax:** `sequence[start:stop:step]`
- `start` is inclusive; `stop` is exclusive.
- `step` defines stride direction and magnitude.
- Reversal idiom: `s[::-1]`.
- **Out of Bounds Rule (Critical Exam Trap):**
  - Direct index out of bounds: `s[10]` -> raises `IndexError`.
  - Slice out of bounds: `s[10:20]` -> safely returns `""` (empty string).

---

## 2. Core String Methods `[Course: IMG-59/64, IMG-60, IMG-62/65]`

Strings are immutable; **every string method returns a new string and does not modify the original**.

### Case Transformations
- `s.upper()`: Converts all cased characters to uppercase.
- `s.lower()`: Converts all cased characters to lowercase.
- `s.title()`: Capitalizes first letter of each word (apostrophe edge case: `"it's".title()` -> `"It'S"`).
- `s.capitalize()`: Capitalizes the very first character; lowercases the rest.
- `s.swapcase()`: Inverts case of each character.

### Whitespace and Stripping
- `s.strip([chars])`: Strips leading and trailing characters (defaults to whitespace).
- `s.lstrip([chars])`: Strips leading characters.
- `s.rstrip([chars])`: Strips trailing characters.
- *Trap:* `chars` is a set of characters to strip, not a prefix/suffix substring: `"apple".strip("el")` -> `"app"`.

### Searching and Counting
- `s.find(sub[, start[, end]])`: Returns the lowest index where `sub` is found, or `-1` if not found.
- `s.rfind(sub)`: Returns highest index, or `-1`.
- `s.index(sub)`: Like `find()`, but **raises `ValueError`** if not found.
- `s.rindex(sub)`: Like `rfind()`, but **raises `ValueError`** if not found.
- `s.count(sub)`: Returns non-overlapping occurrences of `sub`.
- `s.startswith(prefix)`: Returns `True` if `s` starts with `prefix` (can take a tuple of prefixes).
- `s.endswith(suffix)`: Returns `True` if `s` ends with `suffix` (can take a tuple of suffixes).

### Splitting and Joining
- `s.split(sep=None, maxsplit=-1)`: Splits by `sep`. When `sep=None`, consecutive whitespaces are grouped, and leading/trailing whitespace is ignored.
- `sep.join(iterable)`: Concatenates strings from `iterable` with `sep` as delimiter.
  - *Exam Trap:* If `iterable` contains non-string elements (e.g., `[1, 2, 3]`), `TypeError` is raised. Must convert first: `"-".join(str(x) for x in [1, 2, 3])`.
- `s.replace(old, new[, count])`: Replaces occurrences of `old` with `new`.

---

## 3. Character Classification: The `is...` Family `[Course: IMG-76, IMG-52]`

Exam questions frequently test distinguishing between the character classification predicates:

| Method | What It Tests | `"123"` | `"Â²"` (Superscript) | `"Â½"` (Vulgar Fraction) | `"-5"` | `"3.14"` | `"abc"` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `s.isdecimal()` | Strict base-10 digits (0â€“9) | `True` | `False` | `False` | `False` | `False` | `False` |
| `s.isdigit()` | Base-10 digits + compatibility digits (e.g. superscripts `Â²`) | `True` | `True` | `False` | `False` | `False` | `False` |
| `s.isnumeric()` | All numeric representations (digits, superscripts, fractions `Â½`, Roman numerals in Unicode) | `True` | `True` | `True` | `False` | `False` | `False` |
| `s.isalpha()` | Alphabetic Unicode characters only | `False` | `False` | `False` | `False` | `False` | `True` |
| `s.isalnum()` | Alphanumeric (`isalpha() or isnumeric()`) | `True` | `True` | `True` | `False` | `False` | `True` |
| `s.isspace()` | Whitespace characters (` `, `\t`, `\n`, `\r`, `\v`, `\f`) | `False` | `False` | `False` | `False` | `False` | `False` |
| `s.isidentifier()` | Valid Python identifier syntax (`[a-zA-Z_][a-zA-Z0-9_]*`) | `False` | `False` | `False` | `False` | `False` | `True` |

> [!WARNING]
> Negative signs (`-`) and decimal points (`.`) are **not** digits or numeric characters! Neither `"-12"`, `"3.14"`, nor `"1e5"` return `True` for any of `isdecimal()`, `isdigit()`, or `isnumeric()`.

---

## 4. String Formatting Evolution `[Course: IMG-68/72, IMG-69, IMG-73]`

Python has supported three generations of string formatting:

```
Generation 1: %-Formatting (printf style) -> Legacy, still in exams
Generation 2: str.format() (Python 2.6 / 3.0) -> Format specification mini-language
Generation 3: Formatted String Literals / f-strings (Python 3.6+) -> Modern, fastest, readable
```

### Generation 1: `%` Formatting
- `%s` (string via `str()`), `%r` (repr via `repr()`), `%d` / `%i` (integer), `%f` (float), `%x` / `%X` (hex).
- Syntax: `"%s is %d years old" % (name, age)`
- *Trap:* If formatting a single value, parentheses are optional unless the value is a tuple: `"%s" % (val,)`.

### Generation 2: `str.format()`
- Positional: `"{} and {}".format(a, b)`
- Indexed: `"{1} before {0}".format(a, b)`
- Keyword: `"{name}: {score}".format(name="Alice", score=95)`

### Generation 3: f-strings
- Prefix with `f` or `F`: `f"Hello, {name}!"`
- Inline expressions allowed: `f"2 + 2 = {2 + 2}"`
- Self-documenting debugging specifier (Python 3.8+): `f"{x=}"` produces `'x=42'`.

---

## 5. Format Specification Mini-Language `[Course: IMG-68/72, IMG-73]`

Used inside both `str.format()` and f-strings: `{[name]:[[fill]align][sign][#][0][width][grouping_option][.precision][type]}`

| Specifier | Meaning | Example | Output |
| :--- | :--- | :--- | :--- |
| `>10` | Right align in width 10 | `f"{'hi':>10}"` | `'        hi'` |
| `<10` | Left align in width 10 | `f"{'hi':<10}"` | `'hi        '` |
| `^10` | Center align in width 10 | `f"{'hi':^10}"` | `'    hi    '` |
| `*^10` | Center align with fill `*` | `f"{'hi':*^10}"` | `'****hi****'` |
| `.2f` | Float with 2 decimal places | `f"{3.14159:.2f}"` | `'3.14'` |
| `+` | Always show sign (`+` or `-`) | `f"{42:+}"` | `'+42'` |
| `,` | Comma thousands separator | `f"{1000000:,}"` | `'1,000,000'` |
| `_` | Underscore thousands separator | `f"{1000000:_}"` | `'1_000_000'` |
| `b`, `o`, `x`, `X` | Binary, Octal, Hex (lower/upper) | `f"{255:#x}"` | `'0xff'` |
| `08d` | Zero-padded integer to width 8 | `f"{42:08d}"` | `'00000042'` |
| `%` | Percentage (multiplies by 100 + `%`) | `f"{0.75:.1%}"` | `'75.0%'` |

---

## 6. String Immutability and Interning `[Course: IMG-57, IMG-58]`

### Immutability
- Strings in Python are strictly immutable. Modifying an element `s[0] = 'X'` raises:
  `TypeError: 'str' object does not support item assignment`.
- To modify a string, construct a new one via concatenation, slicing, or `str.join()`.

### Interning and Identity (`is` vs `==`)
- CPython automatically interns compile-time constant strings matching identifier syntax (letters, digits, underscores).
- `a = "hello"; b = "hello"` -> `a is b` is `True` (same memory address).
- Dynamically computed strings may not be interned:
  ```python
  a = "".join(["hel", "lo"])
  b = "hello"
  a == b  # True (same value)
  a is b  # False (different objects in memory unless sys.intern() is called)
  ```
- *Certification Rule:* Always use `==` to compare string contents, never `is`.

---

## 7. Day 4 Practical Lab 4.1: Text Tools Application `[Course: IMG-66, IMG-63]`

### Original Classroom Implementation (`IMG-66`)
The slide shows an interactive command loop (`car game` / `text_tools`):
```python
# Verbatim from IMG-66:
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
```
*Note on IMG-66:* In some classroom lecture runs, the `help` branch and `started` state guards were added interactively during class drills. Our reference implementation covers both the baseline and hardened state machines.

---

## 8. Common Exam Traps & Gotchas Summary

1. **`s.find()` vs `s.index()`**: `find()` returns `-1` on absence, `index()` raises `ValueError`.
2. **String immutability**: Methods return a transformed copy; calling `s.replace("a", "b")` without re-assigning leaves `s` unchanged.
3. **`"".join()` type constraint**: Calling `''.join([1, 2, 3])` crashes with `TypeError`.
4. **Fraction / superscript classification**: `"Â½".isnumeric()` is `True`, but `"Â½".isdigit()` and `"Â½".isdecimal()` are `False`.
5. **Slice indexing immunity**: `s[len(s) + 5]` raises `IndexError`, but `s[len(s):len(s) + 5]` evaluates to `""`.
6. **Title case with apostrophes**: `"they're".title()` produces `"They'Re"` because `'` is treated as a word boundary.
