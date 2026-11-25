# Day 14 New Classroom Screenshot Inventory & Verbatim Extractions
**Class Date:** Tuesday 24 Nov 2026 (Week 3, Day 14)  
**Subject:** Modules Part 2: `re`, `time`, `datetime`, own modules  
**BCPD Exam Weight:** Domain 4 · Modules & Libraries (15%)  
**Student Manual Mapping:** Day 15 · §15.1–15.4  
**Image Files Staged:** 8 JPEG files (`WhatsApp Image 2026-11-24 at 21.56.53.jpeg` to `21.57.00.jpeg`)  
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

## 3. Supplementary Syllabus Topics Transcribed from Agenda (`D14-01`)

### §15.2 The `time` Module & Exam Details
- `time.time()`: Returns current Unix epoch time in seconds as float. (Subject to wall-clock adjustment).
- `time.sleep(secs)`: Suspends execution of current thread for `secs` seconds (float or int).
- `time.perf_counter()`: High-resolution monotonic clock with smallest available sleep/interval resolution, immune to system time updates.

### §15.3 The `datetime` Module: Classes, Formatting & Arithmetic
- **The Four Classes:**
  1. `datetime.date(year, month, day)`: Gregorian calendar date.
  2. `datetime.time(hour, minute, second, microsecond)`: Wall-clock time independent of date.
  3. `datetime.datetime(year, month, day, hour, minute, second)`: Combined date and time.
  4. `datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`: Duration / delta between timestamps.
- **Formatting & Parsing:**
  - `dt.strftime(format)`: Format object to string (`%Y-%m-%d %H:%M:%S`).
  - `datetime.strptime(date_string, format)`: Parse string to datetime object.
- **Exam Pitfalls:**
  - `timedelta` only internally stores `days`, `seconds`, and `microseconds`.
  - `timedelta(days=1, seconds=10).seconds` == `10`, whereas `.total_seconds()` == `86410.0`.

### §15.4 Creating Your Own Module & `if __name__ == "__main__":`
- Module file naming and import mechanics.
- Top-level execution on first import.
- Guarding execution scripts vs reusable library modules with `if __name__ == "__main__":`.

### Lab 14.1 — Validators & a Countdown Timer
- **Part A:** Building input validation routines (Email, Phone, Transaction SMS parsing) using compiled regular expressions.
- **Part B:** Building an event countdown timer calculating days, hours, minutes, and seconds until the BCPD exam using `datetime.now()` and `timedelta`.
