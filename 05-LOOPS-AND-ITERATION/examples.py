"""Module 05 Examples â€” Loops, Iteration, Patterns, Traps & Classics.

Sources: IMG-39..IMG-46, IMG-49, IMG-55 (Week 1 Â· Day 3 & Day 4)
Target Python: 3.10+
"""


# =============================================================================
# 1. ORIGINAL CLASSROOM CODE: while_demo.py [Source: IMG-39]
# =============================================================================
def original_while_demo() -> int:
    """Reproduces while_demo.py from IMG-39 verbatim."""
    count = 3
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("Lift-off!")

    n, total = 1234, 0
    while n > 0:
        total += n % 10
        n //= 10
    print(total)
    return total


# =============================================================================
# 2. ORIGINAL CLASSROOM CODE: for_demo.py & control.py [Source: IMG-40, IMG-41]
# =============================================================================
def original_for_and_control_demo() -> None:
    """Reproduces for_demo.py [IMG-40] and control.py [IMG-41] verbatim."""
    assert list(range(5)) == [0, 1, 2, 3, 4]
    assert list(range(1, 10, 3)) == [1, 4, 7]
    assert list(range(10, 0, -4)) == [10, 6, 2]

    # enumerate test
    enum_out = list(enumerate(["Ada", "Bo"], start=1))
    assert enum_out == [(1, "Ada"), (2, "Bo")]

    # zip test
    zip_out = list(zip([1, 2, 3], "ab"))
    assert zip_out == [(1, "a"), (2, "b")]

    # control flow
    evens_skipped = []
    for n in range(1, 10):
        if n % 2 == 0:
            continue
        if n > 7:
            break
        evens_skipped.append(n)
    assert evens_skipped == [1, 3, 5, 7]

    # loop else
    odd_found = None
    for n in [4, 6, 9]:
        if n % 2:
            odd_found = n
            break
    else:
        odd_found = "all even"
    assert odd_found == 9


# =============================================================================
# 3. ORIGINAL CLASSROOM CODE: classics.py [Source: IMG-42]
# =============================================================================
def original_classics_demo() -> None:
    """Reproduces classics.py from IMG-42 verbatim."""
    n = 29
    is_prime = n > 1
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            is_prime = False
            break
    assert is_prime is True

    fact = 1
    for k in range(1, 6):
        fact *= k
    assert fact == 120

    a, b = 0, 1
    fib = []
    while len(fib) < 8:
        fib.append(a)
        a, b = b, a + b
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13]


# =============================================================================
# 4. ORIGINAL CLASSROOM CODE: patterns.py & traps.py [Source: IMG-43, IMG-44]
# =============================================================================
def original_patterns_and_traps() -> None:
    """Reproduces patterns.py [IMG-43] and traps.py [IMG-44] verbatim."""
    rows = 4
    stars = ["*" * i for i in range(1, rows + 1)]
    assert stars == ["*", "**", "***", "****"]

    mult_table = []
    for i in range(1, 4):
        for j in range(1, 4):
            mult_table.append(i * j)
    assert mult_table == [1, 2, 3, 2, 4, 6, 3, 6, 9]

    # Traps from IMG-44
    n = 3
    for i in range(n):
        n = 10
    assert i == 2

    for i in range(3):
        i += 10
    assert i == 12

    s = "abcd"
    while "c" in s:
        s = s[1:]
    assert s == "d"

    items = ["x", "", 0, "y", None]
    assert list(filter(bool, items)) == ["x", "y"]
    assert ["no", "yes"][True] == "yes"
    assert (not 1 == 2) is True


# =============================================================================
# 5. ORIGINAL CLASSROOM CODE: iterate.py [Source: IMG-55]
# =============================================================================
def original_iterate_demo() -> None:
    """Reproduces iterate.py from IMG-55 verbatim."""
    word = "code"
    it = iter(word)
    first = next(it)
    second = next(it)
    assert (first, second) == ("c", "o")

    rest = [ch for ch in it]
    assert rest == ["d", "e"]

    try:
        next(it)
        raise AssertionError("Expected StopIteration")
    except StopIteration:
        pass


# =============================================================================
# 6. LAB 3.1 & 3.2: 5-Attempt Guessing Game [Source: IMG-45, IMG-49]
# =============================================================================
def play_guess_simulator(secret: int, guesses: list[int], max_attempts: int = 5) -> dict[str, object]:
    """Simulator for Lab 3.1 guessing game with 5-attempt homework limit (IMG-49)."""
    attempts = 0
    won = False
    for guess in guesses:
        attempts += 1
        if guess == secret:
            won = True
            break
        if attempts >= max_attempts:
            break
    return {"won": won, "attempts": attempts, "secret": secret}


if __name__ == "__main__":
    assert original_while_demo() == 10
    original_for_and_control_demo()
    original_classics_demo()
    original_patterns_and_traps()
    original_iterate_demo()

    # Simulator check
    assert play_guess_simulator(7, [1, 2, 7]) == {"won": True, "attempts": 3, "secret": 7}
    assert play_guess_simulator(7, [1, 2, 3, 4, 5]) == {"won": False, "attempts": 5, "secret": 7}
    print("Module 05 assertions passed.")
