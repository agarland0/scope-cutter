import argparse
import re
from pathlib import Path

REQUIRED_HEADERS = ("EXISTS TO", "SHIPS AS")

GROUNDWORK_TERMS = [
    "scaffold", "scaffolding", "foundation", "framework",
    "enable future", "prepare", "groundwork", "set up", "setup",
]

MULTI_ARTIFACT_HINTS = [
    " and ", " plus ", " & ", ",",
]

IMPLICIT_DEP_TERMS = [
    "backend", "service", "api", "database",
]

def extract_section(text: str, header: str) -> str:
    """
    Extract a section body for a given header until the next all-caps header or end.
    Very simple v0 parser.
    """
    # Match header on its own line
    pattern = rf"(?m)^{re.escape(header)}\s*$"
    m = re.search(pattern, text)
    if not m:
        return ""

    start = m.end()
    # Find next header-like line (ALL CAPS words/spaces) e.g. "EXPLICITLY DOES NOT DO"
    next_header = re.search(r"(?m)^[A-Z][A-Z\s\-]+$", text[start:])
    end = start + next_header.start() if next_header else len(text)
    return text[start:end].strip()

def blocked(reason: str) -> int:
    print(f"BLOCKED: {reason}")
    return 2

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--phase-file", required=True)
    args = p.parse_args()

    text = Path(args.phase_file).read_text(encoding="utf-8")

    # Required fields
    for h in REQUIRED_HEADERS:
        if not re.search(rf"(?m)^{re.escape(h)}\s*$", text):
            return blocked(f"missing required field: {h}")

    ships_as = extract_section(text, "SHIPS AS")
    if not ships_as:
        return blocked("SHIPS AS is empty")

    ships_lower = ships_as.lower()

    # Rule 1: obvious multi-artifact phrasing
    if any(token in ships_lower for token in MULTI_ARTIFACT_HINTS):
        return blocked("SHIPS AS implies multiple artifacts")

    # Rule 2: groundwork/capability language
    if any(term in ships_lower for term in GROUNDWORK_TERMS):
        return blocked("SHIPS AS describes groundwork/capability, not a standalone thing")

    # Rule 3: implicit dependency rule (v0)
    # If it mentions infra-like terms, require an explicit dependency declaration marker.
    # v0 convention: include "ASSUMES:" in SHIPS AS when relying on external context.
    if any(term in ships_lower for term in IMPLICIT_DEP_TERMS) and "assumes:" not in ships_lower:
        return blocked("implicit dependency; declare it explicitly in SHIPS AS using 'ASSUMES:'")

    print("PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
