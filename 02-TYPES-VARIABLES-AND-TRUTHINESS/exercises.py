"""Module 02 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-06, IMG-09, IMG-11, IMG-12, IMG-30, IMG-32
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def parse_binary_and_hex(bin_str: str, hex_str: str) -> tuple[int, int]:
    """Convert a binary string (e.g. '1010') and hex string (e.g. 'ff') to ints."""
    # TODO: use int(text, base)
    raise NotImplementedError


def bare_bin_hex(n: int) -> tuple[str, str]:
    """Return (binary_without_0b, hex_without_0x) for non-negative int n."""
    # TODO: convert with bin()/hex() or formatting and strip prefix
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application
# -----------------------------------------------------------------------------
def safe_to_int(value: str) -> int | None:
    """Convert numeric string to int.

    Must handle both integer strings ('42' -> 42) and decimal strings
    ('3.9' -> 3, truncated like int(float('3.9'))). Return None for invalid text
    or inf/nan.
    """
    # TODO: implement safe conversion
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving
# -----------------------------------------------------------------------------
def split_by_truthiness(items: list[object]) -> tuple[list[object], list[object]]:
    """Return (truthy_items, falsy_items) preserving original order."""
    # TODO: classify each item using truthiness
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning
# -----------------------------------------------------------------------------
def nearly_equal(a: float, b: float) -> bool:
    """Return True if two floats are equal within standard relative tolerance."""
    # TODO: use math.isclose
    raise NotImplementedError


def predict_trap_values() -> dict[str, object]:
    """Without running first, fill in the exact Python values for each key:
      - 'comma_literal': type(1,000,000) is tuple -> exact value of (1,000,000)
      - 'round_half_even': round(2.5)
      - 'round_binary_quirk': round(2.675, 2)
      - 'str_zero_bool': bool("0")
      - 'float_eq': (0.1 + 0.2 == 0.3)
    """
    # TODO: replace None placeholders with your predicted values
    return {
        "comma_literal": None,
        "round_half_even": None,
        "round_binary_quirk": None,
        "str_zero_bool": None,
        "float_eq": None,
    }
