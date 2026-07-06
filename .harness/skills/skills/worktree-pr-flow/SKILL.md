---
name: worktree-pr-flow
description: Use issue, branch, worktree, PR, and review boundaries for non-trivial or parallel implementation.
allowed-tools: Read, Glob, Bash
---

# Worktree PR Flow

Use this skill for non-trivial implementation or parallel agent work.

Before work:

1. Read `.agent/worktree-policy.md`.
2. Confirm base branch, owned paths, forbidden paths, anatomy impact, and
   claim/evidence impact.
3. Create or update the branch/worktree status note.

During work:

- Keep the diff focused.
- Do not merge, push, or delete branches without explicit approval.
- Update anatomy and ledgers in the same change when affected.

After work:

1. Run targeted tests and `rph validate .`.
2. Prepare a PR summary.
3. Update `memory/current-status.md` or the branch status note.
