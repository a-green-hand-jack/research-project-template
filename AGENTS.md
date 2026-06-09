# Agent Map

This file is a map, not a manual. Keep it short and follow links only as needed.

## Identity

This is an agent-native research project. The harness exists so Codex/agents can reliably enter, advance, validate, and hand off the project.

## Entry order

1. Read `harness.yaml`.
2. Read `memory/current-status.md`.
3. Read `memory/phase-dashboard.yaml`.
4. Read only the board files relevant to your task under `memory/boards/`.
5. Then inspect raw paper/code/experiment artifacts as needed.

Do not recursively read the whole repository before understanding the current task.

## Canonical state

- Project config: `harness.yaml`
- Human-readable status: `memory/current-status.md`
- Canonical phase: `memory/phase-dashboard.yaml`
- Durable boards: `memory/boards/*.yaml`
- Session trace: `memory/sessions/`
- Unverified AI observations: `research-artifact/staging/`

## Writeback requirements

Before ending work:

1. Update touched claim/evidence/action/risk/decision objects.
2. Record provenance, certainty, and links.
3. Preserve negative results and dead ends.
4. Update `memory/current-status.md`.
5. Run `rph validate .`.
6. Leave a next-step briefing if the task is non-trivial.

## Do not

- Do not turn AI guesses into supported claims without evidence or human confirmation.
- Do not cross human gates silently.
- Do not delete dead ends just because they are negative.
- Do not expose private/internal sources in paper-facing or public artifacts without visibility checks.
