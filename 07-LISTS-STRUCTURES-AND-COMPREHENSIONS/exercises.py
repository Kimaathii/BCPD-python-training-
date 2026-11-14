"""
Module 07 Exercises â€” Attempt these BEFORE checking 10-EXAM-PREPARATION/solutions/.

Sources: IMG-03, IMG-53, IMG-54, IMG-61, IMG-67, IMG-70, IMG-71, IMG-74, IMG-75, IMG-77, IMG-78, IMG-79
"""


# -----------------------------------------------------------------------------
# Level 1: Basic Understanding (IMG-03, IMG-53, IMG-61, IMG-77)
# -----------------------------------------------------------------------------
def split_head_middle_tail(sequence: list[object]) -> tuple[object, list[object], object]:
    """Given a list with at least 2 elements:
    - return (first_element, middle_elements_list, last_element) using extended unpacking.
    If the list has length 2, middle_elements_list must be empty [].
    If the list has fewer than 2 elements, raise ValueError("Sequence must have at least 2 items").
    """
    raise NotImplementedError


def safe_slice_modify(items: list[int], start: int, stop: int, replacements: list[int]) -> list[int]:
    """Replace items[start:stop] in place with replacements, and return the modified list."""
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 2: Application (IMG-70, IMG-74)
# -----------------------------------------------------------------------------
def initialize_independent_matrix(rows: int, cols: int, fill: int = 0) -> list[list[int]]:
    """Create an rows x cols 2D grid filled with `fill`.
    
    CRITICAL: Every row MUST be an independent list in memory.
    Modifying matrix[0][0] must NOT modify any other row!
    """
    raise NotImplementedError


def invert_dict_mapping(d: dict[str, int]) -> dict[int, str]:
    """Given a dictionary of unique string keys to unique int values,
    return a new dictionary where keys and values are swapped using a dict comprehension.
    """
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 3: Problem-Solving (IMG-71, IMG-78, IMG-79)
# -----------------------------------------------------------------------------
def flatten_and_filter_matrix(matrix: list[list[int]], min_val: int) -> list[int]:
    """Given a 2D matrix of integers, return a flattened 1D list containing only
    the elements strictly greater than or equal to min_val, preserved in row-major order.
    Use a single list comprehension.
    """
    raise NotImplementedError


def consume_generator_safely(gen_expr) -> tuple[list, list]:
    """Demonstrate generator exhaustion:
    Given a generator expression or iterator:
    1. Consume it completely into a first list.
    2. Attempt to consume it a second time into a second list.
    Return (first_consumption, second_consumption).
    """
    raise NotImplementedError


# -----------------------------------------------------------------------------
# Level 4: Exam-Style Reasoning (Gotchas & Traps)
# -----------------------------------------------------------------------------
def predict_structure_exam_gotchas() -> dict[str, object]:
    """Predict the exact evaluation results of these exam traps:
      - 'sort_returns': return value of [3, 1, 2].sort()
      - 'grid_trap_cell': val of g[1][0] after `g = [[0]*2]*2; g[0][0] = 5`
      - 'exhausted_len': len(list(gen)) when called on an already consumed generator
      - 'shallow_nested_len': len(a[0]) after `a = [[1]]; b = a.copy(); b[0].append(2)`
      - 'singleton_comma_type': type((42,)).__name__
      - 'non_singleton_type': type((42)).__name__
    """
    raise NotImplementedError
