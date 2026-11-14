"""Solutions for Module 03 Exercises (03-OPERATORS-AND-BITWISE/exercises.py).

Target Python: 3.10+
"""


def floor_and_mod_pair(a: int, b: int) -> tuple[int, int]:
    """Compute (a // b, a % b) using divmod."""
    return divmod(a, b)


def bmi_summary(weight_kg: float, height_m: float) -> tuple[float, bool]:
    """Compute rounded BMI and overweight flag (>= 25)."""
    if height_m <= 0:
        raise ValueError("height must be positive")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1), bmi >= 25.0


def active_permission_names(perms: int) -> list[str]:
    """Check bits for READ=1, WRITE=2, EXEC=4."""
    flag_map = [(1, "READ"), (2, "WRITE"), (4, "EXEC")]
    return [name for bit, name in flag_map if bool(perms & bit)]


def toggle_and_clear_flags(perms: int, toggle_mask: int, clear_mask: int) -> int:
    """Toggle bits, then clear specified bits."""
    perms ^= toggle_mask
    perms &= ~clear_mask
    return perms


def predict_precedence_outputs() -> dict[str, object]:
    """Exact evaluated outputs."""
    return {
        "neg_power": -4,       # -(2 ** 2)
        "right_assoc": 512,    # 2 ** 9
        "shift_after_add": 6,  # 3 << 1
        "logic_prec": False,   # not (10 > 5) and (10 % 2 == 0) -> False and True
        "bitwise_not": -13,    # ~12 == -12 - 1
    }


if __name__ == "__main__":
    assert floor_and_mod_pair(-20, 3) == (-7, 1)
    assert bmi_summary(70, 1.75) == (22.9, False)
    assert bmi_summary(85, 1.75) == (27.8, True)
    assert active_permission_names(5) == ["READ", "EXEC"]
    assert active_permission_names(7) == ["READ", "WRITE", "EXEC"]
    assert toggle_and_clear_flags(perms=3, toggle_mask=4, clear_mask=2) == 5  # (0b011 ^ 0b100) & ~0b010 -> 0b101
    assert predict_precedence_outputs() == {
        "neg_power": -4,
        "right_assoc": 512,
        "shift_after_add": 6,
        "logic_prec": False,
        "bitwise_not": -13,
    }
    print("All Module 03 solution assertions passed.")
