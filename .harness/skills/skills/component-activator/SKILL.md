---
name: component-activator
description: Reapply or repair code, paper, reference, reviewer, rebuttal, or artifact components from this project's local harness blueprints.
allowed-tools: Read, Bash
---

# Component Activator

Use this skill when a component scaffold needs to be repaired, refreshed, or
intentionally re-applied from `.harness/blueprints/`. The default template
already includes `reference/`, `code/`, and `paper/`.

## Commands

Run from the project root:

```bash
python .harness/scripts/activate-component.py reference --variant source-library
python .harness/scripts/activate-component.py code --variant ml-python
python .harness/scripts/activate-component.py paper --variant latex-generic
```

The script copies files from `.harness/blueprints/`, updates
`.harness/manifest.yaml`, updates `harness.yaml`, and refuses to overwrite
non-placeholder files unless `--force` is passed.

After activation, update `memory/current-status.md` and run `rph validate .`.
