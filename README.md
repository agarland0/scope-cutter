# Scope Cutter

<<<<<<< HEAD
Scope Cutter is a linter for product decisions.
It checks whether a proposed product release resolves to one concrete deliverable rather than a bundle of outputs.

=======
**Scope Cutter** is a linter for product decisions. It checks whether a proposed product release resolves to **one concrete deliverable** rather than a bundle of outputs.

---
>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)

## The idea

Many scope problems start with how a release is defined.

Releases often become overloaded because multiple pieces of work get bundled together into a single goal.

<<<<<<< HEAD
Scope Cutter (v0) asks one question: Does this release resolve to one deliverable, or several?

=======
Scope Cutter (v0) asks one question: **Does this release resolve to one deliverable, or several?**
>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)

## How it works

<<<<<<< HEAD
A user proposes the kernel of a product release scope, and Scope Cutter evaluates these two fields:

1 - EXISTS TO  
(the purpose of the release)

2 - SHIPS AS  
(the artifact or behavior it delivers)

=======
## How it works

A user proposes the kernel of a product release scope, and Scope Cutter evaluates these two fields:

1. **EXISTS TO**  
   (the purpose of the release)

2. **SHIPS AS**  
   (the artifact or behavior it delivers)

>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)
The tool checks that the release definition resolves to **one standalone deliverable** rather than a bundle of outputs.

Output is either:

<<<<<<< HEAD
PASS
or
BLOCKED: (reason)
=======
- `PASS`
- `BLOCKED: (reason)`

---

## Examples

**PASS: release ships one clear deliverable.**

EXISTS TO  
Help users understand what changed in the latest release.

SHIPS AS  
A release notes page on the product website.

Output:

`PASS`

--

**BLOCK: release attempts to ship multiple deliverables.**

EXISTS TO  
Launch the new reporting feature.

SHIPS AS  
A backend API, database schema, web dashboard, and mobile UI.

Output:

`BLOCKED: release defines multiple deliverables instead of one`
>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)

---

## Examples

### PASS: release ships one clear deliverable.

EXISTS TO
Help users understand what changed in the latest release.

SHIPS AS
A release notes page on the product website.

Output:

PASS

--

### BLOCK: release attempts to ship multiple deliverables.

EXISTS TO
Launch the new reporting feature.

SHIPS AS
A backend API, database schema, web dashboard, and mobile UI.

Output:

BLOCKED: release defines multiple deliverables instead of one


## Usage

Run with Python:

<<<<<<< HEAD
=======
```bash
>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)
python3 src/main.py examples/01-pass.txt

Input files must contain:

EXISTS TO  
(one clear purpose statement)

SHIPS AS  
(one concrete artifact or behavior)

<<<<<<< HEAD
Exit codes: 0 → PASS, 2 → BLOCKED
=======
**Exit codes:** `0 → PASS`, `2 → BLOCKED`

---
>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)

--
## Status

<<<<<<< HEAD
v0 validates one constraint: a release must ship one standalone deliverable. Expanded PASS/BLOCK taxonomy, legitimacy checks and semantic validation are deferred to future versions.
=======
v0 validates one constraint: a release must ship one standalone deliverable.

>>>>>>> 2bfa635 (Clarify v0 behavior and add example runner)
