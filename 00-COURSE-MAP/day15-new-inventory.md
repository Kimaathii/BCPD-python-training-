# Day 15 Classroom Screenshot Inventory & Verbatim Extractions
**Class Date:** Wednesday 25 Nov 2026 (Week 3, Day 15)  
**Subject:** NumPy, Packages & the `os` Module  
**BCPD Exam Weight:** Domain 4 · Modules & Libraries (15%)  
**Student Manual Mapping:** Days 16, 17, 18 & 19 · §16.1–19.6  
**Image Files Staged:** 3 JPEG files (`WhatsApp Image 2026-11-25 at 22.33.55oi.jpeg`, `22.33.55.jpeg`, `22.33.54.jpeg`)  
**Curriculum Mapping:** Module 17 (`17-NUMPY-PACKAGES-AND-OS`) & Central Exam Prep Hub (`10-EXAM-PREPARATION/`)

---

## 1. Master Slide Index & Provenance Cross-Reference

| Slide Tag | Source File(s) | Slide Title / Manual Ref | Core Topic / Code File | Target Curriculum Location |
|---|---|---|---|---|
| `[Course: D15-01]` | `22.33.55oi.jpeg` | NumPy, Packages & the `os` Module (Title Slide) | Domain 4 overview, `day15.py`, array creation & boolean masking | `17-NUMPY-PACKAGES-AND-OS/README.md` |
| `[Course: D15-02]` | `22.33.55.jpeg` | Today's Objectives & Agenda (§16.1–§19.6) | 5 competencies, 12 agenda items, Lab 15.1 (Pixel arrays) | `17-NUMPY-PACKAGES-AND-OS/README.md` |
| `[Course: D15-03]` | `22.33.54.jpeg` | Array creation functions (§16.2) | `zeros`, `ones`, `full`, `empty`, `arange`, `linspace`, `eye`, `diag` | `17-NUMPY-PACKAGES-AND-OS/examples.py`, `exercises.py` |

---

## 2. Verbatim Code & Content Transcriptions

### Slide `D15-01`: Title Slide — NumPy, Packages & the `os` Module
- **Header:** `WEEK 3 • DAY 15 • WEDNESDAY 25 NOV 2026`
- **Domain:** `Domain 4 • Modules & Libraries (15%)`
- **Student Manual:** `Days 16, 17, 18 & 19 • §16.1–19.6`
- **Scope Statement:**
  > "Create, slice and broadcast arrays, summarise data along an axis, then organise code in packages and work with files and folders through the os module."
- **Verbatim Code (`day15.py`):**
```python
import numpy as np

m = np.arange(1, 7).reshape(2, 3)
print(m.shape, m.dtype)
print(m[m > 3])  # [4 5 6]
```

---

### Slide `D15-02`: Today's Objectives & Agenda
- **By the end of today you can:**
  1. Create arrays and read `shape`, `ndim`, `size` and `dtype`
  2. Slice arrays (views vs copies) and filter with boolean masks
  3. Apply the broadcasting rules and reshape arrays
  4. Summarise data with `axis=` and handle missing values
  5. Organise code in packages, use `pip` and venvs, and work with files and folders through `os`
- **Class Agenda Mapping:**
  - `16.2` Array creation functions
  - `16.3` Array attributes
  - `16.5` Slicing, views & copies
  - `16.5` Boolean & fancy indexing
  - `17.4` The broadcasting rules
  - `17.5` reshape, ravel, flatten & transpose
  - `18.2` The axis parameter
  - `18.3` Missing data: `nan`, `where` & `clip`
  - `19.1` Packages: organising modules
  - `19.4` `pip`, requirements & virtual environments
  - `19.5` `os` & `os.path` essentials
  - `lab` Lab 15.1 — Pixel arrays

---

### Slide `D15-03`: Array Creation Functions (Manual §16.2)
- **Header:** `MANUAL §16.2`
- **Title:** `Array creation functions`
- **Function Specification Matrix:**
  | Function | Example | Result | BCPD Exam Nuance |
  |---|---|---|---|
  | `np.zeros(shape)` | `np.zeros((2, 3))` | `2 × 3 array of 0. (floats)` | Default `dtype=float64` unless specified |
  | `np.ones(shape)` | `np.ones(3, dtype=int)` | `[1 1 1]` | `dtype=int` produces integer array |
  | `np.full(shape, value)` | `np.full((2, 2), 7)` | `2 × 2 array of 7` | Constant fill value |
  | `np.empty(shape)` | `np.empty(3)` | `Uninitialised — values are garbage` | Allocates memory without initializing |
  | `np.arange(start, stop, step)` | `np.arange(0, 10, 3)` | `[0 3 6 9]` | **Stop excluded** (standard Python range rule) |
  | `np.linspace(start, stop, num)` | `np.linspace(0, 1, 5)` | `0, 0.25, 0.5, 0.75, 1` | **Stop included** by default (`endpoint=True`) |
  | `np.eye(n) / np.identity(n)` | `np.eye(2)` | `2 × 2 identity matrix` | 1s on main diagonal, 0s elsewhere |
  | `np.diag(values)` | `np.diag([1, 2])` | `[[1 0], [0 2]]` | Construct diagonal matrix or extract diagonal |
