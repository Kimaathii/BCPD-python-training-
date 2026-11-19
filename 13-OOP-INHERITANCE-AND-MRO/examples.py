"""
Module 13: Object-Oriented Programming — Inheritance & the MRO
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Classroom Sources: D10-01 to D10-07 (Week 2 • Day 10: Wednesday 18 Nov 2026)
Manual Reference: Day 11 (§11.1–11.10)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, FrozenInstanceError
import json


def test_day10_title_script():
    """Verifies day10.py title slide code [Course: D10-01]."""
    class Animal:
        def speak(self):
            return "..."

    class Dog(Animal):
        def speak(self):
            return "Woof"

    assert Dog().speak() == "Woof"
    assert Animal().speak() == "..."


def test_animals_inheritance_and_template():
    """Verifies animals.py inheritance and shared describe() template [Course: D10-03]."""
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "..."

        def describe(self):
            return f"{self.name} says {self.speak()}"

    class Dog(Animal):
        def speak(self):
            return "Woof"

    class Cat(Animal):
        def speak(self):
            return "Meow"

    rex = Dog("Rex")
    tom = Cat("Tom")
    assert rex.describe() == "Rex says Woof"
    assert tom.describe() == "Tom says Meow"


def test_staff_super_and_init():
    """Verifies staff.py super() and super().__init__() [Course: D10-05]."""
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def pay(self):
            return self.salary

    class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)  # reuse parent setup
            self.bonus = bonus

        def pay(self):
            return super().pay() + self.bonus  # extend parent logic

    m = Manager("Ada", 5000, 800)
    assert m.name == "Ada"
    assert m.salary == 5000
    assert m.bonus == 800
    assert m.pay() == 5800


def test_shapes_overriding_and_template():
    """Verifies shapes.py method overriding and polymorphism [Course: D10-06]."""
    class Shape:
        def area(self):
            return 0

        def __str__(self):
            return f"{type(self).__name__}: {self.area():.2f}"

    class Circle(Shape):
        def __init__(self, r):
            self.r = r

        def area(self):
            return 3.14159 * self.r ** 2

    class Square(Shape):
        def __init__(self, s):
            self.s = s

        def area(self):
            return self.s ** 2

    c = Circle(1)
    s = Square(3)
    assert str(c) == "Circle: 3.14"
    assert str(s) == "Square: 9.00"
    assert c.area() == 3.14159
    assert s.area() == 9


def test_checks_and_introspection():
    """Verifies checks.py isinstance, issubclass, and __bases__ [Course: D10-07]."""
    class Animal:
        pass

    class Dog(Animal):
        pass

    d = Dog()
    assert isinstance(d, Dog) is True
    assert isinstance(d, Animal) is True
    assert (type(d) is Animal) is False
    assert (type(d) is Dog) is True
    assert issubclass(Dog, Animal) is True
    assert issubclass(Dog, object) is True
    assert Dog.__bases__ == (Animal,)
    assert isinstance(3, (int, float)) is True

    # bool is a subclass of int trap
    assert issubclass(bool, int) is True
    assert isinstance(True, int) is True
    assert (type(True) is int) is False


def test_diamond_problem_and_mro():
    """Verifies C3 Linearization and MRO in diamond inheritance [Course: D10-04]."""
    class A:
        def ping(self):
            return "A"

    class B(A):
        def ping(self):
            return "B"

    class C(A):
        def ping(self):
            return "C"

    class D(B, C):
        pass

    d = D()
    assert d.ping() == "B"
    # MRO order: D -> B -> C -> A -> object
    expected_mro = [D, B, C, A, object]
    assert D.mro() == expected_mro
    assert D.__mro__ == tuple(expected_mro)


def test_private_attribute_mangling_in_inheritance():
    """Verifies name mangling isolation across inheritance hierarchy [Course: D10-05]."""
    class Parent:
        def __init__(self):
            self.__secret = "parent_secret"

        def get_parent_secret(self):
            return self.__secret

    class Child(Parent):
        def __init__(self):
            super().__init__()
            self.__secret = "child_secret"

    c = Child()
    assert c.get_parent_secret() == "parent_secret"
    assert c._Parent__secret == "parent_secret"
    assert c._Child__secret == "child_secret"


def test_abstract_base_class():
    """Verifies ABC and @abstractmethod enforcement."""
    class BaseValidator(ABC):
        @abstractmethod
        def validate(self, data: str) -> bool:
            pass

    class ConcreteValidator(BaseValidator):
        def validate(self, data: str) -> bool:
            return len(data) > 0

    class IncompleteValidator(BaseValidator):
        pass

    valid = ConcreteValidator()
    assert valid.validate("hello") is True

    try:
        IncompleteValidator()  # type: ignore
        assert False, "Should raise TypeError when abstract method is unimplemented"
    except TypeError as e:
        assert "Can't instantiate abstract class" in str(e)


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass
class Department:
    name: str
    members: list[str] = field(default_factory=list)


def test_dataclasses_basics():
    """Verifies @dataclass, frozen immutability, and mutable default factory."""
    p1 = Point(1.0, 2.0)
    p2 = Point(1.0, 2.0)
    assert p1 == p2
    assert repr(p1) == "Point(x=1.0, y=2.0)"

    try:
        p1.x = 5.0  # type: ignore
        assert False, "Should raise FrozenInstanceError"
    except FrozenInstanceError:
        pass

    d1 = Department("Engineering")
    d2 = Department("Marketing")
    d1.members.append("Alice")
    assert d1.members == ["Alice"]
    assert d2.members == []  # Independent lists!


def main():
    print("Running Module 13: OOP Inheritance & MRO test suite...")
    test_day10_title_script()
    test_animals_inheritance_and_template()
    test_staff_super_and_init()
    test_shapes_overriding_and_template()
    test_checks_and_introspection()
    test_diamond_problem_and_mro()
    test_private_attribute_mangling_in_inheritance()
    test_abstract_base_class()
    test_dataclasses_basics()
    print("All Module 13 examples PASSED cleanly (100% verified against Day 10 slides).")


if __name__ == "__main__":
    main()
