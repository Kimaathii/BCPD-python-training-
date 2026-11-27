"""
Module 18: Exceptions, Assertions & Debugging — Executable Examples
Classroom Reference: Week 3 • Day 16 (Manual §20.1–21.12)
Target: Python 3.10+ (Verified on Python 3.15.2)

Deterministic executable implementations of all classroom slides and scripts:
- Three kinds of errors (Syntax, Runtime, Logic)
- Built-in exceptions and CPython class hierarchy
- Structured lifecycle (try, except, else, finally)
- Call stack propagation and nested try re-raising
- Exception chaining (raise ... from e / from None)
- assert sanity checks and the critical tuple trap
"""

import sys


# ==============================================================================
# 1. Three Kinds of Errors [Manual §20.1–20.2]
# ==============================================================================

def demo_three_kinds_of_errors():
    # 1. Syntax Error: Found at parse time before execution begins
    try:
        compile("def bad_syntax(:", "<string>", "exec")
        assert False, "Should have raised SyntaxError"
    except SyntaxError as e:
        assert isinstance(e, SyntaxError)

    # 2. Runtime Exception: Valid syntax, but illegal runtime operation
    try:
        _ = 10 / 0
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError as e:
        assert isinstance(e, ZeroDivisionError)

    # 3. Logic Error: Runs silently to completion, but produces wrong result!
    def calculate_discount(price: float, discount_rate: float) -> float:
        # BUG: Subtracted from 1 instead of price * (1 - rate)
        return price + (price * discount_rate)  # Accidental price increase!

    assert calculate_discount(100.0, 0.10) == 110.0  # Logic bug!


# ==============================================================================
# 2. Common Built-in Exceptions [Manual §20.3]
# ==============================================================================

def demo_common_builtin_exceptions():
    # ValueError: Correct type, invalid value
    try:
        int("abc")
    except ValueError:
        pass

    # TypeError: Incompatible types
    try:
        _ = "2" + 2  # type: ignore
    except TypeError:
        pass

    # IndexError: Sequence subscript out of range
    try:
        _ = [1, 2][5]
    except IndexError:
        pass

    # KeyError: Dictionary key not found
    try:
        _ = {}["missing_key"]
    except KeyError:
        pass

    # AttributeError: Attribute not found on object
    try:
        None.upper()  # type: ignore
    except AttributeError:
        pass

    # NameError: Undefined variable
    try:
        eval("undefined_name_xyz")
    except NameError:
        pass

    # ZeroDivisionError: Div or mod by zero
    try:
        _ = 10 % 0
    except ZeroDivisionError:
        pass

    # FileNotFoundError: File missing
    try:
        open("__non_existent_file_path_12345__.txt", "r")
    except FileNotFoundError:
        pass

    # ModuleNotFoundError: Module import failure
    try:
        __import__("__non_existent_pkg_xyz123__")
    except ModuleNotFoundError:
        pass


# ==============================================================================
# 3. Exception Hierarchy Principles [Manual §20.3]
# ==============================================================================

def demo_exception_hierarchy():
    # Hierarchy Invariants
    assert issubclass(ZeroDivisionError, ArithmeticError)
    assert issubclass(ArithmeticError, Exception)
    assert issubclass(IndexError, LookupError)
    assert issubclass(KeyError, LookupError)
    assert issubclass(LookupError, Exception)
    assert issubclass(FileNotFoundError, OSError)
    assert issubclass(PermissionError, OSError)
    assert issubclass(Exception, BaseException)

    # System signals do NOT inherit from Exception
    assert not issubclass(KeyboardInterrupt, Exception)
    assert not issubclass(SystemExit, Exception)
    assert issubclass(KeyboardInterrupt, BaseException)
    assert issubclass(SystemExit, BaseException)

    # Top-to-bottom evaluation: child handler runs if listed first
    caught_name = ""
    try:
        d = {"a": 1}
        _ = d["b"]
    except KeyError:
        caught_name = "KeyError"
    except LookupError:
        caught_name = "LookupError"
    assert caught_name == "KeyError"


# ==============================================================================
# 4. Structured Handling Lifecycle [Manual §20.4, §21.2, §21.3]
# ==============================================================================

def safe_divide(a: float, b: float):
    """Classroom divide.py implementation."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None


def to_int(text: str):
    """Classroom else_demo.py implementation."""
    try:
        n = int(text)
    except ValueError:
        return None
    else:
        # Executes strictly when try raised no exception
        return n * 2


def process_with_finally(x: float):
    """Classroom finally_demo.py implementation."""
    events = []
    try:
        events.append("start")
        res = 10 / x
        events.append(f"res:{res}")
        return res
    except ZeroDivisionError:
        events.append("divide by zero")
        return None
    finally:
        events.append("cleanup")


def parse_age(text: str, ages: list):
    """Classroom lookup.py implementation."""
    try:
        age = int(text)
        return ages[age]
    except ValueError:
        return "not a number"
    except (IndexError, KeyError):
        return "no such entry"
    except Exception:
        return "something else went wrong"


def demo_structured_handling_lifecycle():
    # divide.py verification
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(1, 0) is None

    # else_demo.py verification
    assert to_int("21") == 42
    assert to_int("invalid") is None

    # finally_demo.py verification
    assert process_with_finally(2) == 5.0
    assert process_with_finally(0) is None

    # lookup.py verification
    table = ["baby", "toddler", "child"]
    assert parse_age("abc", table) == "not a number"
    assert parse_age("7", table) == "no such entry"
    assert parse_age("1", table) == "toddler"
    assert parse_age("1", None) == "something else went wrong"  # TypeError caught by Exception


# ==============================================================================
# 5. Call Stack Propagation & Nested Try [Manual §21.5–21.6]
# ==============================================================================

def demo_propagation_and_nested_try():
    def level3():
        return int("oops")

    def level2():
        try:
            return level3()
        except KeyError:
            return "not handled here"

    def level1():
        try:
            return level2()
        except ValueError as e:
            return f"caught in level1: {type(e).__name__}"

    assert level1() == "caught in level1: ValueError"

    # Nested try with bare raise
    nested_events = []
    try:
        try:
            [][0]
        except IndexError:
            nested_events.append("inner")
            raise  # Re-raises the IndexError to outer block
    except IndexError:
        nested_events.append("outer")

    assert nested_events == ["inner", "outer"]


# ==============================================================================
# 6. Raising Errors & Exception Chaining [Manual §21.7–21.8]
# ==============================================================================

def set_age(age: int) -> int:
    """Classroom raise_demo.py validation."""
    if not isinstance(age, int):
        raise TypeError("age must be an int")
    if age < 0:
        raise ValueError(f"age cannot be negative: {age}")
    return age


def load_config(cfg: dict):
    """Classroom raise_demo.py chaining."""
    try:
        return int(cfg["port"])
    except KeyError as e:
        raise RuntimeError("config missing 'port'") from e


def demo_raising_and_chaining():
    # Validation errors
    assert set_age(25) == 25
    try:
        set_age("old")  # type: ignore
        assert False
    except TypeError as e:
        assert "age must be an int" in str(e)

    try:
        set_age(-5)
        assert False
    except ValueError as e:
        assert "age cannot be negative" in str(e)

    # Chaining with from e sets __cause__
    try:
        load_config({})
        assert False
    except RuntimeError as err:
        assert str(err) == "config missing 'port'"
        assert isinstance(err.__cause__, KeyError)
        assert str(err.__cause__) == "'port'"

    # Suppressed context with from None
    try:
        try:
            _ = 1 / 0
        except ZeroDivisionError:
            raise ValueError("custom error") from None
    except ValueError as err:
        assert err.__suppress_context__ is True
        assert err.__cause__ is None


# ==============================================================================
# 7. Internal Sanity Checks: assert & The Tuple Trap [Manual §21.9]
# ==============================================================================

def average_scores(scores: list) -> float:
    """Classroom assert_demo.py implementation."""
    assert len(scores) > 0, "scores must not be empty"
    return sum(scores) / len(scores)


def demo_assertion_sanity_and_traps():
    # Normal assertion
    assert average_scores([4, 6]) == 5.0
    try:
        average_scores([])
        assert False, "Should have raised AssertionError"
    except AssertionError as e:
        assert "scores must not be empty" in str(e)

    # THE CRITICAL EXAM TRAP: assert (condition, message) is ALWAYS TRUE!
    # In Python, (False, "message") is a 2-tuple. Any non-empty tuple is TRUTHY!
    x = -500
    # The following does NOT raise AssertionError even though x < 0!
    assert (x > 0, "x must be positive")  # Evaluates bool((False, 'msg')) which is True!

    # Correct assertion format (bare comma):
    try:
        assert x > 0, "x must be positive"
        assert False, "Should have raised AssertionError"
    except AssertionError as e:
        assert "x must be positive" in str(e)


def main():
    print("Running Module 18: Exceptions, Assertions & Debugging Executable Examples...")
    demo_three_kinds_of_errors()
    demo_common_builtin_exceptions()
    demo_exception_hierarchy()
    demo_structured_handling_lifecycle()
    demo_propagation_and_nested_try()
    demo_raising_and_chaining()
    demo_assertion_sanity_and_traps()
    print("All Module 18 examples executed successfully!")


if __name__ == "__main__":
    main()
