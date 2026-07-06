# Project

## Goal

TODO: Describe the research target, intended venue, deadline, and definition of done.

## Harness contract

This repository is managed as an agent-native research project:

```text
research project = management graph + epistemic graph + production artifacts
```

The repo is the system of record. Important research state must be written into `memory/`, `research-artifact/`, or production artifact directories, not left only in chat.

## Progressive components

This project starts in a lightweight idea-stage shape. `code/`, `paper/`, and
`reference/` are placeholders until activated from `.harness/blueprints/`.

- `memory/` is durable cross-component research state.
- `.harness/` is the local agent/runtime layer: blueprints, skills, validators,
  lifecycle policy, and activation scripts.
- `docs/` stores project-level designs, experiment plans, updates, audits, and
  timelines.
- `code/` owns implementation, runnable experiments, evaluation, infra, and
  code-side evidence after activation.
- `paper/` owns paper source, paper-facing claims, venue mode, and source
  visibility after activation.
- `reference/` owns raw sources, source cards, processing status, and
  source-to-project notes after activation.
