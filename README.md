# Scope Cutter

**Scope Cutter** is a CLI tool that checks whether a proposed product release phase is defined as a **single standalone deliverable**.

It acts like a linter for release definitions.

---

## The idea

Many scope problems are definition problems. Phases become overloaded because work that merely *enables* future progress gets described as if it were a deliverable.

Scope Cutter asks one question:

**Does this phase legitimately exist as a standalone thing?**

If the project stopped after this phase, the shipped artifact should still make sense on its own.

---

## The invariant

A release phase should ship **one concrete artifact or behavior**.

Phases often fail this when they are:

* groundwork or scaffolding
* a capability promise
* a framework for future work
* a bundle of multiple deliverables

Scope Cutter is a **gate, not a collaborator**. It blocks invalid phase definitions but does not suggest fixes.

---

## How it works (v0)

Scope Cutter evaluates two fields:

```
EXISTS TO
<the purpose of the phase>

SHIPS AS
<the artifact or behavior it delivers>
```

The tool checks that the release definition resolves to **one standalone deliverable**.

Output is either:

```
PASS
```

or

```
BLOCKED: <reason>
```

---

## Usage

Run with Python:

```
python3 src/main.py examples/01-pass.txt
```

Input files must contain:

```
EXISTS TO
<one clear purpose statement>

SHIPS AS
<one concrete artifact or behavior>
```

Exit codes:

```
0 → PASS
2 → BLOCKED
```

---

## Status

v0 validates one constraint: a release phase must ship one standalone deliverable. Legitimacy checks and semantic validation are deferred to v1.
