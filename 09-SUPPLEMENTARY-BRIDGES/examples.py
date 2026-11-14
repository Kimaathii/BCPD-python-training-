"""
Module 09: Supplementary Bridges â€” Executable Examples
BCPD Python Cohort 2 Certification Preparation

Topic Classification: [Supplementary]
Topics:
  - Object-reference model, memory identity (id), small integer caching
  - Import mechanics, sys.path, __name__ idiom
  - Exception handling suite (try, except, else, finally)
"""

import sys


# ==============================================================================
# 1. Object-Reference Model & Identity [Supplementary]
# ==============================================================================

def demo_object_reference_model():
    # Small integer caching [-5, 256]
    small_1 = 100
    small_2 = 100
    assert small_1 is small_2  # Same cached singleton in CPython

    # Identity vs Equality
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    assert list_a == list_b      # Equal values
    assert list_a is not list_b  # Distinct objects in memory
    assert id(list_a) != id(list_b)

    # Rebinding names
    x = [10]
    y = x
    assert y is x
    x = [20]  # Rebinding x does NOT mutate or change y!
    assert y == [10]
    assert x == [20]


# ==============================================================================
# 2. Module System and __name__ [Supplementary / IMG-56]
# ==============================================================================

def demo_module_system():
    # sys.path inspection
    assert isinstance(sys.path, list)
    assert len(sys.path) > 0

    # __name__ reflects whether the file is main or imported
    # When imported, __name__ matches module name; when run directly, it is '__main__'
    assert isinstance(__name__, str)


# ==============================================================================
# 3. Exception Handling Control Flow [Supplementary / IMG-22, IMG-45, IMG-67, IMG-76]
# ==============================================================================

def trace_exception_flow(val: str) -> list[str]:
    """Traces the execution stages of try/except/else/finally."""
    events = []
    try:
        events.append("try_start")
        num = int(val)
        _ = 10 / num
        events.append("try_success")
    except ValueError:
        events.append("caught_value_error")
    except ZeroDivisionError:
        events.append("caught_zero_division")
    else:
        events.append("else_block")
    finally:
        events.append("finally_block")
    return events


def finally_overrides_return() -> str:
    """Demonstrates that finally executes even when try contains a return statement."""
    try:
        return "from_try"
    finally:
        # Note: In real code, returning inside finally overrides try's return value!
        pass


def demo_exception_handling():
    # Case 1: Success (runs try -> else -> finally)
    trace_ok = trace_exception_flow("5")
    assert trace_ok == ["try_start", "try_success", "else_block", "finally_block"]

    # Case 2: Handled ValueError (runs try -> except -> finally; skips else)
    trace_val_err = trace_exception_flow("invalid")
    assert trace_val_err == ["try_start", "caught_value_error", "finally_block"]

    # Case 3: Handled ZeroDivisionError (runs try -> except -> finally; skips else)
    trace_zero = trace_exception_flow("0")
    assert trace_zero == ["try_start", "caught_zero_division", "finally_block"]

    # Case 4: Finally executes on return
    assert finally_overrides_return() == "from_try"


if __name__ == "__main__":
    print("Running Module 09 Executable Examples...")
    demo_object_reference_model()
    demo_module_system()
    demo_exception_handling()
    print("All Module 09 examples executed successfully!")
