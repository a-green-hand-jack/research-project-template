---
name: session-boundary-control
description: Maintain session trees, handoffs, checkpoint reminders, and fresh-context boundaries.
allowed-tools: Read, Write, Glob, Bash
---

# Session Boundary Control

Use this skill when a conversation is long, a phase changes, a child task is
created, or the work is getting hard to track.

1. Read `.agent/session-boundary-protocol.md`.
2. Inspect `memory/current-status.md`, `memory/session-tree.md`, active plans,
   and relevant board files.
3. Classify whether the next step is continue, checkpoint, branch, compact,
   clear, or hand off.
4. Update the smallest state file needed for a fresh session to resume.
5. Leave the exact next entry point in `memory/current-status.md`.

Use fresh context when exploration becomes implementation, implementation
becomes verification, or repeated failed hypotheses are polluting the thread.
