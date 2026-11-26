"""
Master Test Runner for BCPD Python Certification Preparation System
Target: Python 3.10+ (Verified on Python 3.15.2)

Discovers and executes all executable examples and reference solutions across all modules.
"""

import importlib.util
import os
import sys
import time
from pathlib import Path


def run_script(file_path: Path) -> tuple[bool, str]:
    """Execute a Python file in an isolated namespace and capture outcome."""
    start_time = time.time()
    module_name = f"test_{file_path.stem}_{int(start_time * 1000)}"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        return False, f"Could not load spec for {file_path}"
    
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    
    try:
        spec.loader.exec_module(module)
        if hasattr(module, "main") and callable(module.main):
            module.main()
        elif hasattr(module, "test_exercises") and callable(module.test_exercises):
            module.test_exercises()
        elapsed = time.time() - start_time
        return True, f"PASSED ({elapsed:.3f}s)"
    except Exception as e:
        elapsed = time.time() - start_time
        return False, f"FAILED ({elapsed:.3f}s): {type(e).__name__}: {e}"
    finally:
        sys.modules.pop(module_name, None)


def main():
    root_dir = Path(__file__).resolve().parent
    print("=" * 70)
    print(" BCPD Python Certification â€” System Verification Suite")
    print(f" Python Version: {sys.version.split()[0]} ({sys.executable})")
    print(f" Root Directory: {root_dir}")
    print("=" * 70)

    # 1. Discover all example, exercise, trap verification, and solution scripts
    examples = sorted(root_dir.glob("*/examples.py"))
    exercises = sorted(root_dir.glob("*/exercises.py"))
    traps = [root_dir / "10-EXAM-PREPARATION" / "traps_verification.py"]
    functional_tests = [root_dir / "10-EXAM-PREPARATION" / "functional_mastery.py"]
    solutions = sorted((root_dir / "10-EXAM-PREPARATION" / "solutions").glob("*.py"))
    test_files = examples + exercises + traps + functional_tests + solutions

    print(f"\nDiscovered {len(test_files)} executable suites:")
    print(f"  - {len(examples)} module example suites")
    print(f"  - {len(exercises)} module exercise suites")
    print(f"  - {len(traps)} master exam traps verification suite")
    print(f"  - {len(functional_tests)} functional programming mastery suite")
    print(f"  - {len(solutions)} exercise solution suites\n")

    passed = 0
    failed = 0

    for idx, path in enumerate(test_files, 1):
        rel_path = path.relative_to(root_dir)
        print(f"[{idx:02d}/{len(test_files):02d}] Running {rel_path} ... ", end="", flush=True)
        ok, msg = run_script(path)
        if ok:
            print(f"[OK] {msg}")
            passed += 1
        else:
            print(f"[ERROR] {msg}")
            failed += 1

    print("\n" + "=" * 70)
    print(f" Final Result: {passed} Passed, {failed} Failed out of {len(test_files)} suites.")
    print("=" * 70)

    if failed > 0:
        sys.exit(1)
    else:
        print("\nAll BCPD Python preparation examples and solutions verified cleanly!")


if __name__ == "__main__":
    main()
