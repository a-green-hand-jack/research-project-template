# Worktree Policy

Parallelism starts with ownership boundaries, not with more terminals.

## Use A Worktree When

- two agents may edit overlapping areas
- a branch owns a distinct experiment, paper section, or feature
- the task may leave the checkout dirty for a long time
- verification requires a clean comparison against another branch

## Packet

Every non-trivial worktree branch should have:

```text
purpose:
base branch:
worktree path:
owned paths:
forbidden paths:
anatomy impact:
claim / evidence impact:
verification:
exit condition:
```

Do not merge, push, or delete branches without explicit human approval.
