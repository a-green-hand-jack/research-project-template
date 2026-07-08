---
name: harness-router
description: Route project-local research work through the generated harness structure, component state, memory boards, and activation workflow.
allowed-tools: Read, Bash, Glob
---

# Harness Router

Use this skill inside the generated research project when the task is unclear or
crosses project components.

## Entry

1. Read root `AGENTS.md`.
2. Read `harness.yaml`, `.harness/manifest.yaml`, `memory/current-status.md`,
   and `memory/phase-dashboard.yaml`.
3. Inspect only the relevant boards and components.

## Routing

- Idea, claim, risk, action, or decision state -> root `memory/boards/`.
- Runnable implementation or experiment work -> use `code/`.
- Paper source or paper-facing narrative -> use `paper/`.
- Source intake and source cards -> use `reference/`.
- Review simulation -> `reviewer/`.
- Real reviews and responses -> `rebuttal/`.
- Artifact evaluation or release handoff -> `artifact/`.

Before handoff, update touched state and run `rph validate .`.
