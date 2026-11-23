"""
Module 15: Modules Part 1 â€” Imports, sys, math & random
Progressive Certification Exercises (Levels 1â€“4)
Target: Python 3.10+ (Verified on Python 3.15.2)

Attempt these exercises to build muscle memory before reviewing solutions in:
10-EXAM-PREPARATION/solutions/15-modules-sys-math-random-solutions.py
"""

import math
import random
import secrets
import string
import sys
from typing import Any


# =====================================================================
# LEVEL 1: Precision Math & Rounding Engine (Manual Â§14.4, D13-07 to D13-09)
# =====================================================================

def financial_rounding(values: list[float]) -> dict[str, Any]:
    """
    Given a list of float transactions (positive and negative), return a dict:
    - "exact_total": exact floating-point sum using math.fsum(values)
    - "floored": list of math.floor(x) for each x in values
    - "ceiled": list of math.ceil(x) for each x in values
    - "truncated": list of math.trunc(x) for each x in values
    - "fractional_parts": list of fractional parts using math.modf(x)[0]
    - "signed_magnitudes": list of math.copysign(abs(x), x)
    """
    # TODO: Implement Level 1 exercise
    raise NotImplementedError("Level 1 financial_rounding not implemented yet.")


# =====================================================================
# LEVEL 2: CLI Argument & System Environment Parser (Manual Â§14.3, D13-06)
# =====================================================================

def parse_cli_arguments(args: list[str]) -> dict[str, Any]:
    """
    Simulate parsing CLI argument tokens (mimicking sys.argv[1:]).
    Supported tokens:
      - "-h" or "--help": sets "help" = True (default False)
      - "--seed <int>": sets "seed" = parsed int (default None)
      - "--count <int>": sets "count" = parsed int (default 10)
      - any other tokens are collected in order into "extra": list[str]

    If "--seed" or "--count" is provided without a following token, or if
    the argument cannot be converted to int, raise ValueError.
    """
    # TODO: Implement Level 2 exercise
    raise NotImplementedError("Level 2 parse_cli_arguments not implemented yet.")


# =====================================================================
# LEVEL 3: PRNG Sampling, Distributions & Shuffling (Manual Â§14.5, D13-10 to D13-11)
# =====================================================================

def simulate_card_lottery(
    seed_val: int,
    num_draws: int = 3,
    pool_size: int = 50,
    hand_size: int = 5
) -> dict[str, Any]:
    """
    Execute a deterministic lottery draw using random seeded with seed_val:
    1. Seed random with seed_val.
    2. Generate `num_draws` lottery hands. Each hand is drawn using
       random.sample(range(1, pool_size + 1), hand_size) (strictly unique numbers).
    3. Generate `num_draws` tier tokens using random.choices():
       population: ["Bronze", "Silver", "Gold"]
       weights: [0.70, 0.25, 0.05]
       k: num_draws
    4. Take a list of items `list(range(1, 11))` and shuffle it in-place using random.shuffle().
    5. Return a dict:
       {
           "hands": list of hands (each sorted ascending),
           "tokens": list of tokens,
           "shuffled_deck": list of 10 shuffled numbers
       }
    """
    # TODO: Implement Level 3 exercise
    raise NotImplementedError("Level 3 simulate_card_lottery not implemented yet.")


# =====================================================================
# LEVEL 4: Reusable Module & CLI Tool — Lab 13.1 Capstone (Manual §14.6, D13-13)
# =====================================================================

def roll_dice(n: int = 1, sides: int = 6, seed: int | None = None) -> list[int]:
    """
    Roll `n` dice, each having `sides` faces (values 1 to sides inclusive).
    If `seed` is not None, seed random before rolling.
    Validate:
      - If n < 1, raise ValueError("Must roll at least 1 die.")
      - If sides < 2, raise ValueError("Die must have at least 2 sides.")
    Return list of rolled integers.
    """
    # TODO: Implement Level 4 roll_dice
    raise NotImplementedError("Level 4 roll_dice not implemented yet.")


def generate_secure_password(
    length: int = 12,
    use_secrets: bool = False,
    seed: int | None = None
) -> str:
    """
    Generate a password of `length` characters satisfying:
      - At least 1 lowercase letter (string.ascii_lowercase)
      - At least 1 uppercase letter (string.ascii_uppercase)
      - At least 1 digit (string.digits)
      - At least 1 symbol from "!@#$%^&*"
      - Total length exactly equal to `length`
    If length < 4, raise ValueError("Password length must be at least 4.")

    If use_secrets is True:
      - Use `secrets.choice()` to select characters.
      - Use `secrets.SystemRandom().shuffle()` to shuffle characters.
    If use_secrets is False:
      - If seed is not None, call random.seed(seed).
      - Use `random.choice()`, `random.choices()`, and `random.shuffle()`.
    """
    # TODO: Implement Level 4 generate_secure_password
    raise NotImplementedError("Level 4 generate_secure_password not implemented yet.")


# =====================================================================
# Self-Test Suite
# =====================================================================

def test_exercises():
    """Verify solutions against reference implementation."""
    from importlib.util import spec_from_file_location, module_from_spec
    from pathlib import Path

    sol_path = Path(__file__).resolve().parent.parent / "10-EXAM-PREPARATION" / "solutions" / "15-modules-sys-math-random-solutions.py"
    if not sol_path.exists():
        print("Note: Reference solutions file not yet created; skipping exercise runner.")
        return

    spec = spec_from_file_location("ref_sol_15", sol_path)
    if spec is None or spec.loader is None:
        return
    ref = module_from_spec(spec)
    spec.loader.exec_module(ref)

    # Test Level 1
    vals = [2.5, -2.5, 0.1, -2.7]
    res1 = ref.financial_rounding(vals)
    assert res1["exact_total"] == math.fsum(vals)
    assert res1["floored"] == [2, -3, 0, -3]
    assert res1["ceiled"] == [3, -2, 1, -2]
    assert res1["truncated"] == [2, -2, 0, -2]
    assert len(res1["fractional_parts"]) == 4

    # Test Level 2
    args = ["--seed", "42", "-h", "input.txt", "--count", "5", "output.txt"]
    res2 = ref.parse_cli_arguments(args)
    assert res2["seed"] == 42
    assert res2["help"] is True
    assert res2["count"] == 5
    assert res2["extra"] == ["input.txt", "output.txt"]

    # Test Level 3
    res3 = ref.simulate_card_lottery(seed_val=100, num_draws=3, pool_size=50, hand_size=5)
    assert len(res3["hands"]) == 3
    for h in res3["hands"]:
        assert len(h) == 5
        assert len(set(h)) == 5
        assert h == sorted(h)
    assert len(res3["tokens"]) == 3
    assert len(res3["shuffled_deck"]) == 10
    assert sorted(res3["shuffled_deck"]) == list(range(1, 11))

    # Test Level 4
    rolls = ref.roll_dice(n=5, sides=6, seed=42)
    assert len(rolls) == 5
    assert all(1 <= r <= 6 for r in rolls)

    pwd_random = ref.generate_secure_password(length=12, use_secrets=False, seed=42)
    assert len(pwd_random) == 12
    assert any(c in string.ascii_lowercase for c in pwd_random)
    assert any(c in string.ascii_uppercase for c in pwd_random)
    assert any(c in string.digits for c in pwd_random)
    assert any(c in "!@#$%^&*" for c in pwd_random)

    pwd_secrets = ref.generate_secure_password(length=16, use_secrets=True)
    assert len(pwd_secrets) == 16
    assert any(c in string.ascii_lowercase for c in pwd_secrets)
    assert any(c in string.ascii_uppercase for c in pwd_secrets)
    assert any(c in string.digits for c in pwd_secrets)
    assert any(c in "!@#$%^&*" for c in pwd_secrets)

    print("Module 15 exercise tests verified successfully against reference solutions.")


if __name__ == "__main__":
    test_exercises()
