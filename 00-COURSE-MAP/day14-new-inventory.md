# Day 14 New Classroom Screenshot Inventory & Verbatim Extractions
**Class Date:** Tuesday 24 Nov 2026 (Week 3, Day 14)  
**Subject:** Modules Part 2: `re`, `time`, `datetime`, own modules  
**BCPD Exam Weight:** Domain 4 · Modules & Libraries (15%)  
**Student Manual Mapping:** Day 15 · §15.1–15.5  
**Image Files Staged:** 16 JPEG files (Nov 24 batch: `21.56.53.jpeg` to `21.57.00.jpeg`; Nov 25 completion batch: `22.30.28.jpeg`, `22.30.29.jpeg`, `22.33.56.jpeg`, `22.33.56l.jpeg`, `22.33.56lo.jpeg`, `22.33.57.jpeg`, `22.33.57ki.jpeg`, `22.33.57op.jpeg`, `22.33.58.jpeg`, `22.33.58m.jpeg`)  
**Curriculum Mapping:** Module 16 (`16-REGEX-DATETIME-AND-CUSTOM-MODULES`) & Central Exam Prep Hub (`10-EXAM-PREPARATION/`)

---

## 1. Master Slide Index & Provenance Cross-Reference

| Slide Tag | Source File(s) | Slide Title / Manual Ref | Core Topic / Code File | Target Curriculum Location |
|---|---|---|---|---|
| `[Course: D14-01]` | `21.56.53.jpeg` | Objectives & Agenda (§15.1–§15.4) | 5 competencies, 12 agenda items, Lab 14.1 | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md` |
| `[Course: D14-02]` | `21.56.53k.jpeg` | `re` basics: search, match & fullmatch (§15.1) | `re_basics.py`, raw strings, match offsets (`.group()`, `.span()`) | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-03]` | `21.56.55l.jpeg` | Live IDE Coding (`main.py`) | Practical SMS transaction extraction (`re.search()`, regex patterns) | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/examples.py`, Lab 14.1 |
| `[Course: D14-04]` | `21.56.56li.jpeg`, `21.56.57o.jpeg` | Regex syntax cheat-sheet (§15.1) | Metacharacters, character classes, quantifiers, anchors, alternation | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md` |
| `[Course: D14-05]` | `21.56.58.jpeg` | `re.compile` & flags (§15.1) | `re_flags.py`, `re.I`, `re.M`, `re.S`, `re.X`, `re.escape()` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-06]` | `21.56.59.jpeg` | `findall`, `finditer`, `sub` & `split` (§15.1) | `re_tools.py`, scalar vs group tuple return, backreferences `\1`, `\2` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-07]` | `21.57.00.jpeg` | Groups, named groups & greedy matching (§15.1) | `re_groups.py`, `(?P<name>...)`, `groupdict()`, greedy (`.+`) vs lazy (`.+?`) | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, Traps 55–56 |
| `[Course: D14-08]` | `22.30.28.jpeg` | More `re` tools: split, subn, lookahead & errors (§15.1) | `re_more.py`, capturing groups in split, `re.subn`, `(?=...)`, `\b`/`\B`, `re.error` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-09]` | `22.30.29.jpeg` | The `time` module (§15.2) | `time_demo.py`, `perf_counter()`, `struct_time`, `strftime`/`strptime`, `tm_wday` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-10]` | `22.33.58.jpeg` | `datetime`: the four classes (§15.3) | `date`, `time`, `datetime`, `timedelta` properties, constructors & methods | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md` |
| `[Course: D14-11]` | `22.33.58m.jpeg` | `datetime`: formatting, parsing & arithmetic (§15.3) | `dates.py`, `strftime` codes (`%A`, `%B`, `%d`, `%Y`, `%H:%M`), `strptime` `ValueError`, `timedelta` math | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-12]` | `22.33.57op.jpeg` | Dates & times: exam details (§15.3–§15.5) | `dates_more.py`, `weekday()` vs `isoweekday()`, leading zeros syntax error, `timedelta` attributes, `utcnow()` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, Traps 61–63 |
| `[Course: D14-13]` | `22.33.56lo.jpeg`, `22.33.57ki.jpeg` | Creating your own module (§15.4) | `geometry.py`, `main.py`, `__name__ == "__main__"`, `import geometry`, `from geometry import circle_area` | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `examples.py` |
| `[Course: D14-14]` | `22.33.56l.jpeg`, `22.33.57.jpeg` | Lab 14.1 — Validators & a countdown timer (§15.5) | `validate.py`, compiled `PHONE`, date substitution `re.sub()`, `exam - now` timedelta countdown | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/exercises.py`, solutions |
| `[Course: D14-15]` | `22.33.56.jpeg` | Knowledge check (Assessment) | 5 exam-style MCQs: `re.match`, `\d+`, `findall` groups, `strftime` `%M` vs `%m`, calendar date rollover | `16-REGEX-DATETIME-AND-CUSTOM-MODULES/README.md`, `exercises.py` |

---

## 2. Verbatim Code & Content Transcriptions

### Slide `D14-01`: Today's Objectives & Agenda
- **Header:** `BCPD Cohort 2 • Week 3 • Day 14 • Modules Part 2: re, time, datetime, own modules`
- **By the end of today you can:**
  1. Search and match text with `re.search`, `match` and `fullmatch`
  2. Read regex syntax and extract text with groups, `findall`, `sub` and `split`
  3. Measure time with the `time` module
  4. Create, format, parse and do arithmetic with `datetime`
  5. Create your own module and use `if __name__ == "__main__"`
- **Agenda Breakdown:**
  - `15.1` re basics: search, match & fullmatch
  - `15.1` Regex syntax cheat-sheet
  - `15.1` findall, finditer, sub & split
  - `15.1` Groups, named groups & greedy matching
  - `15.1` re.compile & flags
  - `15.1` More re tools: split, subn, lookahead & errors
  - `15.2` The time module
  - `15.3` datetime: the four classes
  - `15.3` datetime: formatting, parsing & arithmetic
  - `15.2` Dates & times: exam details
  - `15.4` Creating your own module
  - `lab` Lab 14.1 - Validators & a countdown timer

---

### Slide `D14-02`: `re` Basics — search, match & fullmatch
- **Manual Ref:** `MANUAL §15.1`
- **Bullets:**
  - Write patterns as raw strings: `r"\d+"`
  - `re.search()` finds the first match anywhere
  - `re.match()` only matches at the start of the string
  - `re.fullmatch()` must match the whole string
  - Each returns a match object or `None`: use `.group()`, `.start()`, `.end()`, `.span()`
- **Code (`re_basics.py`):**
  ```python
  import re
  text = "Order 66 shipped on 2026-10-29"

  m = re.search(r"\d+", text)
  print(m.group(), m.span())            # -> 66 (6, 8)
  print(re.match(r"\d+", text))         # -> None
  print(re.match(r"Order", text).group()) # -> Order
  print(bool(re.fullmatch(r"\d{4}", "2026")))   # -> True
  print(bool(re.fullmatch(r"\d{4}", "20265")))  # -> False
  ```

---

### Slide `D14-03`: Classroom Live Demo — Banking SMS Transaction Extractor
- **IDE Context:** PyCharm / VS Code live demo on transaction parsing (`main.py`)
- **Code:**
  ```python
  import re

  TE = 20000
  sms = 'Acct:***4521 DR: NGN5,000.00 Desc: POS/IKEJA Bal: NGN42,350.75'
  m = re.search(r"DR:\s*NGN([\d,]+\.\d{2})", sms)
  if m:
      amount_str = m.group(1).replace(",", "")
      amount = float(amount_str)
      TE += amount
      print(f"Parsed Debit: {amount}, New Total Expenses: {TE}")
  ```

---

### Slide `D14-04`: Regex Syntax Cheat-Sheet
- **Manual Ref:** `MANUAL §15.1`
- **Cheat Sheet Table:**

| Pattern | Matches | Example |
|---|---|---|
| `.` | Any character except a newline | `a.c` -> `abc`, `a-c` |
| `\d \w \s` | Digit • word character `[A-Za-z0-9_]` • whitespace | `\d\d` -> `42` |
| `\D \W \S` | The opposites of the above | `\S+` -> `one word` |
| `[abc] [a-z] [^0-9]` | Character class • range • negated class | `[aeiou]` |
| `* + ?` | Zero or more • one or more • zero or one | `colou?r` |
| `{n} {m,n}` | Exactly n • between m and n | `\d{3,4}` |
| `^ $ \b` | Start • end • word boundary | `^Hi`, `\bcat\b` |
| `a\|b ( )` | Alternation • capturing group | `(cat\|dog)s?` |

---

### Slide `D14-05`: `re.compile` & Flags
- **Manual Ref:** `MANUAL §15.1`
- **Bullets:**
  - `re.compile(pattern)` builds a reusable pattern object with the same methods
  - Flags: `re.I` ignore case, `re.M` multiline, `re.S` dot matches newline, `re.X` verbose
  - With `re.M`, `^` and `$` match at every line
  - Escape user input with `re.escape()` before putting it in a pattern
- **Code (`re_flags.py`):**
  ```python
  import re
  email = re.compile(r"^[\w.-]+@[\w-]+\.[\w.]+$", re.I)
  print(bool(email.match("Ada.L@BCPD.org")))    # -> True
  print(bool(email.match("bad@address")))        # -> False

  text = "first line\nsecond line"
  print(re.findall(r"^\w+", text))             # -> ['first']
  print(re.findall(r"^\w+", text, re.M))       # -> ['first', 'second']
  print(re.escape("1+1=2"))                    # -> 1\+1\=2
  ```

---

### Slide `D14-06`: `findall`, `finditer`, `sub` & `split`
- **Manual Ref:** `MANUAL §15.1`
- **Method Breakdown:**
  - **`findall`:** Returns strings — or tuples of groups when the pattern has groups.
  - **`finditer`:** Yields match objects, so you get positions as well.
  - **`sub`:** Replaces matches; `\1`, `\2` in the replacement insert captured groups.
  - **`split`:** Splits on a pattern instead of a fixed string.
- **Code (`re_tools.py`):**
  ```python
  import re
  s = "cat 3, dog 12, owl 7"

  print(re.findall(r"\d+", s))                    # -> ['3', '12', '7']
  print(re.findall(r"(\w+) (\d+)", s))            # -> [('cat', '3'), ('dog', '12'), ('owl', '7')]
  for m in re.finditer(r"\d+", s):
      print(m.start(), end=" ")                   # -> 4 11 19
  print()
  print(re.sub(r"\d+", "@", s))                   # -> cat @, dog @, owl @
  print(re.sub(r"(\w+) (\d+)", r"\2x\1", "cat 3")) # -> 3xcat
  print(re.split(r",\s*", s))                     # -> ['cat 3', 'dog 12', 'owl 7']
  ```

---

### Slide `D14-07`: Groups, Named Groups & Greedy Matching
- **Manual Ref:** `MANUAL §15.1`
- **Concepts:**
  - **Groups `()`:** Capture parts of the match: `group(1)`, `group(2)...`; `group(0)` is the whole match.
  - **Named groups:** `(?P<name>...)` — read by name or with `groupdict()`.
  - **Greedy vs lazy:** `.+` grabs as much as possible; `.+?` as little as possible.
- **Code (`re_groups.py`):**
  ```python
  import re
  pat = r"(?P<user>\w+)@(?P<domain>[\w.]+)"
  m = re.search(pat, "mail ada@bcpd.org now")
  print(m.group(0))                    # -> ada@bcpd.org
  print(m.group(1), m.group("domain")) # -> ada bcpd.org
  print(m.groupdict())                 # -> {'user': 'ada', 'domain': 'bcpd.org'}

  html = "<b>bold</b><i>it</i>"
  print(re.findall(r"<.+>", html))     # -> ['<b>bold</b><i>it</i>']
  print(re.findall(r"<.+?>", html))    # -> ['<b>', '</b>', '<i>', '</i>']
  ```

---

## 3. Verbatim Code & Content Transcriptions: Slides D14-08 to D14-15

### Slide `D14-08`: More `re` tools: split, subn, lookahead & errors (Manual §15.1)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.30.28.jpeg` (Slide 8)
- **Side Cards:**
  - *Groups in split:* A capturing group keeps the separators in the result.
  - *subn and count:* `subn` returns `(new_string, count)`; `count=` limits replacements.
  - *Zero-width:* `(?=...)` lookahead, `\b` / `\B` boundaries, `\A` / `\Z` string start and end.
  - *Error vs no match:* A bad pattern raises `re.error`; a failed match just returns `None`.
- **Verbatim Code (`re_more.py`):**
```python
import re

print(re.split(r"(,)", "a,b,c"))
# -> ['a', ',', 'b', ',', 'c']
print(re.split(r";", "abc"))
# -> ['abc']
print(re.subn(r"\d", "#", "a1b22"))
# -> ('a#b##', 3)
print(re.sub(r"\d", "#", "a1b22", count=1))
# -> a#b22
print(re.findall(r"\w+(?=@)", "ada@x.org bo@y.ng"))
# -> ['ada', 'bo']
print(re.findall(r"\Bcat", "cat concat"))
# -> ['cat']
p = re.compile(r"(?P<y>\d{4})-(?P<m>\d\d)")
print(p.groupindex)
# -> {'y': 1, 'm': 2}
try:
    re.compile(r"(unclosed")
except re.error:
    print("re.error")
# -> re.error
print(re.match(r"x", "abc"))
# -> None
```

---

### Slide `D14-09`: The `time` module (Manual §15.2)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.30.29.jpeg` (Slide 9)
- **Core Principles:**
  - `time.time()` — seconds since the epoch (1 Jan 1970 UTC) as a float.
  - `time.sleep(s)` pauses; `time.perf_counter()` times code precisely.
  - `time.localtime()` / `time.gmtime()` return a `struct_time`.
  - `time.strftime(fmt, t)` formats; `time.strptime(text, fmt)` parses.
  - `tm_wday` counts Monday as `0`.
- **Verbatim Code (`time_demo.py`):**
```python
import time

start = time.perf_counter()
time.sleep(0.1)
elapsed = time.perf_counter() - start
print(elapsed >= 0.1)
# -> True

t = time.strptime("2026-10-29", "%Y-%m-%d")
print(t.tm_year, t.tm_mon, t.tm_wday)
# -> 2026 10 3
print(time.strftime("%d/%m/%Y", t))
# -> 29/10/2026
print(type(time.time()).__name__)
# -> float
```

---

### Slide `D14-10`: `datetime`: the four classes (Manual §15.3)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.33.58.jpeg` (Slide 10)
- **Class Reference Table:**
  | Class | Represents | Create | Useful members |
  |---|---|---|---|
  | `date` | A calendar date | `date(2026, 10, 29)`, `date.today()` | `.year`, `.month`, `.day`, `.weekday()` |
  | `time` | A time of day | `time(14, 30)` | `.hour`, `.minute`, `.second` |
  | `datetime` | Date and time | `datetime(2026, 10, 29, 14, 30)`, `datetime.now()` | `.date()`, `.time()`, `.strftime()` |
  | `timedelta` | A duration | `timedelta(days=7, hours=3)` | `.days`, `.seconds`, `.total_seconds()` |
- **Rule:** *Subtracting two dates gives a `timedelta`; adding a `timedelta` to a date gives a new date.*

---

### Slide `D14-11`: `datetime`: formatting, parsing & arithmetic (Manual §15.3)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.33.58m.jpeg` (Slide 11)
- **Directives Reference:**
  - `strftime codes`: `%Y` year, `%m` month, `%d` day, `%H:%M` time, `%A` weekday name, `%B` month name.
  - `strptime`: The format must match the text exactly, or you get `ValueError`.
  - `Arithmetic`: `date + timedelta -> date`; `date - date -> timedelta`.
- **Verbatim Code (`dates.py`):**
```python
from datetime import date, datetime, timedelta

dt = datetime(2026, 10, 29, 14, 5)
print(dt.strftime("%A %d %B %Y, %H:%M"))
# -> Thursday 29 October 2026, 14:05

parsed = datetime.strptime("04/12/2026", "%d/%m/%Y")
print(parsed.date())
# -> 2026-12-04
print(parsed - dt)
# -> 35 days, 9:55:00
print(date(2026, 10, 29) + timedelta(weeks=1))
# -> 2026-11-05
age = date(2026, 10, 29) - date(2000, 3, 15)
print(age.days // 365)
# -> 26
print(date(2026, 10, 29).isoformat())
# -> 2026-10-29
```

---

### Slide `D14-12`: Dates & times: exam details (Manual §15.3–§15.5)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.33.57op.jpeg` (Slide 12)
- **Core Exam Traps:**
  - `weekday()`: Monday = `0`; `isoweekday()`: Monday = `1`
  - Leading zeros such as `09` are a `SyntaxError` — write `9`
  - `timedelta` stores `days`, `seconds` and `microseconds` — there is no `.hours`
  - `struct_time` works like a tuple: `t[0]` is the year; `time.asctime()` formats it
  - `utcnow()` is deprecated — use `datetime.now(timezone.utc)`
- **Verbatim Code (`dates_more.py`):**
```python
from datetime import date, datetime, timedelta, timezone
import time

d = date(2026, 11, 13)  # Note: date(2026, 11, 09) raises SyntaxError!
print(d.weekday(), d.isoweekday())
# -> 4 5
gap = date(2026, 12, 25) - d
print(gap.days, hasattr(gap, "hours"))
# -> 42 False
td = timedelta(hours=36)
print(td.days, td.seconds)
# -> 1 43200
t = time.localtime()
print(t[0] == t.tm_year)
# -> True
s = time.strptime("2026-11-13", "%Y-%m-%d")
print(time.asctime(s))
# -> Fri Nov 13 00:00:00 2026
print(datetime.now(timezone.utc).tzinfo)
# -> UTC
```

---

### Slide `D14-13`: Creating your own module (Manual §15.4)
- **Source Files:** `WhatsApp Image 2026-11-25 at 22.33.56lo.jpeg`, `22.33.57ki.jpeg` (Slide 13)
- **Core Principles:**
  - Any `.py` file is a module; its name is the file name without `.py`.
  - `__name__` is `"__main__"` when a file is run directly, and the module name when imported.
  - Put demo or test code under `if __name__ == "__main__":` so it doesn't run on import.
  - A folder of modules with `__init__.py` is a package (Day 15).
- **Verbatim Code (`geometry.py` + `main.py`):**
```python
# geometry.py
PI = 3.14159

def circle_area(r):
    return PI * r * r

if __name__ == "__main__":
    print("Self-test:", circle_area(1))

# main.py
import geometry
from geometry import circle_area

print(geometry.PI)
print(circle_area(2))
```

---

### Slide `D14-14`: Lab 14.1 — Validators & a countdown timer (Manual §15.5)
- **Source Files:** `WhatsApp Image 2026-11-25 at 22.33.56l.jpeg`, `22.33.57.jpeg` (Slide 14)
- **Lab Requirements:**
  1. `is_valid_email()` and `is_valid_phone()` (e.g. `+234 801 234 5678`) with compiled patterns; test 5 good, 5 bad.
  2. Find every `YYYY-MM-DD` date in a paragraph and rewrite them as `DD/MM/YYYY` with `sub` and groups.
  3. Age calculator: parse a birth date with `strptime` and print the age in years and days.
  4. Countdown: days, hours and minutes until the Week 3 assessment (`Fri 27 Nov 2026, 14:00`).
- **Verbatim Classroom Implementation (`validate.py`):**
```python
import re
from datetime import datetime

# 1. Phone validation
PHONE = re.compile(r"^\+?\d{3}\s?\d{3}\s?\d{3}\s?\d{4}$")
print(bool(PHONE.match("+234 801 234 5678")))
# -> True

# 2. Rewrite date format via substitution
text = "Due 2026-11-13, resit 2026-11-20."
DATE = r"(\d{4})-(\d{2})-(\d{2})"
print(re.sub(DATE, r"\3/\2/\1", text))
# -> Due 13/11/2026, resit 20/11/2026.

# 3. Assessment countdown
exam = datetime(2026, 11, 13, 14, 0)
left = exam - datetime(2026, 11, 12, 9, 30)
print(left)
# -> 1 day, 4:30:00
```

---

### Slide `D14-15`: Classroom Knowledge Check (Assessment)
- **Source File:** `WhatsApp Image 2026-11-25 at 22.33.56.jpeg` (Slide 15)
- **Questions & Official Solutions:**
  1. **Q1:** `Output of print(re.match(r"\d", "a1"))?`
     - Options: `A: A match object`, `B: 1`, `C: None`, `D: a`
     - **Answer: C (None)**. `re.match()` tests only at the beginning of the string (`'a'` is not a digit).
  2. **Q2:** `Which pattern matches one or more digits?`
     - Options: `A: \d*`, `B: \d+`, `C: \d?`, `D: [d]+`
     - **Answer: B (\d+)**. `+` quantifier matches 1 or more occurrences.
  3. **Q3:** `What does re.findall(r"(\w)(\d)", "a1 b2") return?`
     - Options: `A: [('a', '1'), ('b', '2')]`, `B: ['a1', 'b2']`, `C: ['a', 'b']`, `D: None`
     - **Answer: A ([('a', '1'), ('b', '2')])**. When multiple capturing groups are present, `findall` returns a list of tuples containing the matched groups.
  4. **Q4:** `In a strftime format, which code gives the minutes?`
     - Options: `A: %m`, `B: %n`, `C: %M`, `D: %I`
     - **Answer: C (%M)**. `%M` represents minutes (00–59), while `%m` represents month (01–12).
  5. **Q5:** `Output of print(date(2026, 1, 31) + timedelta(days=1))?`
     - Options: `A: 2026-01-32`, `B: 2026-1-32`, `C: Error`, `D: 2026-02-01`
     - **Answer: D (2026-02-01)**. `timedelta` arithmetic correctly rolls over the calendar month into February.

