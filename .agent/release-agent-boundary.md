# Release Agent Boundary

Some projects use this harness to build or evaluate an agent. Keep two layers
separate.

## Outer Development Harness

The outer harness is this repository control plane:

- `AGENTS.md`
- `.agent/`
- `.harness/`
- `memory/`
- `human/`
- `ANATOMY.md`

It exists to help Codex, Claude Code, and other coding agents safely develop the
project.

## Inner Release Agent

An inner release agent is the agent, workflow, model, benchmark, or product that
the project itself may publish or evaluate. Its behavior contract, eval traces,
tool boundary, and release documentation belong in the relevant project
component, usually `code/`, `artifact/`, `paper/`, or `docs/`.

Do not mix outer editing rules with inner product behavior prompts. If both
layers change in one task, update the anatomy and validation surfaces for both.
