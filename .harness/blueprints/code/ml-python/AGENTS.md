# Code Agent Guide

This file is the code-component entry point. Root project memory remains the
durable cross-component source of truth.

## Boundaries

- Put portable implementation under `src/`.
- Put runnable training and evaluation logic under `experiments/`.
- Put baselines, benchmarks, and metrics under `eval/`.
- Put local/remote/HPC configuration under `infra/`.
- Put result summaries in `docs/results/`, reports in `docs/reports/`, and run
  pointers in `docs/runs/`.
- Do not commit raw outputs, checkpoints, large logs, or wandb/tensorboard
  caches.

Before handoff, update relevant code docs and root `memory/boards/` links, then
run the configured gates and `rph validate .` from the project root.
