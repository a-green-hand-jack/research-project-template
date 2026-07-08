# Human Collaboration

This directory is the repo-local surface for human intent, review, approvals,
and materials waiting for triage.

Use it when instructions or decisions should survive a chat session:

- `briefs/active/`: current task briefs and constraints.
- `briefs/completed/`: completed briefs kept for traceability.
- `reviews/plans/`: human comments on plans before implementation.
- `reviews/results/`: human review of outputs, experiments, or paper text.
- `reviews/recipes/`: review of workflow recipes before promotion.
- `decisions/`: human-owned approvals, rejections, and lightweight ADRs.
- `inbox/`: materials or questions awaiting human attention.

Machine-readable gates live in `memory/boards/human-gates.yaml`.
