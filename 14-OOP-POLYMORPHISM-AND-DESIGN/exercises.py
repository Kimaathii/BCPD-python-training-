"""
Module 14: OOP Polymorphism, Overloading & Design — Progressive Practical Exercises
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 12 (§12.1–12.6) + Day 13 (§13.1–13.5)
"""

from functools import singledispatch
from typing import Any, List, Union


# ==============================================================================
# Level 1: Duck Typing & Polymorphic Collection Processor
# ==============================================================================
class HTMLFormatter:
    def format_text(self, text: str) -> str:
        return f"<p>{text}</p>"


class MarkdownFormatter:
    def format_text(self, text: str) -> str:
        return f"**{text}**"


class PlainTextFormatter:
    def format_text(self, text: str) -> str:
        return str(text)


def format_all(formatters: List[Any], text: str) -> List[str]:
    """
    Duck-typing processor [Course: D11-03].
    Iterates through formatters and calls format_text() on each without checking inheritance.
    """
    return [f.format_text(text) for f in formatters]


# ==============================================================================
# Level 2: Operator Overloading (Currency / Money Class)
# ==============================================================================
class Money:
    """
    Represents monetary value supporting arithmetic operators [Course: D11-01, D11-05].
    Attributes:
        amount: float (rounded to 2 decimal places)
        currency: str
    Implements:
        __add__: adds two Money objects with the same currency (raises ValueError if mismatch)
        __sub__: subtracts two Money objects with the same currency
        __mul__: multiplies Money by a numeric scalar
        __rmul__: reflected scalar multiplication: 2 * Money(5)
        __eq__: checks value and currency equality
        __repr__: "Money(<amount>, '<currency>')"
    """
    def __init__(self, amount: float, currency: str = "USD"):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money) or self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        if not isinstance(other, Money) or self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, scalar: Union[int, float]) -> "Money":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Money(self.amount * scalar, self.currency)

    def __rmul__(self, scalar: Union[int, float]) -> "Money":
        return self * scalar

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __repr__(self) -> str:
        return f"Money({self.amount:.2f}, '{self.currency}')"


# ==============================================================================
# Level 3: Type-Based Dispatching with @singledispatch
# ==============================================================================
@singledispatch
def serialize(val: Any) -> str:
    """Fallback serializer [Course: D11-06]."""
    return f"STR:{val}"


@serialize.register
def _(val: int) -> str:
    return f"INT:{val}"


@serialize.register
def _(val: list) -> str:
    return f"LIST:[{', '.join(serialize(x) for x in val)}]"


@serialize.register
def _(val: dict) -> str:
    return f"DICT:keys={sorted(val.keys())}"


# ==============================================================================
# Level 4: Slotted Matrix Architecture with Validation (Lab 11.1)
# ==============================================================================
class SlottedMatrix:
    """
    High-performance 2D Matrix with memory-saving __slots__ [Course: D11-07, Lab 11.1].
    Slots: ("_rows", "_height", "_width")
    """
    __slots__ = ("_rows", "_height", "_width")

    def __init__(self, grid: List[List[float]]):
        if not grid or not grid[0]:
            raise ValueError("Grid cannot be empty")
        width = len(grid[0])
        if any(len(row) != width for row in grid):
            raise ValueError("All rows must have the same width")
        self._rows = [[float(v) for v in row] for row in grid]
        self._height = len(grid)
        self._width = width

    @property
    def shape(self) -> tuple[int, int]:
        return (self._height, self._width)

    def __add__(self, other: "SlottedMatrix") -> "SlottedMatrix":
        if not isinstance(other, SlottedMatrix):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Dimensions must match for addition")
        summed = [
            [self._rows[r][c] + other._rows[r][c] for c in range(self._width)]
            for r in range(self._height)
        ]
        return SlottedMatrix(summed)

    def __mul__(self, scalar: Union[int, float]) -> "SlottedMatrix":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        scaled = [
            [self._rows[r][c] * scalar for c in range(self._width)]
            for r in range(self._height)
        ]
        return SlottedMatrix(scaled)

    def __rmul__(self, scalar: Union[int, float]) -> "SlottedMatrix":
        return self * scalar

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SlottedMatrix):
            return NotImplemented
        return self._rows == other._rows

    def __repr__(self) -> str:
        return f"SlottedMatrix({self._rows})"


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1: Duck typing
    formatters = [HTMLFormatter(), MarkdownFormatter(), PlainTextFormatter()]
    rendered = format_all(formatters, "Hello")
    assert rendered == ["<p>Hello</p>", "**Hello**", "Hello"]

    # Test Level 2: Operator Overloading
    m1 = Money(10.50, "USD")
    m2 = Money(5.25, "USD")
    m3 = m1 + m2
    assert m3 == Money(15.75, "USD")
    assert (m1 * 2) == Money(21.00, "USD")
    assert (3 * m2) == Money(15.75, "USD")  # __rmul__

    # Currency mismatch
    try:
        _ = m1 + Money(5, "EUR")
        assert False, "Should raise ValueError on currency mismatch"
    except ValueError:
        pass

    # Test Level 3: Singledispatch
    assert serialize(42) == "INT:42"
    assert serialize("foo") == "STR:foo"
    assert serialize([1, "x"]) == "LIST:[INT:1, STR:x]"
    assert serialize({"b": 1, "a": 2}) == "DICT:keys=['a', 'b']"

    # Test Level 4: Slotted Matrix
    mat1 = SlottedMatrix([[1, 2], [3, 4]])
    mat2 = SlottedMatrix([[10, 20], [30, 40]])
    assert hasattr(mat1, "__dict__") is False  # Slotted!
    assert mat1 + mat2 == SlottedMatrix([[11, 22], [33, 44]])
    assert 2 * mat1 == SlottedMatrix([[2, 4], [6, 8]])
    assert mat1.shape == (2, 2)


if __name__ == "__main__":
    test_exercises()
    print("All Module 14 exercises PASSED verification tests.")
