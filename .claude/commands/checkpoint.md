---
description: Write memory/current-status.md before compact/clear/handoff
---

Use the `checkpoint-writer` subagent to update `memory/current-status.md`
(and `memory/session-tree.md` if this session branched) with the current
objective, decisions, files touched, commands run, open blockers, and the
exact next action. Then report the 10-line summary it produced.
