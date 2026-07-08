# Code Component Anatomy

This component owns runnable implementation, experiment execution, evaluation,
and code-side evidence.

## Entry Surfaces

- `AGENTS.md` records component-specific agent rules.
- `CLAUDE.md` is the Claude Code adapter for this component.
- `pyproject.toml` defines the local Python package and test settings.
- `.env.example` documents expected environment variables without secrets.

## Components

- `src/project_code/` owns importable project code.
- `experiments/` owns runnable experiment entry points and configs.
- `eval/` owns metrics, benchmarks, and reproduced baselines.
- `infra/` owns local and remote execution descriptors.
- `scripts/` owns command wrappers that call importable code.
- `docs/runs/`, `docs/results/`, and `docs/reports/` own code-side evidence
  summaries that can link back to memory boards.
- `tests/` owns code-level regression checks.

## State

Do not store large datasets, logs, checkpoints, or generated artifacts here
unless the project explicitly allows it. Index them with commit, config, split,
path or URI, status, and inspection command.

## Same-Change Rule

When code changes affect claims, experiments, metrics, baselines, data splits,
or artifact paths, update the relevant memory board and run `rph validate .`.
