"""Solutions for Module 01 Exercises (01-FOUNDATIONS-AND-ENV/exercises.py).

Target Python: 3.10+
"""


def format_iso_date() -> str:
    """Return '2026-11-12' built from integer components."""
    year, month, day = 2026, 11, 12
    return f"{year}-{month}-{day}"


def greet_message(name: str) -> str:
    """Lab 1.1: Clean whitespace and return greeting."""
    return f"Hello, {name.strip()}!"


def safe_divide_report(raw_a: str, raw_b: str) -> str:
    """Lab 1.2 extension: Guard against ValueError and ZeroDivisionError."""
    try:
        a = float(raw_a)
        b = float(raw_b)
    except ValueError:
        return "Invalid number"

    if b == 0:
        return "Cannot divide by zero"
    return f"Quotient: {a / b}"


def build_summary_line(student_name: str, raw_score: str, pass_mark: int = 70) -> str:
    """Parse score and format '<Name>: <score>/100 (PASS|FAIL)'."""
    clean_name = student_name.strip().title()
    score = int(raw_score.strip())
    status = "PASS" if score >= pass_mark else "FAIL"
    return f"{clean_name}: {score}/100 ({status})"


def describe_bug_fixes() -> dict[str, str]:
    """Exact exception names raised by Bugs A, B, and C."""
    return {
        "Bug A": "TypeError",         # str + int fails without int(age)
        "Bug B": "IndentationError",  # missing indent after ':'
        "Bug C": "SyntaxError",       # leading digit & hyphen in variable names
    }


if __name__ == "__main__":
    assert format_iso_date() == "2026-11-12"
    assert greet_message("  ada  ") == "Hello, ada!"
    assert safe_divide_report("10", "4") == "Quotient: 2.5"
    assert safe_divide_report("10", "0") == "Cannot divide by zero"
    assert safe_divide_report("ten", "2") == "Invalid number"
    assert build_summary_line("  ada lovelace ", "72") == "Ada Lovelace: 72/100 (PASS)"
    assert build_summary_line("bo", "69") == "Bo: 69/100 (FAIL)"
    assert describe_bug_fixes() == {
        "Bug A": "TypeError",
        "Bug B": "IndentationError",
        "Bug C": "SyntaxError",
    }
    print("All Module 01 solution assertions passed.")
