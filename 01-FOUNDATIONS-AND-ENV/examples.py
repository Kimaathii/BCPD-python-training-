"""Module 01 Examples â€” Python Environment, I/O, and First Programs.

Sources: IMG-21, IMG-22, IMG-24, IMG-25, IMG-56 (Week 1 Â· Day 1)
Target Python: 3.10+
"""


# =============================================================================
# 1. ORIGINAL CLASSROOM CODE: io_demo.py [Source: IMG-22]
# =============================================================================
def original_print_demo() -> None:
    """Reproduces the print() examples from IMG-22 verbatim."""
    print("a", "b", "c")           # -> a b c
    print("a", "b", sep="-")       # -> a-b
    print("Loading", end="...")
    print("done")                  # -> Loading...done


def original_input_demo_interactive() -> None:
    """Reproduces the interactive input() snippet from IMG-22 verbatim."""
    age = input("Age: ")           # e.g. user types 20
    print(type(age))               # <class 'str'>
    age = int(age)
    print(age + 1)                 # 21


# =============================================================================
# 2. ORIGINAL CLASSROOM CODE: calc.py [Source: IMG-25]
# =============================================================================
def original_calc_interactive() -> None:
    """Reproduces Lab 1.2 calc.py from IMG-25 verbatim."""
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Quotient:", a / b)      # Raises ZeroDivisionError if b == 0.0


# =============================================================================
# 3. CORRECTED / IMPROVED CODE [Supplementary]
# =============================================================================
def improved_calc(raw_a: str, raw_b: str) -> dict[str, float | str] | None:
    """Safely computes sum, difference, product, and quotient from string inputs.

    Guards against ValueError (invalid float text) and ZeroDivisionError (b == 0).
    """
    try:
        a = float(raw_a)
        b = float(raw_b)
    except ValueError:
        return None

    quotient: float | str = "undefined (division by zero)" if b == 0 else a / b
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": quotient,
    }


def pep8_and_print_return_demo() -> None:
    """Demonstrates PEP 8 naming [IMG-56] and print() returning None [Supplementary]."""
    student_count = 30             # snake_case for variables
    MAX_SCORE = 100                # UPPER_CASE for constants

    class ExamSession:             # PascalCase for classes
        pass

    returned_value = print(f"Students: {student_count}, Max: {MAX_SCORE}")
    assert returned_value is None
    assert ExamSession.__name__ == "ExamSession"


if __name__ == "__main__":
    original_print_demo()
    pep8_and_print_return_demo()

    assert improved_calc("10", "2") == {
        "sum": 12.0,
        "difference": 8.0,
        "product": 20.0,
        "quotient": 5.0,
    }
    assert improved_calc("10", "0")["quotient"] == "undefined (division by zero)"
    assert improved_calc("abc", "2") is None
    print("Module 01 non-interactive assertions passed.")
