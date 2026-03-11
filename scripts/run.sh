#!/usr/bin/env bash
set -euo pipefail

# Run main.py against the core example inputs.
# This gives a quick sanity check that PASS/BLOCK behavior
# stays consistent as the tool evolves.

python3 src/main.py examples/01-pass.txt
python3 src/main.py examples/02-pass.txt
python3 src/main.py examples/03-block_multiple_deliverables.txt
