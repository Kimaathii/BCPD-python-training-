"""
Module 15: Modules Part 1 â€” Imports, sys, math & random
Clean Reference Implementations & Comprehensive Solution Suite
Target: Python 3.10+ (Verified on Python 3.15.2)

Classroom Alignment: Manual Day 14 Â§14.1â€“14.6, Slides D13-01 to D13-14
"""

import math
import random
import secrets
import string
import sys
from typing import Any


# =====================================================================
# LEVEL 1: Precision Math & Rounding Engine
# =====================================================================

def financial_rounding(values: list[float]) -> dict[str, Any]:
    """
    Precision math analysis using math.fsum, math.floor, math.ceil,
    math.trunc, math.modf, and math.copysign.
    """
    return {
        "exact_total": math.fsum(values),
        "floored": [math.floor(x) for x in values],
        "ceiled": [math.ceil(x) for x in values],
        "truncated": [math.trunc(x) for x in values],
        "fractional_parts": [math.modf(x)[0] for x in values],
        "signed_magnitudes": [math.copysign(abs(x), x) for x in values]
    }


# =====================================================================
# LEVEL 2: CLI Argument & System Environment Parser
# =====================================================================

def parse_cli_arguments(args: list[str]) -> dict[str, Any]:
    """
    Parses simulated command-line argument tokens (sys.argv[1:]).
    """
    result: dict[str, Any] = {
        "help": False,
        "seed": None,
        "count": 10,
        "extra": []
    }
    
    i = 0
    while i < len(args):
        token = args[i]
        if token in ("-h", "--help"):
            result["help"] = True
            i += 1
        elif token == "--seed":
            if i + 1 >= len(args):
                raise ValueError("--seed requires an integer argument")
            try:
                result["seed"] = int(args[i + 1])
            except ValueError as e:
                raise ValueError(f"Invalid integer for --seed: {args[i + 1]}") from e
            i += 2
        elif token == "--count":
            if i + 1 >= len(args):
                raise ValueError("--count requires an integer argument")
            try:
                result["count"] = int(args[i + 1])
            except ValueError as e:
                raise ValueError(f"Invalid integer for --count: {args[i + 1]}") from e
            i += 2
        else:
            result["extra"].append(token)
            i += 1

    return result


# =====================================================================
# LEVEL 3: PRNG Sampling, Distributions & Shuffling
# =====================================================================

def simulate_card_lottery(
    seed_val: int,
    num_draws: int = 3,
    pool_size: int = 50,
    hand_size: int = 5
) -> dict[str, Any]:
    """
    Executes reproducible PRNG sampling and shuffling routines.
    """
    random.seed(seed_val)
    
    hands = [
        sorted(random.sample(range(1, pool_size + 1), hand_size))
        for _ in range(num_draws)
    ]
    
    tier_population = ["Bronze", "Silver", "Gold"]
    tier_weights = [0.70, 0.25, 0.05]
    tokens = random.choices(tier_population, weights=tier_weights, k=num_draws)
    
    deck = list(range(1, 11))
    random.shuffle(deck)
    
    return {
        "hands": hands,
        "tokens": tokens,
        "shuffled_deck": deck
    }


# =====================================================================
# LEVEL 4: Reusable Module & CLI Tool — Lab 13.1 Capstone
# =====================================================================

def roll_dice(n: int = 1, sides: int = 6, seed: int | None = None) -> list[int]:
    """
    Rolls n dice with specified sides, with optional seed.
    """
    if n < 1:
        raise ValueError("Must roll at least 1 die.")
    if sides < 2:
        raise ValueError("Die must have at least 2 sides.")
    
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, sides) for _ in range(n)]


def generate_secure_password(
    length: int = 12,
    use_secrets: bool = False,
    seed: int | None = None
) -> str:
    """
    Generates a password guaranteeing lowercase, uppercase, digit, and symbol.
    Demonstrates boundary between PRNG (random) and CSPRNG (secrets).
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    
    pools = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*"
    ]
    all_chars = "".join(pools)
    
    if use_secrets:
        # Cryptographically secure random generation
        chars = [secrets.choice(pool) for pool in pools]
        chars += [secrets.choice(all_chars) for _ in range(length - 4)]
        secrets.SystemRandom().shuffle(chars)
        return "".join(chars)
    else:
        # Standard pseudo-random generation
        if seed is not None:
            random.seed(seed)
        chars = [random.choice(pool) for pool in pools]
        chars += random.choices(all_chars, k=length - 4)
        random.shuffle(chars)
        return "".join(chars)


# =====================================================================
# Self-Verification Test Runner
# =====================================================================

def test_module_15_solutions():
    """Direct self-test assertions."""
    # 1. Level 1
    sample_vals = [2.5, -2.5, 0.1, -2.7]
    r1 = financial_rounding(sample_vals)
    assert r1["exact_total"] == math.fsum(sample_vals)
    assert r1["floored"] == [2, -3, 0, -3]
    assert r1["ceiled"] == [3, -2, 1, -2]
    assert r1["truncated"] == [2, -2, 0, -2]
    
    # 2. Level 2
    cli = ["--count", "8", "-h", "--seed", "99", "file.py"]
    r2 = parse_cli_arguments(cli)
    assert r2["count"] == 8
    assert r2["help"] is True
    assert r2["seed"] == 99
    assert r2["extra"] == ["file.py"]
    
    # 3. Level 3
    r3 = simulate_card_lottery(seed_val=42)
    assert len(r3["hands"]) == 3
    assert len(r3["tokens"]) == 3
    assert len(r3["shuffled_deck"]) == 10
    
    # 4. Level 4
    d = roll_dice(3, 6, seed=42)
    assert len(d) == 3
    assert all(1 <= x <= 6 for x in d)
    
    pwd1 = generate_secure_password(length=15, use_secrets=False, seed=42)
    assert len(pwd1) == 15
    assert any(c.islower() for c in pwd1)
    assert any(c.isupper() for c in pwd1)
    assert any(c.isdigit() for c in pwd1)
    assert any(c in "!@#$%^&*" for c in pwd1)
    
    pwd2 = generate_secure_password(length=12, use_secrets=True)
    assert len(pwd2) == 12
    assert any(c.islower() for c in pwd2)
    assert any(c.isupper() for c in pwd2)
    assert any(c.isdigit() for c in pwd2)
    assert any(c in "!@#$%^&*" for c in pwd2)


def main():
    test_module_15_solutions()
    print("Module 15 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
