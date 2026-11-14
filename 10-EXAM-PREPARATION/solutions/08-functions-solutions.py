"""
Solutions for Module 08 Exercises (08-FUNCTIONS-AND-SCOPE/exercises.py).

Target Python: 3.10+
"""


def calculate_summary_stats(*numbers: float) -> tuple[float, float, float]:
    """Calculate min, max, average."""
    if not numbers:
        raise ValueError("At least one number is required")
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = round(sum(numbers) / len(numbers), 2)
    return min_val, max_val, avg_val


def create_user_profile(username: str, role: str = "member", permissions: list[str] | None = None) -> dict:
    """Create a user profile dictionary with safe default initialization."""
    if permissions is None:
        permissions = ["read"]
    return {
        "username": username,
        "role": role,
        "permissions": permissions,
    }


def make_call_limiter(max_invocations: int):
    """Closure tracking invocations using nonlocal."""
    invocations_left = max_invocations
    def limiter() -> bool:
        nonlocal invocations_left
        if invocations_left > 0:
            invocations_left -= 1
            return True
        return False
    return limiter


def predict_function_exam_gotchas() -> dict[str, object]:
    """Exact evaluated outputs for function exam traps."""
    return {
        "mutable_default_second_call_len": 2,
        "var_args_type": "tuple",
        "kwargs_type": "dict",
        "implicit_return_val": None,
    }


if __name__ == "__main__":
    # Test calculate_summary_stats
    mn, mx, avg = calculate_summary_stats(10.0, 20.0, 30.0, 40.0)
    assert (mn, mx, avg) == (10.0, 40.0, 25.0)
    try:
        calculate_summary_stats()
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # Test create_user_profile & verify safe defaults
    u1 = create_user_profile("alice")
    u2 = create_user_profile("bob")
    assert u1["permissions"] == ["read"]
    assert u2["permissions"] == ["read"]
    u1["permissions"].append("write")
    # Verify u2 did not get contaminated:
    assert u2["permissions"] == ["read"]
    assert u1["permissions"] is not u2["permissions"]

    # Test make_call_limiter
    limiter = make_call_limiter(2)
    assert limiter() is True
    assert limiter() is True
    assert limiter() is False
    assert limiter() is False

    # Test predict_function_exam_gotchas
    gotchas = predict_function_exam_gotchas()
    assert gotchas["mutable_default_second_call_len"] == 2
    assert gotchas["var_args_type"] == "tuple"
    assert gotchas["kwargs_type"] == "dict"
    assert gotchas["implicit_return_val"] is None

    print("All Module 08 solutions assertions passed successfully!")
