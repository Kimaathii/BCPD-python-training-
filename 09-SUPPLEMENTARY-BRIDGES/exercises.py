"""
Module 09: Supplementary Bridges — Progressive Practical Exercises
Course: BCPD Python Certification — Architectural Bridges
Student Manual Reference: Bridges between Week 1 (Basics) and Week 2 (OOP, Exceptions, Modules)
"""

from typing import Any, Callable, Dict, List, Optional, Tuple


# ==============================================================================
# Level 1: Object Identity & Small Integer Cache Inspector
# ==============================================================================
def inspect_object_identity(a: Any, b: Any) -> Dict[str, Any]:
    """
    Returns a dictionary inspecting equality and identity between two objects:
    - 'equal': boolean value equality (a == b)
    - 'identical': boolean object identity (a is b)
    - 'same_type': boolean type equality (type(a) is type(b))
    - 'id_a': memory address id(a)
    - 'id_b': memory address id(b)
    """
    return {
        "equal": a == b,
        "identical": a is b,
        "same_type": type(a) is type(b),
        "id_a": id(a),
        "id_b": id(b),
    }


# ==============================================================================
# Level 2: Safe Function Evaluator with Default Fallback
# ==============================================================================
def safe_evaluate(
    func: Callable[..., Any],
    *args: Any,
    fallback: Any = None,
    expected_exceptions: Tuple[type, ...] = (Exception,)
) -> Tuple[Any, Optional[str]]:
    """
    Executes func(*args). If an exception matching expected_exceptions occurs:
    - returns (fallback, exception_class_name).
    If no exception occurs:
    - returns (result, None).
    """
    try:
        res = func(*args)
        return res, None
    except expected_exceptions as e:
        return fallback, type(e).__name__


# ==============================================================================
# Level 3: Full try/except/else/finally Lifecycle Audit Logger
# ==============================================================================
def audited_division(num: float, denom: float) -> Tuple[Optional[float], List[str]]:
    """
    Performs division num / denom while logging the execution steps in order:
    - Always appends 'START' in try block.
    - If division succeeds, appends 'SUCCESS' in else block.
    - If ZeroDivisionError, appends 'DIV_BY_ZERO' in except block.
    - If TypeError, appends 'TYPE_ERROR' in except block.
    - Always appends 'COMPLETED' in finally block.
    Returns (result, log_steps). If error occurs, result is None.
    """
    logs: List[str] = []
    result: Optional[float] = None
    try:
        logs.append("START")
        result = num / denom
    except ZeroDivisionError:
        logs.append("DIV_BY_ZERO")
        result = None
    except TypeError:
        logs.append("TYPE_ERROR")
        result = None
    else:
        logs.append("SUCCESS")
    finally:
        logs.append("COMPLETED")
    return result, logs


# ==============================================================================
# Level 4: Custom Domain Exception Hierarchy
# ==============================================================================
class BankingError(Exception):
    """Base exception for banking domain errors."""
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code


class InsufficientFundsError(BankingError):
    """Raised when withdrawal amount exceeds available balance."""
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Cannot withdraw ${amount:,.2f} from balance ${balance:,.2f}", code=1001)
        self.balance = balance
        self.amount = amount


class DailyLimitExceededError(BankingError):
    """Raised when transfer exceeds maximum daily limit."""
    def __init__(self, limit: float, amount: float):
        super().__init__(f"Amount ${amount:,.2f} exceeds daily limit ${limit:,.2f}", code=1002)
        self.limit = limit
        self.amount = amount


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1
    info1 = inspect_object_identity(100, 100)
    assert info1["equal"] is True
    assert info1["identical"] is True  # Small int caching

    info2 = inspect_object_identity([1, 2], [1, 2])
    assert info2["equal"] is True
    assert info2["identical"] is False  # Separate lists

    # Test Level 2
    r1, err1 = safe_evaluate(int, "123")
    assert r1 == 123 and err1 is None

    r2, err2 = safe_evaluate(int, "invalid", fallback=-1, expected_exceptions=(ValueError,))
    assert r2 == -1 and err2 == "ValueError"

    # Test Level 3
    res_ok, log_ok = audited_division(10, 2)
    assert res_ok == 5.0
    assert log_ok == ["START", "SUCCESS", "COMPLETED"]

    res_zero, log_zero = audited_division(10, 0)
    assert res_zero is None
    assert log_zero == ["START", "DIV_BY_ZERO", "COMPLETED"]

    res_type, log_type = audited_division(10, "bad")  # type: ignore
    assert res_type is None
    assert log_type == ["START", "TYPE_ERROR", "COMPLETED"]

    # Test Level 4
    try:
        raise InsufficientFundsError(50.0, 100.0)
    except BankingError as e:
        assert isinstance(e, InsufficientFundsError)
        assert e.code == 1001
        assert e.balance == 50.0


if __name__ == "__main__":
    test_exercises()
    print("All Module 09 exercises PASSED verification tests.")
