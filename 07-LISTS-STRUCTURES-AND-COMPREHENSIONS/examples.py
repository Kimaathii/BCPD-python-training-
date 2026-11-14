"""
Module 07: Lists, Data Structures, and Comprehensions â€” Executable Examples
BCPD Python Cohort 2 Certification Preparation

Source Screen Mappings:
  - IMG-03, IMG-53, IMG-54, IMG-61: List creation, indexing, slicing, mutation
  - IMG-67, IMG-70: List methods and None return trap
  - IMG-70, IMG-74: 2D list reference trap vs list comprehension
  - IMG-70, IMG-77: Sequence unpacking (PEP 3132) and queues
  - IMG-74, IMG-78: Object references, aliasing, shallow vs deep copy
  - IMG-71, IMG-74, IMG-78, IMG-79: List, dict, set comprehensions & generators
  - IMG-75, IMG-77: Tuples, dictionaries, and sets
"""

import copy
import sys
from collections import deque


# ==============================================================================
# 1. List Indexing, Slicing, and Mutability [Course: IMG-03, IMG-53, IMG-54, IMG-61]
# ==============================================================================

def demo_list_basics():
    items = [10, 20, 30, 40, 50]
    
    # 0-based and -1 based indexing
    assert items[0] == 10
    assert items[-1] == 50
    assert items[1:4] == [20, 30, 40]
    assert items[::-1] == [50, 40, 30, 20, 10]

    # Slice assignment
    items[1:3] = [99, 88, 77]
    assert items == [10, 99, 88, 77, 40, 50]

    # Slice deletion
    items[1:4] = []
    assert items == [10, 40, 50]


# ==============================================================================
# 2. List Methods and the None-Return Trap [Course: IMG-67, IMG-70]
# ==============================================================================

def demo_list_methods_and_traps():
    data = [5, 2, 8, 1, 9]

    # In-place sort returns None
    result = data.sort()
    assert result is None  # CRUCIAL TRAP: data.sort() returns None!
    assert data == [1, 2, 5, 8, 9]  # Mutated in place

    # Builtin sorted() returns a new list
    original = [4, 1, 3]
    sorted_copy = sorted(original)
    assert sorted_copy == [1, 3, 4]
    assert original == [4, 1, 3]  # Original untouched

    # In-place reverse returns None
    rev_res = data.reverse()
    assert rev_res is None
    assert data == [9, 8, 5, 2, 1]

    # append vs extend
    a = [1, 2]
    a.append([3, 4])
    assert a == [1, 2, [3, 4]]  # Appended as a single element

    b = [1, 2]
    b.extend([3, 4])
    assert b == [1, 2, 3, 4]    # Unpacked and extended

    # pop returns the element
    popped = b.pop()
    assert popped == 4
    assert b == [1, 2, 3]


# ==============================================================================
# 3. 2D List Reference Trap vs Comprehension [Course: IMG-70, IMG-74]
# ==============================================================================

def demo_grid_reference_trap():
    # BUGGY INITIALIZATION: All rows reference the SAME inner list object!
    buggy_grid = [[0] * 3] * 3
    buggy_grid[0][0] = 99
    # Every row's first column became 99 because all rows are identical references:
    assert buggy_grid == [[99, 0, 0], [99, 0, 0], [99, 0, 0]]
    assert buggy_grid[0] is buggy_grid[1] is buggy_grid[2]

    # CORRECT INITIALIZATION: Using list comprehension
    correct_grid = [[0] * 3 for _ in range(3)]
    correct_grid[0][0] = 99
    # Only the first row changed:
    assert correct_grid == [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert correct_grid[0] is not correct_grid[1]


# ==============================================================================
# 4. Sequence Unpacking and Queues [Course: IMG-70, IMG-77]
# ==============================================================================

def demo_unpacking_and_queues():
    # Star Unpacking (PEP 3132)
    nums = [1, 2, 3, 4, 5, 6]
    first, *middle, last = nums
    assert first == 1
    assert middle == [2, 3, 4, 5]
    assert last == 6

    # Swapping idiom
    x, y = 10, 20
    x, y = y, x
    assert x == 20 and y == 10

    # Deque for O(1) FIFO queue
    q = deque(["first", "second", "third"])
    q.append("fourth")
    assert q.popleft() == "first"
    assert q.pop() == "fourth"


# ==============================================================================
# 5. Aliasing, Shallow Copies, and Deep Copies [Course: IMG-74, IMG-78]
# ==============================================================================

def demo_copies():
    orig = [1, [2, 3]]
    
    # Alias
    alias = orig
    assert alias is orig

    # Shallow Copy
    shallow = orig.copy()
    assert shallow is not orig
    assert shallow[1] is orig[1]  # Inner list is shared!
    shallow[1].append(4)
    assert orig[1] == [2, 3, 4]   # Mutation reflected in orig!

    # Deep Copy
    deep = copy.deepcopy(orig)
    assert deep is not orig
    assert deep[1] is not orig[1]  # Inner list is completely distinct!
    deep[1].append(5)
    assert orig[1] == [2, 3, 4]    # Orig unaffected!


# ==============================================================================
# 6. Comprehensions & Generator Expressions [Course: IMG-71, IMG-74, IMG-78, IMG-79]
# ==============================================================================

def demo_comprehensions():
    # List comprehension
    evens_squared = [x ** 2 for x in range(10) if x % 2 == 0]
    assert evens_squared == [0, 4, 16, 36, 64]

    # Flattening nested list
    matrix = [[1, 2], [3, 4], [5, 6]]
    flattened = [val for row in matrix for val in row]
    assert flattened == [1, 2, 3, 4, 5, 6]

    # Dict comprehension
    words = ["apple", "bat", "carrot"]
    word_lens = {w: len(w) for w in words}
    assert word_lens == {"apple": 5, "bat": 3, "carrot": 6}

    # Set comprehension
    nums = [1, 2, 2, 3, 3, 3]
    unique_mod = {x % 2 for x in nums}
    assert unique_mod == {0, 1}

    # Generator Expression vs List Comprehension
    gen = (x * 2 for x in range(5))
    eager = [x * 2 for x in range(5)]
    
    # Generator memory is tiny compared to eager list
    big_list = [x for x in range(10000)]
    assert sys.getsizeof(gen) < 300  # Generator is ~200 bytes
    assert sys.getsizeof(big_list) > 80000  # Eager list is > 80 KB

    # Exhaustion rule:
    consumed_once = list(gen)
    assert consumed_once == [0, 2, 4, 6, 8]
    consumed_twice = list(gen)
    assert consumed_twice == []  # Completely exhausted!


# ==============================================================================
# 7. Tuples, Dictionaries, Sets [Course: IMG-75, IMG-77] [Supplementary]
# ==============================================================================

def demo_tuples_dicts_sets():
    # Singleton tuple
    not_tuple = (50)
    assert isinstance(not_tuple, int)
    is_tuple = (50,)
    assert isinstance(is_tuple, tuple)

    # Dictionary safe retrieval
    config = {"host": "localhost", "port": 8080}
    assert config.get("timeout", 30) == 30
    assert config.get("host") == "localhost"

    # Set operations
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    assert s1 & s2 == {3, 4}          # Intersection
    assert s1 | s2 == {1, 2, 3, 4, 5, 6}  # Union
    assert s1 - s2 == {1, 2}          # Difference
    assert s1 ^ s2 == {1, 2, 5, 6}    # Symmetric Difference


# ==============================================================================
# 8. Day 6 Verbatim Scripts: Sorting, Combining, Gotchas & Complexity [Course: D6-01 to D6-09]
# ==============================================================================

def demo_day6_verbatim_scripts():
    # 1. sorting.py (D6-02 / Manual §7.1)
    nums = [5, 2, 9, 1]
    sorted_res = sorted(nums)
    assert sorted_res == [1, 2, 5, 9]
    assert nums == [5, 2, 9, 1]
    assert nums.sort() is None
    assert nums == [1, 2, 5, 9]

    words = ["Pear", "apple", "fig"]
    assert sorted(words) == ["Pear", "apple", "fig"]  # ASCII 'P' < 'a'
    assert sorted(words, key=str.lower) == ["apple", "fig", "Pear"]

    people = [("Bo", 25), ("Ada", 36), ("Cy", 25)]
    # Stable sorting preserves relative order of "Bo" before "Cy"
    assert sorted(people, key=lambda p: p[1]) == [("Bo", 25), ("Cy", 25), ("Ada", 36)]

    # 2. combine.py (D6-03 / Manual §7.2)
    assert ([1, 2, 3] < [1, 3]) is True
    assert ([2] > [1, 9]) is True

    def grow(lst):
        lst += [4]      # in place: caller sees it

    def rebuild(lst):
        lst = lst + [5] # new list: caller doesn't

    a = [1]
    grow(a)
    rebuild(a)
    assert a == [1, 4]

    # Flattening one level with sum(list_of_lists, [])
    assert sum([[1, 2], [3]], []) == [1, 2, 3]

    # zip iterator
    z = zip("ab", [1, 2, 3])
    assert list(z) == [('a', 1), ('b', 2)]

    # Unpacking into arguments
    import io
    buf = io.StringIO()
    print(*[1, 2, 3], sep="-", file=buf)
    assert buf.getvalue().strip() == "1-2-3"

    ins_nums = [5, 9]
    ins_nums.insert(ins_nums.index(9), 7)
    assert ins_nums == [5, 7, 9]

    # 3. comprehensions.py (D6-04 / Manual §7.3)
    c_nums = [3, -1, 4, -2]
    assert [n * 2 for n in c_nums] == [6, -2, 8, -4]
    assert [n for n in c_nums if n > 0] == [3, 4]
    assert [n if n > 0 else 0 for n in c_nums] == [3, 0, 4, 0]
    assert [(x, y) for x in "ab" for y in (1, 2)] == [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

    matrix = [[i * j for j in range(1, 4)] for i in range(1, 3)]
    assert matrix == [[1, 2, 3], [2, 4, 6]]
    transpose = [[row[i] for row in matrix] for i in range(3)]
    assert transpose == [[1, 2], [2, 4], [3, 6]]

    # 4. gotchas.py (D6-05 / Manual §7.3–7.4)
    g_nums = [1, 2, 3]
    try:
        "-".join(g_nums)  # type: ignore
        assert False, "Should raise TypeError"
    except TypeError:
        pass
    assert "-".join(map(str, g_nums)) == "1-2-3"

    m = map(str.upper, ["a", "b"])
    try:
        len(m)  # type: ignore
        assert False, "Should raise TypeError"
    except TypeError:
        pass
    assert list(m) == ['A', 'B']
    assert list(m) == []  # Map is consumed only once!

    assert list(map(list, ["ab", "c"])) == [['a', 'b'], ['c']]
    assert [n if n > 1 else 0 for n in g_nums] == [0, 2, 3]

    grid_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [grid_3x3[i][i] for i in range(3)] == [1, 5, 9]          # Main diagonal
    assert [grid_3x3[i][2 - i] for i in range(3)] == [3, 5, 7]      # Anti-diagonal


if __name__ == "__main__":
    print("Running Module 07 Executable Examples...")
    demo_list_basics()
    demo_list_methods_and_traps()
    demo_grid_reference_trap()
    demo_unpacking_and_queues()
    demo_copies()
    demo_comprehensions()
    demo_tuples_dicts_sets()
    demo_day6_verbatim_scripts()
    print("All Module 07 examples executed successfully!")
