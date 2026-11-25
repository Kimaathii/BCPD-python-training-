"""Module 16 Executable Reference Examples.

Covers:
- re basics: search, match, fullmatch, match objects [Course: D14-02]
- Classroom Live Demo: Banking transaction SMS parser [Course: D14-03]
- Regex syntax metacharacters, character classes, anchors [Course: D14-04]
- re.compile, flags (re.I, re.M, re.S), re.escape [Course: D14-05]
- findall, finditer, sub with backreferences, split [Course: D14-06]
- Groups, named groups, groupdict, greedy vs lazy [Course: D14-07]
- time module (time.time, time.perf_counter, time.sleep) [Course: D14-01]
- datetime module (date, time, datetime, timedelta, strftime, strptime) [Course: D14-01]
- Custom module execution guard (if __name__ == "__main__":) [Course: D14-01]
"""

from __future__ import annotations

import re
import time
from datetime import date, datetime, timedelta


# ------------------------------------------------------------------------------
# 1. Slide D14-02: re Basics (search, match, fullmatch)
# ------------------------------------------------------------------------------
def demonstrate_re_basics() -> None:
    print("=" * 60)
    print("1. DEMONSTRATING RE BASICS [Course: D14-02]")
    print("=" * 60)

    text = "Order 66 shipped on 2026-10-29"

    # search finds first match anywhere
    m = re.search(r"\d+", text)
    assert m is not None
    print(f"re.search group: {m.group()!r}, span: {m.span()}")
    assert m.group() == "66"
    assert m.span() == (6, 8)

    # match only checks index 0
    m_start = re.match(r"\d+", text)
    print(f"re.match(r'\\d+', text): {m_start}")
    assert m_start is None

    m_order = re.match(r"Order", text)
    assert m_order is not None
    print(f"re.match(r'Order', text).group(): {m_order.group()!r}")
    assert m_order.group() == "Order"

    # fullmatch checks complete string
    assert bool(re.fullmatch(r"\d{4}", "2026")) is True
    assert bool(re.fullmatch(r"\d{4}", "20265")) is False
    print("re.fullmatch verification: PASSED")


# ------------------------------------------------------------------------------
# 2. Slide D14-03: Classroom Live Bank SMS Transaction Parser
# ------------------------------------------------------------------------------
def parse_bank_sms_alert(sms: str) -> dict:
    """Parse transaction SMS alert into structured data using regex."""
    pat = (
        r"Acct:\s*\*{3}(?P<acct>\d{4})\s+"
        r"(?P<type>DR|CR):\s*(?P<cur>[A-Z]{3})(?P<amount>[\d,]+\.\d{2})\s+"
        r"Desc:\s*(?P<desc>[^B]+)\s+"
        r"Bal:\s*(?P<bal_cur>[A-Z]{3})(?P<balance>[\d,]+\.\d{2})"
    )
    m = re.search(pat, sms)
    if not m:
        raise ValueError("Unrecognized SMS alert format")
    d = m.groupdict()
    d["amount"] = float(d["amount"].replace(",", ""))
    d["balance"] = float(d["balance"].replace(",", ""))
    return d


def demonstrate_bank_sms_parser() -> None:
    print("\n" + "=" * 60)
    print("2. CLASSROOM LIVE BANK SMS PARSER [Course: D14-03]")
    print("=" * 60)

    sms = "Acct:***4521 DR: NGN5,000.00 Desc: POS/IKEJA Bal: NGN42,350.75"
    parsed = parse_bank_sms_alert(sms)
    print("Parsed Transaction Alert:")
    for k, v in parsed.items():
        print(f"  {k}: {v}")

    assert parsed["acct"] == "4521"
    assert parsed["type"] == "DR"
    assert parsed["amount"] == 5000.0
    assert parsed["balance"] == 42350.75
    print("Bank SMS Parser: VERIFIED")


# ------------------------------------------------------------------------------
# 3. Slide D14-05: re.compile & Flags (re.I, re.M, re.escape)
# ------------------------------------------------------------------------------
def demonstrate_compile_and_flags() -> None:
    print("\n" + "=" * 60)
    print("3. RE.COMPILE & FLAGS [Course: D14-05]")
    print("=" * 60)

    # Precompiled case-insensitive pattern
    email_pat = re.compile(r"^[\w.-]+@[\w-]+\.[\w.]+$", re.I)
    assert bool(email_pat.match("Ada.L@BCPD.org")) is True
    assert bool(email_pat.match("bad@address")) is False
    print("Case-insensitive email match: PASSED")

    # Multiline flag (re.M)
    multiline_text = "first line\nsecond line"
    single_line_matches = re.findall(r"^\w+", multiline_text)
    multiline_matches = re.findall(r"^\w+", multiline_text, re.M)

    print(f"Without re.M: {single_line_matches}")  # ['first']
    print(f"With re.M:    {multiline_matches}")     # ['first', 'second']
    assert single_line_matches == ["first"]
    assert multiline_matches == ["first", "second"]

    # re.escape (In Python 3.7+, only regex metacharacters like + are escaped)
    escaped = re.escape("1+1=2")
    print(f"re.escape('1+1=2'): {escaped}")
    assert escaped == r"1\+1=2"


# ------------------------------------------------------------------------------
# 4. Slide D14-06: findall, finditer, sub & split
# ------------------------------------------------------------------------------
def demonstrate_re_tools() -> None:
    print("\n" + "=" * 60)
    print("4. RE TOOLS: FINDALL, FINDITER, SUB & SPLIT [Course: D14-06]")
    print("=" * 60)

    s = "cat 3, dog 12, owl 7"

    # findall with 0 groups -> list[str]
    nums = re.findall(r"\d+", s)
    print(f"findall (0 groups): {nums}")
    assert nums == ["3", "12", "7"]

    # findall with 2 groups -> list[tuple[str, str]]
    pairs = re.findall(r"(\w+) (\d+)", s)
    print(f"findall (2 groups): {pairs}")
    assert pairs == [("cat", "3"), ("dog", "12"), ("owl", "7")]

    # finditer yields match objects with start/end spans
    spans = [m.start() for m in re.finditer(r"\d+", s)]
    print(f"finditer starts: {spans}")
    assert spans == [4, 11, 19]

    # sub with backreferences (\1, \2)
    masked = re.sub(r"\d+", "@", s)
    print(f"sub mask: {masked}")
    assert masked == "cat @, dog @, owl @"

    swapped = re.sub(r"(\w+) (\d+)", r"\2x\1", "cat 3")
    print(f"sub group swap: {swapped}")
    assert swapped == "3xcat"

    # split
    tokens = re.split(r",\s*", s)
    print(f"split: {tokens}")
    assert tokens == ["cat 3", "dog 12", "owl 7"]


# ------------------------------------------------------------------------------
# 5. Slide D14-07 & D14-08: Groups, Named Groups, Greedy vs Lazy & Advanced re
# ------------------------------------------------------------------------------
def demonstrate_groups_and_greediness() -> None:
    print("\n" + "=" * 60)
    print("5. GROUPS, NAMED GROUPS, GREEDY VS LAZY & ADVANCED RE [Course: D14-07, D14-08]")
    print("=" * 60)

    # Named capture groups and groupdict
    pat = r"(?P<user>\w+)@(?P<domain>[\w.]+)"
    m = re.search(pat, "mail ada@bcpd.org now")
    assert m is not None

    print(f"Group 0: {m.group(0)}")
    print(f"Group 1 & domain: {m.group(1)} {m.group('domain')}")
    print(f"groupdict(): {m.groupdict()}")

    assert m.group(0) == "ada@bcpd.org"
    assert m.group(1) == "ada"
    assert m.group("domain") == "bcpd.org"
    assert m.groupdict() == {"user": "ada", "domain": "bcpd.org"}

    # Greedy (.+) vs Lazy (.+?)
    html = "<b>bold</b><i>it</i>"
    greedy_tags = re.findall(r"<.+>", html)
    lazy_tags = re.findall(r"<.+?>", html)

    print(f"Greedy <.+>:   {greedy_tags}")
    print(f"Lazy   <.+?>:  {lazy_tags}")

    assert greedy_tags == ["<b>bold</b><i>it</i>"]
    assert lazy_tags == ["<b>", "</b>", "<i>", "</i>"]

    # --- Verbatim re_more.py [Course: D14-08] ---
    # Capturing group in split retains delimiters
    split_with_delim = re.split(r"(,)", "a,b,c")
    assert split_with_delim == ["a", ",", "b", ",", "c"]

    # re.subn returns (new_string, number_of_subs_made)
    subn_res, subn_count = re.subn(r"\d", "#", "a1b22")
    assert (subn_res, subn_count) == ("a#b##", 3)

    # count parameter limits replacements
    sub_count1 = re.sub(r"\d", "#", "a1b22", count=1)
    assert sub_count1 == "a#b22"

    # Positive lookahead (?=...)
    lookahead_matches = re.findall(r"\w+(?=@)", "ada@x.org bo@y.ng")
    assert lookahead_matches == ["ada", "bo"]

    # Non-word boundary \B
    b_matches = re.findall(r"\Bcat", "cat concat")
    assert b_matches == ["cat"]  # matches "cat" inside "concat"

    # Compiled groupindex mapping
    p = re.compile(r"(?P<y>\d{4})-(?P<m>\d\d)")
    assert p.groupindex == {"y": 1, "m": 2}

    # Malformed pattern raises re.error
    try:
        re.compile(r"(unclosed")
        re_error_caught = False
    except re.error:
        re_error_caught = True
    assert re_error_caught is True

    # Failed match returns None
    assert re.match(r"x", "abc") is None
    print("re_more.py Verbatim Checks: PASSED")


# ------------------------------------------------------------------------------
# 6. Slides D14-09, D14-10, D14-11, D14-12: Time, DateTime & Exam Traps
# ------------------------------------------------------------------------------
def demonstrate_time_and_datetime() -> None:
    print("\n" + "=" * 60)
    print("6. TIME & DATETIME OPERATIONS [Course: D14-09, D14-10, D14-11, D14-12]")
    print("=" * 60)

    # --- Verbatim time_demo.py [Course: D14-09] ---
    start = time.perf_counter()
    time.sleep(0.005)  # small pause for testing
    elapsed = time.perf_counter() - start
    assert elapsed >= 0.001
    assert type(time.time()).__name__ == "float"

    t = time.strptime("2026-10-29", "%Y-%m-%d")
    assert (t.tm_year, t.tm_mon, t.tm_wday) == (2026, 10, 3)
    assert time.strftime("%d/%m/%Y", t) == "29/10/2026"
    print("time_demo.py Verbatim Checks: PASSED")

    # --- Verbatim dates.py [Course: D14-11] ---
    dt = datetime(2026, 10, 29, 14, 5)
    formatted = dt.strftime("%A %d %B %Y, %H:%M")
    assert formatted == "Thursday 29 October 2026, 14:05"

    parsed = datetime.strptime("04/12/2026", "%d/%m/%Y")
    assert parsed.date() == date(2026, 12, 4)
    diff = parsed - dt
    assert diff.days == 35

    assert date(2026, 10, 29) + timedelta(weeks=1) == date(2026, 11, 5)
    age = date(2026, 10, 29) - date(2000, 3, 15)
    assert age.days // 365 == 26
    assert date(2026, 10, 29).isoformat() == "2026-10-29"
    print("dates.py Verbatim Checks: PASSED")

    # --- Verbatim dates_more.py & Exam Traps [Course: D14-12] ---
    d = date(2026, 11, 13)
    # TRAP: weekday() is Monday=0, isoweekday() is Monday=1!
    assert (d.weekday(), d.isoweekday()) == (4, 5)

    gap = date(2026, 12, 25) - d
    assert gap.days == 42
    # TRAP: timedelta has NO .hours attribute!
    assert hasattr(gap, "hours") is False

    td = timedelta(hours=36)
    assert (td.days, td.seconds) == (1, 43200)

    t_local = time.localtime()
    assert t_local[0] == t_local.tm_year

    s_time = time.strptime("2026-11-13", "%Y-%m-%d")
    assert time.asctime(s_time) == "Fri Nov 13 00:00:00 2026"

    from datetime import timezone
    assert datetime.now(timezone.utc).tzinfo == timezone.utc
    print("dates_more.py Verbatim Checks & Traps: PASSED")


# ------------------------------------------------------------------------------
# 7. Slide D14-13: Creating Your Own Module (__name__ == "__main__")
# ------------------------------------------------------------------------------
def demonstrate_custom_module_mechanics() -> None:
    print("\n" + "=" * 60)
    print("7. CUSTOM MODULE EXECUTION GUARD [Course: D14-13]")
    print("=" * 60)

    # Emulate geometry.py mechanics
    PI = 3.14159

    def circle_area(r: float) -> float:
        return PI * r * r

    assert round(circle_area(1), 5) == 3.14159
    assert round(circle_area(2), 5) == 12.56636
    print("geometry.py area calculations: VERIFIED")


def run_all_module_16_examples() -> None:
    demonstrate_re_basics()
    demonstrate_bank_sms_parser()
    demonstrate_compile_and_flags()
    demonstrate_re_tools()
    demonstrate_groups_and_greediness()
    demonstrate_time_and_datetime()
    demonstrate_custom_module_mechanics()
    print("\n" + "=" * 60)
    print("✅ ALL MODULE 16 EXAMPLES EXECUTED SUCCESSFULLY")
    print("=" * 60)


def main() -> None:
    run_all_module_16_examples()


if __name__ == "__main__":
    main()
