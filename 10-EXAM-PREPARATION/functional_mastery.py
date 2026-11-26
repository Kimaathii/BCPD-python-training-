"""Functional Programming Mastery & Deterministic Verification Suite.

Covers:
- List, Dict, Set Comprehensions & 2D Flattening
- Comprehension Scoping Shield (Python 3 Scope Isolation)
- Generator Expressions, yield, yield from & One-Shot Exhaustion
- Lambdas & Late-Binding Closure Fix
- Under-The-Hood Mechanics of map() & filter(None, ...)
- functools Suite: reduce, partial, lru_cache, wraps, singledispatch
"""

from __future__ import annotations

from functools import lru_cache, partial, reduce, singledispatch, wraps
import sys


def test_comprehensions():
    # 1. List comprehension
    squares = [x * x for x in range(5)]
    assert squares == [0, 1, 4, 9, 16]

    # 2. Set comprehension (deduplicates)
    lengths = {len(w) for w in ["apple", "pear", "fig", "apple"]}
    assert lengths == {3, 4, 5}

    # 3. Dict comprehension
    sq_map = {x: x * x for x in range(3)}
    assert sq_map == {0: 0, 1: 1, 2: 4}

    # 4. Trailing if vs ternary if-else placement
    evens = [x for x in [1, 2, 3, 4] if x % 2 == 0]
    assert evens == [2, 4]

    clamped = [x if x > 0 else 0 for x in [3, -1, 4, -2]]
    assert clamped == [3, 0, 4, 0]

    # 5. 2D Matrix flattening
    matrix = [[1, 2], [3, 4]]
    flattened = [val for row in matrix for val in row]
    assert flattened == [1, 2, 3, 4]

    # 6. Scoping shield: comprehension target does NOT leak in Python 3
    leak_probe = 999
    _ = [leak_probe for leak_probe in range(5)]
    assert leak_probe == 999  # Untouched!


def test_generators():
    # 1. Generator expression one-shot exhaustion
    gen = (x * 2 for x in [1, 2, 3])
    assert sum(gen) == 12
    assert sum(gen) == 0  # Exhausted!

    # 2. Generator function with yield
    def count_up(n):
        c = 1
        while c <= n:
            yield c
            c += 1

    g = count_up(3)
    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 3
    try:
        next(g)
        assert False, "Should raise StopIteration"
    except StopIteration:
        pass

    # 3. yield from delegation
    def combined_stream():
        yield from [10, 20]
        yield from (30, 40)

    assert list(combined_stream()) == [10, 20, 30, 40]


def test_lambdas_and_closures():
    # 1. Lambda calculation
    add = lambda a, b: a + b
    assert add(10, 20) == 30

    # 2. Key function sorting
    pairs = [("Ada", 95), ("Bob", 80), ("Cy", 90)]
    sorted_by_grade = sorted(pairs, key=lambda p: p[1])
    assert sorted_by_grade == [("Bob", 80), ("Cy", 90), ("Ada", 95)]

    # 3. Late-binding trap and default-argument fix
    buggy_funcs = [lambda: i for i in range(3)]
    assert [f() for f in buggy_funcs] == [2, 2, 2]

    fixed_funcs = [lambda i=i: i for i in range(3)]
    assert [f() for f in fixed_funcs] == [0, 1, 2]


def test_map_and_filter_mechanics():
    # 1. Single iterable map
    nums = [1, 2, 3]
    assert list(map(lambda x: x * 10, nums)) == [10, 20, 30]

    # 2. Multiple iterable map (stops at shortest)
    a = [10, 20, 30]
    b = [1, 2]
    combined = list(map(lambda x, y: x + y, a, b))
    assert combined == [11, 22]

    # 3. filter with predicate
    odds = list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5]))
    assert odds == [1, 3, 5]

    # 4. filter(None, ...) strips all falsy values
    dirty = [0, "valid", "", None, 42, False, []]
    clean = list(filter(None, dirty))
    assert clean == ["valid", 42]


def test_functools_suite():
    # 1. reduce cumulative fold
    product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])
    assert product == 24

    sum_with_init = reduce(lambda acc, x: acc + x, [1, 2, 3], 100)
    assert sum_with_init == 106

    # Empty reduce without init raises TypeError
    try:
        reduce(lambda a, b: a + b, [])
        assert False, "Should raise TypeError on empty reduce"
    except TypeError:
        pass

    # 2. partial argument freezing
    def multiply(x, y):
        return x * y

    double = partial(multiply, 2)
    assert double(5) == 10

    # 3. lru_cache memoization
    calls = 0

    @lru_cache(maxsize=16)
    def compute(val):
        nonlocal calls
        calls += 1
        return val * 2

    assert compute(5) == 10
    assert calls == 1
    assert compute(5) == 10
    assert calls == 1  # Cache hit, no re-execution!

    # 4. wraps decorator metadata preservation
    def my_dec(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @my_dec
    def target_func():
        """Original doc."""
        pass

    assert target_func.__name__ == "target_func"
    assert target_func.__doc__ == "Original doc."

    # 5. singledispatch function overloading simulation
    @singledispatch
    def format_item(val):
        return f"GENERIC:{val}"

    @format_item.register(int)
    def _(val):
        return f"INT:{val}"

    @format_item.register(list)
    def _(val):
        return f"LIST:{len(val)}"

    assert format_item("abc") == "GENERIC:abc"
    assert format_item(42) == "INT:42"
    assert format_item([1, 2, 3]) == "LIST:3"


def main():
    print("Running Master Functional Programming Verification Suite...")
    test_comprehensions()
    test_generators()
    test_lambdas_and_closures()
    test_map_and_filter_mechanics()
    test_functools_suite()
    print("All Functional Programming mechanics & functools verified PASSED.")


if __name__ == "__main__":
    main()
