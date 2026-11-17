"""
Module 11: Tuples, Dictionaries & Sets — Executable Classroom Code
Course: BCPD Python Certification — Domain 2: Data Structures (15%)
Classroom Sources: D8-01 to D8-14 (Week 2 • Day 8: Monday 16 Nov 2026)
Manual: Day 8 (§8.1–8.8) + Day 9 (§9.1–9.9)
"""

from collections import Counter, defaultdict, namedtuple


def test_day8_title_script():
    """Verifies day8.py title slide code [Course: D8-01]."""
    words = "to be or not to be".split()
    top1 = Counter(words).most_common(1)
    assert top1 == [("to", 2)], f"Expected [('to', 2)], got {top1}"


def test_tuples_basics():
    """Verifies tuples.py [Course: D8-03]."""
    # Parentheses vs comma single-item trap
    val_int = (5)
    val_tuple = (5,)
    assert type(val_int) is int
    assert type(val_tuple) is tuple

    # Slicing and repetition
    t = (1, 2, 3)
    assert t[1:] == (2, 3)
    assert t * 2 == (1, 2, 3, 1, 2, 3)

    # Methods
    assert t.count(2) == 1
    assert t.index(3) == 2

    # Immutability check
    try:
        t[0] = 9  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError:
        pass

    # Mutability inside immutability
    x = ([1], 2)
    x[0].append(5)
    assert x == ([1, 5], 2)

    # Empty tuple and tuple() constructor
    assert len(()) == 0
    assert tuple("ab") == ("a", "b")


def test_records_and_namedtuple():
    """Verifies records.py [Course: D8-04]."""
    # Packing and unpacking
    point = 3, 4
    x, y = point
    assert x + y == 7

    # Multiple return values
    def min_max(nums):
        return min(nums), max(nums)

    lo, hi = min_max([7, 2, 9])
    assert (lo, hi) == (2, 9)

    # Count mismatch trap
    try:
        a, b = (1, 2, 3)  # type: ignore
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    assert p.x == 1
    assert p[1] == 2
    assert p == (1, 2)
    assert repr(p) == "Point(x=1, y=2)"


def test_dictionaries_and_lookups():
    """Verifies dicts.py [Course: D8-07]."""
    ages = {"Ada": 36, "Bo": 25}
    ages["Cy"] = 30  # add
    ages["Bo"] = 26  # update
    assert ages == {"Ada": 36, "Bo": 26, "Cy": 30}

    # Safe get lookups
    assert ages.get("Zed") is None
    assert ages.get("Zed", 0) == 0

    # Membership operator tests keys, not values
    assert "Ada" in ages
    assert 36 not in ages

    del ages["Cy"]
    assert len(ages) == 2

    # Numeric key collision: 1 == 1.0 and hash(1) == hash(1.0)
    d_collision = {1: "a", 1.0: "b"}
    assert d_collision == {1: "b"}
    assert len(d_collision) == 1


def test_dictionary_methods():
    """Verifies Dictionary methods table [Course: D8-05, D8-06]."""
    d = {"a": 1}
    assert list(d.items()) == [("a", 1)]
    assert d.get("z", 0) == 0
    assert d.pop("a") == 1
    assert "a" not in d

    d["x"] = 10
    d["y"] = 20
    assert d.popitem() == ("y", 20)  # LIFO removal

    d.update(b=2)
    assert d["b"] == 2

    val = d.setdefault("c", [])
    assert val == []
    assert d["c"] == []

    d_fromkeys = dict.fromkeys("ab", 0)
    assert d_fromkeys == {"a": 0, "b": 0}

    # CRITICAL TRAP: dict.fromkeys("ab", []) shared mutable list
    d_trap = dict.fromkeys("ab", [])
    d_trap["a"].append(99)
    assert d_trap["b"] == [99], "Both keys must reference the exact same list!"


def test_edge_cases():
    """Verifies edge_cases.py [Course: D8-08, D8-09]."""
    d = {"a": 1, "b": 2}
    d["c"] = 3
    assert d.popitem() == ("c", 3)

    # Equality ignores key order
    assert {"x": 1, "y": 2} == {"y": 2, "x": 1}

    # Sorting dict returns sorted keys
    assert sorted({"b": 1, "a": 2}) == ["a", "b"]

    # Vacuous truth
    assert all({}) is True

    # Inverting dictionary
    inverted = dict(zip(d.values(), d))
    assert inverted == {1: "a", 2: "b"}

    # Counter union and intersection
    c1, c2 = Counter("aab"), Counter("abb")
    assert (c1 | c2) == Counter({"a": 2, "b": 2})  # Union takes max
    assert (c1 & c2) == Counter({"a": 1, "b": 1})  # Intersection takes min

    # defaultdict defaults
    assert defaultdict(int)["x"] == 0
    assert defaultdict(str)["y"] == ""

    # Tuple comparison and sum
    assert (1, 2) < (1, 3)
    assert sum((1, 2), 10) == 13
    assert sorted((3, 1, 2)) == [1, 2, 3]


def test_collections_counter_and_defaultdict():
    """Verifies collections_demo.py [Course: D8-10]."""
    words = "the cat and the hat and the bat".split()
    counts = Counter(words)
    assert counts["the"] == 3
    assert counts.most_common(2) == [("the", 3), ("and", 2)]
    assert counts["dog"] == 0  # No KeyError

    by_letter = defaultdict(list)
    for w in ["apple", "avocado", "banana"]:
        by_letter[w[0]].append(w)
    assert dict(by_letter) == {
        "a": ["apple", "avocado"],
        "b": ["banana"],
    }


def test_sets_and_algebra():
    """Verifies sets.py and Set algebra [Course: D8-11, D8-12, D8-14]."""
    s = {3, 1, 3, 2}
    assert len(s) == 3  # Duplicates removed
    assert type({}) is dict
    assert type(set()) is set

    s.add(4)
    s.discard(10)  # No error on absent element
    assert sorted(s) == [1, 2, 3, 4]
    assert sorted(set("banana")) == ["a", "b", "n"]

    # Algebra operations
    a = {1, 2, 3}
    b = {3, 4}
    assert (a | b) == {1, 2, 3, 4}
    assert (a & b) == {3}
    assert (a - b) == {1, 2}
    assert (a ^ b) == {1, 2, 4}

    # Subsets
    assert {1, 2} <= a
    assert {1, 2} < {1, 2, 3}
    assert a.isdisjoint({9}) is True

    # frozenset
    fs = frozenset(a)
    assert type(fs) is frozenset
    assert hash(fs)  # Hashable, can be set member or dict key
    set_of_sets = {frozenset({1, 2}), frozenset({3})}
    assert len(set_of_sets) == 2

    # Operator vs method type checking
    try:
        _ = {1, 2} | [3, 4]  # type: ignore
        assert False, "Bitwise operator must raise TypeError with non-set"
    except TypeError:
        pass

    assert {1, 2}.union([3, 4]) == {1, 2, 3, 4}

    # Unsupported + and * operators
    try:
        _ = {1} + {2}  # type: ignore
        assert False
    except TypeError:
        pass

    try:
        _ = {1} * 2  # type: ignore
        assert False
    except TypeError:
        pass

    # Truthiness of empty set
    assert all(set()) is True
    assert any(set()) is False


def main():
    print("Running Module 11: Tuples, Dicts & Sets test suite...")
    test_day8_title_script()
    test_tuples_basics()
    test_records_and_namedtuple()
    test_dictionaries_and_lookups()
    test_dictionary_methods()
    test_edge_cases()
    test_collections_counter_and_defaultdict()
    test_sets_and_algebra()
    print("All Module 11 examples PASSED cleanly (100% verified against Day 8 slides).")


if __name__ == "__main__":
    main()
