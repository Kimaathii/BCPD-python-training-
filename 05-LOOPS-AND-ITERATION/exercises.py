"""Module 05 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-39, IMG-40, IMG-41, IMG-42, IMG-43, IMG-44, IMG-45, IMG-47, IMG-49, IMG-55
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def sum_digits_loop(n: int) -> int:
    """Sum the base-10 digits of non-negative integer n using a while loop."""
    # TODO: while n > 0 with n % 10 and n //= 10
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (Lab 3.1 & 3.2 â€” IMG-42, IMG-45, IMG-49)
# -----------------------------------------------------------------------------
def is_prime(n: int) -> bool:
    """Return True if n is prime, testing divisors up to sqrt(n) in O(sqrt(n)) time."""
    # TODO: implement O(sqrt(n)) primality test
    raise NotImplementedError


def first_n_fibonacci(count: int) -> list[int]:
    """Return first count Fibonacci numbers starting [0, 1, 1, 2, 3, ...]."""
    # TODO: while loop with tuple swap
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving (Lab 3.2 Bonus â€” IMG-45)
# -----------------------------------------------------------------------------
def centered_star_pyramid(rows: int) -> list[str]:
    """Return a list of strings representing a centered pyramid of odd stars.

    Example for rows = 3:
      ['  *  ',
       ' *** ',
       '*****']
    """
    # TODO: build centered star rows
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning
# -----------------------------------------------------------------------------
def predict_loop_traps() -> dict[str, object]:
    """Predict exact outputs before running:
      - 'range_step': list(range(10, 0, -4))
      - 'loop_var_rebind': i after for i in range(3): i += 10
      - 'range_prebuilt': i after n=3; for i in range(n): n=10
      - 'iter_resume': rest of iter after next() on 'code'
      - 'not_precedence': not 1 == 2
    """
    # TODO: replace None with predicted values
    return {
        "range_step": None,
        "loop_var_rebind": None,
        "range_prebuilt": None,
        "iter_resume": None,
        "not_precedence": None,
    }
