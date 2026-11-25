"""Module 17 Progressive Exercises & Lab 15.1 Foundation.

Contains:
- Level 1: Array Creation & Dtypes (zeros, ones, arange, linspace) [Course: D15-03]
- Level 2: Array Dimensions & Reshaping (shape, size, ndim, reshape) [Course: D15-02]
- Level 3: Boolean Masking & Threshold Filtering (m[m > threshold]) [Course: D15-01]
- Level 4: 2D Pixel Grid Pattern Generator (Lab 15.1 Foundation) [Course: D15-02]
- Automated Test Harness (run directly: python exercises.py)
"""

from __future__ import annotations

from typing import Any, Dict, List, Sequence, Tuple


# ==============================================================================
# LEVEL 1: Array Creation & Dtypes [Course: D15-03]
# ==============================================================================

def create_zeros_matrix(rows: int, cols: int) -> List[List[float]]:
    """Return a 2D matrix of shape (rows, cols) filled with 0.0 floats."""
    return [[0.0 for _ in range(cols)] for _ in range(rows)]


def create_linear_samples(start: float, stop: float, num: int) -> List[float]:
    """Generate evenly spaced numbers over specified interval, inclusive of stop (like np.linspace)."""
    if num <= 0:
        return []
    if num == 1:
        return [float(start)]
    step = (stop - start) / (num - 1)
    return [round(start + i * step, 6) for i in range(num)]


def create_stepped_range(start: int, stop: int, step: int) -> List[int]:
    """Generate stepped numbers, strictly excluding stop (like np.arange)."""
    return list(range(start, stop, step))


# ==============================================================================
# LEVEL 2: Dimensions & Reshaping [Course: D15-02]
# ==============================================================================

def inspect_grid_attributes(grid: Sequence[Sequence[Any]]) -> Dict[str, Any]:
    """Inspect multidimensional grid attributes (ndim, shape, size)."""
    if not grid or not isinstance(grid[0], (list, tuple)):
        return {
            "ndim": 1 if grid else 0,
            "shape": (len(grid),),
            "size": len(grid),
        }
    rows = len(grid)
    cols = len(grid[0])
    return {
        "ndim": 2,
        "shape": (rows, cols),
        "size": rows * cols,
        "is_square": rows == cols,
    }


def reshape_1d_to_2d(flat_list: Sequence[Any], rows: int, cols: int) -> List[List[Any]]:
    """Reshape a 1D sequence into a 2D matrix of (rows, cols).
    
    Raises ValueError if rows * cols != len(flat_list).
    """
    if rows * cols != len(flat_list):
        raise ValueError(f"Cannot reshape sequence of size {len(flat_list)} into shape ({rows}, {cols})")
    return [list(flat_list[i * cols : (i + 1) * cols]) for i in range(rows)]


# ==============================================================================
# LEVEL 3: Boolean Masking & Thresholding [Course: D15-01]
# ==============================================================================

def apply_threshold_filter(grid: Sequence[Sequence[float | int]], threshold: float | int) -> List[float | int]:
    """Filter elements strictly greater than threshold, flattening into 1D list (emulating m[m > 3])."""
    result: List[float | int] = []
    for row in grid:
        for val in row:
            if val > threshold:
                result.append(val)
    return result


def verify_boolean_mask_is_copy(original_grid: List[List[int]], threshold: int) -> bool:
    """Verify that filtering produces an independent memory copy rather than a mutating view."""
    filtered = apply_threshold_filter(original_grid, threshold)
    if filtered:
        filtered[0] = 999999  # mutate extracted list
    # Original grid must remain untouched
    for row in original_grid:
        if 999999 in row:
            return False
    return True


# ==============================================================================
# LEVEL 4: Lab 15.1 Foundation — Pixel Array Generator [Course: D15-02]
# ==============================================================================

def create_checkerboard_pixel_array(n: int, black_val: int = 0, white_val: int = 255) -> List[List[int]]:
    """Create an n x n pixel grid with alternating black and white pixel values."""
    grid: List[List[int]] = []
    for r in range(n):
        row: List[int] = []
        for c in range(n):
            row.append(white_val if (r + c) % 2 == 0 else black_val)
        grid.append(row)
    return grid


# ==============================================================================
# Automated Test Suite
# ==============================================================================

def test_level_1() -> None:
    # 1. Zeros matrix
    z = create_zeros_matrix(2, 3)
    assert len(z) == 2 and len(z[0]) == 3
    assert all(val == 0.0 for row in z for val in row)

    # 2. Linspace stop-included
    samples = create_linear_samples(0, 1, 5)
    assert samples == [0.0, 0.25, 0.5, 0.75, 1.0]

    # 3. Arange stop-excluded
    rng = create_stepped_range(0, 10, 3)
    assert rng == [0, 3, 6, 9]
    print("Level 1 Tests: PASSED")


def test_level_2() -> None:
    grid = [[1, 2, 3], [4, 5, 6]]
    attrs = inspect_grid_attributes(grid)
    assert attrs["ndim"] == 2
    assert attrs["shape"] == (2, 3)
    assert attrs["size"] == 6
    assert attrs["is_square"] is False

    flat = list(range(1, 7))
    reshaped = reshape_1d_to_2d(flat, 2, 3)
    assert reshaped == [[1, 2, 3], [4, 5, 6]]

    try:
        reshape_1d_to_2d(flat, 2, 4)
        assert False, "Should raise ValueError on mismatched shape"
    except ValueError:
        pass
    print("Level 2 Tests: PASSED")


def test_level_3() -> None:
    grid = [[1, 2, 3], [4, 5, 6]]
    # Day 15 kickoff verification: m[m > 3] == [4, 5, 6]
    filtered = apply_threshold_filter(grid, 3)
    assert filtered == [4, 5, 6]

    # Copy vs view integrity
    assert verify_boolean_mask_is_copy([[1, 2], [3, 4]], 2) is True
    print("Level 3 Tests: PASSED")


def test_level_4() -> None:
    pixels = create_checkerboard_pixel_array(4, black_val=0, white_val=255)
    assert len(pixels) == 4 and len(pixels[0]) == 4
    assert pixels[0] == [255, 0, 255, 0]
    assert pixels[1] == [0, 255, 0, 255]
    assert pixels[2] == [255, 0, 255, 0]
    assert pixels[3] == [0, 255, 0, 255]
    print("Level 4 Tests (Lab 15.1 Foundation): PASSED")


def run_all_tests() -> None:
    test_level_1()
    test_level_2()
    test_level_3()
    test_level_4()
    print("\n" + "=" * 60)
    print("✅ ALL MODULE 17 EXERCISES & LAB 15.1 FOUNDATION PASSED")
    print("=" * 60)


def main() -> None:
    run_all_tests()


if __name__ == "__main__":
    main()
