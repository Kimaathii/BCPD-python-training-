"""Solutions for Module 02 Exercises (02-TYPES-VARIABLES-AND-TRUTHINESS/exercises.py).

Target Python: 3.10+
"""

import math


def parse_binary_and_hex(bin_str: str, hex_str: str) -> tuple[int, int]:
    """Convert binary and hexadecimal strings to base-10 integers."""
    return int(bin_str, 2), int(hex_str, 16)


def bare_bin_hex(n: int) -> tuple[str, str]:
    """Return binary and hex strings without '0b' / '0x' prefixes."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return bin(n)[2:], hex(n)[2:]


def safe_to_int(value: str) -> int | None:
    """Convert integer or decimal string to int; return None on invalid/non-finite input."""
    text = value.strip()
    try:
        return int(text)
    except ValueError:
        try:
            num = float(text)
        except ValueError:
            return None
        if not math.isfinite(num):
            return None
        return int(num)


def split_by_truthiness(items: list[object]) -> tuple[list[object], list[object]]:
    """Partition items into (truthy, falsy) while preserving order."""
    truthy: list[object] = []
    falsy: list[object] = []
    for item in items:
        if item:
            truthy.append(item)
        else:
            falsy.append(item)
    return truthy, falsy


def nearly_equal(a: float, b: float) -> bool:
    """Compare two floats safely with math.isclose."""
    return math.isclose(a, b)


def predict_trap_values() -> dict[str, object]:
    """Exact Python evaluation values for each trap."""
    return {
        "comma_literal": (1, 0, 0),
        "round_half_even": 2,
        "round_binary_quirk": 2.67,
        "str_zero_bool": True,
        "float_eq": False,
    }


if __name__ == "__main__":
    assert parse_binary_and_hex("1010", "ff") == (10, 255)
    assert bare_bin_hex(42) == ("101010", "2a")
    assert safe_to_int("42") == 42
    assert safe_to_int("3.9") == 3
    assert safe_to_int("inf") is None
    assert safe_to_int("abc") is None
    assert split_by_truthiness([0, "0", "", [], [0], None, False, " "]) == (
        ["0", [0], " "],
        [0, "", [], None, False],
    )
    assert nearly_equal(0.1 + 0.2, 0.3) is True
    assert predict_trap_values() == {
        "comma_literal": (1, 0, 0),
        "round_half_even": 2,
        "round_binary_quirk": 2.67,
        "str_zero_bool": True,
        "float_eq": False,
    }
    print("All Module 02 solution assertions passed.")
