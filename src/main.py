import argparse
import sys

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--phase-file", required=True)
    _ = p.parse_args()

    print("BLOCKED: not implemented")
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
