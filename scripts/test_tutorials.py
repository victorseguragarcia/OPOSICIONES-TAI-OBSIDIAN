#!/usr/bin/env python3
"""
Tutorial Test Suite Runner
Validates that tutorials 01 through 06 are properly set up,
queries work as expected, and wiki linter passes with zero errors.
"""

import sys
import subprocess
from pathlib import Path

# Force UTF-8 on Windows stdout if possible
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent

def test_tutorials():
    print("=" * 60)
    print("[*] EXECUTING LLM WIKI TUTORIAL VALIDATION SUITE")
    print("=" * 60)

    # 1. Check tutorials 01 - 06 exist
    tutorials = [
        "01-raw-ingest.md",
        "02-entity-concept-extraction.md",
        "03-cross-referencing.md",
        "04-index-and-logging.md",
        "05-synthesis-and-filing.md",
        "06-query-and-lint.md",
    ]
    for tut in tutorials:
        tut_path = ROOT_DIR / "tutorials" / tut
        if not tut_path.exists():
            print(f"[X] Missing tutorial file: {tut}")
            return 1
        print(f"[OK] Verified tutorial present: {tut}")

    # 2. Test query functionality
    print("\n[*] Testing query execution...")
    res_query = subprocess.run([sys.executable, str(ROOT_DIR / "scripts" / "query.py"), "transformer"], capture_output=True, text=True, encoding="utf-8")
    if res_query.returncode != 0 or "Transformer Architecture" not in res_query.stdout:
        print(f"[X] Query test failed:\n{res_query.stderr}")
        return 1
    print("[OK] Query tool verified.")

    # 3. Test lint health check (Tutorial 06 pass criteria)
    print("\n[*] Running tutorial-06-query-and-lint health checks...")
    res_lint = subprocess.run([sys.executable, str(ROOT_DIR / "scripts" / "lint.py")], capture_output=True, text=True, encoding="utf-8")
    print(res_lint.stdout)
    if res_lint.returncode != 0:
        print(f"[X] Linter failed:\n{res_lint.stderr}")
        return 1

    print("=" * 60)
    print("[PASS] TUTORIAL-06-QUERY-AND-LINT COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(test_tutorials())
