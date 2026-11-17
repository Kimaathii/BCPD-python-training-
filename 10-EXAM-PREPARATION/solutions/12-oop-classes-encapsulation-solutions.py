"""
Module 12 Solutions: OOP Classes & Encapsulation
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 10 (§10.1–10.10)
"""

from typing import List, Optional, Tuple


# ==============================================================================
# Solution 1: Student Class
# ==============================================================================
class StudentSolution:
    def __init__(self, name: str):
        self.name = name
        self.scores: List[float] = []

    def add_score(self, score: float) -> None:
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(float(score))

    def average(self) -> float:
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 1)

    def __str__(self) -> str:
        return f"Student(name={self.name}, avg={self.average()})"


# ==============================================================================
# Solution 2: QueryBuilder Fluent Interface
# ==============================================================================
class QueryBuilderSolution:
    def __init__(self):
        self._fields = ["*"]
        self._table: Optional[str] = None
        self._conditions: List[str] = []

    def select(self, *fields: str) -> "QueryBuilderSolution":
        if fields:
            self._fields = list(fields)
        return self

    def from_table(self, table: str) -> "QueryBuilderSolution":
        self._table = table
        return self

    def where(self, condition: str) -> "QueryBuilderSolution":
        self._conditions.append(condition)
        return self

    def build(self) -> str:
        if not self._table:
            raise ValueError("Table name must be specified via from_table()")
        sql = f"SELECT {', '.join(self._fields)} FROM {self._table}"
        if self._conditions:
            sql += f" WHERE {' AND '.join(self._conditions)}"
        return sql


# ==============================================================================
# Solution 3: Vector2D Protocol Class
# ==============================================================================
class Vector2DSolution:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2DSolution):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __add__(self, other: "Vector2DSolution") -> "Vector2DSolution":
        if not isinstance(other, Vector2DSolution):
            return NotImplemented
        return Vector2DSolution(self.x + other.x, self.y + other.y)


# ==============================================================================
# Solution 4: Encapsulated BankAccount
# ==============================================================================
class BankAccountSolution:
    def __init__(self, owner: str, initial_deposit: float = 0.0):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative")
        self.owner = owner
        self.__balance = float(initial_deposit)
        self.__transactions: List[Tuple[str, float]] = []
        if initial_deposit > 0:
            self.__transactions.append(("OPENING_BALANCE", initial_deposit))

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transactions.append(("DEPOSIT", float(amount)))
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transactions.append(("WITHDRAW", float(amount)))
        return self.__balance

    def statement(self) -> List[Tuple[str, float]]:
        return list(self.__transactions)


def main():
    s = StudentSolution("Ada")
    s.add_score(100)
    assert s.average() == 100.0

    qb = QueryBuilderSolution().select("a", "b").from_table("tbl")
    assert qb.build() == "SELECT a, b FROM tbl"

    v = Vector2DSolution(3, 4)
    assert len(v) == 5

    acc = BankAccountSolution("Bo", 50)
    acc.deposit(25)
    assert acc.balance == 75.0
    print("Module 12 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
