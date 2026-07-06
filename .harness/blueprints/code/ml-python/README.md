# Code Component

This component owns implementation, runnable experiments, evaluation logic,
remote execution policy, and code-side evidence.

## Layout

```text
README.md
AGENTS.md
CLAUDE.md
pyproject.toml
.env.example
.gitignore
src/project_code/    portable algorithm/library code; rename package later
experiments/         runnable training/evaluation logic and configs
eval/                benchmarks, baselines, metrics, and comparison code
infra/               local/remote/HPC environment and submit policy
docs/results/        stable result summaries and table/figure notes
docs/reports/        experiment reports and technical narratives
docs/runs/           run registry, job IDs, config/commit pointers
tests/               unit tests for src-level behavior
scripts/             small executable helpers
.agent/              private/local agent state and overrides
```

Raw outputs, checkpoints, large logs, TensorBoard caches, and wandb runs should
stay ignored or external. Commit small pointers and summaries under `docs/runs/`
and connect durable evidence to root `memory/boards/evidence.yaml`.

## Suggested Gates

Record the real project commands once the Python package exists. Common defaults
are:

```bash
export UV_PROJECT_ENVIRONMENT=<absolute-project-root>/.uv-envs/code
uv sync
uv run ruff format --check src tests experiments scripts
uv run ruff check src tests experiments scripts
uv run mypy src
uv run pytest tests -v
uv run pre-commit run --all-files
```

Use mutating format/fix commands only when requested or documented by project
policy, then review the diff.

The scaffold uses `project_code` as a placeholder package so it can run tests
immediately after activation. Rename it once the project identity is stable.
