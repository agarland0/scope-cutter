# Example Decisions Using Scope Cutter

Scope Cutter evaluates whether a release definition produces a clear deliverable.

Each example below shows a release definition and the outcome produced by the tool.

---

## Example 1 — Valid Release

This release produces a single deliverable that fulfills the goal.

EXISTS TO  
Help users understand what changed in the latest release.

SHIPS AS  
A release notes page on the product website.

Result

PASS

Reason  
The release produces one clear artifact that directly fulfills the goal.

---

## Example 2 — Valid Release

This release produces a single deliverable that customers can use.

EXISTS TO  
Allow customers to analyze their account activity outside the product.

SHIPS AS  
A downloadable CSV export of account usage.

Result

PASS

Reason  
The release definition specifies one deliverable artifact.

---

## Example 3 — Blocked Release (Multiple Deliverables)

This release attempts to ship multiple artifacts.

EXISTS TO  
Launch the new reporting feature.

SHIPS AS  
A backend API, database schema, web dashboard, and mobile UI.

Result

BLOCKED

Reason  
The release definition lists multiple deliverables instead of a single artifact.