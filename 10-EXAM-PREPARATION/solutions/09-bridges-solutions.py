"""
Module 09 Solutions: Supplementary Bridges
Course: BCPD Python Certification — Architectural Bridges
"""

from typing import Any, Callable, Dict, List, Optional, Tuple


# ==============================================================================
# Solution 1: Object Identity Inspector
# ==============================================================================
def inspect_object_identity_solution(a: Any, b: Any) -> Dict[str, Any]:
    return {
        "equal": a == b,
        "identical": a is b,
        "same_type": type(a) is type(b),
        "id_a": id(a),
        "id_b": id(b),
    }


# ==============================================================================
# Solution 2: Safe Function Evaluator
# ==============================================================================
def safe_evaluate_solution(
    func: Callable[..., Any],
    *args: Any,
    fallback: Any = None,
    expected_exceptions: Tuple[type, ...] = (Exception,)
) -> Tuple[Any, Optional[str]]:
    try:
        res = func(*args)
        return res, None
    except expected_exceptions as e:
        return fallback, type(e).__name__


# ==============================================================================
# Solution 3: Audited Division Lifecycle
# ==============================================================================
def audited_division_solution(num: float, denom: float) -> Tuple[Optional[float], List[str]]:
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
# Solution 4: Custom Domain Exception Hierarchy
# ==============================================================================
class BankingErrorSolution(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code


class InsufficientFundsErrorSolution(BankingErrorSolution):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Cannot withdraw ${amount:,.2f} from balance ${balance:,.2f}", code=1001)
        self.balance = balance
        self.amount = amount


def main():
    info = inspect_object_identity_solution(42, 42)
    assert info["equal"] is True and info["identical"] is True

    val, err = safe_evaluate_solution(int, "99")
    assert val == 99 and err is None

    res, logs = audited_division_solution(8, 2)
    assert res == 4.0 and logs == ["START", "SUCCESS", "COMPLETED"]

    err_instance = InsufficientFundsErrorSolution(10.0, 50.0)
    assert err_instance.code == 1001
    print("Module 09 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
