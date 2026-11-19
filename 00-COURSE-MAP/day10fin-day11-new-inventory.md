# Day 10 Finalization & Day 11 Screenshot Inventory & Analysis

> **BCPD Python Cohort 2 Certification Preparation**  
> **Batch Date:** 19 Nov 2026 (20 Newly Added Class Screenshots: 8:27 PM – 8:31 PM)  
> **Course Scope:** 
> - **Week 2 • Day 10 Finalization:** `mro.py`, C3 linearization mechanics, constructor lifecycle `__new__` vs `__init__` (`construct.py`), `abstract.py`, composition & mixins, `dataclasses_demo.py`, Lab 10.1 `hierarchy.py` (`Square(Rectangle)`), and official Day 10 Quiz answer key (`[Course: D10-08 to D10-15]`).
> - **Week 2 • Day 11 (Thursday 19 Nov 2026):** Polymorphism, Overloading & OOP Design (Manual Day 12 §12.1–12.6 + Day 13 §13.1–13.5; Domain 3: Object-Oriented Programming, 15%) (`[Course: D11-01 to D11-08]`).

---

## 1. Inventory & Metadata Matrix

| Image ID | Original Filename | Topic | Manual / Slide | Slide Title | Code / Artifact | Status | Description & Key Pedagogical Points |
|---|---|---|---|---|---|:---:|---|
| **D10-RET-01** | `WhatsApp Image 2026-11-19 at 20.20.51.jpeg` | Day 10 Agenda | Slide 2 | Today's objectives & agenda | — | Verified | Retake/high-res of Day 10 Agenda slide. |
| **D10-RET-02** | `WhatsApp Image 2026-11-19 at 20.20.51K.jpeg` | Day 10 Title | Slide 1 | OOP Part 2: Inheritance & the MRO | `day10.py` | Verified | Retake/high-res of Day 10 Title slide. |
| **D10-RET-03** | `WhatsApp Image 2026-11-19 at 20.20.51L.jpeg` | Day 10 Inheritance | Manual §11.1 | Inheritance: the IS-A relationship | `animals.py` | Verified | Retake/high-res of `animals.py` slide. |
| **D10-08** | `WhatsApp Image 2026-11-19 at 20.20.53.jpeg` | Day 10 Multiple Inheritance & MRO | Manual §11.5 | Multiple inheritance & the MRO | `mro.py` | Verified | `class D(B, C): pass`. Method lookup left-to-right (`B` checked before `C`). Inspecting via `D.__mro__`, `D.mro()`, `help(D)`. Output: `['D', 'B', 'C', 'A', 'object']`. |
| **D10-09** | `WhatsApp Image 2026-11-19 at 20.20.54.jpeg` | Day 10 Diamond Problem & C3 | Manual §11.5 | The diamond problem & C3 linearisation | 4 Step Flowchart | Verified | 4-step lookup: 1. Class itself (`D`), 2. Parents left to right (`B` then `C`), 3. Shared base last (`A` after all children), 4. Finally `object`. Callout: *For a D object, `super()` inside B calls C — not A!* |
| **D10-10** | `WhatsApp Image 2026-11-19 at 20.20.55.jpeg` | Day 10 Constructors & Private Names | Manual §11.2, 11.5 | Constructors & private names across a hierarchy | `construct.py` | Verified | `__new__` creates object, `__init__` initialises it. `Base.__init__(self)` explicit alternative to `super()`. Calling `self.setup()` in base dispatches to child's override. `__secret` mangled to `_Base__secret`. |
| **D10-11** | `WhatsApp Image 2026-11-19 at 20.20.55LP.jpeg` | Day 10 Abstract Base Classes | Manual §11.6 | Abstract base classes | `abstract.py` | Verified | `from abc import ABC, abstractmethod`. Enforces interface contracts. `Shape(ABC)` with `@abstractmethod def area()`. Subclasses must implement or cannot be instantiated (`TypeError`). |
| **D10-12** | `WhatsApp Image 2026-11-19 at 20.20.55KI.jpeg` | Day 10 Composition & Mixins | Manual §11.7–11.8 | Composition, mixins & good design | 3 Concept Cards | Verified | 1. Composition (HAS-A): *Car has an Engine*. 2. Mixins: small reusable capability classes (`JsonMixin`, `LogMixin`). 3. Rule of thumb: prefer composition, keep hierarchies shallow. |
| **D10-13** | `WhatsApp Image 2026-11-19 at 20.20.55PO.jpeg` | Day 10 Dataclasses | Manual §11.9 | Dataclasses (Python 3.7+) | `dataclasses_demo.py` | Verified | `@dataclass` generates `__init__`, `__repr__`, `__eq__`. `order=True` adds `<` and `>`. Mutable defaults need `field(default_factory=list)`. Child dataclasses append fields after parent. |
| **D10-14** | `WhatsApp Image 2026-11-19 at 20.20.55IU.jpeg` | Day 10 Lab 10.1 | Manual §11.10 | Lab 10.1 — School system & shape hierarchy | `hierarchy.py` | Verified | School system (`Person -> Student, Teacher`). Abstract `Shape` with `Rectangle` and `Square(Rectangle)`. Calling `super().__init__(side, side)`. MRO inspection. Dataclass `Point`. |
| **D10-15** | `WhatsApp Image 2026-11-19 at 20.20.56.jpeg` | Day 10 Official Quiz | Knowledge Check | Knowledge check | 5 MCQ Quiz | Verified | Official Day 10 Quiz: Q1 parent `__init__` call (**B**: `super().__init__()`), Q2 `D(B, C).go()` (**D**: `B.go`), Q3 `isinstance(B(), A)` (**A**: `True`), Q4 incomplete abstract method (**B**: `TypeError`), Q5 composition vs inheritance (**C**: `Car -> Engine`). |
| **D11-01** | `WhatsApp Image 2026-11-19 at 20.20.56KL.jpeg` | Day 11 Title Slide | Title / Slide 1 | Polymorphism, Overloading & OOP Design | `day11.py` | Verified | Week 2 • Day 11 (Thursday 19 Nov 2026). Domain 3: OOP (15%). Manual Day 12 (§12.1–12.6) + Day 13 (§13.1–13.5). `Money.__add__`. |
| **D11-02** | `WhatsApp Image 2026-11-19 at 20.20.56KJ.jpeg` | Day 11 Agenda & Objectives | Slide 2 | Today's objectives & agenda | — | Verified | 5 learning outcomes; syllabus mapping: 12.1 Duck typing, 12.2 Built-in polymorphism, 12.3 Operator overloading, 12.4 Function overloading, 12.5 `__slots__` vs `__dict__`, 13.1 SRP & constructors, 13.1 classmethod vs staticmethod, 13.2 Anti-patterns, 13.3 LSP & Singleton, 13.5 Python vs Java/C++, extra Decorators, Lab 11.1 Matrix class challenge. |
| **D11-03** | `WhatsApp Image 2026-11-19 at 20.20.57.jpeg` | Day 11 Duck Typing | Manual §12.1 | Polymorphism & duck typing | `duck.py` | Verified | Duck typing: *"If it walks like a duck and quacks like a duck..."* No common parent required. `Duck` and unrelated `Robot` both implement `speak()`. `total_length(["ab", [1, 2, 3], {"k": 1}])` summing `len(x)` $\rightarrow$ `6`. |
| **D11-04** | `WhatsApp Image 2026-11-19 at 20.20.57XS.jpeg`<br>`WhatsApp Image 2026-11-19 at 20.20.57IU.jpeg` | Day 11 Built-in Polymorphism | Manual §12.2 | Built-in polymorphism | Comparison Table | Verified | Operators adapting across Numbers, Strings, and Lists: `a + b`, `a * 3`, `len(x)` (`TypeError` on numbers), `x in y` (`TypeError` on numbers), `max(x)`. |
| **D11-05** | `WhatsApp Image 2026-11-19 at 20.20.58PO.jpeg` | Day 11 Operator Overloading | Manual §12.3 | Operator overloading | `vector.py` | Verified | Dunder operator mapping (`__add__`, `__mul__`, `__eq__`, `__lt__`, `__abs__`, `__repr__`). Returning new objects (immutability of operands). Reflected operators `__rmul__` for `2 * v`. `@total_ordering` decorator. |
| **D11-06** | `WhatsApp Image 2026-11-19 at 20.20.59.jpeg` | Day 11 Function Overloading | Manual §12.4 | Function overloading in Python | `overloading.py` | Verified | No native function overloading (re-definition overwrites previous). Simulation via default arguments (`b=None`). Single dispatch via `functools.singledispatch` and `@describe.register`. |
| **D11-07** | `WhatsApp Image 2026-11-19 at 20.20.59IY.jpeg` | Day 11 `__slots__` & Data Hiding | Manual §12.5 | Data hiding with `__slots__` and `__dict__` | `slots.py` | Verified | `__slots__ = ("x", "y")` removes per-instance `__dict__`. Restricts attribute creation (`AttributeError` on `p.z = 3`). Saves memory and blocks typos (`p.xx = 5`). `hasattr(p, "__dict__") is False`. |
| **D11-08** | `WhatsApp Image 2026-11-19 at 20.21.01.jpeg` | Day 11 Clean Design & SRP | Manual §13.1 | Class design: SRP & constructor best practices | `design.py` | Verified | Single Responsibility Principle (SRP): one reason to change. `Customer` constructor validates early via `_validate_email()`. Raises `ValueError` rather than creating broken state. |

---

## 2. Verbatim Classroom Code Extractions

### 2.1 Day 10 Multiple Inheritance & MRO: `mro.py` `[Course: D10-08]`
```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

print(D().hello())                             # B
print([k.__name__ for k in D.__mro__])        # ['D', 'B', 'C', 'A', 'object']
```

### 2.2 Day 10 Constructor Lifecycle & Cross-Hierarchy Private State: `construct.py` `[Course: D10-10]`
```python
class Base:
    def __new__(cls, *args):
        print("1. __new__ creates")
        return super().__new__(cls)

    def __init__(self):
        print("2. __init__ initialises")
        self.__secret = "base"                 # stored as _Base__secret
        self.setup()                           # dispatches to the child!

    def setup(self):
        print("Base.setup")


class Child(Base):
    def __init__(self):
        Base.__init__(self)                   # explicit parent call

    def setup(self):
        print("Child.setup")


c = Child()
# 1. __new__ creates
# 2. __init__ initialises
# Child.setup
print(c._Base__secret)                        # base
```

### 2.3 Day 10 Abstract Base Classes: `abstract.py` `[Course: D10-11]`
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """..."""

    def describe(self):
        return f"Area = {self.area()}"


class Rect(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


print(Rect(2, 3).describe())                  # Area = 6
# Shape() -> TypeError: Can't instantiate abstract class
```

### 2.4 Day 10 Dataclasses: `dataclasses_demo.py` `[Course: D10-13]`
```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Point:
    x: int
    y: int = 0


@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)


p = Point(1, 2)
print(p)                                      # Point(x=1, y=2)
print(p == Point(1, 2))                       # True
print(Point(1) < Point(2))                    # True
print(Team("A"))                              # Team(name='A', members=[])
```

### 2.5 Day 10 Lab 10.1: Shape Hierarchy: `hierarchy.py` `[Course: D10-14]`
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


print(Square(4).area())                       # 16
print([c.__name__ for c in Square.__mro__])    # ['Square', 'Rectangle', 'Shape', 'ABC', 'object']
```

### 2.6 Day 11 Title Snippet: `day11.py` `[Course: D11-01]`
```python
class Money:
    def __init__(self, amt):
        self.amt = amt

    def __add__(self, other):
        return Money(self.amt + other.amt)


print((Money(5) + Money(7)).amt)             # 12
```

### 2.7 Day 11 Duck Typing: `duck.py` `[Course: D11-03]`
```python
class Duck:
    def speak(self):
        return "Quack"


class Robot:                                   # unrelated class!
    def speak(self):
        return "Beep"


for thing in [Duck(), Robot()]:
    print(thing.speak())
# Quack
# Beep

def total_length(items):
    return sum(len(x) for x in items)

print(total_length(["ab", [1, 2, 3], {"k": 1}])) # 6
```

### 2.8 Day 11 Operator Overloading: `vector.py` `[Course: D11-05]`
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __rmul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v = Vector(1, 2) + Vector(3, 4)
print(v, v * 2)                               # Vector(4, 6) Vector(8, 12)
print(v == Vector(4, 6), Vector(1, 1) < v)    # True True
```

### 2.9 Day 11 Function Overloading Simulation & Single Dispatch: `overloading.py` `[Course: D11-06]`
```python
def area(r):
    return 3.14 * r * r

def area(w, h):                               # replaces the first one!
    return w * h
# area(2) -> TypeError: missing argument 'h'

def area(a, b=None):                          # simulate with a default
    return 3.14 * a * a if b is None else a * b

print(area(2), area(2, 3))                    # 12.56 6

from functools import singledispatch

@singledispatch
def describe(x):
    return "something"

@describe.register
def _(x: int):
    return "an int"

@describe.register
def _(x: list):
    return f"a list of {len(x)}"

print(describe(5), describe([1, 2]), describe(2.5))
# an int a list of 2 something
```

### 2.10 Day 11 Data Hiding & Memory Optimization: `slots.py` `[Course: D11-07]`
```python
class Free:
    pass

class Fixed:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

f = Free()
f.anything = 1
print(f.__dict__)                             # {'anything': 1}

p = Fixed(1, 2)
print(hasattr(p, "__dict__"))                 # False
try:
    p.z = 3
except AttributeError:
    print("AttributeError")                   # AttributeError
print(p.__class__.__name__)                   # Fixed
```

### 2.11 Day 11 Clean Class Design & SRP: `design.py` `[Course: D11-08]`
```python
class Customer:
    def __init__(self, name, email, phone=None):
        self._validate_email(email)
        self.name = name
        self.email = email
        self.phone = phone

    def _validate_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email address")


c = Customer("Ada", "ada@bcpd.org")
print(c.name, c.phone)                        # Ada None
try:
    Customer("Bo", "bo.example.com")
except ValueError as e:
    print(e)                                  # Invalid email address
```

---

## 3. Official Classroom Quiz Answer Key: Day 10 `[Course: D10-15]`

| Question # | Slide Prompt | Options | Correct Answer | Technical Explanation |
|:---:|---|---|:---:|---|
| **Q1** | Which call runs the parent's `__init__` from inside a child's `__init__`? | A) `parent.__init__()`<br>B) `super().__init__()`<br>C) `self.__init__()`<br>D) `base()` | **B** | `super().__init__()` dynamically resolves the proxy to the next class in the MRO and invokes its constructor with the current instance bound to `self`. |
| **Q2** | With `class D(B, C)` where B and C both define `go()`, `D().go()` runs... | A) Both<br>B) `C.go`<br>C) Error<br>D) `B.go` | **D** | In multiple inheritance, C3 Linearization checks base classes left to right according to the class definition `(B, C)`. Therefore, `B` is checked before `C`. |
| **Q3** | Given `class A: pass` and `class B(A): pass`, what is `isinstance(B(), A)`? | A) `True`<br>B) `False`<br>C) `None`<br>D) `Error` | **A** | `isinstance(obj, Cls)` checks whether `obj` is an instance of `Cls` or any derived subclass of `Cls`. Since `B` derives from `A`, `isinstance(B(), A)` is `True`. |
| **Q4** | What happens if you instantiate a class with an unimplemented `@abstractmethod`? | A) It returns `None`<br>B) `TypeError` is raised<br>C) A warning is printed<br>D) It works normally | **B** | Python's `ABCMeta` intercepts instantiation at `__call__` time and raises `TypeError: Can't instantiate abstract class with abstract methods`. |
| **Q5** | Which relationship should use composition rather than inheritance? | A) `Dog -> Animal`<br>B) `Manager -> Employee`<br>C) `Car -> Engine`<br>D) `Square -> Shape` | **C** | A Car *has an* Engine (HAS-A relationship), whereas Dog is an Animal, Manager is an Employee, and Square is a Shape (IS-A relationships). HAS-A relationships should always use composition. |
