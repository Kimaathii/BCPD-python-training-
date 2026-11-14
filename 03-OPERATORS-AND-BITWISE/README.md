# Module 03 â€” Operators, Precedence & Bitwise Flags

> **Sources:** `IMG-07`, `IMG-08`, `IMG-10`, `IMG-11`, `IMG-13`, `IMG-14`, `IMG-15`, `IMG-16`, `IMG-17`, `IMG-18`, `IMG-20`, `IMG-30` (Q2â€“Q4), `IMG-31` (`Day 2 Â· MANUAL Â§2.22â€“2.29, Â§2.32 & BEYOND THE MANUAL`)

---

## 1. Conceptual Foundation

- **Arithmetic Operators `[Course: IMG-07, IMG-08]`:**
  - `/` (true division) **always** returns a `float` (`7 / 2 â†’ 3.5`).
  - `//` (floor division) rounds down **toward negative infinity ($-\infty$)**, not toward zero (`7 // 2 â†’ 3`, `-7 // 2 â†’ -4`).
  - `%` (modulo) satisfies `a == (a // b) * b + (a % b)` and **takes the sign of the divisor** (`-7 % 3 â†’ 2`, because `-7 // 3 == -3` and `-7 - (-3 * 3) == 2`).
  - `**` (exponentiation, right-associative) and `divmod(a, b)` returning `(a // b, a % b)`.
- **Augmented Assignment & Walrus Operator `:=` `[Course: IMG-07]`:**
  - `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` update/rebind a variable in place of `x = x <op> y`.
  - `:=` (Python 3.8+) assigns inside an expression (e.g., `if (n := len("hello")) > 3:`).
- **Operator Precedence & Associativity `[Course: IMG-10, IMG-11]`:**
  - Expressions evaluate by precedence level (highest first), left-to-right within a levelâ€”**except `**`**, which is **right-to-left** (`2 ** 3 ** 2 == 512`).
  - **Expression vs. Statement `[Course: IMG-11]`:** An expression produces a value (`3 * 2`); a statement performs an action (`x = 5`, `if ...:`).
- **Bitwise Operators & Flags (`BEYOND THE MANUAL`) `[Course: IMG-13â€“IMG-17]`:**
  - Operate on binary representations of integers: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT, `~x == -x - 1`), `<<` (left shift: $\times 2$ per bit), `>>` (right shift: $\div 2$ floored per bit).
  - Used for compact permission flags/masks (`READ, WRITE, EXEC = 1, 2, 4`).

---

## 2. Mental Models

- **Floor Division `//` as an Elevator Going Down:**
  - Truncation toward zero chops off decimals (`-3.5 â†’ -3`). Floor division pushes the number **down** on the number line to the next lower integer (`-3.5 â†’ -4`, `-6.67 â†’ -7`).
  - **Instructor Whiteboard Trace `[Course: IMG-08]`:** On the board, the instructor verified `20 // 3 = 6`, `20 - 18 = 2`, drew `-5 -4 -3 -2 -1 0 1 2 3 4`, and posed `-20 % 3` and `-20 // 3`: `-20 / 3 = -6.66...` floors down to **`-7`**, leaving remainder `-20 - (-7 * 3) =` **`1`**.
- **Two's Complement `~x == -x - 1` (`[Supplementary]` Why `~12` is `-13`, Not `3`):**
  - Beginners expect flipping `0b1100` (`12`) to yield `0b0011` (`3`). Because Python integers have **unlimited** bits, there are infinitely many leading `0`s (`...00001100`). Flipping every bit produces infinitely many leading `1`s (`...11110011`), which in two's complement represents **`-13`** (`-12 - 1`).
- **Bit Flags as Light Switches `[Course: IMG-14, IMG-17]`:**
  - `|` flips switches **ON**, `&` **peeks** whether a switch is ON, `& ~FLAG` forces a switch **OFF**, and `^` **toggles** a switch.
- **Instructor Binary Subtraction Table `[Course: IMG-15, IMG-16]`:**
  - Powers of 2 (`512 256 128 64 32 16 8 4 2 1`) convert `564` via greedy subtraction: `564 - 512 = 52`, `52 - 32 = 20`, `20 - 16 = 4`, `4 - 4 = 0` â†’ `1000110100`.

---

## 3. Syntax and Code

### A. Precedence Table `[Course: IMG-10]`

| Level | Operators | Notes |
|---:|---|---|
| 1 | `( )` parentheses | Always evaluated first |
| 2 | `**` | Right-to-left: `2 ** 3 ** 2 = 512` |
| 3 | unary `+x`, `-x`, `~x` | `-2 ** 2 = -4` (`**` binds tighter than unary `-`) |
| 4 | `*`, `/`, `//`, `%` | Left-to-right |
| 5 | `+`, `-` | Left-to-right |
| 6 | `<<`, `>>` | Below arithmetic (`1 + 2 << 1 == 6`) |
| 7 | `&`, then `^`, then `\|` | Below shifts, above comparisons |
| 8 | `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in` | Comparisons chain: `1 < x < 5` |
| 9 *(digit obscured by head in `IMG-10`)* | `not`, then `and`, then `or` | Lowest of the common operators |

### B. Arithmetic & Assignment `[Course: IMG-07, IMG-08 | arith.py]`

**ORIGINAL CLASSROOM CODE:**
```python
print(7 / 2)               # -> 3.5
print(7 // 2)              # -> 3
print(-7 // 2)             # -> -4
print(-7 % 3)              # -> 2
print(2 ** 10)             # -> 1024
print(divmod(17, 5))       # -> (3, 2)
x = 5
x **= 2
print(x)                   # -> 25
if (n := len("hello")) > 3:
    print(n)               # -> 5
```

### C. Step-by-Step Evaluation `[Course: IMG-11 | evaluate.py]`

**ORIGINAL CLASSROOM CODE:**
```python
x = 10
result = x + 3 * 2 ** 2 // 4 - 1
# 2 ** 2      gives 4
# 3 * 4       gives 12
# 12 // 4     gives 3
# 10 + 3 - 1  gives 12
print(result)                     # -> 12

print(not x > 5 and x % 2 == 0)   # -> False
print(5 > 3 > 1)                  # -> True
print(0.1 + 0.2 == 0.3)           # -> False
```

### D. Bitwise & Flags `[Course: IMG-13, IMG-14, IMG-17 | bits.py & flags.py]`

**ORIGINAL CLASSROOM CODE (`bits.py`):**
```python
a, b = 0b1100, 0b1010   # 12, 10

print(a & b)            # -> 8
print(a | b)            # -> 14
print(a ^ b)            # -> 6
print(~a)               # -> -13
print(a << 2)           # -> 48
print(a >> 2)           # -> 3
print(bin(a & b))       # -> 0b1000
```

**ORIGINAL CLASSROOM CODE (`flags.py`):**
```python
READ, WRITE, EXEC = 1, 2, 4   # 0b001, 0b010, 0b100

perms = READ | WRITE          # combine flags
print(perms)                  # -> 3
print(bool(perms & WRITE))    # -> True   (is it set?)
print(bool(perms & EXEC))     # -> False
perms |= EXEC                 # turn a flag on
perms &= ~WRITE               # turn a flag off
print(bin(perms))             # -> 0b101
print(perms ^ READ)           # -> 4      (toggle)
print(1 + 2 << 1)             # -> 6      (+ before <<)
```

### E. Lab 2.1 â€” BMI Calculator & Bit Flags `[Course: IMG-18, IMG-20 | bmi.py]`

**ORIGINAL CLASSROOM CODE (`bmi.py`):**
```python
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / height ** 2
print("BMI:", round(bmi, 1))
print("Overweight?", bmi >= 25)

READ, WRITE, EXEC = 1, 2, 4
perms = 5
print("Can read? ", bool(perms & READ))
print("Can write?", bool(perms & WRITE))
```

**CORRECTED / IMPROVED CODE (`[Supplementary]` â€” completes Lab step 4 & guards `height <= 0`):**
```python
def compute_bmi_and_flags(weight: float, height: float, perms: int = 5) -> None:
    if height <= 0:
        raise ValueError("Height must be positive.")
    bmi = weight / height ** 2
    print("BMI:", round(bmi, 1))
    print("Overweight?", bmi >= 25)

    READ, WRITE, EXEC = 1, 2, 4
    print("Can read? ", bool(perms & READ))
    print("Can write?", bool(perms & WRITE))
    print("Can exec? ", bool(perms & EXEC))   # Missing in IMG-20!
```
*Difference:* `IMG-18` step 4 asks *"for `perms = 5`, print which flags are set"*, yet `IMG-20` stopped after `READ` and `WRITE` without printing `EXEC`.

---

## 4. Line-by-Line Explanation (`evaluate.py` & `flags.py`)

- `not x > 5 and x % 2 == 0` (`x = 10`): `>` and `==` (Level 8) and `%` (Level 4) all bind tighter than `not` and `and` (Level 9). So `x > 5` (`True`) and `x % 2 == 0` (`True`) evaluate first, then `not True` (`False`), then `False and True` (`False`).
- `perms |= EXEC`: `3 | 4` (`0b011 | 0b100 = 0b111 = 7`).
- `perms &= ~WRITE`: `~2` is `-3` (`...11111101` in two's complement). ANDing `0b111` with `~0b010` clears only bit 1 â†’ `0b101` (`5`).
- `1 + 2 << 1`: `+` (Level 5) precedes `<<` (Level 6), so `(1 + 2) << 1 == 3 << 1 == 6`.

---

## 5. Code Tracing (`result = x + 3 * 2 ** 2 // 4 - 1`, `x = 10`)

| Step | Sub-expression | Precedence Level | Value | Remaining Expression |
|---|---|---|---|---|
| 1 | `2 ** 2` | Level 2 (`**`) | `4` | `10 + 3 * 4 // 4 - 1` |
| 2 | `3 * 4` | Level 4 (`*`, left-to-right) | `12` | `10 + 12 // 4 - 1` |
| 3 | `12 // 4` | Level 4 (`//`) | `3` | `10 + 3 - 1` |
| 4 | `10 + 3` | Level 5 (`+`, left-to-right) | `13` | `13 - 1` |
| 5 | `13 - 1` | Level 5 (`-`) | `12` | `12` |

---

## 6. Common Pitfalls

1. **Expecting `-7 // 2 == -3` (`IMG-07, IMG-30`):** Python floors toward $-\infty$ (`-4`), unlike C/Java integer truncation toward zero.
2. **Expecting `2 ** 3 ** 2 == 64` (`IMG-10, IMG-30`):** `**` is right-associative â†’ `2 ** 9 = 512`.
3. **Writing `-2 ** 2` expecting `+4` (`IMG-10`):** Power runs before unary minus â†’ `-(2 ** 2) = -4`. Use `(-2) ** 2` for `+4`.
4. **Expecting `1 + 2 << 1 == 5` (`IMG-14`):** `+` binds tighter than `<<` â†’ `3 << 1 = 6`.
5. **Misusing `~x` as unsigned bit flip (`IMG-13`):** `~12` is `-13`, never `3`.

---

## 7. MCQ Examination Traps

### Instructor Slide Questions `[Course: IMG-30 | Reconstructed Key]`

1. **Output of `print(-7 // 2)`?** `[Course: IMG-30 Q2]`
   - A. `-3` *(Incorrect â€” truncation toward 0, not floor.)*
   - B. `3` *(Incorrect â€” wrong sign.)*
   - C. `-3.5` *(Incorrect â€” that is `-7 / 2`.)*
   - **D. `-4`** *(Correct â€” `-3.5` floored toward $-\infty$ is `-4`.)*

2. **Output of `print(5 & 3, 5 | 3)`?** `[Course: IMG-30 Q3]`
   - **A. `1 7`** *(Correct â€” `0b101 & 0b011 = 0b001` (`1`), `0b101 | 0b011 = 0b111` (`7`).)*
   - B. `8 2` *(Incorrect â€” arithmetic confusion.)*
   - C. `[?] 6` *(Obscured first digit in `IMG-30`; `6` is `5 ^ 3`, not `5 | 3`.)*
   - D. `15 2` *(Incorrect.)*

3. **What does `2 ** 3 ** 2` evaluate to?** `[Course: IMG-30 Q4]`
   - A. `64` *(Incorrect â€” left-to-right `(2 ** 3) ** 2` would give `64`.)*
   - **B. `512`** *(Correct â€” `**` is right-associative: `2 ** (3 ** 2) = 2 ** 9 = 512`.)*
   - C. `36` *(Incorrect.)*
   - D. `81` *(Incorrect.)*

### Exam-Style Practice `[Supplementary]`

4. **What is the output of `print(-2 ** 2, (-2) ** 2)`?**
   - A. `4 4`
   - **B. `-4 4`** *(Correct â€” `**` binds tighter than unary `-`, so `-2 ** 2` means `-(2 ** 2)`.)*
   - C. `-4 -4`
   - D. `4 -4`

5. **What is `~12 + (1 + 2 << 1)`?**
   - A. `9`
   - B. `-8`
   - **C. `-7`** *(Correct â€” `~12 = -13` and `(1 + 2) << 1 = 6`; `-13 + 6 = -7`.)*
   - D. `10`

---

## 8. Practice Exercises *(Attempt in `exercises.py` Before Checking Solutions!)*

- **Level 1 (Basic):** Compute quotient and remainder of `(-20, 3)` using `divmod` and verify `-20 == (-20 // 3) * 3 + (-20 % 3)`.
- **Level 2 (Application â€” Lab 2.1 `[Course: IMG-18, IMG-20]`):** Implement `bmi_report(weight, height)` returning `(round(bmi, 1), bmi >= 25)` and `active_flags(perms)` returning active flag names among `READ=1, WRITE=2, EXEC=4`.
- **Level 3 (Problem-Solving):** Write `toggle_and_clear(perms, toggle_mask, clear_mask)` using bitwise `^=` and `&= ~`.
- **Level 4 (Exam Reasoning):** Implement `predict_precedence()` without running Python first for `-2 ** 2`, `1 + 2 << 1`, `not 10 > 5 and 10 % 2 == 0`, and `~0b1100`.

---

## 9. Topic Mastery Checklist
- [ ] I can predict `/` vs `//` vs `%` on negative numbers (e.g., `-20 // 3`, `-20 % 3`).
- [ ] I can evaluate multi-operator expressions using Levels 1â€“9 without guessing.
- [ ] I can apply `&`, `|`, `^`, `~`, `<<`, `>>` to set, test, clear, and toggle bit flags.
- [ ] I have completed the Sanfoundry drills listed in `IMG-31` (*Basic Operators*, *Precedence & Associativity 1â€“2*, *Bitwise 1â€“2*).
