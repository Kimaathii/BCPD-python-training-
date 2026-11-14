"""Module 01 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-22, IMG-25, IMG-26, IMG-29, IMG-56
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def format_iso_date() -> str:
    """Return '2026-11-12' using a single expression or print-style sep logic.

    Hint: Try printing print(2026, 11, 12, sep='-') in the REPL first,
    then implement this helper to return the same string.
    """
    # TODO: return "2026-11-12" built from (2026, 11, 12)
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (Lab 1.1 & 1.2 â€” IMG-25)
# -----------------------------------------------------------------------------
def greet_message(name: str) -> str:
    """Lab 1.1: Given a user's name (possibly with extra whitespace), return 'Hello, <name>!'."""
    # TODO: strip surrounding whitespace and return greeting
    raise NotImplementedError


def safe_divide_report(raw_a: str, raw_b: str) -> str:
    """Lab 1.2 extension: Parse raw_a and raw_b as floats and return 'Quotient: <val>'.

    If either input is non-numeric, return 'Invalid number'.
    If raw_b is zero, return 'Cannot divide by zero'.
    """
    # TODO: implement guarded parsing and division
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving
# -----------------------------------------------------------------------------
def build_summary_line(student_name: str, raw_score: str, pass_mark: int = 70) -> str:
    """Convert raw_score to int and return '<Name>: <score>/100 (PASS|FAIL)'.

    Note: BCPD pass mark is 70 [IMG-56]. Strip whitespace from student_name
    and title-case it.
    """
    # TODO: implement summary builder
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning (Spot & Fix Bugs Without Running First)
# -----------------------------------------------------------------------------
# Examine each snippet below mentally before coding:
#
# Bug A:
#   age = input("Age: ")
#   next_year = age + 1
#
# Bug B:
#   if True:
#   print("Inside block")
#
# Bug C:
#   1st_student = "Ada"
#   total-score = 95
#
def describe_bug_fixes() -> dict[str, str]:
    """Return a dict mapping 'Bug A', 'Bug B', 'Bug C' to the exact exception name
    Python raises for each ('TypeError', 'IndentationError', or 'SyntaxError')."""
    # TODO: fill in the three exception names
    raise NotImplementedError
