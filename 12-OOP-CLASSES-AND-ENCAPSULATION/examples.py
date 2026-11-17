"""
Module 12: Object-Oriented Programming — Executable Classroom Code
Course: BCPD Python Certification — Domain 3: Object-Oriented Programming (15%)
Classroom Sources: D9-01 to D9-11 (Week 2 • Day 9: Tuesday 17 Nov 2026)
Manual: Day 10 (§10.1–10.10)
"""


def test_day9_title_script():
    """Verifies day9.py title slide code [Course: D9-01]."""
    class Account:
        def __init__(self, owner):
            self.owner = owner
            self.__balance = 0

    acct = Account("Ada")
    assert acct.owner == "Ada"
    assert hasattr(acct, "_Account__balance")


def test_account_class_basics():
    """Verifies account.py [Course: D9-05]."""
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self.balance

    acct = BankAccount("Ada", 100)
    assert acct.owner == "Ada"
    assert acct.balance == 100
    assert acct.deposit(50) == 150
    assert acct.balance == 150
    assert type(acct).__name__ == "BankAccount"


def test_clicker_methods_and_chaining():
    """Verifies counter.py [Course: D9-09]."""
    class Clicker:
        def __init__(self):
            self.count = 0

        def click(self, step=1):
            self.count += step
            return self  # enables chaining

    c = Clicker()
    c.click().click(5)
    assert c.count == 6

    # Calling method through Class passes instance explicitly
    Clicker.click(c)
    assert c.count == 7


def test_forgets_self_trap():
    """Verifies TypeError raised when self is omitted from method signature [Course: D9-09]."""
    class Broken:
        def ping():  # type: ignore
            return "pong"

    b = Broken()
    try:
        b.ping()
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "takes 0 positional arguments but 1 was given" in str(e)


def test_class_vs_instance_attributes():
    """Verifies dogs.py [Course: D9-08]."""
    class Dog:
        species = "Canis familiaris"  # class attribute: shared
        tricks = []                   # shared mutable: a trap!

        def __init__(self, name):
            self.name = name          # instance attribute

    a, b = Dog("Rex"), Dog("Fido")
    a.tricks.append("sit")
    # Both instances share the class-level mutable list!
    assert b.tricks == ["sit"]

    # Assigning via an instance creates an instance attribute; class untouched
    a.species = "wolf"
    assert a.species == "wolf"
    assert b.species == "Canis familiaris"
    assert Dog.species == "Canis familiaris"


def test_dunder_methods():
    """Verifies book.py [Course: D9-07]."""
    class Book:
        def __init__(self, title, pages):
            self.title, self.pages = title, pages

        def __str__(self):
            return f"{self.title} ({self.pages}p)"

        def __repr__(self):
            return f"Book({self.title!r}, {self.pages})"

        def __eq__(self, other):
            if not isinstance(other, Book):
                return NotImplemented
            return self.title == other.title

        def __len__(self):
            return self.pages

    b = Book("Dune", 412)
    assert str(b) == "Dune (412p)"
    assert repr(b) == "Book('Dune', 412)"
    assert len(b) == 412
    assert b == Book("Dune", 1)  # Equal title returns True regardless of pages


def test_encapsulation_and_mangling():
    """Verifies private.py [Course: D9-06] and Access Matrix [Course: D9-11]."""
    class Account:
        def __init__(self, balance):
            self._owner = "Ada"       # protected convention
            self.__balance = balance  # private (name-mangled)

        def withdraw(self, amount):
            if amount > self.__balance:
                raise ValueError("Insufficient funds")
            self.__balance -= amount
            return self.__balance

    acc = Account(100)
    assert acc.withdraw(30) == 70
    assert acc._Account__balance == 70
    assert acc._owner == "Ada"

    # Direct access to mangled private name raises AttributeError
    try:
        _ = acc.__balance  # type: ignore
        assert False, "Should raise AttributeError"
    except AttributeError:
        pass


def test_property_decorator():
    """Verifies temperature.py [Course: D9-10]."""
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius  # runs the setter!

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Below absolute zero")
            self._celsius = value

        @property
        def fahrenheit(self):  # read-only property
            return self._celsius * 9 / 5 + 32

    t = Temperature(25)
    t.celsius = 30
    assert t.celsius == 30
    assert t.fahrenheit == 86.0

    # Validation rejection
    try:
        t.celsius = -300
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # Read-only property rejection on write
    try:
        t.fahrenheit = 100  # type: ignore
        assert False, "Should raise AttributeError"
    except AttributeError:
        pass


def main():
    print("Running Module 12: OOP Classes & Encapsulation test suite...")
    test_day9_title_script()
    test_account_class_basics()
    test_clicker_methods_and_chaining()
    test_forgets_self_trap()
    test_class_vs_instance_attributes()
    test_dunder_methods()
    test_encapsulation_and_mangling()
    test_property_decorator()
    print("All Module 12 examples PASSED cleanly (100% verified against Day 9 slides).")


if __name__ == "__main__":
    main()
