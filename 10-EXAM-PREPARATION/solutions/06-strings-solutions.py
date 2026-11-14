"""
Solutions for Module 06 Exercises (06-STRINGS-AND-FORMATTING/exercises.py).

Target Python: 3.10+
"""


def safe_slice_and_index(text: str, start: int, stop: int, index: int) -> tuple[str, str | None]:
    """Return slice and indexed char safely."""
    slice_res = text[start:stop]
    try:
        index_res = text[index]
    except IndexError:
        index_res = None
    return slice_res, index_res


def sanitize_input(raw: str) -> str:
    """Clean user input: strip whitespace, lowercase, and collapse multiple spaces."""
    words = raw.strip().lower().split()
    return " ".join(words)


def format_invoice_line(item_name: str, price: float, quantity: int) -> str:
    """Format an invoice line using format specification mini-language."""
    formatted_price = f"${price:>10,.2f}"
    return f"{item_name:<15} | {formatted_price} | {quantity:05d}"


def classify_numeric_string(s: str) -> dict[str, bool]:
    """Return boolean classifications for isdecimal, isdigit, isnumeric."""
    return {
        "isdecimal": s.isdecimal(),
        "isdigit": s.isdigit(),
        "isnumeric": s.isnumeric(),
    }


def simulate_car_controller(commands: list[str]) -> list[str]:
    """Simulate Car Game controller from IMG-66."""
    responses = []
    started = False
    
    for raw in commands:
        cmd = raw.strip().lower()
        if cmd == "start":
            if started:
                responses.append("Car is already started!")
            else:
                started = True
                responses.append("Car started...")
        elif cmd == "stop":
            if not started:
                responses.append("Car is already stopped!")
            else:
                started = False
                responses.append("Car stopped.")
        elif cmd == "help":
            responses.append("start - start car | stop - stop car | quit - exit")
        elif cmd == "quit":
            responses.append("Engine turned off.")
            break
        else:
            responses.append(f"Unknown command: {cmd}")
            
    return responses


def predict_string_exam_gotchas() -> dict[str, object]:
    """Exact evaluated outputs for exam traps."""
    return {
        "slice_out_of_bounds": "",
        "find_not_found": -1,
        "fraction_isnumeric": True,
        "fraction_isdigit": False,
        "fraction_isdecimal": False,
        "strip_chars": "nan",
        "title_apostrophe": "Don'T",
    }


if __name__ == "__main__":
    # Test safe_slice_and_index
    s_res, i_res = safe_slice_and_index("Python", 10, 20, 2)
    assert s_res == ""
    assert i_res == "t"
    _, i_none = safe_slice_and_index("Python", 0, 2, 100)
    assert i_none is None

    # Test sanitize_input
    assert sanitize_input("  HELLO    WORLD   BCPD  ") == "hello world bcpd"

    # Test format_invoice_line
    line = format_invoice_line("Widget A", 1234.5, 7)
    assert line == "Widget A        | $  1,234.50 | 00007"

    # Test classify_numeric_string
    assert classify_numeric_string("123") == {"isdecimal": True, "isdigit": True, "isnumeric": True}
    assert classify_numeric_string("Â²") == {"isdecimal": False, "isdigit": True, "isnumeric": True}
    assert classify_numeric_string("Â½") == {"isdecimal": False, "isdigit": False, "isnumeric": True}
    assert classify_numeric_string("-5") == {"isdecimal": False, "isdigit": False, "isnumeric": False}

    # Test simulate_car_controller
    cmds = ["START", "start", "STOP", "stop", "help", "accel", "quit", "start"]
    expected_resp = [
        "Car started...",
        "Car is already started!",
        "Car stopped.",
        "Car is already stopped!",
        "start - start car | stop - stop car | quit - exit",
        "Unknown command: accel",
        "Engine turned off."
    ]
    assert simulate_car_controller(cmds) == expected_resp

    # Test predict_string_exam_gotchas
    gotchas = predict_string_exam_gotchas()
    assert gotchas["slice_out_of_bounds"] == "hello"[10:20]
    assert gotchas["find_not_found"] == "hello".find("z")
    assert gotchas["fraction_isnumeric"] == "Â½".isnumeric()
    assert gotchas["fraction_isdigit"] == "Â½".isdigit()
    assert gotchas["fraction_isdecimal"] == "Â½".isdecimal()
    assert gotchas["strip_chars"] == "banana".strip("ba")
    assert gotchas["title_apostrophe"] == "don't".title()

    print("All Module 06 solutions assertions passed successfully!")
