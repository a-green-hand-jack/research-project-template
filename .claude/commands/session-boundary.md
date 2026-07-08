---
description: Check whether this is a good point to checkpoint, branch, compact, clear, or hand off
---

Use the `session-boundary-agent` subagent to evaluate the current session
against `.agent/session-boundary-protocol.md`. Report its recommendation and
follow it before starting new work if it recommends anything other than
"continue".
