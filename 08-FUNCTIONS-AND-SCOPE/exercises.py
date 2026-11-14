"""
Module 08 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Source: Day 5 Agenda (IMG-75) [Agenda-Mapped / Supplementary]
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def calculate_summary_stats(*numbers: float) -> tuple[float, float, float]:
    """Given variable number of numerical arguments:
    - return (min_val, max_val, average_val) rounded to 2 decimals.
    If no numbers are provided, raise ValueError("At least one number is required").
    """
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (Safe Defaults)
# -----------------------------------------------------------------------------
def create_user_profile(username: str, role: str = "member", permissions: list[str] | None = None) -> dict:
    """Create a user profile dictionary:
    {"username": username, "role": role, "permissions": permissions}
    
    CRITICAL: permissions must default to a fresh list ["read"] if None.
    Do NOT fall into the mutable default argument trap!
    """
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving (Closures & Scope)
# -----------------------------------------------------------------------------
def make_call_limiter(max_invocations: int):
    """Return a callable that can be invoked without arguments.
    It returns True for the first max_invocations calls, and False thereafter.
    Implement using a closure and the nonlocal keyword.
    """
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning (Gotchas & Traps)
# -----------------------------------------------------------------------------
def predict_function_exam_gotchas() -> dict[str, object]:
    """Predict the exact evaluation results of these exam traps:
      - 'mutable_default_second_call_len': length of collection after calling `buggy_func(1); buggy_func(2)`
      - 'var_args_type': type of `args` inside `def f(*args): return type(args).__name__`
      - 'kwargs_type': type of `kwargs` inside `def f(**kwargs): return type(kwargs).__name__`
      - 'implicit_return_val': return value of a function with no return statement
    """
    raise NotImplementedError
