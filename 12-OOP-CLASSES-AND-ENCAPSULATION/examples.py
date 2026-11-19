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


def test_lifecycle_and_dynamic_attributes():
    """Verifies lifecycle.py dynamic attributes, introspection, and destructor [Course: D9-EXT-02]."""
    class Employee:
        pass

    e = Employee()
    # Dynamic attributes (any object can grow them)
    e.colour = "red"
    setattr(e, "size", 3)
    assert getattr(e, "colour") == "red"
    assert hasattr(e, "size") is True
    assert hasattr(e, "salary") is False
    delattr(e, "colour")
    assert hasattr(e, "colour") is False

    # Introspection
    assert vars(e) == {"size": 3}
    assert e.__dict__ == {"size": 3}
    assert Employee.__name__ == "Employee"
    assert Employee.__doc__ is None
    assert e.__class__ is Employee

    # Destructor __del__
    cleanup_log = []
    class TempFile:
        def __init__(self, tag):
            self.tag = tag
        def __del__(self):
            cleanup_log.append(f"cleanup {self.tag}!")

    t = TempFile("alpha")
    del t
    assert cleanup_log == ["cleanup alpha!"]


def test_bank_account_lab_9_1():
    """Verifies bank.py Lab 9.1 BankAccount with transfer and formatting [Course: D9-EXT-03]."""
    class BankAccount:
        def __init__(self, owner: str, initial_balance: float = 0.0):
            self.owner = owner
            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative")
            self.__balance = float(initial_balance)

        @property
        def balance(self) -> float:
            return self.__balance

        def deposit(self, amount: float) -> float:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.__balance += amount
            return self.__balance

        def withdraw(self, amount: float) -> float:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self.__balance:
                raise ValueError("Insufficient funds")
            self.__balance -= amount
            return self.__balance

        def transfer(self, target: "BankAccount", amount: float) -> None:
            self.withdraw(amount)
            target.deposit(amount)

        def __str__(self) -> str:
            return f"{self.owner}: {self.__balance:.2f}"

    b1 = BankAccount("Ada", 100.0)
    b2 = BankAccount("Charles", 50.0)

    assert str(b1) == "Ada: 100.00"
    assert b1.balance == 100.0
    b1.deposit(50.0)
    assert b1.balance == 150.0
    b1.withdraw(20.0)
    assert b1.balance == 130.0

    # Test transfer
    b1.transfer(b2, 30.0)
    assert b1.balance == 100.0
    assert b2.balance == 80.0

    # Overdraft protection
    try:
        b1.withdraw(500.0)
        assert False, "Should raise ValueError on overdraft"
    except ValueError:
        pass

    # Read-only property
    try:
        b1.balance = 999.0  # type: ignore
        assert False, "Should raise AttributeError on read-only property"
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
    test_lifecycle_and_dynamic_attributes()
    test_bank_account_lab_9_1()
    print("All Module 12 examples PASSED cleanly (100% verified against Day 9 slides).")


if __name__ == "__main__":
    main()
