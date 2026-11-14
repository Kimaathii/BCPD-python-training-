"""Solutions for Module 05 Exercises (05-LOOPS-AND-ITERATION/exercises.py).

Target Python: 3.10+
"""


def sum_digits_loop(n: int) -> int:
    """Sum digits using while loop with modulo and floor division."""
    if n < 0:
        n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_prime(n: int) -> bool:
    """Test primality up to sqrt(n) in O(sqrt(n)) time."""
    if n <= 1:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def first_n_fibonacci(count: int) -> list[int]:
    """Generate first count Fibonacci numbers using tuple swap."""
    if count <= 0:
        return []
    fib: list[int] = []
    a, b = 0, 1
    while len(fib) < count:
        fib.append(a)
        a, b = b, a + b
    return fib


def centered_star_pyramid(rows: int) -> list[str]:
    """Generate centered star rows."""
    if rows <= 0:
        return []
    max_width = 2 * rows - 1
    result: list[str] = []
    for i in range(1, rows + 1):
        stars = "*" * (2 * i - 1)
        result.append(stars.center(max_width))
    return result


def predict_loop_traps() -> dict[str, object]:
    """Exact evaluated outputs."""
    return {
        "range_step": [10, 6, 2],
        "loop_var_rebind": 12,
        "range_prebuilt": 2,
        "iter_resume": ["d", "e"],
        "not_precedence": True,
    }


if __name__ == "__main__":
    assert sum_digits_loop(1234) == 10
    assert sum_digits_loop(9) == 9
    assert is_prime(29) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert first_n_fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert centered_star_pyramid(3) == [
        "  *  ",
        " *** ",
        "*****",
    ]
    assert predict_loop_traps() == {
        "range_step": [10, 6, 2],
        "loop_var_rebind": 12,
        "range_prebuilt": 2,
        "iter_resume": ["d", "e"],
        "not_precedence": True,
    }
    print("All Module 05 solution assertions passed.")
