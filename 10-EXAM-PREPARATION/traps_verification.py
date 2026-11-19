"""
Master Exam Traps Verification Test Suite
Course: BCPD Python Certification — All Syllabus Domains
Purpose: Programmatically asserts the exact CPython behavior for all traps documented in MASTER-EXAM-TRAPS-ENCYCLOPEDIA.md.
"""

from abc import ABC, abstractmethod
from collections import Counter, defaultdict, namedtuple
from dataclasses import dataclass, field
import math
import sys


def test_domain_1_syntax_and_env():
    # Trap 1.1: Comma tuple
    revenue = 1, 000, 000
    assert type(revenue) is tuple
    assert revenue == (1, 0, 0)
    assert len(revenue) == 3

    # Trap 1.2: String concatenation on input
    x_input = "5"
    y_input = "10"
    assert x_input + y_input == "510"


def test_domain_2_types_and_memory():
    # Trap 2.1: Banker's rounding
    assert round(2.5) == 2
    assert round(3.5) == 4
    assert round(4.5) == 4

    # Trap 2.2: Floating point drift
    assert 0.1 + 0.2 != 0.3
    assert math.isclose(0.1 + 0.2, 0.3)

    # Trap 2.3: Small integer caching
    a = 256
    b = 256
    assert a is b


def test_domain_3_operators_and_bitwise():
    # Trap 3.1: Unary minus vs exponentiation
    assert -2 ** 4 == -16
    assert (-2) ** 4 == 16

    # Trap 3.2: Right associativity
    assert 2 ** 3 ** 2 == 512
    assert (2 ** 3) ** 2 == 64

    # Trap 3.3: Two's complement ~x = -x - 1
    assert ~10 == -11
    assert ~(-10) == 9
    assert ~0 == -1

    # Trap 3.4: Negative floor division and modulo
    assert -17 // 5 == -4
    assert -17 % 5 == 3
    assert -17 == (-17 // 5) * 5 + (-17 % 5)


def test_domain_4_conditionals_and_logic():
    # Trap 4.1: Short-circuit returns deciding operand
    assert (0 or [] or "python") == "python"
    assert ("hello" and 42 and [1, 2]) == [1, 2]

    # Trap 4.2: Truthiness of non-empty collections/strings
    assert bool("False") is True
    assert bool("0") is True
    assert bool(" ") is True
    assert bool([0]) is True
    assert bool((None,)) is True

    # Trap 4.3: Chained comparison precedence
    assert (False == False in [False]) is True


def test_domain_5_loops_and_iteration():
    # Trap 5.1: Loop else skipped on break
    log = []
    for i in range(3):
        if i == 1:
            break
    else:
        log.append("else_ran")
    assert log == []

    # Trap 5.2: Modifying list during iteration shifts elements
    nums = [1, 2, 4, 5]
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    assert nums == [1, 4, 5]

    # Trap 5.3: Generator one-shot exhaustion
    gen = (x * x for x in range(3))
    assert sum(gen) == 5
    assert sum(gen) == 0


def test_domain_6_strings_and_formatting():
    # Trap 6.1: String immutability
    s = "python"
    s.upper()
    assert s == "python"

    # Trap 6.2: Slice out of bounds vs index out of bounds
    s2 = "abc"
    assert s2[10:20] == ""
    try:
        _ = s2[10]
        assert False
    except IndexError:
        pass

    # Trap 6.3: str.join on ints
    try:
        "-".join([1, 2, 3])  # type: ignore
        assert False
    except TypeError:
        pass

    # Trap 6.4: Literal braces
    assert "{{literal}}".format() == "{literal}"
    assert f"{{{42}}}" == "{42}"


def test_domain_7_lists_and_sorting():
    # Trap 7.1: In-place sort returns None
    items = [3, 1, 2]
    result = items.sort()
    assert result is None
    assert items == [1, 2, 3]

    # Trap 7.2: 2D pointer duplication
    grid = [[0] * 3] * 3
    grid[0][0] = 1
    assert grid == [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

    # Trap 7.3: ASCII case sensitivity in sorting
    fruits = ["apple", "Pear", "banana"]
    assert sorted(fruits) == ["Pear", "apple", "banana"]


def test_domain_8_functions_and_scope():
    # Trap 8.1: Mutable default argument
    def append_to(val, target=[]):  # type: ignore
        target.append(val)
        return target

    assert append_to(1) == [1]
    assert append_to(2) == [1, 2]
    assert append_to(3) == [1, 2, 3]

    # Trap 8.2: UnboundLocalError
    x = 10
    def read_then_assign():
        nonlocal_read = x  # Refers to global if not assigned locally
        return nonlocal_read
    assert read_then_assign() == 10

    def trigger_unbound():
        try:
            print(y)  # Local y exists later in block
            y = 20
        except UnboundLocalError:
            return "caught"
        return "failed"
    assert trigger_unbound() == "caught"

    # Trap 8.3: Late-binding closures
    funcs = [lambda: i for i in range(3)]
    assert [f() for f in funcs] == [2, 2, 2]


def test_domain_9_identity_and_exceptions():
    # Trap 9.1: Finally return override
    def return_override():
        try:
            return 1
        finally:
            return 2
    assert return_override() == 2

    # Trap 9.2: In-place mutation inside tuple augmented assignment
    t = ([1], 2)
    try:
        t[0] += [3]  # type: ignore
        assert False
    except TypeError:
        pass
    assert t == ([1, 3], 2)


def test_domain_10_tuples_and_collections():
    # Trap 10.1: Single item tuple comma
    assert type((42)) is int
    assert type((42,)) is tuple

    # Trap 10.2: Unpacking count mismatch
    try:
        x, y = (1, 2, 3)  # type: ignore
        assert False
    except ValueError:
        pass

    # Trap 10.3: namedtuple immutability
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    try:
        p.x = 10  # type: ignore
        assert False
    except AttributeError:
        pass
    assert p._replace(x=10) == Point(10, 2)


def test_domain_11_dicts_and_sets():
    # Trap 11.1: dict.fromkeys shared list
    d = dict.fromkeys(["a", "b"], [])
    d["a"].append(99)
    assert d["b"] == [99]

    # Trap 11.2: Numeric key collision
    d_coll = {1: "one", 1.0: "float_one", True: "bool_one"}
    assert len(d_coll) == 1
    assert d_coll == {1: "bool_one"}

    # Trap 11.3: Set bitwise operator vs method
    s = {1, 2}
    assert s.union([3, 4]) == {1, 2, 3, 4}
    try:
        _ = s | [3, 4]  # type: ignore
        assert False
    except TypeError:
        pass

    # Trap 11.4: Sets do not support +
    try:
        _ = {1} + {2}  # type: ignore
        assert False
    except TypeError:
        pass

    # Trap 11.5: Vacuous truth
    assert all(set()) is True
    assert any(set()) is False


def test_domain_12_oop_and_encapsulation():
    # Trap 12.1: Shared mutable class attribute
    class Dog:
        tricks = []
        def __init__(self, name):
            self.name = name

    d1 = Dog("A")
    d2 = Dog("B")
    d1.tricks.append("sit")
    assert d2.tricks == ["sit"]

    # Trap 12.2: Instance masking
    class Animal:
        species = "Canis"
    a1 = Animal()
    a2 = Animal()
    a1.species = "Wolf"
    assert a1.species == "Wolf"
    assert a2.species == "Canis"
    assert Animal.species == "Canis"

    # Trap 12.3: Forgetting self
    class Calc:
        def add(x, y):  # type: ignore
            return x + y
    c = Calc()
    try:
        c.add(1, 2)
        assert False
    except TypeError:
        pass

    # Trap 12.4: Name mangling
    class Bank:
        def __init__(self, bal):
            self.__balance = bal
    b = Bank(500)
    try:
        _ = b.__balance  # type: ignore
        assert False
    except AttributeError:
        pass
    assert b._Bank__balance == 500

    # Trap 12.5: Read-only property
    class Circle:
        def __init__(self, r):
            self._r = r
        @property
        def r(self):
            return self._r
    circ = Circle(5)
    try:
        circ.r = 10  # type: ignore
        assert False
    except AttributeError:
        pass


def test_domain_13_inheritance_and_mro():
    # Trap 13.1: Forgotten super().__init__()
    class Base:
        def __init__(self, name):
            self.name = name

    class Child(Base):
        def __init__(self, name, age):
            self.age = age

    c = Child("Ada", 25)
    try:
        _ = c.name
        assert False, "Should raise AttributeError because Base.__init__ was not called"
    except AttributeError:
        pass

    # Trap 13.2: Diamond inheritance MRO
    class A:
        def who(self): return "A"
    class B(A):
        def who(self): return "B"
    class C(A):
        def who(self): return "C"
    class D(B, C):
        pass

    assert D().who() == "B"
    assert D.mro() == [D, B, C, A, object]

    # Trap 13.3: isinstance(True, int) is True vs type(True) is int is False
    assert isinstance(True, int) is True
    assert (type(True) is int) is False
    assert issubclass(bool, int) is True

    # Trap 13.4: Incomplete ABC instantiation raises TypeError
    class AbstractWorker(ABC):
        @abstractmethod
        def work(self): pass

    class IncompleteWorker(AbstractWorker):
        pass

    try:
        IncompleteWorker()  # type: ignore
        assert False, "Should raise TypeError on instantiation of incomplete ABC"
    except TypeError:
        pass

    # Trap 13.5: Private attribute mangling across inheritance
    class ParentSecret:
        def __init__(self):
            self.__token = "parent"

    class ChildSecret(ParentSecret):
        def __init__(self):
            super().__init__()
            self.__token = "child"

    cs = ChildSecret()
    assert cs._ParentSecret__token == "parent"
    assert cs._ChildSecret__token == "child"

    # Trap 13.6: Dataclass mutable default assignment raises ValueError
    try:
        @dataclass
        class BadDataclass:
            items: list = []  # type: ignore
        assert False, "Should raise ValueError on direct mutable default in dataclass"
    except ValueError:
        pass


def main():
    print("Running Master Exam Traps Verification Suite...")
    test_domain_1_syntax_and_env()
    test_domain_2_types_and_memory()
    test_domain_3_operators_and_bitwise()
    test_domain_4_conditionals_and_logic()
    test_domain_5_loops_and_iteration()
    test_domain_6_strings_and_formatting()
    test_domain_7_lists_and_sorting()
    test_domain_8_functions_and_scope()
    test_domain_9_identity_and_exceptions()
    test_domain_10_tuples_and_collections()
    test_domain_11_dicts_and_sets()
    test_domain_12_oop_and_encapsulation()
    test_domain_13_inheritance_and_mro()
    print("All 42+ Exam Traps rigorously verified and PASSED against CPython runtime.")


if __name__ == "__main__":
    main()
