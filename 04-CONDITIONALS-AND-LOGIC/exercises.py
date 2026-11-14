"""Module 04 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-32, IMG-36, IMG-37, IMG-38, IMG-45, IMG-47
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding
# -----------------------------------------------------------------------------
def fallback_username(raw_name: str, default: str = "Guest") -> str:
    """Return stripped raw_name if non-empty, otherwise return default using 'or'."""
    # TODO: use stripped name or default
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (Lab 3.1 â€” IMG-45)
# -----------------------------------------------------------------------------
def letter_grade(score: int) -> str:
    """Return 'A' (>=80), 'B' (>=70), 'C' (>=60), else 'F'."""
    # TODO: implement if/elif/else
    raise NotImplementedError


def is_leap_year(year: int) -> bool:
    """Lab 3.1 step 2: True if year is divisible by 4 and not 100, or div by 400."""
    # TODO: implement leap year condition
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving (Python 3.10+ match-case)
# -----------------------------------------------------------------------------
def route_action(command: str) -> str:
    """Use match-case on command.split():
      - ['exit' | 'quit'] -> 'Terminating'
      - ['get', item] -> 'Fetching <item>'
      - ['set', key, value] -> 'Assigning <key>=<value>'
      - _ -> 'Invalid'
    """
    # TODO: implement match-case
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning
# -----------------------------------------------------------------------------
def predict_logic_values() -> dict[str, object]:
    """Predict exact evaluated outputs before running:
      - 'chained_or': 0 or "" or [0]
      - 'short_and': 5 and [] and "a"
      - 'all_check': all([1, 2, 3])
      - 'any_check': any([0, "", None])
      - 'de_morgan': not (True and False) == (not True or not False)
    """
    # TODO: replace None with predicted values
    return {
        "chained_or": None,
        "short_and": None,
        "all_check": None,
        "any_check": None,
        "de_morgan": None,
    }
