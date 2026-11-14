"""Module 03 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-07, IMG-08, IMG-10, IMG-11, IMG-13, IMG-14, IMG-18, IMG-20, IMG-30
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def floor_and_mod_pair(a: int, b: int) -> tuple[int, int]:
    """Return (a // b, a % b) using divmod."""
    # TODO: implement using divmod
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (Lab 2.1 â€” IMG-18, IMG-20)
# -----------------------------------------------------------------------------
def bmi_summary(weight_kg: float, height_m: float) -> tuple[float, bool]:
    """Return (bmi_rounded_to_1_decimal, is_overweight_25_or_more)."""
    # TODO: compute weight / height ** 2
    raise NotImplementedError


def active_permission_names(perms: int) -> list[str]:
    """Given READ=1, WRITE=2, EXEC=4, return a list of active flag names in order.

    Example: perms=5 -> ['READ', 'EXEC']
    """
    # TODO: test each bit with &
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving
# -----------------------------------------------------------------------------
def toggle_and_clear_flags(perms: int, toggle_mask: int, clear_mask: int) -> int:
    """First toggle bits in toggle_mask, then clear bits in clear_mask."""
    # TODO: apply ^= then &= ~
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning
# -----------------------------------------------------------------------------
def predict_precedence_outputs() -> dict[str, object]:
    """Predict exact results before running Python:
      - 'neg_power': -2 ** 2
      - 'right_assoc': 2 ** 3 ** 2
      - 'shift_after_add': 1 + 2 << 1
      - 'logic_prec': not 10 > 5 and 10 % 2 == 0
      - 'bitwise_not': ~0b1100
    """
    # TODO: replace None with predicted values
    return {
        "neg_power": None,
        "right_assoc": None,
        "shift_after_add": None,
        "logic_prec": None,
        "bitwise_not": None,
    }
