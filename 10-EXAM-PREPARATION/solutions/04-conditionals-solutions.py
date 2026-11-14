"""Solutions for Module 04 Exercises (04-CONDITIONALS-AND-LOGIC/exercises.py).

Target Python: 3.10+
"""


def fallback_username(raw_name: str, default: str = "Guest") -> str:
    """Return stripped name if non-empty; otherwise default."""
    return raw_name.strip() or default


def letter_grade(score: int) -> str:
    """Classify score into grade."""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    return "F"


def is_leap_year(year: int) -> bool:
    """Leap year condition: (div by 4 and not 100) or (div by 400)."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def route_action(command: str) -> str:
    """Pattern match tokens using Python 3.10+ match-case."""
    match command.split():
        case ["exit" | "quit"]:
            return "Terminating"
        case ["get", item]:
            return f"Fetching {item}"
        case ["set", key, value]:
            return f"Assigning {key}={value}"
        case _:
            return "Invalid"


def predict_logic_values() -> dict[str, object]:
    """Exact evaluated outputs."""
    return {
        "chained_or": [0],
        "short_and": [],
        "all_check": True,
        "any_check": False,
        "de_morgan": True,
    }


if __name__ == "__main__":
    assert fallback_username("   ") == "Guest"
    assert fallback_username("ada") == "ada"
    assert letter_grade(85) == "A"
    assert letter_grade(72) == "B"
    assert letter_grade(60) == "C"
    assert letter_grade(59) == "F"
    assert is_leap_year(2024) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True
    assert route_action("quit") == "Terminating"
    assert route_action("get user") == "Fetching user"
    assert route_action("set host localhost") == "Assigning host=localhost"
    assert route_action("unknown foo") == "Invalid"
    assert predict_logic_values() == {
        "chained_or": [0],
        "short_and": [],
        "all_check": True,
        "any_check": False,
        "de_morgan": True,
    }
    print("All Module 04 solution assertions passed.")
