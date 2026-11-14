"""Module 04 Examples â€” Conditionals, Logic, Identity & Pattern Matching.

Sources: IMG-32, IMG-36, IMG-37, IMG-38, IMG-45 (Week 1 Â· Day 3)
Target Python: 3.10+
"""


# =============================================================================
# 1. ORIGINAL CLASSROOM CODE: compare.py [Source: IMG-32]
# =============================================================================
def original_compare_demo() -> None:
    """Reproduces compare.py from IMG-32 verbatim."""
    a = [1, 2]
    b = [1, 2]
    print(a == b, a is b)     # -> True False
    c = a
    print(c is a)             # -> True
    x = 7
    print(1 < x < 10)         # -> True
    print("Z" < "a")          # -> True
    print(3 == 3.0)           # -> True
    x = None
    print(x is None)          # -> True


# =============================================================================
# 2. ORIGINAL CLASSROOM CODE: grade.py [Source: IMG-36]
# =============================================================================
def original_grade_demo(score: int = 72) -> tuple[str, str]:
    """Reproduces grade.py from IMG-36 verbatim."""
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    print(grade)                                  # -> B

    status = "pass" if score >= 60 else "fail"
    print(status)                                 # -> pass
    return grade, status


# =============================================================================
# 3. ORIGINAL CLASSROOM CODE: logic.py [Source: IMG-37]
# =============================================================================
def original_logic_demo() -> None:
    """Reproduces logic.py from IMG-37 verbatim."""
    print(True and False)              # -> False
    print(0 or "default")              # -> default
    print(repr("" and "x"))            # -> ''
    print(5 and 10)                    # -> 10
    print(any([3 > 5, 8 > 5]))         # -> True
    print(all([1, 2, 0]))              # -> False
    age, has_id = 20, True
    print(age >= 18 and has_id)        # -> True


# =============================================================================
# 4. ORIGINAL CLASSROOM CODE: commands.py (Python 3.10+) [Source: IMG-38]
# =============================================================================
def original_match_demo(cmd: str = "go north", point: tuple[int, int] = (3, 0)) -> tuple[str, str]:
    """Reproduces match-case from IMG-38 verbatim."""
    cmd_result = ""
    match cmd.split():
        case ["quit"]:
            cmd_result = "Bye"
        case ["go", direction]:
            cmd_result = f"Moving {direction}"
        case ["look" | "inspect"]:
            cmd_result = "You see a door"
        case _:
            cmd_result = "Unknown command"

    point_result = ""
    match point:
        case (0, 0):
            point_result = "origin"
        case (x, 0) if x > 0:
            point_result = "on the +x axis"
        case _:
            point_result = "elsewhere"

    print(cmd_result)
    print(point_result)
    return cmd_result, point_result


# =============================================================================
# 5. LAB 3.1 HELPERS [Source: IMG-45]
# =============================================================================
def compute_leap_year(year: int) -> bool:
    """Lab 3.1 step 2: Divisible by 4 and not by 100, or divisible by 400."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    original_compare_demo()
    assert original_grade_demo(72) == ("B", "pass")
    original_logic_demo()
    assert original_match_demo("go north", (3, 0)) == ("Moving north", "on the +x axis")
    assert original_match_demo("look", (0, 0)) == ("You see a door", "origin")

    assert compute_leap_year(2024) is True
    assert compute_leap_year(1900) is False
    assert compute_leap_year(2000) is True
    print("Module 04 assertions passed.")
