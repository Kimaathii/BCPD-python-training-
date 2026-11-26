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


# ==============================================================================
# 4. File I/O Operations & Cursor Mechanics [Supplementary / IMG-45, IMG-76]
# ==============================================================================

def demo_file_io_and_cursor():
    import os
    import tempfile

    # Mode 'w' truncation and cursor seeking
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tf:
        tf.write("Line 1: Hello Python\nLine 2: File IO Bridges\nLine 3: Stream Mastery\n")
        temp_path = tf.name

    try:
        with open(temp_path, "r", encoding="utf-8") as f:
            # 1. Cursor starts at 0
            assert f.tell() == 0
            first_line = f.readline()
            assert first_line == "Line 1: Hello Python\n"
            pos_after_line1 = f.tell()
            assert pos_after_line1 > 0

            # 2. Seek back to start
            f.seek(0)
            assert f.tell() == 0
            assert f.readline() == "Line 1: Hello Python\n"

            # 3. Stream reading line by line (O(1) memory)
            f.seek(0)
            lines = [line.strip() for line in f]
            assert len(lines) == 3
            assert lines[1] == "Line 2: File IO Bridges"

        # Mode 'w' immediate truncation verification (Trap 9.4)
        with open(temp_path, "w", encoding="utf-8") as f_trunc:
            pass  # Immediately wipes file to 0 bytes
        assert os.path.getsize(temp_path) == 0

        # Mode 'a' append verification
        with open(temp_path, "a", encoding="utf-8") as f_app:
            f_app.write("Appended content")
        with open(temp_path, "r", encoding="utf-8") as f_read:
            assert f_read.read() == "Appended content"

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


# ==============================================================================
# 5. Context Manager Dunders & Exception Suppression [Supplementary / IMG-45]
# ==============================================================================

class SafeContextResource:
    """Demonstrates __enter__, __exit__, and exception suppression semantics."""
    def __init__(self, suppress: bool = False):
        self.suppress = suppress
        self.entered = False
        self.exited = False
        self.caught_exception = None

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        if exc_type is not None:
            self.caught_exception = exc_type.__name__
        # Returning True suppresses the exception; False allows propagation
        return self.suppress


def demo_context_manager_protocol():
    # 1. Normal exit without error
    with SafeContextResource(suppress=False) as res:
        assert res.entered is True
        assert res.exited is False
    assert res.exited is True
    assert res.caught_exception is None

    # 2. Exception suppression enabled (Trap 9.5)
    with SafeContextResource(suppress=True) as res_suppress:
        _ = 1 / 0  # ZeroDivisionError occurs here
    # Exception was suppressed; control proceeds here!
    assert res_suppress.exited is True
    assert res_suppress.caught_exception == "ZeroDivisionError"

    # 3. Exception propagation when suppression is disabled
    propagated = False
    try:
        with SafeContextResource(suppress=False) as res_prop:
            _ = 1 / 0
    except ZeroDivisionError:
        propagated = True
    assert propagated is True
    assert res_prop.exited is True


# ==============================================================================
# 6. Exception Hierarchy Masking [Supplementary / IMG-22, IMG-45]
# ==============================================================================

def demo_exception_masking_order():
    # Trap 9.3: Parent class LookupError masks child KeyError
    target_caught = ""
    try:
        sample_dict = {"valid": 100}
        _ = sample_dict["missing"]
    except LookupError:
        target_caught = "LookupError"
    except KeyError:
        target_caught = "KeyError"
    assert target_caught == "LookupError"  # Caught by parent first!


if __name__ == "__main__":
    print("Running Module 09 Executable Examples...")
    demo_object_reference_model()
    demo_module_system()
    demo_exception_handling()
    demo_file_io_and_cursor()
    demo_context_manager_protocol()
    demo_exception_masking_order()
    print("All Module 09 examples executed successfully!")
