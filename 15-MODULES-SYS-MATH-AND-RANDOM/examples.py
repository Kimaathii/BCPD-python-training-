"""
Module 15: Modules Part 1 â€” Imports, sys, math & random
Executable Classroom Examples & Runtime Verifications
Verified with Python 3.10+ (Tested on Python 3.15.2)

Classroom Slides: D13-01 through D13-14 (Week 3 Day 13 / Manual Day 14 Â§14.1â€“14.6)
"""

import io
import math
import random
import string
import sys


def test_opening_teaser():
    """Slide D13-01: day13.py teaser."""
    random.seed(42)
    val = random.randint(1, 6)
    ceil_val = math.ceil(2.1)
    
    assert val == 6, f"Expected 6 with seed(42), got {val}"
    assert ceil_val == 3, f"Expected 3, got {ceil_val}"
    assert isinstance(sys.platform, str) and len(sys.platform) > 0


def test_sys_path_and_modules():
    """Slide D13-04: paths.py & sys.modules caching."""
    # sys.path has at least 1 entry
    assert len(sys.path) > 0
    # math is in sys.modules
    assert "math" in sys.modules
    assert math.__name__ == "math"
    
    # Demonstrating runtime sys.path inspection
    first_three = sys.path[:3]
    assert len(first_three) >= 1
    assert all(isinstance(p, str) for p in first_three)


def test_sys_module_features():
    """Slide D13-06: The sys module environment & streams."""
    assert isinstance(sys.argv, list)
    assert len(sys.argv) >= 1  # argv[0] is script name
    assert isinstance(sys.argv[0], str)
    
    # Introspection
    assert hasattr(sys, "version_info")
    assert sys.version_info.major >= 3
    assert sys.getrecursionlimit() >= 1000
    
    # Standard streams exist
    assert hasattr(sys, "stdin")
    assert hasattr(sys, "stdout")
    assert hasattr(sys, "stderr")


def test_math_everyday_functions():
    """Slide D13-07: math everyday functions table."""
    # sqrt
    assert math.sqrt(16) == 4.0
    assert isinstance(math.sqrt(16), float)
    
    # pow (always returns float)
    assert math.pow(2, 3) == 8.0
    assert isinstance(math.pow(2, 3), float)
    
    # ceil and floor on negative numbers
    assert math.ceil(-2.5) == -2
    assert math.floor(-2.5) == -3
    assert isinstance(math.ceil(-2.5), int)
    assert isinstance(math.floor(-2.5), int)
    
    # trunc
    assert math.trunc(-2.7) == -2
    assert isinstance(math.trunc(-2.7), int)
    
    # fabs (always returns float) vs abs
    assert math.fabs(-3) == 3.0
    assert isinstance(math.fabs(-3), float)
    assert abs(-3) == 3
    assert isinstance(abs(-3), int)
    
    # factorial & gcd
    assert math.factorial(5) == 120
    assert math.gcd(12, 18) == 6
    
    # isclose
    assert math.isclose(0.1 + 0.2, 0.3) is True


def test_math_constants_logs_trig():
    """Slide D13-08: math_more.py."""
    assert round(math.pi, 4) == 3.1416
    assert round(math.log(100, 10)) == 2
    assert math.log10(1000) == 3.0
    assert math.log2(8) == 3.0
    assert math.exp(0) == 1.0
    
    # Trig functions expect radians
    assert round(math.sin(math.pi / 2), 2) == 1.0
    assert math.degrees(math.pi) == 180.0
    assert math.radians(180) == math.pi
    
    # Special floats
    assert math.inf > 10 ** 100
    assert math.isnan(math.nan) is True
    assert math.hypot(3, 4) == 5.0


def test_math_question_bank_favourites():
    """Slide D13-09: Question-bank favourites."""
    # copysign
    assert math.copysign(3, -0.0) == -3.0
    assert math.copysign(5.0, 1.0) == 5.0
    
    # fabs vs abs
    assert math.fabs(-3) == 3.0
    assert abs(-3) == 3
    
    # modf returns (fractional_part, integer_part) both floats
    fraction, whole = math.modf(2.5)
    assert math.isclose(fraction, 0.5)
    assert math.isclose(whole, 2.0)
    assert isinstance(fraction, float) and isinstance(whole, float)
    
    # frexp and ldexp
    m, e = math.frexp(8)
    assert m == 0.5 and e == 4
    assert math.ldexp(0.5, 4) == 8.0
    
    # fsum: exact floating point accumulation vs naive loop (slide D13-09)
    loop_val = 0.0
    for _ in range(10):
        loop_val += 0.1
    exact_sum = math.fsum([0.1] * 10)
    assert exact_sum == 1.0
    assert loop_val == 0.9999999999999999
    assert loop_val != 1.0
    
    # isfinite, isinf, nan
    assert math.isfinite(math.inf) is False
    assert math.isinf(-math.inf) is True
    diff = math.inf - math.inf
    assert math.isnan(diff) is True
    
    # Factorial edge cases
    assert math.factorial(0) == 1
    try:
        math.factorial(-1)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    
    try:
        math.factorial(5.0)  # type: ignore
        assert False, "Should raise TypeError in Python 3.10+"
    except TypeError:
        pass
    
    # Logs
    assert math.isclose(math.log(math.e), 1.0)
    assert math.isclose(math.log(8, 2), 3.0)


def test_random_numbers_and_choices():
    """Slide D13-10: random_basics.py."""
    random.seed(42)
    assert random.randint(1, 6) == 6
    assert random.choice(["red", "green", "blue"]) == "red"
    
    x = random.random()
    assert 0.0 <= x < 1.0
    
    deck = list(range(1, 6))
    shuffle_result = random.shuffle(deck)
    assert shuffle_result is None  # in-place shuffle returns None
    assert sorted(deck) == [1, 2, 3, 4, 5]
    
    # randrange with step
    val = random.randrange(0, 10, 5)
    assert val in (0, 5)


def test_random_sampling_distributions_seeds():
    """Slide D13-11: random_more.py."""
    # Seed reproducibility
    random.seed(1)
    a = [random.randint(1, 100) for _ in range(3)]
    random.seed(1)
    b = [random.randint(1, 100) for _ in range(3)]
    assert a == b
    
    # Sample without replacement
    hand = random.sample(range(1, 50), 6)
    assert len(hand) == 6
    assert len(set(hand)) == 6  # strictly unique
    
    # Choices with replacement
    flips = random.choices("HT", k=10)
    assert len(flips) == 10
    assert all(f in "HT" for f in flips)
    
    # Uniform and Gauss
    u = random.uniform(1.5, 2.5)
    assert 1.5 <= u <= 2.5
    g = random.gauss(0, 1)
    assert isinstance(g, float)


def test_exam_details_and_pitfalls():
    """Slide D13-12: details.py."""
    # sys.stdout.write returns character count
    captured = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured
    try:
        char_count = sys.stdout.write("hi\n")
    finally:
        sys.stdout = old_stdout
    assert char_count == 3
    assert captured.getvalue() == "hi\n"
    
    # len vs getsizeof
    text = "abc"
    assert len(text) == 3
    assert sys.getsizeof(text) > 3  # object header overhead
    
    # seed() returns None
    assert random.seed(7) is None
    
    # randint(a, b) vs randrange(a, b + 1)
    random.seed(1)
    r1 = random.randint(1, 6)
    random.seed(1)
    r2 = random.randrange(1, 7)
    assert r1 == r2
    
    # choice on sequence
    assert random.choice("xyz") in "xyz"
    
    # shuffle on immutable tuple raises TypeError
    try:
        random.shuffle((1, 2, 3))  # type: ignore
        assert False, "Should raise TypeError"
    except TypeError:
        pass


def make_password(length: int = 12) -> str:
    """Slide D13-13: Lab 13.1 password.py implementation."""
    if length < 3:
        raise ValueError("Password length must be at least 3.")
    pools = [string.ascii_letters, string.digits, "!@#$%"]
    chars = [random.choice(p) for p in pools]
    everything = "".join(pools)
    chars += random.choices(everything, k=length - 3)
    random.shuffle(chars)
    return "".join(chars)


def test_lab_password_generator():
    """Slide D13-13: Lab 13.1 password verification."""
    random.seed(42)
    pwd = make_password(14)
    assert len(pwd) == 14
    # Must contain at least one letter, one digit, and one symbol
    has_letter = any(c in string.ascii_letters for c in pwd)
    has_digit = any(c in string.digits for c in pwd)
    has_symbol = any(c in "!@#$%" for c in pwd)
    assert has_letter, "Password missing letter"
    assert has_digit, "Password missing digit"
    assert has_symbol, "Password missing symbol"


def main():
    print("Running Module 15: Modules, sys, math & random test suite...")
    test_opening_teaser()
    test_sys_path_and_modules()
    test_sys_module_features()
    test_math_everyday_functions()
    test_math_constants_logs_trig()
    test_math_question_bank_favourites()
    test_random_numbers_and_choices()
    test_random_sampling_distributions_seeds()
    test_exam_details_and_pitfalls()
    test_lab_password_generator()
    print("All Module 15 examples PASSED cleanly (100% verified against Day 13 slides).")


if __name__ == "__main__":
    main()
