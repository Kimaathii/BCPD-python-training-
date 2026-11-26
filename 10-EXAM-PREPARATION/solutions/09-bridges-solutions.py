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


# ==============================================================================
# Solution 5: File I/O Stream & Cursor Inspector
# ==============================================================================
def inspect_file_stream_solution(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        assert f.tell() == 0
        line_count = 0
        non_empty = 0
        for line in f:
            line_count += 1
            if line.strip():
                non_empty += 1
        
        # Determine total bytes via cursor jump
        f.seek(0, 2)
        total_bytes = f.tell()

        # Rewind cursor back to start
        f.seek(0)
        rewound = (f.tell() == 0)

    return {
        "line_count": line_count,
        "non_empty_lines": non_empty,
        "total_bytes": total_bytes,
        "rewound_to_start": rewound,
    }


# ==============================================================================
# Solution 6: Context Manager Exception Shield
# ==============================================================================
class ContextExceptionShieldSolution:
    def __init__(self, suppressed_types: Tuple[type, ...] = (Exception,)):
        self.suppressed_types = suppressed_types
        self.events: List[str] = []

    def __enter__(self):
        self.events.append("ENTERED")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.events.append("EXITED")
        if exc_type is not None and issubclass(exc_type, self.suppressed_types):
            self.events.append(f"SUPPRESSED:{exc_type.__name__}")
            return True
        return False


def main():
    info = inspect_object_identity_solution(42, 42)
    assert info["equal"] is True and info["identical"] is True

    val, err = safe_evaluate_solution(int, "99")
    assert val == 99 and err is None

    res, logs = audited_division_solution(8, 2)
    assert res == 4.0 and logs == ["START", "SUCCESS", "COMPLETED"]

    err_instance = InsufficientFundsErrorSolution(10.0, 50.0)
    assert err_instance.code == 1001

    # Test Solution 5
    import os
    import tempfile
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tf:
        tf.write("One\nTwo\n\nThree\n")
        tf_name = tf.name

    try:
        f_info = inspect_file_stream_solution(tf_name)
        assert f_info["line_count"] == 4
        assert f_info["non_empty_lines"] == 3
        assert f_info["total_bytes"] > 0
        assert f_info["rewound_to_start"] is True
    finally:
        if os.path.exists(tf_name):
            os.remove(tf_name)

    # Test Solution 6
    with ContextExceptionShieldSolution(suppressed_types=(KeyError,)) as shield:
        _ = {}["key"]
    assert shield.events == ["ENTERED", "EXITED", "SUPPRESSED:KeyError"]

    print("Module 09 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
