---
name: interactive-plan-doc
description: Create a durable human-agent plan document for staged or ambiguous research work.
allowed-tools: Read, Write, Glob
---

# Interactive Plan Doc

Use this skill when the task needs discussion, staged planning, human comments,
or a durable anchor against drift.

1. Choose or create `plans/YYYYMMDD-<slug>.zh.md`.
2. Record current objective, non-goals, owned paths, forbidden paths, task tree,
   open questions, verification, and exit condition.
3. Let human comments live in the plan file when needed.
4. Read the plan diff before implementation and summarize accepted changes.
5. Start implementation only after scope, verification, and stop conditions are
   clear.

For non-trivial implementation, route through `worktree-pr-flow`.
