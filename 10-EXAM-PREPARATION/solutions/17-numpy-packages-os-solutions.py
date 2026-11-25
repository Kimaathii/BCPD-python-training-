"""Module 17: NumPy, Packages & the os Module.

Clean Reference Implementations & Comprehensive Solution Suite
Target: Python 3.10+ (Verified on Python 3.15.2)

Classroom Alignment: Manual Days 16–19 §16.1–19.6, Slides D15-01 to D15-03, Lab 15.1
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
    """Reshape a 1D sequence into a 2D matrix of (rows, cols)."""
    if rows * cols != len(flat_list):
        raise ValueError(f"Cannot reshape sequence of size {len(flat_list)} into shape ({rows}, {cols})")
    return [list(flat_list[i * cols : (i + 1) * cols]) for i in range(rows)]


# ==============================================================================
# LEVEL 3: Boolean Masking & Thresholding [Course: D15-01]
# ==============================================================================

def apply_threshold_filter(grid: Sequence[Sequence[float | int]], threshold: float | int) -> List[float | int]:
    """Filter elements strictly greater than threshold, flattening into 1D list."""
    result: List[float | int] = []
    for row in grid:
        for val in row:
            if val > threshold:
                result.append(val)
    return result


def verify_boolean_mask_is_copy(original_grid: List[List[int]], threshold: int) -> bool:
    """Verify that filtering produces an independent memory copy."""
    filtered = apply_threshold_filter(original_grid, threshold)
    if filtered:
        filtered[0] = 999999
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


def main() -> None:
    # 1. Level 1 verification
    z = create_zeros_matrix(2, 3)
    assert len(z) == 2 and len(z[0]) == 3
    assert create_linear_samples(0, 1, 5) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert create_stepped_range(0, 10, 3) == [0, 3, 6, 9]

    # 2. Level 2 verification
    attrs = inspect_grid_attributes([[1, 2], [3, 4]])
    assert attrs["shape"] == (2, 2) and attrs["is_square"] is True
    assert reshape_1d_to_2d([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]]

    # 3. Level 3 verification
    assert apply_threshold_filter([[1, 2, 3], [4, 5, 6]], 3) == [4, 5, 6]
    assert verify_boolean_mask_is_copy([[1, 2], [3, 4]], 2) is True

    # 4. Level 4 verification
    pixels = create_checkerboard_pixel_array(2, 0, 255)
    assert pixels == [[255, 0], [0, 255]]

    print("Module 17 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
