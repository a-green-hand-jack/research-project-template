# Project

## Goal

TODO: Describe the research target, intended venue, deadline, and definition of done.

## Harness contract

This repository is managed as an agent-native research project:

```text
research project = management graph + epistemic graph + production artifacts
```

The repo is the system of record. Important research state must be written into `memory/`, `research-artifact/`, or production artifact directories, not left only in chat.

## Complete components

This project starts with the full research control surface. `code/`, `paper`,
and `reference/` are scaffolded already; use only the relevant surfaces for the
current stage.

- `memory/` is durable cross-component research state.
- `.harness/` is the local agent/runtime layer: blueprints, skills, validators,
  lifecycle policy, and activation scripts.
- `human/` stores human briefs, reviews, decisions, and inbox material that
  should outlive chat.
- `docs/` stores project-level designs, experiment plans, updates, audits, and
  timelines.
- `code/` owns implementation, runnable experiments, evaluation, infra, tests,
  and code-side evidence.
- `paper/` owns paper source, paper-facing claims, venue mode, figures, tables,
  bibliography, and source visibility.
- `reference/` owns raw sources, source cards, processing status, and
  source-to-project notes.
