# Action Boundary

Prompts express intent; this file defines the project boundary for side effects.

## Safe Local Actions

Agents may do these when they are relevant to the current task:

- read repository files through bounded search or direct file reads
- edit tracked project text, code, tests, and memory files within the task scope
- run local validators, targeted tests, formatters, and static checks
- create plan, handoff, review, and session notes in approved directories

## Human Gate Required

Agents must record or request a human gate before:

- launching, killing, restarting, or scaling remote or expensive jobs
- deleting or moving datasets, checkpoints, run directories, logs, or private
  source material
- changing target venue, main claim, baseline set, metric, visibility policy,
  data split, or public release scope
- pushing, publishing, opening release surfaces, merging, or changing remote
  repository settings
- promoting an AI observation or tentative claim to supported, paper-facing, or
  final without linked evidence and visibility checks

Use `memory/boards/human-gates.yaml` for open gates and `human/decisions/` for
human-owned approval notes when the decision should be easy to review later.

## Protected Local Paths

The template `.gitignore` protects common generated or private bytes:

- `code/data/`
- `code/runs/`
- `code/checkpoints/`
- `code/wandb/`
- `paper/build/`
- `reference/sources/raw/`
- `reference/sources/private/`
- `.harness/private/`

Tracked indexes, summaries, checksums, and inspection commands are preferred
over committing large or private bytes.
