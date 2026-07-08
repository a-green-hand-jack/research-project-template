# Claude Code Entry

Follow `AGENTS.md` as the canonical project map.

This is a research-project-harness project. Enter through `harness.yaml`,
`.harness/manifest.yaml`, `memory/current-status.md`, and
`memory/phase-dashboard.yaml` before reading task-specific boards or component
files.

Use `.agent/` for repo-local policy and `ANATOMY.md` for structural edits. Use
`memory/change-control.yaml` when goals, claims, baselines, metrics, venues,
deadlines, visibility, or data splits change.

`reference/`, `code/`, and `paper/` are already scaffolded. Use bounded reads
and edits; do not create duplicate component roots.

Before handoff, update touched memory boards and `memory/current-status.md`,
then run `rph validate .`.
