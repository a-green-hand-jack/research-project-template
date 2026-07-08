# Human Gates

Human gates are reviewable project objects, not informal promises in chat.

## Gate Surfaces

- `memory/boards/human-gates.yaml` stores machine-readable open and closed gate
  objects.
- `human/decisions/` stores human-owned approval or rejection notes.
- `memory/change-control.yaml` stores synchronized project-shape changes.

## Gate Object Expectations

Each non-trivial gate should include:

```yaml
id: GATE-001
title:
status: open
requires:
  - human approval
rationale:
linked_actions: []
linked_claims: []
opened_by:
closed_by:
```

## Never Cross Silently

Do not silently cross gates for supported-claim promotion, paper-facing release,
private-source exposure, expensive compute, deletion of research artifacts, or
remote publication.
