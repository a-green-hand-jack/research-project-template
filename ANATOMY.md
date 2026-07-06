# Project Anatomy

This file is a structural router. Keep operational instructions in `AGENTS.md`,
research state in `memory/`, and generated/runtime capabilities in `.harness/`.

## Entry Surfaces

- `AGENTS.md` is the canonical agent entry map.
- `CLAUDE.md` is the thin Claude Code adapter and points back to `AGENTS.md`.
- `README.md` is the human-facing project entry.
- `harness.yaml` records project identity, component status, and default policy.
- `.harness/manifest.yaml` records local runtime, blueprints, skills, and validators.

## Control Plane

- `.harness/` owns the generated runtime: component blueprints, local skills,
  validators, activation scripts, and private local overlays.
- `.agent/` owns stable agent policies that should be reviewed like code.
- `memory/` owns current project state, boards, session traces, and change
  control. It is active memory, not a place for large artifacts.
- `research-artifact/` owns problem framing, assumptions, contribution maps,
  staging notes, dead ends, and negative results.

## Component Boundaries

- `reference/` starts as a placeholder for source intake and source cards.
- `code/` starts as a placeholder for runnable code and experiment machinery.
- `paper/` starts as a placeholder for paper source and paper-facing evidence.
- `reviewer/`, `rebuttal/`, and `artifact/` are available lightweight
  deliverable surfaces from day one.
- `code-worktrees/` and `paper-worktrees/` document parallel checkout
  boundaries and should not contain normal tracked project state.

## State And Evidence

- Canonical boards live in `memory/boards/*.yaml`.
- Goal, claim, baseline, metric, venue, and data-split changes go through
  `memory/change-control.yaml`.
- Long or branched work records routing in `memory/session-tree.md` and
  session notes in `memory/sessions/`.
- AI observations start in `research-artifact/staging/` or low-certainty board
  states before becoming supported claims.

## Same-Change Rule

Structural edits update this file, affected component anatomy files, and the
matching validator or memory board in the same change.
