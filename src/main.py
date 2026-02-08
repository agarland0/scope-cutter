import argparse
from pathlib import Path
import sys

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--phase-file", required=True)
    args = p.parse_args()

    text = Path(args.phase_file).read_text(encoding="utf-8")

    # Temporary v0 wiring: if file contains both required headers, PASS.
    # We'll replace this with real Existence logic next.
    if "EXISTS TO" in text and "SHIPS AS" in text:
        print("PASS")
        return 0

    print("BLOCKED: missing required fields")
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
