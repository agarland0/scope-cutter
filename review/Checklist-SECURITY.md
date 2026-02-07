SECURITY CHECKLIST (quick)

- Any network calls, telemetry, or external APIs introduced?
- Any persistence of user data (files, caches, logs) beyond execution?
- Any sensitive data printed to console or written to disk?
- Any risky new dependencies?
- Any unsafe file path handling (path traversal, temp files)?
- Does the change violate IP.txt / local-only posture?
- If the user pastes company data, what could leak?
