"""Module 16: Modules Part 2 — Regular Expressions, time, datetime & Custom Modules.

Clean Reference Implementations & Comprehensive Solution Suite
Target: Python 3.10+ (Verified on Python 3.15.2)

Classroom Alignment: Manual Day 15 §15.1–15.4, Slides D14-01 to D14-07, Lab 14.1
"""

from __future__ import annotations

import re
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple


# ==============================================================================
# LEVEL 1: Basic Regex Validation & Date Instantiation
# ==============================================================================

def is_valid_hex_color(code: str) -> bool:
    """Validate 3-digit or 6-digit hex color strings (e.g. #FFF or #1A2B3C)."""
    pattern = r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
    return bool(re.fullmatch(pattern, code))


def create_exam_date(year: int, month: int, day: int) -> date:
    """Instantiate and return a valid date object with input bounds checking."""
    return date(year, month, day)


# ==============================================================================
# LEVEL 2: Group Extraction & timedelta Math
# ==============================================================================

def extract_key_value_pairs(log_line: str) -> List[Tuple[str, str]]:
    """Extract key=value tokens from a log string using capturing groups."""
    pattern = r"(\b\w+)=([^\s]+)"
    return re.findall(pattern, log_line)


def add_exam_buffer(start_dt: datetime, days: int, hours: int) -> datetime:
    """Add a calendar duration buffer using timedelta and return new datetime."""
    return start_dt + timedelta(days=days, hours=hours)


# ==============================================================================
# LEVEL 3: Named Capture & Lazy Tokenization
# ==============================================================================

def extract_html_tags(html: str) -> List[str]:
    """Extract all individual opening, closing, and self-closing HTML tags."""
    pattern = r"<.+?>"
    return re.findall(pattern, html)


def parse_semver(version_str: str) -> Optional[Dict[str, Any]]:
    """Parse Semantic Versioning string into components using named capture groups."""
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
        """Parse bank transaction SMS into normalized financial record."""
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


def main() -> None:
    # Level 1 verification
    assert is_valid_hex_color("#FFF") is True
    assert is_valid_hex_color("#12345") is False
    assert create_exam_date(2026, 12, 5).year == 2026

    # Level 2 verification
    pairs = extract_key_value_pairs("k1=v1 k2=v2")
    assert pairs == [("k1", "v1"), ("k2", "v2")]
    buffered = add_exam_buffer(datetime(2026, 12, 1, 0, 0), days=1, hours=2)
    assert buffered == datetime(2026, 12, 2, 2, 0)

    # Level 3 verification
    assert extract_html_tags("<a><b></b></a>") == ["<a>", "<b>", "</b>", "</a>"]
    sem = parse_semver("v1.2.3")
    assert sem == {"major": 1, "minor": 2, "patch": 3, "prerelease": None}

    # Level 4 verification
    assert Lab14Validator.validate_nigerian_phone("+2348012345678") is True
    sms = "Acct:***4521 DR: NGN5,000.00 Desc: POS/IKEJA Bal: NGN42,350.75"
    alert = Lab14Validator.parse_bank_alert(sms)
    assert alert is not None and alert["amount"] == 5000.0

    timer = ExamCountdownTimer("2026-12-05 09:00:00")
    rem = timer.get_remaining_time(datetime(2026, 12, 1, 9, 0, 0))
    assert rem["days"] == 4 and rem["is_expired"] is False

    print("Module 16 solutions self-test PASSED.")


if __name__ == "__main__":
    main()
