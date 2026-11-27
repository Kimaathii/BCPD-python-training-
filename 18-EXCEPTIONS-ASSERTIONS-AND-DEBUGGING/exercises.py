"""
Module 18: Exceptions, Assertions & Debugging — Progressive Exercises
Classroom Reference: Week 3 • Day 16 (Manual §20.1–21.12)
Target: Python 3.10+ (Verified on Python 3.15.2)

Exercises:
- Level 1: Safe Type Converter with Multi-Exception Handling
- Level 2: Exception Hierarchy Classifier (Family Groups)
- Level 3: Configuration Parser with Explicit Exception Chaining (__cause__)
- Level 4: Full Lifecycle Audit Runner (try / except / else / finally)
- Level 5: Classroom Knowledge Check Verification (Questions 1–5)
"""

from typing import Any, Callable, Dict, List, Optional, Tuple


# ==============================================================================
# Level 1: Safe Type Converter
# ==============================================================================
def safe_cast(
    val: Any,
    target_type: type,
    fallback: Any = None
) -> Tuple[Any, Optional[str]]:
    """
    Attempts to convert val to target_type(val).
    If conversion succeeds:
        returns (converted_value, None)
    If ValueError or TypeError occurs:
        returns (fallback, exception_class_name)
    """
    try:
        return target_type(val), None
    except (ValueError, TypeError) as e:
        return fallback, type(e).__name__


# ==============================================================================
# Level 2: Exception Hierarchy Classifier
# ==============================================================================
def classify_exception_family(exc: BaseException) -> str:
    """
    Classifies an exception instance into its primary standard family:
    - 'ARITHMETIC' if isinstance of ArithmeticError
    - 'LOOKUP' if isinstance of LookupError
    - 'OS_SYSTEM' if isinstance of OSError
    - 'SYSTEM_EXIT_OR_INTERRUPT' if isinstance of (SystemExit, KeyboardInterrupt)
    - 'GENERAL_EXCEPTION' if isinstance of Exception
    - 'RAW_BASE' otherwise
    """
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
# Level 3: Configuration Parser with Exception Chaining
# ==============================================================================
class ConfigError(RuntimeError):
    """Domain error for configuration parsing failures."""
    pass


def parse_service_port(cfg: Dict[str, Any]) -> int:
    """
    Parses 'port' from cfg dict:
    - If 'port' key is missing: raises ConfigError("Missing port key") from KeyError
    - If 'port' value cannot be converted to int or is negative:
        raises ConfigError("Invalid port number") from original error
    - If valid (e.g. 8080): returns integer port.
    """
    try:
        raw_port = cfg["port"]
    except KeyError as e:
        raise ConfigError("Missing port key") from e

    try:
        port = int(raw_port)
        if port < 1 or port > 65535:
            raise ValueError(f"Port {port} out of range")
        return port
    except (ValueError, TypeError) as e:
        raise ConfigError("Invalid port number") from e


# ==============================================================================
# Level 4: Full Lifecycle Audit Runner
# ==============================================================================
def execute_with_lifecycle(func: Callable[..., Any], *args: Any) -> Tuple[Any, List[str]]:
    """
    Executes func(*args) while auditing the exact stage events:
    - Appends 'TRY_START'
    - If successful: appends 'SUCCESS', then 'ELSE'
    - If exception occurs: appends f'CAUGHT:{type(e).__name__}'
    - In finally: appends 'FINALLY'
    Returns (result, events_list). If exception occurred, result is None.
    """
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


# ==============================================================================
# Level 5: Classroom Knowledge Check Verification (Slide 13)
# ==============================================================================
def run_knowledge_check_q1() -> str:
    """Q1: Which exception does int('3.5') raise?"""
    try:
        int("3.5")
        return "None"
    except Exception as e:
        return type(e).__name__


def run_knowledge_check_q2() -> bool:
    """Q2: Which is a parent class of KeyError? Checks if LookupError is parent."""
    return issubclass(KeyError, LookupError)


def run_knowledge_check_q3() -> str:
    """Q3: Handlers print 'Z' (ZeroDivisionError, first) and 'E' (Exception). What does 1 / 0 print?"""
    output = []
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        output.append("Z")
    except Exception:
        output.append("E")
    return "".join(output)


def run_knowledge_check_q4() -> bool:
    """Q4: When does the else block of a try statement run? True if only on zero exceptions."""
    ran_on_success = False
    ran_on_error = False

    try:
        _ = 10 + 5
    except Exception:
        pass
    else:
        ran_on_success = True

    try:
        _ = 10 / 0
    except ZeroDivisionError:
        pass
    else:
        ran_on_error = True

    return ran_on_success is True and ran_on_error is False


def run_knowledge_check_q5() -> bool:
    """Q5: Which block runs even if try executes return?"""
    finally_executed = False

    def helper():
        nonlocal finally_executed
        try:
            return "from_try"
        finally:
            finally_executed = True

    res = helper()
    return res == "from_try" and finally_executed is True


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1
    val1, err1 = safe_cast("42", int)
    assert val1 == 42 and err1 is None

    val2, err2 = safe_cast("abc", int, fallback=-1)
    assert val2 == -1 and err2 == "ValueError"

    val3, err3 = safe_cast(None, int, fallback=-99)
    assert val3 == -99 and err3 == "TypeError"

    # Test Level 2
    assert classify_exception_family(ZeroDivisionError()) == "ARITHMETIC"
    assert classify_exception_family(KeyError()) == "LOOKUP"
    assert classify_exception_family(IndexError()) == "LOOKUP"
    assert classify_exception_family(FileNotFoundError()) == "OS_SYSTEM"
    assert classify_exception_family(SystemExit()) == "SYSTEM_EXIT_OR_INTERRUPT"
    assert classify_exception_family(ValueError()) == "GENERAL_EXCEPTION"

    # Test Level 3
    valid_port = parse_service_port({"port": "8080"})
    assert valid_port == 8080

    try:
        parse_service_port({})
        assert False
    except ConfigError as ce:
        assert str(ce) == "Missing port key"
        assert isinstance(ce.__cause__, KeyError)

    try:
        parse_service_port({"port": "invalid_num"})
        assert False
    except ConfigError as ce:
        assert str(ce) == "Invalid port number"
        assert isinstance(ce.__cause__, ValueError)

    # Test Level 4
    r_ok, events_ok = execute_with_lifecycle(lambda x: x * 2, 5)
    assert r_ok == 10
    assert events_ok == ["TRY_START", "SUCCESS", "ELSE", "FINALLY"]

    r_err, events_err = execute_with_lifecycle(lambda: 1 / 0)
    assert r_err is None
    assert events_err == ["TRY_START", "CAUGHT:ZeroDivisionError", "FINALLY"]

    # Test Level 5 (Classroom Knowledge Check)
    assert run_knowledge_check_q1() == "ValueError"
    assert run_knowledge_check_q2() is True
    assert run_knowledge_check_q3() == "Z"
    assert run_knowledge_check_q4() is True
    assert run_knowledge_check_q5() is True


if __name__ == "__main__":
    test_exercises()
    print("All Module 18 exercises & Classroom Knowledge Check PASSED cleanly.")
