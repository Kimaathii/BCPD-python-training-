"""
Module 06: Strings, Text Processing, and String Formatting â€” Executable Examples
BCPD Python Cohort 2 Certification Preparation

Source Screen Mappings:
  - IMG-01, IMG-02, IMG-04, IMG-05: String literals, escaping, multiline strings
  - IMG-52, IMG-57, IMG-58: Indexing, slicing, negative indexing, immutability
  - IMG-59/64, IMG-60, IMG-62/65: Core string methods (case, strip, split, join, search)
  - IMG-63, IMG-66: text_tools.py / car game state machine
  - IMG-68/72, IMG-69, IMG-73: String formatting (%, .format(), f-strings, format mini-language)
  - IMG-76: Character classification edge cases (isdecimal, isdigit, isnumeric)
"""

import sys


# ==============================================================================
# 1. String Literals, Escaping, Slicing [Course: IMG-01, IMG-02, IMG-52, IMG-57, IMG-58]
# ==============================================================================

def demo_literals_and_slicing():
    # Quotes and Escapes
    s1 = 'Single quotes allow "double quotes" inside'
    s2 = "Double quotes allow 'single quotes' inside"
    raw_path = r"C:\new_folder\test"  # \n and \t are preserved as literal chars
    
    assert "\\new_folder\\test" in raw_path
    assert s1 != s2

    # Multiline String
    multi = """Line 1
Line 2
Line 3"""
    assert len(multi.splitlines()) == 3

    # Slicing: s[start:stop:step]
    text = "Python Programming"
    assert text[0] == "P"
    assert text[-1] == "g"
    assert text[0:6] == "Python"
    assert text[:6] == "Python"
    assert text[7:] == "Programming"
    assert text[::2] == "Pto rgamn"
    assert text[::-1] == "gnimmargorP nohtyP"  # Reversal idiom

    # Slice out of bounds does NOT raise IndexError (Crucial Exam Rule!)
    assert text[100:200] == ""
    assert text[-50:6] == "Python"

    # Direct indexing out of bounds DOES raise IndexError
    try:
        _ = text[100]
        assert False, "Should have raised IndexError"
    except IndexError:
        pass

    # Immutability verification
    try:
        # text[0] = "J" # TypeError
        text.__setitem__(0, "J")
        assert False, "Should have raised AttributeError or TypeError"
    except (AttributeError, TypeError):
        pass


# ==============================================================================
# 2. Core String Methods [Course: IMG-59/64, IMG-60, IMG-62/65]
# ==============================================================================

def demo_string_methods():
    msg = "  bcpd python cohort  "
    
    # Case manipulations
    assert msg.strip().title() == "Bcpd Python Cohort"
    assert "it's time".title() == "It'S Time"  # Apostrophe trap
    assert "python".capitalize() == "Python"
    assert "PyThOn".swapcase() == "pYtHoN"

    # Stripping
    assert msg.strip() == "bcpd python cohort"
    assert msg.lstrip() == "bcpd python cohort  "
    assert msg.rstrip() == "  bcpd python cohort"
    assert "www.example.com".strip("w.moc") == "example"  # Chars set trap!

    # Searching: find vs index
    sample = "The quick brown fox jumps over the lazy dog"
    assert sample.find("fox") == 16
    assert sample.find("unicorn") == -1  # find returns -1 when absent
    
    try:
        sample.index("unicorn")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # index raises ValueError when absent

    # Prefix and Suffix
    assert sample.startswith("The")
    assert sample.startswith(("A", "An", "The"))  # Tuple of prefixes
    assert sample.endswith("dog")

    # Splitting and Joining
    csv_line = "apple,banana,orange,grape"
    fruits = csv_line.split(",")
    assert fruits == ["apple", "banana", "orange", "grape"]
    
    rejoined = " | ".join(fruits)
    assert rejoined == "apple | banana | orange | grape"

    # join() raises TypeError on non-string items
    try:
        "-".join([1, 2, 3])  # type: ignore
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


# ==============================================================================
# 3. Character Classification: is... Family [Course: IMG-76, IMG-52]
# ==============================================================================

def demo_character_classification():
    # Regular ascii digits
    d = "12345"
    assert d.isdecimal() and d.isdigit() and d.isnumeric()

    # Unicode superscript (e.g., 'Â²' = \u00b2)
    sq = "Â²"
    assert not sq.isdecimal()
    assert sq.isdigit()
    assert sq.isnumeric()

    # Unicode vulgar fraction (e.g., 'Â½' = \u00bd)
    half = "Â½"
    assert not half.isdecimal()
    assert not half.isdigit()
    assert half.isnumeric()  # Vulgar fraction is numeric!

    # Negative numbers and decimals are NOT numeric by method definition
    neg = "-42"
    flt = "3.14"
    assert not neg.isdigit() and not neg.isnumeric() and not neg.isdecimal()
    assert not flt.isdigit() and not flt.isnumeric() and not flt.isdecimal()

    # Identifiers
    assert "valid_var_123".isidentifier()
    assert not "123_invalid".isidentifier()
    assert not "invalid-hyphen".isidentifier()


# ==============================================================================
# 4. String Formatting Evolution [Course: IMG-68/72, IMG-69, IMG-73]
# ==============================================================================

def demo_string_formatting():
    name = "Kimat"
    score = 98.546
    cohort = 2

    # Generation 1: % formatting
    g1 = "Hello %s, score: %.1f in Cohort %03d" % (name, score, cohort)
    assert g1 == "Hello Kimat, score: 98.5 in Cohort 002"

    # Generation 2: str.format()
    g2 = "Hello {}, score: {:.1f} in Cohort {:03d}".format(name, score, cohort)
    g2_kw = "Hello {n}, score: {s:.1f}".format(n=name, s=score)
    assert g2 == "Hello Kimat, score: 98.5 in Cohort 002"
    assert g2_kw == "Hello Kimat, score: 98.5"

    # Generation 3: f-strings
    g3 = f"Hello {name}, score: {score:.1f} in Cohort {cohort:03d}"
    assert g3 == "Hello Kimat, score: 98.5 in Cohort 002"

    # Format Mini-Language Demos
    val = 42
    assert f"{val:>8}" == "      42"
    assert f"{val:<8}" == "42      "
    assert f"{val:^8}" == "   42   "
    assert f"{val:*^8}" == "***42***"
    assert f"{val:+06d}" == "+00042"
    assert f"{1000000:,}" == "1,000,000"
    assert f"{1000000:_}" == "1_000_000"
    assert f"{255:#x}" == "0xff"
    assert f"{255:#X}" == "0XFF"
    assert f"{255:#b}" == "0b11111111"
    assert f"{0.852:.1%}" == "85.2%"


# ==============================================================================
# 5. Day 4 Practical Lab 4.1: Car Game / text_tools.py [Course: IMG-66, IMG-63]
# ==============================================================================

def run_car_game_simulation(command_list: list[str]) -> list[str]:
    """
    Simulates the car game state machine without requiring blocking interactive input.
    Provides the exact logic shown in IMG-66 with duplicate start/stop prevention.
    """
    logs = []
    started = False
    
    for raw_cmd in command_list:
        cmd = raw_cmd.strip().lower()
        if cmd == "start":
            if started:
                logs.append("Car is already started!")
            else:
                started = True
                logs.append("Car started...")
        elif cmd == "stop":
            if not started:
                logs.append("Car is already stopped!")
            else:
                started = False
                logs.append("Car stopped.")
        elif cmd == "help":
            logs.append("start - to start\nstop - to stop\nquit - to quit")
        elif cmd == "quit":
            logs.append("Game quit.")
            break
        else:
            logs.append("Sorry, I don't understand that!")
            
    return logs


def demo_car_game_state_machine():
    # Test valid sequence: start -> duplicate start -> stop -> duplicate stop -> help -> quit
    cmds = ["start", "start", "stop", "stop", "help", "invalid_cmd", "quit"]
    output = run_car_game_simulation(cmds)
    
    expected = [
        "Car started...",
        "Car is already started!",
        "Car stopped.",
        "Car is already stopped!",
        "start - to start\nstop - to stop\nquit - to quit",
        "Sorry, I don't understand that!",
        "Game quit."
    ]
    assert output == expected, f"State machine error:\nExpected: {expected}\nGot: {output}"


if __name__ == "__main__":
    print("Running Module 06 Executable Examples...")
    demo_literals_and_slicing()
    demo_string_methods()
    demo_character_classification()
    demo_string_formatting()
    demo_car_game_state_machine()
    print("All Module 06 examples executed successfully!")
