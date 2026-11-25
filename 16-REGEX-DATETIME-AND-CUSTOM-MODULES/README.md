# Module 16: Modules Part 2 — Regular Expressions (`re`), `time`, `datetime` & Custom Modules

Welcome to **Module 16** of the BCPD Python Certification curriculum. This module continues **Domain 4: Modules & Standard Libraries (15% of the certification exam)**, mapped directly to **Student Manual Day 15 (§15.1–15.4)** and **Classroom Deck Day 14 (`[Course: D14-01]` to `[Course: D14-07]`)**.

---

## 1. Domain 4 Certification Overview & Objectives

In the BCPD certification, string parsing via pattern matching, temporal calculations, and modular program packaging form core assessment objectives under Domain 4.

```
       BCPD Certification Exam Breakdown
┌───────────────────────────────────────────────┐
│ Domain 1: Basics & Foundations         (15%)  │
│ Domain 2: Data Types & Control Flow    (30%)  │
│ Domain 3: Object-Oriented Programming  (25%)  │
│ Domain 4: Modules & Standard Libraries (15%) ◄── THIS MODULE (Part 2)
│ Domain 5: Exceptions & File I/O        (15%)  │
└───────────────────────────────────────────────┘
```

### Classroom Competency Checklist `[Course: D14-01]`
1. **Search & Match Patterns:** Distinguish `re.search()`, `re.match()`, and `re.fullmatch()`, inspecting matched text via `.group()`, `.span()`, and `.groups()`.
2. **Regex Syntax Mastery:** Formulate raw string patterns using character classes (`\d`, `\w`, `\s`, `\D`, `\W`, `\S`), sets (`[abc]`, `[^0-9]`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`, `\b`), and alternations (`|`).
3. **Extraction & Transformation:** Extract string tokens with `re.findall()` and `re.finditer()`, substitute text with backreferences via `re.sub()`, and split structured strings via `re.split()`.
4. **Groups, Named Capture & Greediness:** Implement capturing groups `()`, named capture groups `(?P<name>...)` with `.groupdict()`, and control greedy (`.+`) vs. lazy (`.+?`) repetition behavior.
5. **Pattern Compilation & Flags:** Precompile regex objects with `re.compile()`, apply flags (`re.I`, `re.M`, `re.S`, `re.X`), and escape dynamic user inputs with `re.escape()`.
6. **Temporal Operations with `time` & `datetime`:** Measure runtime with `time.perf_counter()`, manipulate Gregorian dates with `date`, combine timestamps with `datetime`, format/parse strings with `strftime`/`strptime`, and perform date arithmetic with `timedelta`.
7. **Custom Modules & Execution Guards:** Package reusable modules and employ the `if __name__ == "__main__":` idiom.
8. **Lab 14.1 Mastery:** Build input validation engines (SMS transaction alerts, email, phone numbers) and a live countdown timer.

---

## 2. Regular Expressions Core: Search, Match & Fullmatch `[Course: D14-02]`

The `re` module provides text matching engine primitives based on deterministic/non-deterministic finite automata. Always write regex patterns using **raw string notation (`r"..."`)** to prevent Python's string literal parser from consuming backslashes before the regex engine receives them.

### Function Comparison Matrix

| Function | Search Scope | Match Requirement | Return Value on Match | Return on Failure |
|---|---|---|---|---|
| `re.search(pat, s)` | Scans entire string `s` from left to right | First occurrence anywhere in `s` | `re.Match` object | `None` |
| `re.match(pat, s)` | Examines only index 0 of `s` | Must match at the very start of `s` | `re.Match` object | `None` |
| `re.fullmatch(pat, s)` | Examines entire string `s` | Entire string from start to end must match | `re.Match` object | `None` |

### Match Object Methods
- `m.group(0)` or `m.group()`: The entire matched substring.
- `m.group(1), m.group(2)...`: Substrings captured by indexed parentheses groups `()`.
- `m.start()`: Zero-based starting index of the match in the source string.
- `m.end()`: Zero-based ending index (exclusive bound) of the match.
- `m.span()`: 2-tuple `(m.start(), m.end())`.

### Code Walkthrough (`re_basics.py`) `[Course: D14-02]`
```python
import re

text = "Order 66 shipped on 2026-10-29"

# 1. re.search finds the first match anywhere
m = re.search(r"\d+", text)
print(m.group(), m.span())            # -> '66' (6, 8)

# 2. re.match requires match at start of string (index 0)
print(re.match(r"\d+", text))         # -> None ("Order" starts at index 0, not digits!)
print(re.match(r"Order", text).group()) # -> 'Order'

# 3. re.fullmatch requires the entire string to match
print(bool(re.fullmatch(r"\d{4}", "2026")))   # -> True
print(bool(re.fullmatch(r"\d{4}", "20265")))  # -> False (length is 5, not 4)
```

---

## 3. Regex Syntax Cheat-Sheet `[Course: D14-04]`

| Metacharacter | Definition / Meaning | Example Pattern | Matching Sample |
|---|---|---|---|
| `.` | Any single character except newline (`\n`) | `a.c` | Matches `"abc"`, `"a-c"`, `"a c"` |
| `\d` | Any decimal digit (`[0-9]`) | `\d\d` | Matches `"42"`, `"07"` |
| `\D` | Any non-digit character (`[^0-9]`) | `\D+` | Matches `"Order "` in `"Order 66"` |
| `\w` | Word character (`[a-zA-Z0-9_]`) | `\w+` | Matches `"BCPD_2026"` |
| `\W` | Non-word character | `\W+` | Matches `" @#$ "` |
| `\s` | Whitespace (`[ \t\n\r\f\v]`) | `\s+` | Matches spaces, tabs, newlines |
| `\S` | Non-whitespace character | `\S+` | Matches `"Python"` |
| `[abc]` | Explicit character set | `[aeiou]` | Matches any lowercase vowel |
| `[a-z]` | Character range | `[0-9A-Fa-f]` | Matches valid hex character |
| `[^abc]` | Negated character set | `[^0-9]` | Matches any character except digits |
| `*` | 0 or more repetitions (Greedy) | `colou*r` | Matches `"color"`, `"colour"`, `"colouur"` |
| `+` | 1 or more repetitions (Greedy) | `\d+` | Matches `"6"`, `"2026"` |
| `?` | 0 or 1 repetition (Optional) | `colou?r` | Matches `"color"`, `"colour"` |
| `{n}` | Exactly `n` repetitions | `\d{4}` | Matches `"2026"` |
| `{m,n}` | Between `m` and `n` repetitions (inclusive) | `\d{2,4}` | Matches `"12"`, `"123"`, `"1234"` |
| `^` | Anchor: Start of string (or line in `re.M`) | `^Order` | Matches `"Order 66"`, not `"An Order"` |
| `$` | Anchor: End of string (or line in `re.M`) | `\d+$` | Matches `"Code 99"`, not `"Code 99."` |
| `\b` | Word boundary anchor (0-width transition) | `\bcat\b` | Matches `"cat"`, not `"concatenate"` |
| `a\|b` | Alternation (OR) | `cat\|dog` | Matches `"cat"` or `"dog"` |
| `( )` | Capturing group | `(cat\|dog)s?` | Groups choices and captures value |

---

## 4. Extraction & Transformation Tools `[Course: D14-06]`

### 1. `re.findall(pattern, string, flags=0)`
Returns all non-overlapping matches of `pattern` in `string`:
- **If no capturing groups `()` exist:** Returns a `list[str]`.
- **If exactly 1 capturing group exists:** Returns a `list[str]` of captured substrings.
- **If 2 or more capturing groups exist:** Returns a `list[tuple[str, ...]]` where each tuple holds the groups.

```python
import re
s = "cat 3, dog 12, owl 7"

# 0 groups -> list of strings
print(re.findall(r"\d+", s))
# Output: ['3', '12', '7']

# 2 groups -> list of tuples!
print(re.findall(r"(\w+) (\d+)", s))
# Output: [('cat', '3'), ('dog', '12'), ('owl', '7')]
```

### 2. `re.finditer(pattern, string, flags=0)`
Returns an iterator yielding `re.Match` objects over all non-overlapping matches. Essential when start/end character offsets are required without storing all match objects in memory at once.

```python
for m in re.finditer(r"\d+", s):
    print(f"Matched {m.group()} at index {m.start()}..{m.end()}")
# Output:
# Matched 3 at index 4..5
# Matched 12 at index 11..13
# Matched 7 at index 19..20
```

### 3. `re.sub(pattern, repl, string, count=0, flags=0)`
Replaces occurrences of `pattern` in `string` with `repl`.
- `repl` can refer to captured groups using backreferences `\1`, `\2` (or `\g<name>`).
- `count=0` replaces all occurrences; positive int limits replacements.

```python
# Literal substitution
print(re.sub(r"\d+", "@", s))
# Output: cat @, dog @, owl @

# Backreference group swap
print(re.sub(r"(\w+) (\d+)", r"\2x\1", "cat 3"))
# Output: 3xcat
```

### 4. `re.subn(pattern, repl, string)`
Identical to `re.sub`, but returns a 2-tuple: `(new_string, number_of_subs_made)`.

### 5. `re.split(pattern, string, maxsplit=0, flags=0)`
Splits `string` by occurrences of `pattern`.

```python
print(re.split(r",\s*", s))
# Output: ['cat 3', 'dog 12', 'owl 7']
```

---

## 5. Groups, Named Groups & Greedy vs. Lazy Matching `[Course: D14-07]`

### Capturing Groups vs. Non-Capturing Groups
- `(pattern)`: Captures matched substring into numerical slots `1, 2, ...`.
- `(?:pattern)`: Non-capturing group. Groups logical tokens without capturing or shifting group indices.

### Named Capture Groups `(?P<name>pattern)`
Enables descriptive dictionary lookups instead of brittle numerical indices:

```python
import re

pat = r"(?P<user>\w+)@(?P<domain>[\w.]+)"
m = re.search(pat, "mail ada@bcpd.org now")

print(m.group(0))                    # -> 'ada@bcpd.org' (entire match)
print(m.group(1), m.group("domain")) # -> 'ada' 'bcpd.org'
print(m.groupdict())                 # -> {'user': 'ada', 'domain': 'bcpd.org'}
```

### Greedy vs. Lazy Matching Quantifiers
By default, quantifiers (`*`, `+`, `?`, `{m,n}`) are **greedy**: they consume as many characters as possible while still allowing the overall pattern to succeed.
Appending a `?` after any quantifier converts it to **lazy** (minimal): it consumes as few characters as possible.

```python
html = "<b>bold</b><i>it</i>"

# Greedy (.+) consumes everything up to the FINAL '>'
print(re.findall(r"<.+>", html))
# Output: ['<b>bold</b><i>it</i>']

# Lazy (.+?) stops at the FIRST '>'
print(re.findall(r"<.+?>", html))
# Output: ['<b>', '</b>', '<i>', '</i>']
```

---

## 6. Compilation, Flags & Escaping `[Course: D14-05]`

### `re.compile(pattern, flags=0)`
Compiles a regular expression pattern into a reusable `re.Pattern` object. In production and tight loops, compiling amortizes pattern compilation overhead.

```python
email_pat = re.compile(r"^[\w.-]+@[\w-]+\.[\w.]+$", re.I)
print(bool(email_pat.match("Ada.L@BCPD.org")))  # True
print(bool(email_pat.match("bad@address")))      # False
```

### Essential Regex Flags

| Flag | Short Form | Effect on Matching |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Case-insensitive matching (`[a-z]` matches `[A-Z]`). |
| `re.MULTILINE` | `re.M` | `^` matches string start **and start of every newline** (`\n`). `$` matches line end. |
| `re.DOTALL` | `re.S` | `.` matches **any character including newline** (`\n`). |
| `re.VERBOSE` | `re.X` | Ignores whitespace and `#` comments inside pattern for documentation. |

```python
text = "first line\nsecond line"

# Without re.M: '^' matches only beginning of the entire string
print(re.findall(r"^\w+", text))
# Output: ['first']

# With re.M: '^' matches start of each line
print(re.findall(r"^\w+", text, re.M))
# Output: ['first', 'second']
```

### `re.escape(string)`
Escapes all special regex metacharacters in `string`, making it safe to interpolate user input into a pattern without regex injection vulnerabilities:

```python
print(re.escape("1+1=2"))  # -> '1\\+1\\=2'
```

---

## 7. The `time` Module & Runtime Benchmarking `[Course: D14-01, §15.2]`

Python's `time` standard library module provides low-level C runtime clock access:

```python
import time

# 1. Wall-clock timestamp (Unix Epoch seconds: 1970-01-01 00:00:00 UTC)
epoch_now = time.time()
print(isinstance(epoch_now, float))  # True

# 2. High-resolution monotonic benchmark counter (immune to system clock drift/NTP)
t0 = time.perf_counter()
time.sleep(0.01)  # sleep for 10ms
elapsed = time.perf_counter() - t0
print(f"Elapsed: {elapsed:.4f}s")
```

### Exam Invariant: `time.time()` vs. `time.perf_counter()`
- `time.time()` returns wall-clock time; if the system administrator or NTP adjusts system time backward, `time.time() - start` can evaluate to a **negative duration**.
- `time.perf_counter()` uses a monotonic clock; its value **never moves backward**, making it mandatory for benchmarking and timeout gates.

---

## 8. The `datetime` Module: The Four Core Classes `[Course: D14-01, §15.3]`

The `datetime` module offers object-oriented calendar and clock abstractions:

```python
from datetime import date, time, datetime, timedelta

# 1. date: year, month, day
d = date(2026, 12, 5)
print(d.year, d.month, d.day)  # 2026 12 5

# 2. time: hour, minute, second, microsecond
t = time(14, 30, 0)
print(t.hour, t.minute)        # 14 30

# 3. datetime: combined date + time
dt = datetime(2026, 12, 5, 14, 30, 0)
print(dt.isoformat())          # '2026-12-05T14:30:00'

# 4. timedelta: duration
delta = timedelta(days=2, hours=3, minutes=15)
future_date = dt + delta
print(future_date)             # 2026-12-07 17:45:00
```

### Formatting (`strftime`) vs. Parsing (`strptime`)
- **`dt.strftime(fmt)`** (**String Format Time**): Converts `datetime` object → `str`.
- **`datetime.strptime(s, fmt)`** (**String Parse Time**): Parses `str` → `datetime` object.

| Format Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit Year | `2026` |
| `%y` | 2-digit Year (00-99) | `26` |
| `%m` | 2-digit Month (01-12) | `11` |
| `%d` | 2-digit Day (01-31) | `24` |
| `%H` | 24-hour clock (00-23) | `14` |
| `%I` | 12-hour clock (01-12) | `02` |
| `%M` | Minute (00-59) | `30` |
| `%S` | Second (00-59) | `45` |
| `%p` | AM or PM | `PM` |

```python
# Format object to string
dt = datetime(2026, 11, 24, 21, 56, 53)
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # "2026-11-24 21:56:53"

# Parse string to object
parsed = datetime.strptime("2026-11-24 21:56:53", "%Y-%m-%d %H:%M:%S")
print(parsed == dt)  # True
```

### `timedelta` Internals & Exam Trap
A `timedelta` object normalizes and internally stores **only 3 attributes**:
- `days`
- `seconds` (0 to 86,399)
- `microseconds` (0 to 999,999)

```python
td = timedelta(days=1, seconds=10)

# Attribute .seconds only returns the sub-day remainder:
print(td.seconds)          # -> 10 (NOT 86410!)

# Method .total_seconds() returns the entire span in seconds:
print(td.total_seconds())  # -> 86410.0
```

---

## 9. Custom Modules & the `if __name__ == "__main__":` Guard `[Course: D14-01, §15.4]`

When a Python script is imported, its global variable `__name__` is assigned the module's name. When executed directly from the shell, `__name__` is set to `"__main__"`.

```python
# validator.py
def validate_email(email: str) -> bool:
    import re
    return bool(re.fullmatch(r"^[\w.-]+@[\w-]+\.[\w.]+$", email))

if __name__ == "__main__":
    # Test suite only runs when validator.py is executed directly:
    # python validator.py
    print("Testing validator.py...")
    assert validate_email("ada@bcpd.org") is True
    assert validate_email("invalid-email") is False
    print("All validator tests passed!")
```

---

## 10. Lab 14.1 Walkthrough & Solution: Validators & Countdown Timer `[Course: D14-01]`

### Lab Objectives:
1. **Validator Engine:**
   - Validate Nigerian telephone numbers (`+234...` or `080...`).
   - Parse Bank SMS transaction alerts to extract Transaction Type (`DR`/`CR`), Currency, Amount, and Account Number.
2. **Exam Countdown Timer:**
   - Calculate remaining days, hours, minutes, and seconds until the BCPD exam window (`2026-12-05 09:00:00`).

```python
import re
from datetime import datetime

# Part A: Bank SMS Transaction Parser
def parse_bank_sms(sms: str) -> dict:
    pat = (
        r"Acct:\s*\*{3}(?P<acct>\d{4})\s+"
        r"(?P<type>DR|CR):\s*(?P<cur>[A-Z]{3})(?P<amount>[\d,]+\.\d{2})\s+"
        r"Desc:\s*(?P<desc>[^B]+)\s+"
        r"Bal:\s*(?P<bal_cur>[A-Z]{3})(?P<balance>[\d,]+\.\d{2})"
    )
    m = re.search(pat, sms)
    if not m:
        return {}
    data = m.groupdict()
    data["amount"] = float(data["amount"].replace(",", ""))
    data["balance"] = float(data["balance"].replace(",", ""))
    return data

# Part B: Countdown Timer
def exam_countdown(target_dt_str: str, now: datetime = None) -> dict:
    target = datetime.strptime(target_dt_str, "%Y-%m-%d %H:%M:%S")
    now = now or datetime.now()
    diff = target - now
    if diff.total_seconds() <= 0:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "expired": True}

    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds, "expired": False}
```

---

## 11. BCPD High-Yield Certification Traps (Traps 55–60)

### Trap 55: The Greedy HTML Tag Swallowing Trap
- **Bait:** Candidate expects `re.findall(r"<.+>", "<b>hi</b>")` to return `['<b>', '</b>']`.
- **Reality:** `.+` is greedy and consumes through `>hi<` to reach the final `>`, returning `['<b>hi</b>']`.
- **Antidote:** Use lazy quantifier `re.findall(r"<.+?>", "<b>hi</b>")` or negated class `re.findall(r"<[^>]+>", "<b>hi</b>")`.

### Trap 56: The `findall` Return Shape-Shift
- **Bait:** Candidate expects `re.findall` to always return a list of strings.
- **Reality:** When 2+ capturing groups `()` exist, `re.findall` returns a list of **tuples** `[('val1', 'val2')]`.
- **Antidote:** Use non-capturing groups `(?:...)` if grouping is needed without tuple formation.

### Trap 57: `re.match()` Zero-Index Lock
- **Bait:** `re.match(r"\d+", "Year 2026")` expected to return a match on `"2026"`.
- **Reality:** Returns `None` because `re.match()` tests only character index 0 (`"Y"`).
- **Antidote:** Use `re.search()` to find matches anywhere in the string.

### Trap 58: Date Format Specifier Collision (`%m` vs. `%M`)
- **Bait:** Using `%M` for month.
- **Reality:** `%m` is zero-padded month (01–12); `%M` is zero-padded minute (00–59).
- **Antidote:** Remember capital `%M` stands for **M**inute; lowercase `%m` stands for **m**onth.

### Trap 59: `timedelta.seconds` Attribute vs. `.total_seconds()` Method
- **Bait:** `td = timedelta(days=2); print(td.seconds)` prints `172800`.
- **Reality:** Prints `0`! `.seconds` is modulo 86,400.
- **Antidote:** Always invoke `td.total_seconds()` for total elapsed seconds.

### Trap 60: Dynamic Regex Pattern Metacharacter Injection
- **Bait:** Interpolating user search terms directly: `re.search(user_query, text)`.
- **Reality:** If `user_query` is `"1+1"`, `+` is parsed as 1-or-more quantifier and crashes with `re.error` (nothing to repeat).
- **Antidote:** Sanitize dynamic strings with `re.escape(user_query)`.

---

## 12. Practice Exam Questions (10 MCQs with Detailed Explanations)

#### Q1. What will be the output of the following code?
```python
import re
print(re.findall(r"\d+", "A12B34C"))
```
- A) `['A', 'B', 'C']`
- B) `['12', '34']`
- C) `[12, 34]`
- D) `('12', '34')`
> **Answer: B**  
> `re.findall` returns a list of matched substrings (`str`). Digits `'12'` and `'34'` are returned as strings.

#### Q2. What is the output of this regex substitution?
```python
import re
s = "June 2026"
print(re.sub(r"(\w+) (\d+)", r"\2/\1", s))
```
- A) `2026/June`
- B) `June/2026`
- C) `\2/\1`
- D) `TypeError`
> **Answer: A**  
> `\1` captures `"June"`, `\2` captures `"2026"`. The replacement `r"\2/\1"` swaps their order to `"2026/June"`.

#### Q3. What is the return type of `re.findall(r"(\d{2})-(\d{2})", "10-20, 30-40")`?
- A) `list[str]`
- B) `list[tuple[str, str]]`
- C) `dict[str, str]`
- D) `tuple[str, ...]`
> **Answer: B**  
> When multiple capturing groups are present in the pattern, `re.findall` returns a list of tuples: `[('10', '20'), ('30', '40')]`.

#### Q4. What is the output of the following lazy matching snippet?
```python
import re
text = "<p>para 1</p><p>para 2</p>"
print(len(re.findall(r"<p>.*?</p>", text)))
```
- A) 1
- B) 2
- C) 4
- D) 0
> **Answer: B**  
> The lazy quantifier `.*?` stops at the earliest `</p>`, yielding two distinct matches: `'<p>para 1</p>'` and `'<p>para 2</p>'`.

#### Q5. What will the following expression evaluate to?
```python
import re
print(re.match(r"BCPD", "Welcome to BCPD"))
```
- A) `<re.Match object; span=(11, 15), match='BCPD'>`
- B) `'BCPD'`
- C) `None`
- D) `False`
> **Answer: C**  
> `re.match` anchors strictly to index 0 of the string. Since `"Welcome"` starts at index 0, `re.match` returns `None`.

#### Q6. What does `re.escape("file[1].txt")` return?
- A) `'file[1].txt'`
- B) `'file\\[1\\]\\.txt'`
- C) `'file\\[1\\]\\\.txt'`
- D) `SyntaxError`
> **Answer: B**  
> `re.escape` backslash-escapes all regex metacharacters (`[`, `]`, `.`).

#### Q7. Given `from datetime import timedelta; td = timedelta(days=1, minutes=1)`, what is `td.seconds`?
- A) `86460`
- B) `60`
- C) `1`
- D) `1440`
> **Answer: B**  
> `timedelta` stores days separately. `td.seconds` evaluates only the remainder within the single day (1 minute = 60 seconds).

#### Q8. What format code produces a 4-digit year in `datetime.strftime`?
- A) `%y`
- B) `%Y`
- C) `%yr`
- D) `%YYYY`
> **Answer: B**  
> `%Y` generates the full 4-digit year (e.g., `2026`), while `%y` produces a 2-digit year (e.g., `26`).

#### Q9. Why is `time.perf_counter()` preferred over `time.time()` for elapsed time benchmarks?
- A) `time.perf_counter()` returns an integer.
- B) `time.time()` is slower to execute.
- C) `time.perf_counter()` is a monotonic clock that cannot jump backwards if the system time is changed.
- D) `time.time()` only measures milliseconds.
> **Answer: C**  
> `perf_counter` provides a monotonic clock reference immune to NTP adjustments and system clock updates.

#### Q10. What is the value of `__name__` when a module is imported via `import my_module`?
- A) `"__main__"`
- B) `"my_module"`
- C) `None`
- D) `"__import__"`
> **Answer: B**  
> When imported, Python assigns the module's file/symbol name to `__name__`.
