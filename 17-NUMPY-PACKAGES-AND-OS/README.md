# Module 17: NumPy, Packages & the `os` Module

**BCPD Exam Domain:** Domain 4 · Modules & Libraries (15%)  
**Student Manual Reference:** Days 16, 17, 18 & 19 · §16.1–19.6  
**Classroom Alignment:** Week 3, Day 15 (Wednesday 25 Nov 2026) · Slides `D15-01` to `D15-03`  
**Prerequisites:** Modules 01–16

---

## 1. Domain Overview & Learning Objectives

By the end of this module, aligned directly with the official BCPD syllabus, candidates will be able to:
1. **Create NumPy arrays** using dedicated constructor functions (`zeros`, `ones`, `full`, `empty`, `arange`, `linspace`, `eye`, `diag`) with explicit `dtype` specifications.
2. **Inspect multidimensional array attributes**: `shape`, `ndim`, `size`, and `dtype`.
3. **Slice and index arrays**, distinguishing strictly between in-place **views** and memory **copies**, and filter data with **boolean masks** (`m[m > 3]`).
4. **Reshape, flatten, and transpose arrays** (`reshape`, `ravel`, `flatten`, `T`) and apply NumPy **broadcasting rules** across differing shapes.
5. **Summarise and aggregate data** across dimensions using the `axis=` parameter (`axis=0` vs `axis=1`), handling `np.nan` missing values, `np.where`, and `np.clip`.
6. **Organise Python code into packages** using `__init__.py`, configure dependencies with `pip` and virtual environments (`venv`), and traverse the filesystem with `os` and `os.path`.

---

## 2. Array Creation Functions (Manual §16.2)

NumPy provides optimized C-level memory allocators for homogeneous multidimensional arrays (`ndarray`):

| Function | Signature / Example | Shape & Dtype Default | Exam Traps & Nuances |
|---|---|---|---|
| `np.zeros(shape)` | `np.zeros((2, 3))` | $(2, 3)$, `float64` (`0.`) | Allocates and zeros memory. Default `dtype=float`! |
| `np.ones(shape)` | `np.ones(3, dtype=int)` | $(3,)$, explicit `int` | Explicit `dtype=int` yields integer `1`s instead of `1.0`. |
| `np.full(shape, val)` | `np.full((2, 2), 7)` | $(2, 2)$, matches `val` dtype | Fills array with specified scalar constant. |
| `np.empty(shape)` | `np.empty(3)` | $(3,)$, uninitialized | **Memory Garbage Trap:** Fast heap allocation without zeroing memory. Values are indeterminate! |
| `np.arange(start, stop, step)` | `np.arange(0, 10, 3)` | 1D: `[0, 3, 6, 9]` | **Stop Excluded:** Mirrors built-in `range()`; does not include upper bound. |
| `np.linspace(start, stop, num)`| `np.linspace(0, 1, 5)` | 1D: `[0.0, 0.25, 0.5, 0.75, 1.0]` | **Stop Included:** By default `endpoint=True`, inclusive of both boundaries! |
| `np.eye(n)` / `identity(n)` | `np.eye(2)` | $(2, 2)$ Identity | Diagonal elements are `1.0`, off-diagonals are `0.0`. |
| `np.diag(v)` | `np.diag([1, 2])` | Diagonal matrix or vector | If passed 1D array, constructs 2D diagonal matrix; if passed 2D, extracts diagonal. |

---

## 3. Core Array Attributes (Manual §16.3)

Given an ndarray `m`:
- `m.ndim`: Number of array dimensions (axes). Scalar: 0, Vector: 1, Matrix: 2, Tensor: 3+.
- `m.shape`: Tuple of integers showing the size of each dimension (e.g. `(2, 3)` for 2 rows, 3 columns).
- `m.size`: Total count of elements across all axes ($2 \times 3 = 6$).
- `m.dtype`: Data type descriptor of elements (`int32`, `int64`, `float64`, `bool_`).

```python
import numpy as np

m = np.arange(1, 7).reshape(2, 3)
print(m.shape)  # (2, 3)
print(m.ndim)   # 2
print(m.size)   # 6
print(m.dtype)  # int64 or int32
```

---

## 4. Indexing, Slicing & Boolean Masking (Manual §16.5)

### Views vs. Copies Trap
- **Basic Slicing returns a VIEW:**
  `sub = m[0, :]` creates a view referencing the same memory block. Modifying `sub[0] = 99` mutates the parent array `m`!
- **Fancy Indexing & Boolean Masking return a COPY:**
  `filtered = m[m > 3]` allocates independent new memory. Modifying `filtered` does **not** alter `m`.

```python
# Boolean masking:
m = np.arange(1, 7).reshape(2, 3)
mask = m > 3
print(mask)
# [[False False False]
#  [ True  True  True]]

print(m[mask])  # [4 5 6]
```

---

## 5. Reshaping, Flattening & Dimensions (Manual §17.5)

- `m.reshape(rows, cols)`: Returns a view with new shape whose total elements match `m.size`. Pass `-1` for one dimension to auto-calculate (e.g. `m.reshape(3, -1)`).
- `m.ravel()`: Flattens array to 1D, returning a view whenever possible.
- `m.flatten()`: Flattens array to 1D, strictly returning an independent deep copy.
- `m.T`: Transposes axes (flips rows and columns).

---

## 6. The Axis Parameter in Reductions (Manual §18.2)

In multidimensional operations (`sum`, `mean`, `max`, `min`):
- `axis=None`: Default. Flattens array and reduces over all elements.
- `axis=0`: Collapses along rows (operates column-by-column).
- `axis=1`: Collapses along columns (operates row-by-row).

---

## 7. Packages, Virtual Environments & `os` (Manual §19.1–19.5)

### Packaging & `__init__.py`
- A folder containing `__init__.py` is treated by Python as an importable package.
- `__all__ = ['func_a', 'func_b']`: Controls public API when imported via `from pkg import *`.

### Environment Management
- `python -m venv .venv`: Creates an isolated virtual environment.
- `pip freeze > requirements.txt`: Serializes installed dependencies.
- `pip install -r requirements.txt`: Reproduces environment.

### Operating System Interfaces (`os` & `os.path`)
- `os.getcwd()`: Returns absolute path to current working directory.
- `os.listdir(path)`: Lists directory contents.
- `os.path.join("a", "b", "c.txt")`: Platform-agnostic path concatenation.
- `os.path.exists(path)` & `os.path.isfile(path)`: Filesystem existence probes.
- `os.environ`: Dictionary of current process environment variables.
