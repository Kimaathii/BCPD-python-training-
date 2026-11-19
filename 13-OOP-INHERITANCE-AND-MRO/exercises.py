"""
Module 13: OOP Inheritance & the MRO — Progressive Practical Exercises
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 11 (§11.1–11.10)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import math
from typing import List, Optional, Tuple


# ==============================================================================
# Level 1: Single & Multilevel Inheritance with super() (Lab 10.1 School System)
# ==============================================================================
class Person:
    """
    Base class representing a person in the school system.
    Attributes:
        name: str
        email: str
    Methods:
        describe() -> str: returns f"{self.name} <{self.email}>"
        get_role() -> str: returns "Person"
    """
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def describe(self) -> str:
        return f"{self.name} <{self.email}>"

    def get_role(self) -> str:
        return "Person"


class Student(Person):
    """
    Child class inheriting from Person [Course: D10-03, D10-05].
    Attributes:
        student_id: str
        courses: list[str]
    Methods:
        enroll(course: str) -> None
        get_role() -> str: overrides to return "Student"
    """
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.courses: List[str] = []

    def enroll(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def get_role(self) -> str:
        return "Student"


class Teacher(Person):
    """
    Child class inheriting from Person.
    Attributes:
        employee_id: str
        department: str
    Methods:
        get_role() -> str: overrides to return "Teacher"
    """
    def __init__(self, name: str, email: str, employee_id: str, department: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department

    def get_role(self) -> str:
        return "Teacher"


# ==============================================================================
# Level 2: Method Overriding & Shared Template / Polymorphic Shapes
# ==============================================================================
class Shape:
    """
    Template pattern base class [Course: D10-06].
    Defines area() and perimeter() returning 0.0,
    and __str__() template returning f"{type(self).__name__}(area={self.area():.2f}, perim={self.perimeter():.2f})"
    """
    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"{type(self).__name__}(area={self.area():.2f}, perim={self.perimeter():.2f})"


class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


# ==============================================================================
# Level 3: Multiple Inheritance, Diamond MRO & Mixins
# ==============================================================================
class JSONExportMixin:
    """Mixin class adding JSON serialization capabilities without state [Course: D10-04]."""
    def to_dict(self) -> dict:
        return {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_")
        }


class TimestampMixin:
    """Mixin adding creation timestamp string."""
    def get_timestamp(self) -> str:
        return "2026-11-18T00:00:00Z"


class Document(JSONExportMixin, TimestampMixin):
    """Multiple inheritance subclass combining mixins."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


# Diamond Pattern Test Classes
class Device:
    def identify(self) -> str:
        return "Device"


class Scanner(Device):
    def identify(self) -> str:
        return "Scanner"


class Printer(Device):
    def identify(self) -> str:
        return "Printer"


class Copier(Scanner, Printer):
    """Diamond inheritance: Copier -> Scanner -> Printer -> Device -> object."""
    pass


# ==============================================================================
# Level 4: Abstract Base Classes & Dataclass Integration
# ==============================================================================
class PaymentProcessor(ABC):
    """Abstract Base Class enforcing payment gateway contracts [Course: D10-02, Manual §11.6]."""
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass

    @abstractmethod
    def capture(self, amount: float) -> bool:
        pass


@dataclass
class TransactionRecord:
    processor_name: str
    amount: float
    authorized: bool = False
    captured: bool = False


class CreditCardProcessor(PaymentProcessor):
    def __init__(self, merchant_id: str):
        self.merchant_id = merchant_id
        self.ledger: List[TransactionRecord] = []

    def authorize(self, amount: float) -> bool:
        if amount <= 0:
            return False
        record = TransactionRecord(processor_name="CreditCard", amount=amount, authorized=True)
        self.ledger.append(record)
        return True

    def capture(self, amount: float) -> bool:
        for record in self.ledger:
            if record.amount == amount and record.authorized and not record.captured:
                record.captured = True
                return True
        return False


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1
    s = Student("Bo", "bo@school.edu", "S101")
    t = Teacher("Dr. Smith", "smith@school.edu", "T501", "CS")
    assert s.describe() == "Bo <bo@school.edu>"
    assert s.get_role() == "Student"
    s.enroll("Python 101")
    s.enroll("Python 101")  # duplicate avoided
    assert s.courses == ["Python 101"]
    assert t.get_role() == "Teacher"
    assert isinstance(s, Person) is True
    assert issubclass(Student, Person) is True

    # Test Level 2
    c = Circle(10)
    r = Rectangle(4, 5)
    assert round(c.area(), 2) == 314.16
    assert round(c.perimeter(), 2) == 62.83
    assert r.area() == 20.0
    assert r.perimeter() == 18.0
    assert str(r) == "Rectangle(area=20.00, perim=18.00)"

    # Test Level 3
    doc = Document("Curriculum", "Ada")
    assert doc.to_dict() == {"title": "Curriculum", "author": "Ada"}
    assert doc.get_timestamp() == "2026-11-18T00:00:00Z"
    copier = Copier()
    assert copier.identify() == "Scanner"  # Scanner declared before Printer in Copier(Scanner, Printer)
    assert Copier.mro() == [Copier, Scanner, Printer, Device, object]

    # Test Level 4
    proc = CreditCardProcessor("MERCH_001")
    assert proc.authorize(150.0) is True
    assert proc.capture(150.0) is True
    assert len(proc.ledger) == 1
    assert proc.ledger[0].captured is True


if __name__ == "__main__":
    test_exercises()
    print("All Module 13 exercises PASSED verification tests.")
