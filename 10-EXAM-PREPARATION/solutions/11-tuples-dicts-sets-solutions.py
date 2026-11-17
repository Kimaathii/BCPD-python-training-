"""
Module 11 Solutions: Tuples, Dictionaries & Sets
Course: BCPD Python Certification — Domain 2: Data Structures (15%)
Student Manual Reference: Day 8 (§8.1–8.8) + Day 9 (§9.1–9.9)
"""

from collections import Counter, defaultdict, namedtuple
import string
from typing import Any, Dict, List, Set, Tuple


# ==============================================================================
# Solution 1: Tuples, Unpacking & Named Tuples
# ==============================================================================
StudentRecord = namedtuple("StudentRecord", ["name", "avg", "grade"])

def create_student_record_solution(name: str, grades: List[int]) -> StudentRecord:
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
# Solution 2: Dictionary Inversion Multivalue
# ==============================================================================
def invert_dictionary_multivalue_solution(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    result = defaultdict(list)
    for k, v in d.items():
        result[v].append(k)
    return {k: sorted(v) for k, v in result.items()}


# ==============================================================================
# Solution 3: Token Frequency Analyzer (Lab 8.1)
# ==============================================================================
def analyze_token_frequencies_solution(text: str, top_k: int = 3) -> Tuple[List[Tuple[str, int]], int]:
    cleaned_tokens = [
        word.strip(string.punctuation).lower()
        for word in text.split()
        if word.strip(string.punctuation)
    ]
    counts = Counter(cleaned_tokens)
    return counts.most_common(top_k), len(counts)


# ==============================================================================
# Solution 4: Set Algebra & Venn Classification Engine
# ==============================================================================
def classify_user_permissions_solution(
    admin_perms: Set[str],
    user_perms: Set[str],
    guest_perms: Set[str]
) -> Dict[str, Set[str]]:
    return {
        "universal": admin_perms & user_perms & guest_perms,
        "admin_exclusive": admin_perms - (user_perms | guest_perms),
        "user_or_guest_only": (user_perms | guest_perms) - admin_perms,
        "all_unique_permissions": admin_perms | user_perms | guest_perms,
    }


def main():
    rec = create_student_record_solution("Ada", [90, 95, 85])
    assert rec.avg == 90.0 and rec.grade == "A"

    inv = invert_dictionary_multivalue_solution({"x": 10, "y": 20, "z": 10})
    assert inv == {10: ["x", "z"], 20: ["y"]}

    top, total = analyze_token_frequencies_solution("One, two, two, three, three, three!", top_k=2)
    assert top == [("three", 3), ("two", 2)] and total == 3

    perms = classify_user_permissions_solution({"a", "b"}, {"a", "c"}, {"a"})
    assert perms["universal"] == {"a"}
    assert perms["admin_exclusive"] == {"b"}
    assert perms["user_or_guest_only"] == {"c"}
    print("Module 11 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
