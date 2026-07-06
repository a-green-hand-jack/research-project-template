# Code Component

Activation status: inactive.

This placeholder marks where the implementation component will live. Activate it
when the project has a method to implement, experiments to run, or code-side
evidence to preserve.

```bash
python .harness/scripts/activate-component.py code --variant ml-python
```

Run the command from the project root.

The full scaffold is already stored in
`.harness/blueprints/code/ml-python/`. Activation copies that scaffold here and
marks `code` active in `.harness/manifest.yaml` and `harness.yaml`.

## Activated Shape

```text
code/
  README.md
  AGENTS.md
  CLAUDE.md
  pyproject.toml
  .env.example
  .gitignore
  src/
    project_code/
      __init__.py
      models/
      data/
      utils/
  experiments/
    config.py
    train.py
    evaluate.py
    configs/base.yaml
  eval/
    metrics.py
    benchmarks/
    baselines/
  infra/
    envs/local.yaml
    envs/cluster.yaml.example
    remote-projects.yaml
    submit/slurm/
  docs/
    results/
    reports/
    runs/
    ops/current-status.md
    ops/decision-log.md
    outlines/
    dev/
    src/
  scripts/
    train.py
    download_data.py
  tests/
    conftest.py
    test_placeholder.py
  .agent/local-overrides.yaml
  .vscode/settings.json
```

When active, this component owns:

- `src/` for portable algorithm and library code;
- `experiments/` for runnable training and evaluation logic;
- `eval/` for benchmarks, baselines, and metrics;
- `infra/` for local/remote/HPC execution policy;
- `docs/results/`, `docs/reports/`, and `docs/runs/` for code-side evidence.

Raw outputs, checkpoints, large logs, TensorBoard caches, and wandb runs should
stay ignored or external, with small pointers written into `docs/runs/` and
durable claim/evidence links written into root `memory/boards/`.

The default package name is `project_code` so the scaffold is immediately
testable. Rename it once the project name is settled, then update `pyproject.toml`
and imports.
