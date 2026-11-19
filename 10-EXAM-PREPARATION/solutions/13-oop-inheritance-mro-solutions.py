"""
Module 13 Solutions: OOP Inheritance & the MRO
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Student Manual Reference: Day 11 (§11.1–11.10)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math
from typing import List, Optional


# ==============================================================================
# Solution 1: Single & Multilevel Inheritance with super()
# ==============================================================================
class PersonSolution:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def describe(self) -> str:
        return f"{self.name} <{self.email}>"

    def get_role(self) -> str:
        return "Person"


class StudentSolution(PersonSolution):
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.courses: List[str] = []

    def enroll(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def get_role(self) -> str:
        return "Student"


class TeacherSolution(PersonSolution):
    def __init__(self, name: str, email: str, employee_id: str, department: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department

    def get_role(self) -> str:
        return "Teacher"


# ==============================================================================
# Solution 2: Method Overriding & Shared Template
# ==============================================================================
class ShapeSolution:
    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"{type(self).__name__}(area={self.area():.2f}, perim={self.perimeter():.2f})"


class CircleSolution(ShapeSolution):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class RectangleSolution(ShapeSolution):
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
# Solution 3: Multiple Inheritance & Diamond MRO
# ==============================================================================
class JSONExportMixinSolution:
    def to_dict(self) -> dict:
        return {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_")
        }


class TimestampMixinSolution:
    def get_timestamp(self) -> str:
        return "2026-11-18T00:00:00Z"


class DocumentSolution(JSONExportMixinSolution, TimestampMixinSolution):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class DeviceSolution:
    def identify(self) -> str:
        return "Device"


class ScannerSolution(DeviceSolution):
    def identify(self) -> str:
        return "Scanner"


class PrinterSolution(DeviceSolution):
    def identify(self) -> str:
        return "Printer"


class CopierSolution(ScannerSolution, PrinterSolution):
    pass


# ==============================================================================
# Solution 4: ABC & Dataclass Contract
# ==============================================================================
class PaymentProcessorSolution(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass

    @abstractmethod
    def capture(self, amount: float) -> bool:
        pass


@dataclass
class TransactionRecordSolution:
    processor_name: str
    amount: float
    authorized: bool = False
    captured: bool = False


class CreditCardProcessorSolution(PaymentProcessorSolution):
    def __init__(self, merchant_id: str):
        self.merchant_id = merchant_id
        self.ledger: List[TransactionRecordSolution] = []

    def authorize(self, amount: float) -> bool:
        if amount <= 0:
            return False
        record = TransactionRecordSolution(processor_name="CreditCard", amount=amount, authorized=True)
        self.ledger.append(record)
        return True

    def capture(self, amount: float) -> bool:
        for record in self.ledger:
            if record.amount == amount and record.authorized and not record.captured:
                record.captured = True
                return True
        return False


def main():
    s = StudentSolution("Ada", "ada@example.com", "S001")
    s.enroll("Python")
    assert s.describe() == "Ada <ada@example.com>"
    assert s.get_role() == "Student"

    c = CircleSolution(5)
    assert round(c.area(), 2) == 78.54
    assert str(c) == "CircleSolution(area=78.54, perim=31.42)"

    doc = DocumentSolution("Spec", "Guido")
    assert doc.to_dict() == {"title": "Spec", "author": "Guido"}

    copier = CopierSolution()
    assert copier.identify() == "Scanner"
    assert CopierSolution.mro() == [CopierSolution, ScannerSolution, PrinterSolution, DeviceSolution, object]

    proc = CreditCardProcessorSolution("M999")
    assert proc.authorize(200.0) is True
    assert proc.capture(200.0) is True
    print("Module 13 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
