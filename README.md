# Scope Cutter

Scope Cutter is a CLI that lints product release definitions.

It enforces one rule: a release must ship exactly one deliverable.

## The idea

Many scope problems start with how a release is defined.

Releases often become overloaded because multiple pieces of work get bundled together into a single goal.

Scope Cutter asks one question: Does this release resolve to one deliverable, or several?

## How it works

A user proposes the kernel of a product release scope, and Scope Cutter evaluates these two fields:

1. EXISTS TO  
(the purpose of the release)

2. SHIPS AS  
(the artifact or behavior it delivers)


Output is either:

- PASS
- BLOCKED: (reason)

## Examples

### PASS: release ships one clear deliverable

EXISTS TO
Help users understand what changed in the latest release.

SHIPS AS
A release notes page on the product website.

Output:

PASS

### BLOCK: release attempts to ship multiple deliverables

EXISTS TO
Launch the new reporting feature.

SHIPS AS
A backend API, database schema, web dashboard, and mobile UI.

Output:

BLOCKED: release defines multiple deliverables instead of one

## Repository structure

src/main.py        – CLI implementation  
examples/          – example release definitions  
scripts/run.sh     – example runner

## Usage

Run with Python:

```bash
python3 src/main.py examples/01-pass.txt
```

Input files must contain:

EXISTS TO  
(one clear purpose statement)

SHIPS AS  
(one concrete artifact or behavior)

Exit codes: 0 → PASS, 2 → BLOCKED

## Status

v0 validates one constraint: a release must ship one standalone deliverable

## Workflow Integration

Scope Cutter can run automatically on pull requests.

When a release definition is added or modified, the check runs and blocks the merge if the scope does not resolve to a single deliverable.

This enforces scope constraints at commit time rather than relying on manual review.