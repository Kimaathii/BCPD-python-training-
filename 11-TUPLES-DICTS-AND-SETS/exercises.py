"""
Module 11: Tuples, Dictionaries & Sets — Progressive Practical Exercises
Course: BCPD Python Certification — Domain 2: Data Structures (15%)
Student Manual Reference: Day 8 (§8.1–8.8) + Day 9 (§9.1–9.9)
"""

from collections import Counter, defaultdict, namedtuple
from typing import Any, Dict, List, Set, Tuple


# ==============================================================================
# Level 1: Tuples, Unpacking & Named Tuples
# ==============================================================================
def create_student_record(name: str, grades: List[int]) -> Tuple[Any, ...]:
    """
    Creates an immutable student record containing (name, average_grade, letter_grade).
    Average grade is rounded to 1 decimal place.
    Letter grades: >=90: 'A', >=80: 'B', >=70: 'C', >=60: 'D', else: 'F'.
    If grades is empty, average is 0.0 and letter grade is 'F'.
    The return value must be a namedtuple 'StudentRecord' with fields ('name', 'avg', 'grade').
    """
    StudentRecord = namedtuple("StudentRecord", ["name", "avg", "grade"])
    if not grades:
        return StudentRecord(name=name, avg=0.0, grade="F")
    avg = round(sum(grades) / len(grades), 1)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return StudentRecord(name=name, avg=avg, grade=grade)


# ==============================================================================
# Level 2: Dictionary Manipulation & Collision-Resistant Inversion
# ==============================================================================
def invert_dictionary_multivalue(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """
    Inverts a dictionary mapping keys to values.
    Since multiple original keys may map to the same value,
    the resulting dictionary must map each unique value to a sorted list of its keys.

    Example:
        invert_dictionary_multivalue({"a": 1, "b": 2, "c": 1})
        -> {1: ['a', 'c'], 2: ['b']}
    """
    result: Dict[Any, List[Any]] = defaultdict(list)
    for k, v in d.items():
        result[v].append(k)
    return {k: sorted(v) for k, v in result.items()}


# ==============================================================================
# Level 3: Counter Arithmetic & Multiset Frequency Analyzer (Lab 8.1)
# ==============================================================================
def analyze_token_frequencies(text: str, top_k: int = 3) -> Tuple[List[Tuple[str, int]], int]:
    """
    Splits text by whitespace, normalizes each token to lowercase with punctuation
    stripped ('.', ',', '!', '?', ';', ':'), and returns:
    1. A list of (word, count) tuples for the top_k most common words.
    2. The total count of unique words in the text.
    """
    import string
    cleaned_words = [
        w.strip(string.punctuation).lower()
        for w in text.split()
        if w.strip(string.punctuation)
    ]
    counts = Counter(cleaned_words)
    return counts.most_common(top_k), len(counts)


# ==============================================================================
# Level 4: Set Algebra & Venn Classification Engine
# ==============================================================================
def classify_user_permissions(
    admin_perms: Set[str],
    user_perms: Set[str],
    guest_perms: Set[str]
) -> Dict[str, Set[str]]:
    """
    Performs set algebra across three permission profiles:
    - 'universal': permissions present in all three roles.
    - 'admin_exclusive': permissions present ONLY in admin_perms.
    - 'user_or_guest_only': permissions in user or guest, but NOT in admin.
    - 'all_unique_permissions': union of all permissions.
    """
    universal = admin_perms & user_perms & guest_perms
    admin_exclusive = admin_perms - (user_perms | guest_perms)
    user_or_guest_only = (user_perms | guest_perms) - admin_perms
    all_unique = admin_perms | user_perms | guest_perms

    return {
        "universal": universal,
        "admin_exclusive": admin_exclusive,
        "user_or_guest_only": user_or_guest_only,
        "all_unique_permissions": all_unique,
    }


# ==============================================================================
# Self-Verification Tests
# ==============================================================================
def test_exercises():
    # Test Level 1
    r = create_student_record("Ada", [95, 88, 92])
    assert r.name == "Ada"
    assert r.avg == 91.7
    assert r.grade == "A"
    assert r[0] == "Ada"

    # Test Level 2
    inv = invert_dictionary_multivalue({"a": 1, "b": 2, "c": 1})
    assert inv == {1: ["a", "c"], 2: ["b"]}

    # Test Level 3
    sample_text = "To be or not to be, that is the question: to be!"
    top, unique_cnt = analyze_token_frequencies(sample_text, top_k=2)
    assert top[0] == ("to", 3)
    assert top[1] == ("be", 3)
    # unique tokens: 'to', 'be', 'or', 'not', 'that', 'is', 'the', 'question' -> exactly 8
    assert unique_cnt == 8

    # Test Level 4
    admin = {"read", "write", "delete", "sudo"}
    user = {"read", "write", "comment"}
    guest = {"read"}
    analysis = classify_user_permissions(admin, user, guest)
    assert analysis["universal"] == {"read"}
    assert analysis["admin_exclusive"] == {"delete", "sudo"}
    assert analysis["user_or_guest_only"] == {"comment"}
    assert analysis["all_unique_permissions"] == {"read", "write", "delete", "sudo", "comment"}


if __name__ == "__main__":
    test_exercises()
    print("All Module 11 exercises PASSED verification tests.")
