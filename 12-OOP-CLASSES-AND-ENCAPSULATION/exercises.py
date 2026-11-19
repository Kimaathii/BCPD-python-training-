"""
Module 12: OOP Classes & Encapsulation — Progressive Practical Exercises
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 10 (§10.1–10.10)
"""

from typing import List, Optional, Tuple


# ==============================================================================
# Level 1: Basic Class Definition & Dunder String Representation
# ==============================================================================
class Student:
    """
    Represents a student designed according to UML specification [Course: D9-EXT-01].
    Attributes:
        - name: str
        - grades: list[int]
    Methods:
        + add_grade(g: int) -> None (validates 0 <= g <= 100)
        + gpa() -> float (average rounded to 1 decimal place, or 0.0 if empty)
    Dunder:
        __str__(): returns "Student(name=<name>, gpa=<gpa>)"
    """
    def __init__(self, name: str):
        self.name = name
        self.grades: List[int] = []

    def add_grade(self, g: int) -> None:
        if not (0 <= g <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(int(g))

    # Backward compatibility alias
    add_score = add_grade

    def gpa(self) -> float:
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 1)

    average = gpa

    def __str__(self) -> str:
        return f"Student(name={self.name}, avg={self.gpa()})"


# ==============================================================================
# Level 2: Method Chaining with Returning self
# ==============================================================================
class QueryBuilder:
    """
    A SQL SELECT query builder supporting fluent method chaining.
    Methods:
        select(*fields: str): records columns to select. Returns self.
        from_table(table: str): records table name. Returns self.
        where(condition: str): records filter condition. Returns self.
        build(): constructs the SQL query string.
                 Format: "SELECT <fields> FROM <table> WHERE <condition>"
                 If no condition was set, omit WHERE clause.
    """
    def __init__(self):
        self._fields = ["*"]
        self._table: Optional[str] = None
        self._conditions: List[str] = []

    def select(self, *fields: str) -> "QueryBuilder":
        if fields:
            self._fields = list(fields)
        return self

    def from_table(self, table: str) -> "QueryBuilder":
        self._table = table
        return self

    def where(self, condition: str) -> "QueryBuilder":
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
# Level 3: Dunder Methods Implementation (Protocol Compliance)
# ==============================================================================
class Vector2D:
    """
    A 2D mathematical vector with x and y coordinates.
    Implements:
        __repr__: "Vector2D(x, y)"
        __str__: "(x, y)"
        __eq__: compares x and y
        __len__: returns integer truncated magnitude: int((x**2 + y**2)**0.5)
        __add__: returns new Vector2D with element-wise sum
    """
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)


# ==============================================================================
# Level 4: Full Encapsulation with @property and Validation (Lab 9.1)
# ==============================================================================
class BankAccount:
    """
    Enterprise-grade bank account with encapsulated private state.
    Attributes:
        owner: public string
        balance: private float accessed via @property (read-only from outside direct assignment)
    Methods:
        deposit(amount: float) -> float
        withdraw(amount: float) -> float
        statement() -> List[Tuple[str, float]]
    """
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

    def transfer(self, target: "BankAccount", amount: float) -> None:
        """Transfers amount from self to target account [Course: D9-EXT-03]."""
        self.withdraw(amount)
        target.deposit(amount)

    def statement(self) -> List[Tuple[str, float]]:
        return list(self.__transactions)

    def __str__(self) -> str:
        return f"{self.owner}: {self.__balance:.2f}"


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1
    s = Student("Bo")
    s.add_score(85)
    s.add_score(95)
    assert s.average() == 90.0
    assert str(s) == "Student(name=Bo, avg=90.0)"

    # Test Level 2
    qb = QueryBuilder()
    sql = qb.select("id", "name").from_table("users").where("active = 1").build()
    assert sql == "SELECT id, name FROM users WHERE active = 1"

    # Test Level 3
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    assert str(v1) == "(3.0, 4.0)"
    assert repr(v1) == "Vector2D(3.0, 4.0)"
    assert len(v1) == 5  # sqrt(3^2 + 4^2) = 5
    assert (v1 + v2) == Vector2D(4, 6)

    # Test Level 4
    acct = BankAccount("Ada", 100.0)
    assert acct.owner == "Ada"
    assert acct.balance == 100.0
    assert str(acct) == "Ada: 100.00"
    acct.deposit(50.0)
    assert acct.balance == 150.0
    acct.withdraw(20.0)
    assert acct.balance == 130.0

    target = BankAccount("Bob", 20.0)
    acct.transfer(target, 30.0)
    assert acct.balance == 100.0
    assert target.balance == 50.0

    stmt = acct.statement()
    assert len(stmt) == 4

    # Ensure balance cannot be directly overwritten
    try:
        acct.balance = 500  # type: ignore
        assert False, "Should raise AttributeError on read-only property assignment"
    except AttributeError:
        pass


if __name__ == "__main__":
    test_exercises()
    print("All Module 12 exercises PASSED verification tests.")
