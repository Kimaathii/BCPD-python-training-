"""
Module 18 Reference Solutions: Exceptions, Assertions & Debugging
Classroom Reference: Week 3 • Day 16 (Manual §20.1–21.12)
Target: Python 3.10+ (Verified on Python 3.15.2)
"""

from typing import Any, Callable, Dict, List, Optional, Tuple


# ==============================================================================
# Solution 1: Safe Type Converter
# ==============================================================================
def safe_cast_solution(
    val: Any,
    target_type: type,
    fallback: Any = None
) -> Tuple[Any, Optional[str]]:
    try:
        return target_type(val), None
    except (ValueError, TypeError) as e:
        return fallback, type(e).__name__


# ==============================================================================
# Solution 2: Exception Hierarchy Classifier
# ==============================================================================
def classify_exception_family_solution(exc: BaseException) -> str:
    if isinstance(exc, (SystemExit, KeyboardInterrupt)):
        return "SYSTEM_EXIT_OR_INTERRUPT"
    elif isinstance(exc, ArithmeticError):
        return "ARITHMETIC"
    elif isinstance(exc, LookupError):
        return "LOOKUP"
    elif isinstance(exc, OSError):
        return "OS_SYSTEM"
    elif isinstance(exc, Exception):
        return "GENERAL_EXCEPTION"
    return "RAW_BASE"


# ==============================================================================
# Solution 3: Configuration Parser with Chaining
# ==============================================================================
class ConfigErrorSolution(RuntimeError):
    pass


def parse_service_port_solution(cfg: Dict[str, Any]) -> int:
    try:
        raw_port = cfg["port"]
    except KeyError as e:
        raise ConfigErrorSolution("Missing port key") from e

    try:
        port = int(raw_port)
        if port < 1 or port > 65535:
            raise ValueError(f"Port {port} out of range")
        return port
    except (ValueError, TypeError) as e:
        raise ConfigErrorSolution("Invalid port number") from e


# ==============================================================================
# Solution 4: Full Lifecycle Audit Runner
# ==============================================================================
def execute_with_lifecycle_solution(func: Callable[..., Any], *args: Any) -> Tuple[Any, List[str]]:
    events: List[str] = []
    result: Any = None
    try:
        events.append("TRY_START")
        result = func(*args)
        events.append("SUCCESS")
    except Exception as e:
        events.append(f"CAUGHT:{type(e).__name__}")
        result = None
    else:
        events.append("ELSE")
    finally:
        events.append("FINALLY")
    return result, events


def main():
    # Verify Level 1
    v, err = safe_cast_solution("100", int)
    assert v == 100 and err is None

    # Verify Level 2
    assert classify_exception_family_solution(KeyError()) == "LOOKUP"

    # Verify Level 3
    port = parse_service_port_solution({"port": "9000"})
    assert port == 9000

    # Verify Level 4
    r, ev = execute_with_lifecycle_solution(lambda: 42)
    assert r == 42 and ev == ["TRY_START", "SUCCESS", "ELSE", "FINALLY"]

    print("Module 18 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
