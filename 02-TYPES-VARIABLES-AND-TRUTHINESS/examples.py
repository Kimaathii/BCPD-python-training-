"""Module 02 Examples â€” Variables, Core Types, Base Conversions & Truthiness.

Sources: IMG-06, IMG-09, IMG-11, IMG-12, IMG-32 (Week 1 Â· Day 2 & Day 3)
Target Python: 3.10+
"""

import math


# =============================================================================
# 1. ORIGINAL CLASSROOM CODE: Number literals & bases [Source: IMG-06]
# =============================================================================
def original_literals_and_bases() -> None:
    """Reproduces the expressions and conversions table from IMG-06."""
    assert (0b1010, 0o17, 0x1F) == (10, 15, 31)
    assert (bin(10), oct(8), hex(255)) == ("0b1010", "0o10", "0xff")
    assert (int("101", 2), int("ff", 16)) == (5, 255)
    assert (float("1e3"), float(" 3.5 ")) == (1000.0, 3.5)
    assert math.isinf(float("inf"))
    assert complex("1+2j") == (1 + 2j)
    assert (2J).imag == 2.0


# =============================================================================
# 2. ORIGINAL CLASSROOM CODE: assign.py [Source: IMG-09]
# =============================================================================
def original_assign_demo() -> None:
    """Reproduces assign.py from IMG-09 verbatim."""
    a, b, c = 1, 2, 3
    x = y = 0
    n = 1,000,000
    print(n, 1_000_000)                      # -> (1, 0, 0) 1000000
    a ^= b; b ^= a; a ^= b                   # XOR swap
    print(a, b)                              # -> 2 1
    print(7 & 1, 8 & 1)                      # -> 1 0   (odd / even)
    print(pow(2, 10, 1000), divmod(-7, 2))   # -> 24 (-4, 1)
    print(round(2.5), round(2.675, 2))       # -> 2 2.67
    print(int(), float(), repr(str()), bool())
    # -> 0 0.0 '' False
    assert (c, x, y) == (3, 0, 0)


# =============================================================================
# 3. ORIGINAL CLASSROOM CODE: convert.py [Source: IMG-12]
# =============================================================================
def original_convert_demo() -> None:
    """Reproduces convert.py from IMG-12 verbatim."""
    print(3 + 2.0)                           # -> 5.0
    print(int(3.9))                          # -> 3
    print(int("0x1f", 16))                   # -> 31
    print(round(2.5), round(3.5))            # -> 2 4
    print(bool(""), bool("0"))               # -> False True
    print(bool([]), bool([0]))               # -> False True
    print(float("1e3"))                      # -> 1000.0


# =============================================================================
# 4. SUPPLEMENTARY: Float Precision, Identity & Safe Conversions [IMG-06, 11, 32]
# =============================================================================
def supplementary_float_and_identity() -> None:
    """Demonstrates float comparison, exception edge cases, and == vs is."""
    assert (0.1 + 0.2 == 0.3) is False
    assert math.isclose(0.1 + 0.2, 0.3) is True

    a = [1, 2]
    b = [1, 2]
    c = a
    assert (a == b) is True
    assert (a is b) is False
    assert (c is a) is True
    assert (3 == 3.0) is True

    # Exception distinctions from IMG-06
    for expr, exc_type in [
        (lambda: int(5, 2), TypeError),
        (lambda: int("2.5"), ValueError),
        (lambda: int(float("inf")), OverflowError),
    ]:
        try:
            expr()
            raise AssertionError(f"Expected {exc_type.__name__}")
        except exc_type:
            pass


if __name__ == "__main__":
    original_literals_and_bases()
    original_assign_demo()
    original_convert_demo()
    supplementary_float_and_identity()
    print("Module 02 assertions passed.")
