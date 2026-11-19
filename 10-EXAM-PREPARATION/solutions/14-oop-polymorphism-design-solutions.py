"""
Module 14 Solutions: OOP Polymorphism, Overloading & Design
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 12 (§12.1–12.6) + Day 13 (§13.1–13.5)
"""

from functools import singledispatch
from typing import Any, List, Union


# ==============================================================================
# Solution 1: Duck Typing
# ==============================================================================
class HTMLFormatterSolution:
    def format_text(self, text: str) -> str:
        return f"<p>{text}</p>"


class MarkdownFormatterSolution:
    def format_text(self, text: str) -> str:
        return f"**{text}**"


class PlainTextFormatterSolution:
    def format_text(self, text: str) -> str:
        return str(text)


def format_all_solution(formatters: List[Any], text: str) -> List[str]:
    return [f.format_text(text) for f in formatters]


# ==============================================================================
# Solution 2: Money Operator Overloading
# ==============================================================================
class MoneySolution:
    def __init__(self, amount: float, currency: str = "USD"):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def __add__(self, other: "MoneySolution") -> "MoneySolution":
        if not isinstance(other, MoneySolution) or self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return MoneySolution(self.amount + other.amount, self.currency)

    def __sub__(self, other: "MoneySolution") -> "MoneySolution":
        if not isinstance(other, MoneySolution) or self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return MoneySolution(self.amount - other.amount, self.currency)

    def __mul__(self, scalar: Union[int, float]) -> "MoneySolution":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return MoneySolution(self.amount * scalar, self.currency)

    def __rmul__(self, scalar: Union[int, float]) -> "MoneySolution":
        return self * scalar

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MoneySolution):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __repr__(self) -> str:
        return f"MoneySolution({self.amount:.2f}, '{self.currency}')"


# ==============================================================================
# Solution 3: Singledispatch Serializer
# ==============================================================================
@singledispatch
def serialize_solution(val: Any) -> str:
    return f"STR:{val}"


@serialize_solution.register
def _(val: int) -> str:
    return f"INT:{val}"


@serialize_solution.register
def _(val: list) -> str:
    return f"LIST:[{', '.join(serialize_solution(x) for x in val)}]"


@serialize_solution.register
def _(val: dict) -> str:
    return f"DICT:keys={sorted(val.keys())}"


# ==============================================================================
# Solution 4: Slotted Matrix Class
# ==============================================================================
class SlottedMatrixSolution:
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

    def __add__(self, other: "SlottedMatrixSolution") -> "SlottedMatrixSolution":
        if not isinstance(other, SlottedMatrixSolution):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Dimensions must match for addition")
        summed = [
            [self._rows[r][c] + other._rows[r][c] for c in range(self._width)]
            for r in range(self._height)
        ]
        return SlottedMatrixSolution(summed)

    def __mul__(self, scalar: Union[int, float]) -> "SlottedMatrixSolution":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        scaled = [
            [self._rows[r][c] * scalar for c in range(self._width)]
            for r in range(self._height)
        ]
        return SlottedMatrixSolution(scaled)

    def __rmul__(self, scalar: Union[int, float]) -> "SlottedMatrixSolution":
        return self * scalar

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SlottedMatrixSolution):
            return NotImplemented
        return self._rows == other._rows

    def __repr__(self) -> str:
        return f"SlottedMatrixSolution({self._rows})"


def main():
    res = format_all_solution([HTMLFormatterSolution(), PlainTextFormatterSolution()], "Hi")
    assert res == ["<p>Hi</p>", "Hi"]

    m = MoneySolution(10, "USD") * 2
    assert m == MoneySolution(20, "USD")
    assert 3 * m == MoneySolution(60, "USD")

    assert serialize_solution(100) == "INT:100"

    mat = SlottedMatrixSolution([[1, 2], [3, 4]])
    assert 2 * mat == SlottedMatrixSolution([[2, 4], [6, 8]])
    print("Module 14 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
