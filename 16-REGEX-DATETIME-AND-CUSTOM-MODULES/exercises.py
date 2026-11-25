"""Module 16 Progressive Exercises & Lab 14.1.

Contains:
- Level 1: Basic Regex Validation & Date Instantiation
- Level 2: findall Group Extraction & timedelta Math
- Level 3: Named Capture Parsing & Lazy Regex Tokenization
- Level 4 (Lab 14.1): Robust Multi-Field Validator & Exam Countdown Timer
- Automated Test Harness (run directly: python exercises.py)
"""

from __future__ import annotations

import re
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple


# ==============================================================================
# LEVEL 1: Basic Regex Validation & Date Instantiation
# ==============================================================================

def is_valid_hex_color(code: str) -> bool:
    """Validate 3-digit or 6-digit hex color strings (e.g. #FFF or #1A2B3C).

    Must match entire string from start to finish.
    """
    pattern = r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
    return bool(re.fullmatch(pattern, code))


def create_exam_date(year: int, month: int, day: int) -> date:
    """Instantiate and return a valid date object with input bounds checking."""
    return date(year, month, day)


# ==============================================================================
# LEVEL 2: Group Extraction & timedelta Math
# ==============================================================================

def extract_key_value_pairs(log_line: str) -> List[Tuple[str, str]]:
    """Extract key=value tokens from a log string using capturing groups.

    Example: "user=ada status=200 error=None" -> [('user', 'ada'), ('status', '200'), ('error', 'None')]
    """
    pattern = r"(\b\w+)=([^\s]+)"
    return re.findall(pattern, log_line)


def add_exam_buffer(start_dt: datetime, days: int, hours: int) -> datetime:
    """Add a calendar duration buffer using timedelta and return new datetime."""
    return start_dt + timedelta(days=days, hours=hours)


# ==============================================================================
# LEVEL 3: Named Capture & Lazy Tokenization
# ==============================================================================

def extract_html_tags(html: str) -> List[str]:
    """Extract all individual opening, closing, and self-closing HTML tags.

    Must use lazy matching to prevent greedy swallowing across multiple tags!
    Example: "<div><p>Hello</p></div>" -> ['<div>', '<p>', '</p>', '</div>']
    """
    pattern = r"<.+?>"
    return re.findall(pattern, html)


def parse_semver(version_str: str) -> Optional[Dict[str, Any]]:
    """Parse Semantic Versioning string (e.g. 'v2.14.3-alpha') into components.

    Returns dict with keys: major, minor, patch (ints) and prerelease (str or None).
    """
    pattern = r"^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<prerelease>[\w.]+))?$"
    m = re.match(pattern, version_str)
    if not m:
        return None
    d = m.groupdict()
    return {
        "major": int(d["major"]),
        "minor": int(d["minor"]),
        "patch": int(d["patch"]),
        "prerelease": d["prerelease"],
    }


# ==============================================================================
# LEVEL 4: Lab 14.1 — Complete Validator Engine & Countdown Timer [Course: D14-01]
# ==============================================================================

class Lab14Validator:
    """Comprehensive input validation suite for Nigerian phone numbers, emails & Bank SMS."""

    @staticmethod
    def validate_nigerian_phone(phone: str) -> bool:
        """Validate Nigerian mobile numbers (+234... or 080/081/090/070...)."""
        clean = re.sub(r"[\s-]", "", phone)
        pattern = r"^(?:\+234|234|0)(?:70|80|81|90|91)\d{8}$"
        return bool(re.fullmatch(pattern, clean))

    @staticmethod
    def parse_bank_alert(sms: str) -> Optional[Dict[str, Any]]:
        """Parse bank transaction SMS into normalized financial record.

        Expected format:
        'Acct:***4521 DR: NGN5,000.00 Desc: POS/IKEJA Bal: NGN42,350.75'
        """
        pattern = (
            r"Acct:\s*\*{3}(?P<acct>\d{4})\s+"
            r"(?P<tx_type>DR|CR):\s*(?P<cur>[A-Z]{3})(?P<amount>[\d,]+\.\d{2})\s+"
            r"Desc:\s*(?P<desc>.+?)\s+"
            r"Bal:\s*(?P<bal_cur>[A-Z]{3})(?P<balance>[\d,]+\.\d{2})"
        )
        m = re.search(pattern, sms)
        if not m:
            return None
        res = m.groupdict()
        res["amount"] = float(res["amount"].replace(",", ""))
        res["balance"] = float(res["balance"].replace(",", ""))
        return res


class ExamCountdownTimer:
    """Precision exam countdown calculator using datetime and timedelta."""

    def __init__(self, target_exam_dt_str: str) -> None:
        self.target_dt = datetime.strptime(target_exam_dt_str, "%Y-%m-%d %H:%M:%S")

    def get_remaining_time(self, current_dt: Optional[datetime] = None) -> Dict[str, Any]:
        """Calculate remaining days, hours, minutes, and seconds until exam."""
        now = current_dt or datetime.now()
        delta = self.target_dt - now

        if delta.total_seconds() <= 0:
            return {
                "days": 0,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
                "total_seconds": 0.0,
                "is_expired": True,
            }

        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60

        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": delta.total_seconds(),
            "is_expired": False,
        }


# ==============================================================================
# AUTOMATED TEST HARNESS
# ==============================================================================

def test_level_1() -> None:
    assert is_valid_hex_color("#FFF") is True
    assert is_valid_hex_color("#1a2b3c") is True
    assert is_valid_hex_color("#12345") is False  # 5 digits invalid
    assert is_valid_hex_color("FFF") is False     # missing #
    assert is_valid_hex_color("#GGGGGG") is False # G invalid hex

    d = create_exam_date(2026, 12, 5)
    assert d.year == 2026 and d.month == 12 and d.day == 5
    print("Level 1 Tests: PASSED")


def test_level_2() -> None:
    pairs = extract_key_value_pairs("user=ada status=200 error=None")
    assert pairs == [("user", "ada"), ("status", "200"), ("error", "None")]

    start = datetime(2026, 11, 24, 10, 0, 0)
    buffered = add_exam_buffer(start, days=1, hours=4)
    assert buffered == datetime(2026, 11, 25, 14, 0, 0)
    print("Level 2 Tests: PASSED")


def test_level_3() -> None:
    tags = extract_html_tags("<div><p>Hello <b>World</b></p></div>")
    assert tags == ["<div>", "<p>", "<b>", "</b>", "</p>", "</div>"]

    sem = parse_semver("v2.14.3-alpha")
    assert sem == {"major": 2, "minor": 14, "patch": 3, "prerelease": "alpha"}

    sem_clean = parse_semver("1.0.0")
    assert sem_clean == {"major": 1, "minor": 0, "patch": 0, "prerelease": None}

    assert parse_semver("invalid.ver") is None
    print("Level 3 Tests: PASSED")


def test_level_4() -> None:
    # Phone validation
    assert Lab14Validator.validate_nigerian_phone("+2348012345678") is True
    assert Lab14Validator.validate_nigerian_phone("08012345678") is True
    assert Lab14Validator.validate_nigerian_phone("0801-234-5678") is True
    assert Lab14Validator.validate_nigerian_phone("0123456789") is False

    # Bank SMS Alert
    sms = "Acct:***4521 DR: NGN5,000.00 Desc: POS/IKEJA Bal: NGN42,350.75"
    alert = Lab14Validator.parse_bank_alert(sms)
    assert alert is not None
    assert alert["acct"] == "4521"
    assert alert["tx_type"] == "DR"
    assert alert["amount"] == 5000.0
    assert alert["desc"] == "POS/IKEJA"
    assert alert["balance"] == 42350.75

    # Countdown Timer
    timer = ExamCountdownTimer("2026-12-05 09:00:00")
    frozen_now = datetime(2026, 12, 1, 9, 0, 0)
    rem = timer.get_remaining_time(frozen_now)
    assert rem["days"] == 4
    assert rem["hours"] == 0
    assert rem["minutes"] == 0
    assert rem["seconds"] == 0
    assert rem["total_seconds"] == 4 * 86400.0
    assert rem["is_expired"] is False

    expired_rem = timer.get_remaining_time(datetime(2026, 12, 6, 10, 0, 0))
    assert expired_rem["is_expired"] is True
    print("Level 4 (Lab 14.1) Tests: PASSED")


def run_all_tests() -> None:
    test_level_1()
    test_level_2()
    test_level_3()
    test_level_4()
    print("\n" + "=" * 60)
    print("✅ ALL MODULE 16 EXERCISES & LAB 14.1 PASSED DETERMINISTICALLY")
    print("=" * 60)


def main() -> None:
    run_all_tests()


if __name__ == "__main__":
    main()
