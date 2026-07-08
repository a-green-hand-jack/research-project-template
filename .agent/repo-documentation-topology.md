# Repository Documentation Topology

Keep each document type narrow so future agents can navigate without reading the
whole repository.

## Root Files

- `README.md`: human entry, project shape, common commands.
- `PROJECT.md`: research target, venue or milestone, definition of done.
- `AGENTS.md`: agent entry map and work contract.
- `CLAUDE.md`: thin Claude Code adapter that points back to `AGENTS.md`.
- `ANATOMY.md`: structural router for ownership and state surfaces.
- `harness.yaml`: machine-readable project identity and policy.

## Directories

- `.agent/`: stable agent policy, not research facts.
- `.harness/`: local runtime, skills, blueprints, and validators, not research
  memory.
- `.claude/`: Claude Code subagents, permissions, hooks, commands, and
  statusline. Machinery that enforces `.agent/` policy, not policy itself.
- `human/`: human briefs, reviews, decisions, and inbox.
- `memory/`: active state, boards, session tree, practices, and handoffs.
- `research-artifact/`: problem logic, staging, negative results, and narrative
  workspace.
- `reference/`: sources, source cards, and source-to-project notes.
- `code/`: runnable code, experiments, evaluation, infra, and code-side reports.
- `paper/`: paper source, figures, tables, and paper-facing writing state.

Long tutorials belong in `docs/` or component README files. Structural claims
belong in `ANATOMY.md`.
