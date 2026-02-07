CTO CHECKLIST (quick)

- Does this change stay inside the constraint docs (PRODUCT.md or INVARIANT.md/RULES.md) + scope docs?
- Any new "configurability", "memory", or "explainability" creeping in?
- Are failure modes obvious and contained?
- Is the change reversible / easy to rip out?
- Any hidden coupling or premature architecture?
- Are error messages and behavior predictable?
- Does it create maintenance debt disproportionate to the value?
- Is there any reason to block shipping?
