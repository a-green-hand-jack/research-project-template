# Agent Map

This file is a map, not a manual. Keep it short and follow links only as needed.

## Identity

This is an agent-native research project. The harness exists so Codex/agents can
reliably enter, advance, validate, and hand off the project.

The template is complete from the first commit: `reference/`, `code/`, and
`paper/` are scaffolded already. Use only the surfaces relevant to the task.

## Entry order

1. Read `harness.yaml`.
2. Read `.harness/manifest.yaml` to see which components are active.
3. Read `memory/current-status.md`.
4. Read `memory/phase-dashboard.yaml`.
5. Read `memory/change-control.yaml` if the task may change goals, claims,
   baselines, metrics, venues, deadlines, visibility, or data splits.
6. Read `ANATOMY.md` only when structure, ownership, or component boundaries
   may change.
7. Read only the board files relevant to your task under `memory/boards/`.
8. Then inspect only the relevant component or artifact files.

Do not recursively read the whole repository before understanding the current task.

## Canonical state

- Project config: `harness.yaml`
- Structural map: `ANATOMY.md`
- Agent policy: `.agent/`
- Project-local runtime and blueprints: `.harness/`
- Human-readable status: `memory/current-status.md`
- Canonical phase: `memory/phase-dashboard.yaml`
- Goal and scope changes: `memory/change-control.yaml`
- Durable boards: `memory/boards/*.yaml`
- Session tree: `memory/session-tree.md`
- Session trace: `memory/sessions/`
- Unverified AI observations: `research-artifact/staging/`

## Component surfaces

`reference/`, `code/`, and `paper/` are available from day one. Do not activate
a second scaffold or create duplicate top-level directories. Runnable experiment
logic belongs in `code/experiments/`. Project-level experiment plans belong in
`docs/experiments/`, and canonical experiment objects belong in
`memory/boards/experiments.yaml`.

## Writeback requirements

Before ending work:

1. Update touched claim/evidence/action/risk/decision objects.
2. Record provenance, certainty, and links.
3. Preserve negative results and dead ends.
4. Update `memory/change-control.yaml` when goals, claims, baselines, metrics,
   venues, deadlines, visibility, or data splits changed.
5. Update `ANATOMY.md` when structure changed.
6. Update `memory/current-status.md`.
7. Run `rph validate .`.
8. Leave a next-step briefing if the task is non-trivial.

## Do not

- Do not turn AI guesses into supported claims without evidence or human confirmation.
- Do not cross human gates silently.
- Do not delete dead ends just because they are negative.
- Do not expose private/internal sources in paper-facing or public artifacts without visibility checks.
- Do not treat `.harness/` as durable research memory; write durable state into `memory/` or component docs.
- Do not treat generated data, run outputs, checkpoints, or private source
  bytes as tracked project state; index them instead.
