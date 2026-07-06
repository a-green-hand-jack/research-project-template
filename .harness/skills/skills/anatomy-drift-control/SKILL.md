---
name: anatomy-drift-control
description: Use ANATOMY.md as the repo-local structure map and keep it synchronized with structural edits.
allowed-tools: Read, Glob, Bash
---

# Anatomy Drift Control

Use this skill before and after structural edits.

1. Read root `ANATOMY.md`.
2. Read the nearest component `ANATOMY.md` when the component is active.
3. Identify owned paths, state files, inbound dependencies, and outbound effects.
4. Before moving, renaming, splitting, or deleting files, search anatomy and
   index files for touched names.
5. Update anatomy in the same change when ownership, routing, lifecycle, state,
   or component boundaries change.
6. Run `rph validate .`.

Stop if the touched directory has no clear owner or if the structural edit would
cross a human gate.
