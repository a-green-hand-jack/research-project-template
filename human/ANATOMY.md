# Human Surface Anatomy

`human/` records human-agent collaboration artifacts.

## Components

| Path | Role |
| --- | --- |
| `briefs/active/` | Current task briefs, constraints, and human instructions. |
| `briefs/completed/` | Completed briefs retained for traceability. |
| `reviews/plans/` | Human comments on plans and scope before implementation. |
| `reviews/results/` | Human review of outputs, results, paper text, or artifacts. |
| `reviews/recipes/` | Human review of workflow recipes before adoption. |
| `decisions/` | Human-owned approvals, rejections, and lightweight ADRs. |
| `inbox/` | Materials, questions, and requests waiting for triage. |

## Connections

- Machine-readable gates are tracked in `memory/boards/human-gates.yaml`.
- Project-shape changes are synchronized through `memory/change-control.yaml`.
- Accepted plans normally live in `plans/` or the relevant component docs.

## Notes

Do not infer approval from the presence of a draft or comment. Approval requires
an explicit decision or closed human gate.
