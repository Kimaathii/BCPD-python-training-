"""Module 03 Examples â€” Arithmetic, Precedence, Bitwise & Lab 2.1.

Sources: IMG-07, IMG-08, IMG-10, IMG-11, IMG-13..IMG-18, IMG-20 (Week 1 Â· Day 2)
Target Python: 3.10+
"""


# =============================================================================
# 1. ORIGINAL CLASSROOM CODE: arith.py [Source: IMG-07, IMG-08]
# =============================================================================
def original_arith_demo() -> None:
    """Reproduces arith.py from IMG-07 verbatim + whiteboard checks from IMG-08."""
    print(7 / 2)               # -> 3.5
    print(7 // 2)              # -> 3
    print(-7 // 2)             # -> -4
    print(-7 % 3)              # -> 2
    print(2 ** 10)             # -> 1024
    print(divmod(17, 5))       # -> (3, 2)
    x = 5
    x **= 2
    print(x)                   # -> 25
    if (n := len("hello")) > 3:
        print(n)               # -> 5

    # Instructor whiteboard examples (IMG-08)
    assert (20 // 3, 20 % 3) == (6, 2)
    assert (-20 // 3, -20 % 3) == (-7, 1)


# =============================================================================
# 2. ORIGINAL CLASSROOM CODE: evaluate.py [Source: IMG-11]
# =============================================================================
def original_evaluate_demo() -> None:
    """Reproduces evaluate.py from IMG-11 verbatim."""
    x = 10
    result = x + 3 * 2 ** 2 // 4 - 1
    print(result)                     # -> 12

    print(not x > 5 and x % 2 == 0)   # -> False
    print(5 > 3 > 1)                  # -> True
    print(0.1 + 0.2 == 0.3)           # -> False


# =============================================================================
# 3. ORIGINAL CLASSROOM CODE: bits.py & flags.py [Source: IMG-13, IMG-14, IMG-17]
# =============================================================================
def original_bitwise_demo() -> None:
    """Reproduces bits.py [IMG-13] and flags.py [IMG-14] verbatim."""
    a, b = 0b1100, 0b1010   # 12, 10
    print(a & b)            # -> 8
    print(a | b)            # -> 14
    print(a ^ b)            # -> 6
    print(~a)               # -> -13
    print(a << 2)           # -> 48
    print(a >> 2)           # -> 3
    print(bin(a & b))       # -> 0b1000

    # Whiteboard decimal-to-binary check [IMG-15, IMG-16]
    assert bin(564) == "0b1000110100"

    READ, WRITE, EXEC = 1, 2, 4   # 0b001, 0b010, 0b100
    perms = READ | WRITE
    print(perms)                  # -> 3
    print(bool(perms & WRITE))    # -> True
    print(bool(perms & EXEC))     # -> False
    perms |= EXEC
    perms &= ~WRITE
    print(bin(perms))             # -> 0b101
    print(perms ^ READ)           # -> 4
    print(1 + 2 << 1)             # -> 6


# =============================================================================
# 4. ORIGINAL vs CORRECTED: Lab 2.1 bmi.py [Source: IMG-18, IMG-20]
# =============================================================================
def original_bmi_interactive() -> None:
    """Reproduces bmi.py from IMG-20 verbatim (note: omits EXEC print)."""
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = weight / height ** 2
    print("BMI:", round(bmi, 1))
    print("Overweight?", bmi >= 25)

    READ, WRITE, EXEC = 1, 2, 4
    perms = 5
    print("Can read? ", bool(perms & READ))
    print("Can write?", bool(perms & WRITE))
    _ = EXEC


def improved_bmi_and_flags(weight: float, height: float, perms: int = 5) -> dict[str, object]:
    """Completed Lab 2.1 validating positive height and checking all 3 flags."""
    if height <= 0:
        raise ValueError("height must be > 0")
    bmi = weight / height ** 2
    READ, WRITE, EXEC = 1, 2, 4
    return {
        "bmi": round(bmi, 1),
        "overweight": bmi >= 25,
        "read": bool(perms & READ),
        "write": bool(perms & WRITE),
        "exec": bool(perms & EXEC),
    }


if __name__ == "__main__":
    original_arith_demo()
    original_evaluate_demo()
    original_bitwise_demo()
    assert improved_bmi_and_flags(75.0, 1.75, perms=5) == {
        "bmi": 24.5,
        "overweight": False,
        "read": True,
        "write": False,
        "exec": True,
    }
    print("Module 03 assertions passed.")
