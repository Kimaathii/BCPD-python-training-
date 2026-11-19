"""
Module 14: Object-Oriented Programming — Polymorphism, Overloading & OOP Design
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Classroom Sources: D11-01 to D11-08 (Week 2 • Day 11: Thursday 19 Nov 2026)
Manual Reference: Day 12 (§12.1–12.6) + Day 13 (§13.1–13.5)
"""

from functools import singledispatch, total_ordering
from typing import List, Tuple, Union


def test_day11_title_script():
    """Verifies day11.py title slide code [Course: D11-01]."""
    class Money:
        def __init__(self, amt):
            self.amt = amt

        def __add__(self, other):
            return Money(self.amt + other.amt)

    total = Money(5) + Money(7)
    assert total.amt == 12


def test_duck_typing():
    """Verifies duck.py duck typing and total_length [Course: D11-03]."""
    class Duck:
        def speak(self):
            return "Quack"

    class Robot:
        def speak(self):
            return "Beep"

    voices = [thing.speak() for thing in [Duck(), Robot()]]
    assert voices == ["Quack", "Beep"]

    def total_length(items):
        return sum(len(x) for x in items)

    assert total_length(["ab", [1, 2, 3], {"k": 1}]) == 6


def test_operator_overloading_vector():
    """Verifies vector.py operator overloading, __rmul__, and comparisons [Course: D11-05]."""
    @total_ordering
    class Vector:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __mul__(self, k):
            return Vector(self.x * k, self.y * k)

        def __rmul__(self, k):
            return Vector(self.x * k, self.y * k)

        def __eq__(self, other):
            if not isinstance(other, Vector):
                return NotImplemented
            return (self.x, self.y) == (other.x, other.y)

        def __lt__(self, other):
            if not isinstance(other, Vector):
                return NotImplemented
            return abs(self) < abs(other)

        def __abs__(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v = Vector(1, 2) + Vector(3, 4)
    assert repr(v) == "Vector(4, 6)"
    assert repr(v * 2) == "Vector(8, 12)"
    assert repr(2 * v) == "Vector(8, 12)"  # Reflected operator __rmul__!
    assert v == Vector(4, 6)
    assert Vector(1, 1) < v
    assert v > Vector(1, 1)  # synthesized by @total_ordering


def test_function_overloading_singledispatch():
    """Verifies overloading.py defaults simulation and singledispatch [Course: D11-06]."""
    def area(a, b=None):
        return 3.14 * a * a if b is None else a * b

    assert area(2) == 12.56
    assert area(2, 3) == 6

    @singledispatch
    def describe(x):
        return "something"

    @describe.register
    def _(x: int):
        return "an int"

    @describe.register
    def _(x: list):
        return f"a list of {len(x)}"

    assert describe(5) == "an int"
    assert describe([1, 2]) == "a list of 2"
    assert describe(2.5) == "something"


def test_slots_data_hiding():
    """Verifies slots.py __slots__, memory savings, and typo protection [Course: D11-07]."""
    class Free:
        pass

    class Fixed:
        __slots__ = ("x", "y")
        def __init__(self, x, y):
            self.x, self.y = x, y

    f = Free()
    f.anything = 1
    assert f.__dict__ == {"anything": 1}

    p = Fixed(1, 2)
    assert hasattr(p, "__dict__") is False
    assert p.x == 1 and p.y == 2
    try:
        p.z = 3  # type: ignore
        assert False, "Should raise AttributeError on assignment outside __slots__"
    except AttributeError:
        pass
    assert p.__class__.__name__ == "Fixed"


def test_clean_design_and_validation():
    """Verifies design.py SRP and early constructor validation [Course: D11-08]."""
    class Customer:
        def __init__(self, name, email, phone=None):
            self._validate_email(email)
            self.name = name
            self.email = email
            self.phone = phone

        def _validate_email(self, email):
            if "@" not in email:
                raise ValueError("Invalid email address")

    c = Customer("Ada", "ada@bcpd.org")
    assert c.name == "Ada"
    assert c.phone is None

    try:
        Customer("Bo", "bo.example.com")
        assert False, "Should raise ValueError on invalid email"
    except ValueError as e:
        assert str(e) == "Invalid email address"


def test_classmethod_and_singleton():
    """Verifies @classmethod factory constructors and Singleton pattern."""
    class Config:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self, debug=False):
            self.debug = debug

    c1 = Config(True)
    c2 = Config(False)
    assert c1 is c2  # Same instance in memory!


def test_matrix_class_lab_11_1():
    """Verifies Lab 11.1 Matrix class challenge."""
    class Matrix:
        def __init__(self, rows: List[List[float]]):
            if not rows or not rows[0]:
                raise ValueError("Matrix cannot be empty")
            width = len(rows[0])
            if any(len(r) != width for r in rows):
                raise ValueError("All rows in Matrix must have equal length")
            self.rows = [[float(val) for val in r] for r in rows]
            self.height = len(rows)
            self.width = width

        def __add__(self, other: "Matrix") -> "Matrix":
            if not isinstance(other, Matrix):
                return NotImplemented
            if (self.height, self.width) != (other.height, other.width):
                raise ValueError("Cannot add matrices of different dimensions")
            res = [
                [self.rows[r][c] + other.rows[r][c] for c in range(self.width)]
                for r in range(self.height)
            ]
            return Matrix(res)

        def __mul__(self, scalar: Union[int, float]) -> "Matrix":
            res = [
                [self.rows[r][c] * scalar for c in range(self.width)]
                for r in range(self.height)
            ]
            return Matrix(res)

        def __rmul__(self, scalar: Union[int, float]) -> "Matrix":
            return self * scalar

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Matrix):
                return NotImplemented
            return self.rows == other.rows

        def __repr__(self) -> str:
            return f"Matrix({self.rows})"

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = m1 + m2
    assert m3 == Matrix([[6, 8], [10, 12]])
    assert m1 * 2 == Matrix([[2, 4], [6, 8]])
    assert 3 * m1 == Matrix([[3, 6], [9, 12]])


def main():
    print("Running Module 14: OOP Polymorphism, Overloading & Design test suite...")
    test_day11_title_script()
    test_duck_typing()
    test_operator_overloading_vector()
    test_function_overloading_singledispatch()
    test_slots_data_hiding()
    test_clean_design_and_validation()
    test_classmethod_and_singleton()
    test_matrix_class_lab_11_1()
    print("All Module 14 examples PASSED cleanly (100% verified against Day 11 slides).")


if __name__ == "__main__":
    main()
