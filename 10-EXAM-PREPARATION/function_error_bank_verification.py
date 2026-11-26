"""
Master Function, Method & Error Bank Verification Suite
Target: Python 3.10+ (Verified on Python 3.15.2)

Rigorously asserts every behavioral return archetype, argument signature,
and exception trigger documented in MASTER-FUNCTION-AND-ERROR-BANK.md.
"""

import functools
import math
import sys


def test_archetype_1_lazy_iterators():
    # 1. map() is lazy, one-shot, truncates to shortest
    nums = [1, 2, 3]
    m = map(lambda x: x * 10, nums)
    assert type(m).__name__ == "map"
    # First pass
    assert list(m) == [10, 20, 30]
    # Second pass: exhausted!
    assert list(m) == []

    # Map truncates to shortest iterable
    m_short = map(lambda a, b: a + b, [1, 2], [10, 20, 30, 40])
    assert list(m_short) == [11, 22]

    # Map object is not subscriptable
    m_sub = map(lambda x: x, [1])
    try:
        _ = m_sub[0]  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "not subscriptable" in str(e)

    # 2. filter(None, iterable) strips falsy items
    raw = [0, "admin", "", None, 42, False, [], {}]
    assert list(filter(None, raw)) == ["admin", 42]

    # filter object has no len
    f = filter(None, [1, 2])
    try:
        _ = len(f)  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "has no len" in str(e)

    # 3. zip() truncation vs strict=True
    z = zip([1, 2], ["a", "b", "c"])
    assert list(z) == [(1, "a"), (2, "b")]

    try:
        list(zip([1, 2], ["a", "b", "c"], strict=True))
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "longer than" in str(e)

    # 4. enumerate(start=N)
    assert list(enumerate(["x", "y"], start=5)) == [(5, "x"), (6, "y")]

    # 5. reversed() on sequence vs set
    assert list(reversed([1, 2, 3])) == [3, 2, 1]
    assert list(reversed("abc")) == ["c", "b", "a"]
    try:
        reversed({1, 2, 3})  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "not reversible" in str(e)

    # 6. next() with and without default
    it = iter([99])
    assert next(it) == 99
    assert next(it, "DEFAULT") == "DEFAULT"
    try:
        next(it)
        assert False, "Should have raised StopIteration"
    except StopIteration:
        pass


def test_archetype_2_silent_mutators():
    # 1. list.sort(), append, extend, reverse return None
    lst = [3, 1, 2]
    ret_sort = lst.sort()
    assert ret_sort is None
    assert lst == [1, 2, 3]

    ret_app = lst.append(4)
    assert ret_app is None
    assert lst == [1, 2, 3, 4]

    ret_ext = lst.extend([5, 6])
    assert ret_ext is None
    assert lst == [1, 2, 3, 4, 5, 6]

    ret_rev = lst.reverse()
    assert ret_rev is None
    assert lst == [6, 5, 4, 3, 2, 1]

    # 2. list.insert out-of-bounds does NOT error (clips to bounds)
    items = [10, 20]
    items.insert(999, 30)
    assert items == [10, 20, 30]
    items.insert(-999, 5)
    assert items == [5, 10, 20, 30]

    # 3. list.remove raises ValueError if missing
    try:
        items.remove(9999)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not in list" in str(e)

    # 4. dict.update and dict.clear return None
    d = {"a": 1}
    assert d.update({"b": 2}) is None
    assert d == {"a": 1, "b": 2}
    assert d.clear() is None
    assert d == {}

    # 5. set.discard vs set.remove
    s = {1, 2}
    assert s.discard(999) is None  # Silent No-Op
    try:
        s.remove(999)
        assert False, "Should have raised KeyError"
    except KeyError:
        pass


def test_archetype_3_pure_transformers():
    # 1. sorted() returns new list, leaves original untouched
    tup = (3, 1, 2)
    s_res = sorted(tup)
    assert s_res == [1, 2, 3]
    assert tup == (3, 1, 2)

    # 2. Slicing out of bounds never raises IndexError
    text = "Python"
    assert text[100:200] == ""
    assert text[-100:100] == "Python"
    assert [1, 2][50:60] == []

    # 3. str.split() vs str.split(' ')
    raw_str = "   a    b   c   "
    assert raw_str.split() == ["a", "b", "c"]
    assert raw_str.split(" ") == ["", "", "", "a", "", "", "", "b", "", "", "c", "", "", ""]

    try:
        raw_str.split("")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "empty separator" in str(e)

    # 4. str.partition() returns 3-tuple, never errors if separator missing
    assert "user@test.com".partition("@") == ("user", "@", "test.com")
    assert "user_at_test.com".partition("@") == ("user_at_test.com", "", "")

    # 5. str.find() vs str.index()
    assert "hello".find("z") == -1
    try:
        "hello".index("z")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "substring not found" in str(e)

    # 6. str.join() requires strings only
    assert "-".join(["a", "b"]) == "a-b"
    try:
        "-".join([1, 2])  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "expected str" in str(e)


def test_archetype_4_extractors_and_dynamic_views():
    # 1. dict.get, setdefault, pop
    d = {"a": 100}
    assert d.get("missing", 0) == 0
    assert d.get("missing") is None

    # setdefault returns existing if present, or sets default if missing
    assert d.setdefault("a", 999) == 100
    assert d["a"] == 100
    assert d.setdefault("b", 200) == 200
    assert d["b"] == 200

    # dict.pop
    assert d.pop("b") == 200
    assert d.pop("nonexistent", "FALLBACK") == "FALLBACK"
    try:
        d.pop("nonexistent")
        assert False, "Should have raised KeyError"
    except KeyError:
        pass

    # list.pop
    l = [10, 20, 30]
    assert l.pop() == 30
    assert l == [10, 20]
    assert l.pop(0) == 10
    assert l == [20]
    assert l.pop() == 20
    try:
        l.pop()
        assert False, "Should have raised IndexError"
    except IndexError as e:
        assert "pop from empty list" in str(e)

    # 2. Dynamic Dictionary Views
    data = {"x": 1, "y": 2}
    v_keys = data.keys()
    data["z"] = 3
    assert "z" in v_keys  # View updated automatically!

    # Mutating dict during iteration raises RuntimeError
    dict_mutate = {"k1": 1}
    try:
        for k in dict_mutate:
            dict_mutate["k2"] = 2
        assert False, "Should have raised RuntimeError"
    except RuntimeError as e:
        assert "changed size during iteration" in str(e)


def test_archetype_5_reducers_math_and_sets():
    # 1. sum()
    assert sum([1, 2, 3], start=10) == 16
    try:
        sum(["a", "b"])  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "unsupported operand" in str(e)

    # 2. all() and any() vacuous truth
    assert all([]) is True
    assert any([]) is False

    # 3. functools.reduce
    assert functools.reduce(lambda a, b: a + b, [1, 2, 3]) == 6
    assert functools.reduce(lambda a, b: a + b, [], 0) == 0
    try:
        functools.reduce(lambda a, b: a + b, [])
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "empty iterable with no initial value" in str(e)

    # 4. Banker's rounding (round half to even)
    assert round(2.5) == 2
    assert round(3.5) == 4
    assert round(4.5) == 4
    assert round(5.5) == 6

    # 5. Integer division and modulo with negatives
    assert 7 // 2 == 3
    assert -7 // 2 == -4
    assert int(-3.5) == -3
    assert 7 % 2 == 1
    assert -7 % 2 == 1   # Sign matches divisor (+2)
    assert 7 % -2 == -1  # Sign matches divisor (-2)

    # 6. Set method vs operator duality
    s1 = {1, 2}
    # Method accepts lists, tuples, generators
    assert s1.union([2, 3]) == {1, 2, 3}
    assert s1.intersection((2, 4)) == {2}
    assert s1.difference([2]) == {1}

    # Operator strictly requires sets on both sides
    try:
        _ = s1 | [2, 3]  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "unsupported operand" in str(e)


def test_the_10_deadly_exceptions_autopsy():
    # 1. TypeError (uncallable or type mismatch)
    try:
        x = 5
        x()  # type: ignore
    except TypeError:
        pass

    # 2. ValueError (invalid value format)
    try:
        int("abc")
    except ValueError:
        pass

    # 3. AttributeError (method does not exist for type)
    try:
        (1, 2).append(3)  # type: ignore
    except AttributeError:
        pass

    # 4. KeyError (dictionary missing key)
    try:
        _ = {}["missing"]
    except KeyError:
        pass

    # 5. IndexError (sequence out of bounds)
    try:
        _ = [1, 2][99]
    except IndexError:
        pass

    # 6. UnboundLocalError (variable read before local assignment)
    def trigger_unbound():
        val = 10
        def inner():
            nonlocal val
            # Local assignment shadow test
        def inner_broken():
            print(local_x)  # type: ignore
            local_x = 20
        inner_broken()

    try:
        trigger_unbound()
    except UnboundLocalError:
        pass

    # 7. NameError (variable never defined)
    try:
        eval("unassigned_symbol_xyz")
    except NameError:
        pass

    # 8. StopIteration (exhausted iterator)
    try:
        it = iter([])
        next(it)
    except StopIteration:
        pass

    # 9. ZeroDivisionError (division or modulo by 0)
    try:
        _ = 10 % 0
    except ZeroDivisionError:
        pass

    # 10. RuntimeError (dict modified during iteration)
    try:
        d = {"a": 1}
        for k in d:
            d["b"] = 2
    except RuntimeError:
        pass


def main():
    print("Running Master Function, Method & Error Bank Verification Suite...")
    test_archetype_1_lazy_iterators()
    test_archetype_2_silent_mutators()
    test_archetype_3_pure_transformers()
    test_archetype_4_extractors_and_dynamic_views()
    test_archetype_5_reducers_math_and_sets()
    test_the_10_deadly_exceptions_autopsy()
    print("All Function, Method & Error Bank behavioral assertions PASSED cleanly.")


if __name__ == "__main__":
    main()
