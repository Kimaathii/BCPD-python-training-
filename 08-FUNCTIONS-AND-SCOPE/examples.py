"""
Module 08: Functions, Scope, and Parameter Mechanics â€” Executable Examples
BCPD Python Cohort 2 Certification Preparation

Topic Classification: [Agenda-Mapped / Supplementary â€” slides pending] (IMG-75)
Topics:
  - Function definitions, parameter types, default values
  - The mutable default argument trap (buggy vs idiomatic)
  - Variable arguments (*args, **kwargs) and unpacking
  - Positional-only (/) and keyword-only (*) parameters
  - LEGB scoping rules, global, nonlocal, and UnboundLocalError
  - First-class functions, lambdas, closures
"""

# ==============================================================================
# 1. Parameter Mechanics & Mutable Default Trap
# ==============================================================================

def buggy_accumulator(item, collection=[]):
    """BUGGY: collection is shared across calls!"""
    collection.append(item)
    return collection


def idiomatic_accumulator(item, collection=None):
    """CORRECT: Default None with internal instantiation creates a fresh list."""
    if collection is None:
        collection = []
    collection.append(item)
    return collection


def demo_default_argument_trap():
    # Demonstrating the trap
    first = buggy_accumulator("a")
    second = buggy_accumulator("b")
    # Because collection=[] was evaluated once at def time, both calls modified the SAME list!
    assert first is second
    assert first == ["a", "b"]

    # Demonstrating the fix
    safe1 = idiomatic_accumulator("a")
    safe2 = idiomatic_accumulator("b")
    assert safe1 is not safe2
    assert safe1 == ["a"]
    assert safe2 == ["b"]


# ==============================================================================
# 2. Variable Arguments (*args, **kwargs) and Parameter Modifiers (/, *)
# ==============================================================================

def format_report(title: str, *sections, status: str = "DRAFT", **metadata) -> dict:
    """Combines positional, *args (tuple), keyword-only, and **kwargs (dict)."""
    assert isinstance(sections, tuple)
    assert isinstance(metadata, dict)
    return {
        "title": title,
        "sections": sections,
        "status": status,
        "metadata": metadata,
    }


def strict_signature(pos_only, /, standard, *, kw_only):
    """Demonstrates PEP 570 positional-only and PEP 3102 keyword-only parameters."""
    return f"{pos_only}-{standard}-{kw_only}"


def demo_parameter_mechanics():
    rep = format_report("Sprint Review", "Intro", "Demo", "Retro", status="FINAL", author="Kimat", week=1)
    assert rep["title"] == "Sprint Review"
    assert rep["sections"] == ("Intro", "Demo", "Retro")
    assert rep["status"] == "FINAL"
    assert rep["metadata"] == {"author": "Kimat", "week": 1}

    # Strict signature calls
    res = strict_signature(1, 2, kw_only=3)
    assert res == "1-2-3"
    res2 = strict_signature(1, standard=2, kw_only=3)
    assert res2 == "1-2-3"

    # Positional-only parameter cannot be passed by keyword:
    try:
        strict_signature(pos_only=1, standard=2, kw_only=3)  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError:
        pass

    # Keyword-only parameter cannot be passed positionally:
    try:
        strict_signature(1, 2, 3)  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


# ==============================================================================
# 3. LEGB Scope Rules, global, nonlocal, and UnboundLocalError
# ==============================================================================

GLOBAL_COUNTER = 0

def increment_global():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1


def make_counter(start: int = 0):
    """Closure demonstrating nonlocal binding in enclosing scope."""
    val = start
    def step():
        nonlocal val
        val += 1
        return val
    return step


def demo_scope_and_closures():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER = 0
    increment_global()
    increment_global()
    assert GLOBAL_COUNTER == 2

    # Closure
    c1 = make_counter(10)
    c2 = make_counter(100)
    assert c1() == 11
    assert c1() == 12
    assert c2() == 101

    # UnboundLocalError Demonstration
    flag = True
    def trigger_unbound_error():
        # Referencing flag before assignment raises UnboundLocalError
        # because the assignment 'flag = False' makes flag local to this function!
        try:
            if flag:
                pass
            flag = False
        except UnboundLocalError:
            return "Caught Expected UnboundLocalError"
        return "Not Caught"

    assert trigger_unbound_error() == "Caught Expected UnboundLocalError"


# ==============================================================================
# 4. First-Class Functions, Lambdas, and Higher-Order Tools
# ==============================================================================

def demo_first_class_and_lambdas():
    # Lambdas for sorting keys
    students = [("Bob", 82), ("Alice", 95), ("Charlie", 74)]
    by_score = sorted(students, key=lambda s: s[1], reverse=True)
    assert by_score == [("Alice", 95), ("Bob", 82), ("Charlie", 74)]

    # Higher-order map and filter
    nums = [1, 2, 3, 4, 5, 6]
    evens_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
    assert evens_squared == [4, 16, 36]


# ==============================================================================
# 5. Day 5 & Day 6 Verbatim Scripts: Functions, Recursion, Functional Tools [Course: D5-01 to D5-04, D6-06, D6-07, D6-10]
# ==============================================================================

def demo_day5_and_day6_verbatim_scripts():
    import sys
    from functools import reduce

    # 1. functions.py (D5-01 / Beyond Manual Slide 8)
    def area(width, height):
        """Return the area of a rectangle."""
        return width * height

    def greet(name):
        _ = f"Hi {name}"  # no return

    assert area(3, 4) == 12
    assert greet("Ada") is None
    assert area.__doc__ == "Return the area of a rectangle."

    # 2. defaults.py (D5-02 / Beyond Manual Slide 9)
    def add_item(item, basket=[]):
        basket.append(item)
        return basket

    assert add_item("apple") == ["apple"]
    assert add_item("pear") == ["apple", "pear"]

    def add_item_safe(item, basket=None):
        if basket is None:
            basket = []
        basket.append(item)
        return basket

    assert add_item_safe("apple") == ["apple"]
    assert add_item_safe("pear") == ["pear"]

    # 3. varargs.py (D5-03 / Beyond Manual Slide 10)
    def total(*args):
        return sum(args)

    def profile(name, **kwargs):
        return name, kwargs

    assert total(1, 2, 3) == 6
    assert total() == 0
    p_name, p_kw = profile("Ada", age=36, lang="py")
    assert p_name == "Ada" and p_kw == {"age": 36, "lang": "py"}
    nums = [4, 5]
    assert total(*nums) == 9
    opts = {"age": 20}
    b_name, b_kw = profile("Bo", **opts)
    assert b_name == "Bo" and b_kw == {"age": 20}

    # 4. scope.py (D5-04 / Beyond Manual Slide 11)
    g_x = "global"
    def outer():
        x = "enclosing"
        def inner():
            nonlocal x
            x = "changed"
        inner()
        return x

    assert outer() == "changed"
    assert g_x == "global"

    counter = 0
    def bump():
        nonlocal counter
        counter += 1

    bump()
    bump()
    assert counter == 2

    # 5. functional.py & lambdas.py (D6-06, D6-07 / Manual §7.4)
    fn_nums = [1, 2, 3, 4]
    assert list(map(lambda n: n ** 2, fn_nums)) == [1, 4, 9, 16]
    assert list(filter(lambda n: n % 2, fn_nums)) == [1, 3]
    assert reduce(lambda a, b: a * b, fn_nums) == 24
    assert list(map(str, fn_nums)) == ['1', '2', '3', '4']
    assert list(map(lambda a, b: a + b, [1, 2], [10, 20, 30])) == [11, 22]

    square = lambda x: x * x
    assert square(6) == 36

    def apply(func, value):
        return func(value)

    assert apply(str.upper, "hi") == "HI"
    assert apply(lambda n: n + 1, 9) == 10
    w_list = ["kiwi", "fig", "banana"]
    assert sorted(w_list, key=len) == ["fig", "kiwi", "banana"]
    assert max(w_list, key=len) == "banana"

    # 6. recursion.py (D6-10 / Beyond Manual Slide 10)
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    def digit_sum(n):
        return n if n < 10 else n % 10 + digit_sum(n // 10)

    assert factorial(5) == 120
    assert fib(10) == 55
    assert digit_sum(1234) == 10
    assert sys.getrecursionlimit() >= 1000


if __name__ == "__main__":
    print("Running Module 08 Executable Examples...")
    demo_default_argument_trap()
    demo_parameter_mechanics()
    demo_scope_and_closures()
    demo_first_class_and_lambdas()
    demo_day5_and_day6_verbatim_scripts()
    print("All Module 08 examples executed successfully!")
