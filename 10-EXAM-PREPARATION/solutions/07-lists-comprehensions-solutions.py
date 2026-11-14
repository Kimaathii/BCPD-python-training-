"""
Solutions for Module 07 Exercises (07-LISTS-STRUCTURES-AND-COMPREHENSIONS/exercises.py).

Target Python: 3.10+
"""


def split_head_middle_tail(sequence: list[object]) -> tuple[object, list[object], object]:
    """Return (first, middle, last) using extended unpacking."""
    if len(sequence) < 2:
        raise ValueError("Sequence must have at least 2 items")
    first, *middle, last = sequence
    return first, middle, last


def safe_slice_modify(items: list[int], start: int, stop: int, replacements: list[int]) -> list[int]:
    """Replace slice in place and return list."""
    items[start:stop] = replacements
    return items


def initialize_independent_matrix(rows: int, cols: int, fill: int = 0) -> list[list[int]]:
    """Create independent rows using list comprehension."""
    return [[fill] * cols for _ in range(rows)]


def invert_dict_mapping(d: dict[str, int]) -> dict[int, str]:
    """Invert dict mapping with comprehension."""
    return {val: key for key, val in d.items()}


def flatten_and_filter_matrix(matrix: list[list[int]], min_val: int) -> list[int]:
    """Flatten and filter in a single list comprehension."""
    return [elem for row in matrix for elem in row if elem >= min_val]


def consume_generator_safely(gen_expr) -> tuple[list, list]:
    """Demonstrate generator exhaustion."""
    first = list(gen_expr)
    second = list(gen_expr)
    return first, second


def predict_structure_exam_gotchas() -> dict[str, object]:
    """Exact evaluated outputs for list and structure exam traps."""
    return {
        "sort_returns": None,
        "grid_trap_cell": 5,
        "exhausted_len": 0,
        "shallow_nested_len": 2,
        "singleton_comma_type": "tuple",
        "non_singleton_type": "int",
    }


if __name__ == "__main__":
    # Test split_head_middle_tail
    f, m, l = split_head_middle_tail([10, 20, 30, 40, 50])
    assert f == 10 and m == [20, 30, 40] and l == 50
    f2, m2, l2 = split_head_middle_tail([1, 2])
    assert f2 == 1 and m2 == [] and l2 == 2
    try:
        split_head_middle_tail([1])
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # Test safe_slice_modify
    lst = [1, 2, 3, 4, 5]
    res = safe_slice_modify(lst, 1, 4, [20, 30])
    assert res == [1, 20, 30, 5]
    assert res is lst  # modified in place

    # Test initialize_independent_matrix
    mat = initialize_independent_matrix(3, 3, 0)
    mat[0][0] = 99
    assert mat[0] == [99, 0, 0]
    assert mat[1] == [0, 0, 0]
    assert mat[2] == [0, 0, 0]
    assert mat[0] is not mat[1]

    # Test invert_dict_mapping
    d = {"a": 1, "b": 2, "c": 3}
    assert invert_dict_mapping(d) == {1: "a", 2: "b", 3: "c"}

    # Test flatten_and_filter_matrix
    grid = [[1, 5, 2], [8, 3, 9], [4, 7, 6]]
    assert flatten_and_filter_matrix(grid, 5) == [5, 8, 9, 7, 6]

    # Test consume_generator_safely
    gen = (x * 10 for x in range(3))
    first_run, second_run = consume_generator_safely(gen)
    assert first_run == [0, 10, 20]
    assert second_run == []

    # Test predict_structure_exam_gotchas
    gotchas = predict_structure_exam_gotchas()
    assert gotchas["sort_returns"] is None
    
    g = [[0] * 2] * 2
    g[0][0] = 5
    assert gotchas["grid_trap_cell"] == g[1][0]

    gen2 = (x for x in [1, 2])
    list(gen2)
    assert gotchas["exhausted_len"] == len(list(gen2))

    a = [[1]]
    b = a.copy()
    b[0].append(2)
    assert gotchas["shallow_nested_len"] == len(a[0])

    assert gotchas["singleton_comma_type"] == type((42,)).__name__
    assert gotchas["non_singleton_type"] == type((42)).__name__

    print("All Module 07 solutions assertions passed successfully!")
