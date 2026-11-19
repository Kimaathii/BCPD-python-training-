# Day 9 Extensions & Day 10 Screenshot Inventory & Analysis

> **BCPD Python Cohort 2 Certification Preparation**  
> **Batch Date:** 19 Nov 2026 (14 Newly Added Class Screenshots)  
> **Course Scope:** 
> - **Week 2 • Day 9 Extensions:** UML class diagrams, dynamic attributes & object lifecycle (`lifecycle.py`), Lab 9.1 BankAccount class (`bank.py`), and official Day 9 Quiz answer key (`[Course: D9-EXT-01 to D9-EXT-04]`).
> - **Week 2 • Day 10 (Wednesday 18 Nov 2026):** OOP Part 2: Inheritance & the MRO (Manual Day 11 §11.1–11.10; Domain 3: Object-Oriented Programming, 15%) (`[Course: D10-01 to D10-07]`).

---

## 1. Inventory & Metadata Matrix

| Image ID | Original Filename | Topic | Manual / Slide | Slide Title | Code / Artifact | Status | Description & Key Pedagogical Points |
|---|---|---|---|---|---|:---:|---|
| **D9-EXT-01** | `WhatsApp Image 2026-11-19 at 07.36.23.jpeg` | Day 9 Extension — UML Basics | Beyond the Manual | Designing a class (UML basics) | UML diagram | Verified | Class box notation: Name (PascalCase), Attributes (`-` private, `+` public), Methods (`+` public, `-` private). 4-step workflow: 1. Name class, 2. List attributes, 3. List methods, 4. Code & test (`__init__` first). |
| **D9-EXT-02** | `WhatsApp Image 2026-11-19 at 07.36.23g.jpeg` | Day 9 Extension — Object Lifecycle | Beyond the Manual | Object lifecycle & dynamic attributes | `lifecycle.py` | Verified | Dynamic attributes via dot assignment, `setattr()`, `getattr()`, `hasattr()`, `delattr()`; `vars(obj)` / `obj.__dict__`; class metadata (`__name__`, `__doc__`, `__class__`); destructor `__del__(self)` executed on ref-count 0. |
| **D9-EXT-03** | `WhatsApp Image 2026-11-19 at 07.36.23t.jpeg` | Day 9 Extension — Lab 9.1 | Manual §10.9 | Lab 9.1 BankAccount class | `bank.py` | Verified | Build `BankAccount` with owner, private `__balance = 0.0`, `@property balance` (read-only), `deposit(amount)`, `withdraw(amount)` with validation, `__str__` format `f"{self.owner}: {self.__balance:.2f}"`, and inter-account transfer. |
| **D9-EXT-04** | `WhatsApp Image 2026-11-19 at 07.36.24h.jpeg` | Day 9 Official Quiz | Knowledge Check | Knowledge check | 5 MCQ Quiz | Verified | Official Day 9 Quiz: Q1 self (D: current object), Q2 print uses (C: `__str__`), Q3 `self.__secret` in `Vault` (D: `_Vault__secret`), Q4 `a == b` without `__eq__` (A: Identity `is`), Q5 `@property` without setter (B: Read-only). |
| **D10-01** | `WhatsApp Image 2026-11-19 at 07.36.25ty.jpeg`<br>`WhatsApp Image 2026-11-19 at 07.36.53.jpeg` | Day 10 Title Slide | Title / Slide 1 | OOP Part 2: Inheritance & the MRO | `day10.py` | Verified | Week 2 • Day 10 (Wednesday 18 Nov 2026). Domain 3: OOP (15%). Manual Day 11 (§11.1–11.10). `Animal` vs `Dog(Animal)` method overriding. |
| **D10-02** | `WhatsApp Image 2026-11-19 at 07.36.25bn.jpeg`<br>`WhatsApp Image 2026-11-19 at 07.36.54.jpeg` | Day 10 Agenda & Objectives | Slide 2 | Today's objectives & agenda | — | Verified | 5 learning outcomes; syllabus mapping: 11.1 IS-A & Types of inheritance, 11.2 `super()` & `__init__`, 11.3 Overriding & shared template, 11.4 `isinstance`/`issubclass`, 11.5 Multiple inheritance & MRO / C3, 11.2 Private names across hierarchy, 11.6 ABCs, 11.7 Composition & mixins, 11.9 Dataclasses, Lab 10.1. |
| **D10-03** | `WhatsApp Image 2026-11-19 at 07.36.26bh.jpeg`<br>`WhatsApp Image 2026-11-19 at 07.36.54v.jpeg` | Day 10 Inheritance: IS-A | Manual §11.1 | Inheritance: the IS-A relationship | `animals.py` | Verified | Syntax `class Dog(Animal):`. Child inherits attributes & methods. Override `speak()`. Shared template `describe()` calling `self.speak()`. Every class inherits from `object`. True IS-A relationships only. |
| **D10-04** | `WhatsApp Image 2026-11-19 at 07.36.26gt.jpeg` | Day 10 Types of Inheritance | Manual §11.1 | Types of inheritance | 6 Concept Cards | Verified | 1. Single (`B(A)`), 2. Multilevel (`C(B)` where `B(A)`), 3. Hierarchical (`B(A)` and `C(A)`), 4. Multiple (`C(A, B)`), 5. Hybrid (Diamond `B(A), C(A), D(B, C)`), 6. Inspection tools (`help()`, `D.__mro__`, `D.__bases__`, `issubclass()`). |
| **D10-05** | `WhatsApp Image 2026-11-19 at 07.36.26bjj.jpeg` | Day 10 super() & `__init__` | Manual §11.2 | `super()` and `super().__init__()` | `staff.py` | Verified | `super()` proxies to next MRO class. Skipping `super().__init__()` leaves parent attributes uninitialized -> `AttributeError`. Method extension via `super().pay() + bonus`. |
| **D10-06** | `WhatsApp Image 2026-11-19 at 07.36.26h.jpeg` | Day 10 Overriding & Templates | Manual §11.3 | Method overriding & a shared template | `shapes.py` | Verified | Method overriding: child method takes precedence. Shared template pattern: `Shape.__str__` calls `self.area()`. Parent methods remain reachable via `super().area()`. |
| **D10-07** | `WhatsApp Image 2026-11-19 at 07.36.27g.jpeg` | Day 10 Introspection Tools | Manual §11.4 | `isinstance()`, `issubclass()` & `object` | `checks.py` | Verified | `isinstance(obj, C)` checks inheritance chain; `type(obj) is C` checks exact class; `issubclass(A, B)` compares classes; tuple of types `isinstance(x, (int, float))`; `Dog.__bases__`. |

---

## 2. Verbatim Classroom Code Extractions

### 2.1 Day 9 Extension: Object Lifecycle & Dynamic Attributes (`lifecycle.py`) `[Course: D9-EXT-02]`
```python
class Employee:
    pass

e = Employee()
# Dynamic attributes (any object can grow them)
e.colour = "red"
setattr(e, "size", 3)
print(getattr(e, "colour"))      # red
print(hasattr(e, "salary"))      # False
delattr(e, "colour")

# Introspection
print(vars(e))                   # {'size': 3}
print(e.__dict__)                # {'size': 3}
print(Employee.__name__)         # Employee
print(Employee.__doc__)          # None
print(e.__class__)               # <class '__main__.Employee'>

# Destructor
class TempFile:
    def __del__(self):
        print("cleanup!")

t = TempFile()
del t                            # runs __del__ when ref count hits 0
```

### 2.2 Day 9 Extension: Lab 9.1 BankAccount Specification (`bank.py`) `[Course: D9-EXT-03]`
```python
class BankAccount:
    """
    Lab 9.1 BankAccount specification:
    - owner: str
    - __balance: float, initialized to 0.0 (private)
    - balance: @property (read-only, returns __balance)
    - deposit(amount): amount must be > 0, raises ValueError on invalid input
    - withdraw(amount): amount must be > 0 and <= __balance, raises ValueError on overdraft
    - __str__(): returns f"{self.owner}: {self.__balance:.2f}"
    - transfer(target, amount): withdraws from self and deposits into target
    """
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
```

### 2.3 Day 10 Title Snippet: `day10.py` `[Course: D10-01]`
```python
class Animal:
    def speak(self): 
        return "..."

class Dog(Animal):
    def speak(self): 
        return "Woof"

print(Dog().speak())  # Woof
```

### 2.4 Day 10 Single Inheritance & Shared Template: `animals.py` `[Course: D10-03]`
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def describe(self) -> str:
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


print(Dog("Rex").describe())  # Rex says Woof
print(Cat("Tom").describe())  # Tom says Meow
```

### 2.5 Day 10 Parent Calls & Extending Logic: `staff.py` `[Course: D10-05]`
```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def pay(self) -> float:
        return self.salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)  # reuse parent setup
        self.bonus = bonus

    def pay(self) -> float:
        return super().pay() + self.bonus  # extend parent logic


m = Manager("Ada", 5000, 800)
print(m.name, m.pay())  # Ada 5800
```

### 2.6 Day 10 Overriding & Template Pattern: `shapes.py` `[Course: D10-06]`
```python
class Shape:
    def area(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.area():.2f}"


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r ** 2


class Square(Shape):
    def __init__(self, s: float):
        self.s = s

    def area(self) -> float:
        return self.s ** 2


for shape in [Circle(1), Square(3)]:
    print(shape)
# Circle: 3.14
# Square: 9.00
```

### 2.7 Day 10 Type Checking & Hierarchy Introspection: `checks.py` `[Course: D10-07]`
```python
class Animal: 
    pass

class Dog(Animal): 
    pass

d = Dog()
print(isinstance(d, Dog), isinstance(d, Animal))    # True True
print(type(d) is Animal)                            # False
print(issubclass(Dog, Animal))                      # True
print(issubclass(Dog, object))                      # True
print(Dog.__bases__)                                # (<class '__main__.Animal'>,)
print(isinstance(3, (int, float)))                  # True
```

---

## 3. Official Classroom Quiz Answer Key: Day 9 `[Course: D9-EXT-04]`

| Question # | Slide Prompt | Options | Correct Answer | Technical Explanation |
|:---:|---|---|:---:|---|
| **Q1** | In an instance method, what is `self`? | A) The class name<br>B) A Python keyword<br>C) The return value<br>D) The current object | **D** | `self` is a parameter name (by convention, not a keyword) that receives the reference to the instance on which the method is called. |
| **Q2** | Which method does `print(obj)` use first? | A) `__repr__`<br>B) `__init__`<br>C) `__str__`<br>D) `__format__` | **C** | `print()` and `str()` invoke `obj.__str__()`. If `__str__` is not defined on the class, Python falls back to `obj.__repr__()`. |
| **Q3** | An attribute `self.__secret` in class `Vault` is stored as: | A) `__secret`<br>B) `secret`<br>C) `__Vault_secret`<br>D) `_Vault__secret` | **D** | Name mangling rewrites identifiers with two leading underscores to `_<ClassName>__<attrName>`. Thus `self.__secret` in `Vault` is stored as `_Vault__secret`. |
| **Q4** | Without `__eq__`, what does `a == b` compare for two objects? | A) Identity (`is`)<br>B) Their `__dict__`<br>C) Their types<br>D) Memory size | **A** | The default implementation of `__eq__` inherited from `object` compares object identity: `a is b` (i.e. `id(a) == id(b)`). |
| **Q5** | A `@property` with no setter makes the attribute: | A) Static<br>B) Read-only<br>C) Private<br>D) Inherited | **B** | In Python's descriptor protocol, defining a getter method decorated with `@property` without a corresponding `@prop.setter` creates a read-only property; assigning to it raises `AttributeError`. |
