# Research Project

This repository is an agent-native research project control root. It is designed
to start small at the idea stage and grow only when the research needs more
structure.

The durable project state lives in `memory/`. The local agent runtime,
component blueprints, validator registry, and project-local skills live in
`.harness/`. Stable agent policy lives in `.agent/`, and structural routing
lives in `ANATOMY.md`.

## First Session

1. Fill `PROJECT.md` with the research target, venue or milestone, and current
   definition of done.
2. Update `harness.yaml` and `memory/current-status.md`.
3. Check `memory/change-control.yaml` for goal or scope changes that need
   synchronized edits.
4. Add initial claims, risks, actions, and source visibility entries under
   `memory/boards/`.
5. Validate the project.

If `rph` is already installed:

```bash
rph validate .
```

For one-off validation from the harness repository:

```bash
uvx --from git+ssh://git@github.com/a-green-hand-jack/research-project-harness.git rph validate .
```

For a persistent local tool install:

```bash
uv tool install git+ssh://git@github.com/a-green-hand-jack/research-project-harness.git
```

## Project Anatomy

```text
memory/            durable cross-component claim/evidence/action/risk state
memory/change-control.yaml
                   synchronized changes to venue, claim, baseline, metric, split
memory/session-tree.md
                   durable context branching and handoff map
research-artifact/ staging, trace, problem logic, and narrative workspace
docs/              project-level designs, experiment plans, updates, audits
plans/             human-agent plans for ambiguous or staged work
code/              code component placeholder; activate when implementation starts
paper/             paper component placeholder; activate when writing starts
reference/         source library placeholder; activate when sources need indexing
reviewer/          simulated review state
rebuttal/          real reviews and response planning
artifact/          artifact evaluation and release handoff
.agent/            stable agent policy and cookbook promotion rules
.harness/          project-local agent runtime, skills, blueprints, validators
ANATOMY.md         structural router for ownership, state, and component boundaries
```

`code/`, `paper/`, and `reference/` begin as lightweight placeholders. Activate
their full scaffold only when the project reaches that stage.

## Progressive Activation

Use the project-local activation script from the repository root:

```bash
python .harness/scripts/activate-component.py reference --variant source-library
python .harness/scripts/activate-component.py code --variant ml-python
python .harness/scripts/activate-component.py paper --variant latex-generic
```

Activation copies a blueprint from `.harness/blueprints/`, updates
`.harness/manifest.yaml`, and updates `harness.yaml`. It refuses to overwrite
non-placeholder files unless `--force` is passed.

## Project-Local Skills

This template carries a project-local skill bundle. Install it into the active
agent runtime from the project root:

```bash
npx skills add ./.harness/skills -a codex claude-code -y
```

The skills are local operating instructions for this project. They are not the
durable research state; durable state must still be written to `memory/`,
component docs, or production artifacts.

The default skill pack includes routing, component activation, claim/evidence
review, experiment workflow, paper writing, artifact indexing, anatomy drift
control, session boundary control, worktree PR flow, subagent routing,
interactive planning, and recipe harvesting.

## Component Boundaries

- `code/` owns implementation, runnable experiments, evaluation logic, remote
  execution policy, code-side run records, and code-side evidence docs.
- `paper/` owns paper source, venue-specific formatting, paper-facing figures
  and tables, source visibility, and submission cleanup.
- `reference/` owns raw or private sources, source cards, processing status, and
  source-to-project notes.
- `docs/experiments/` is for project-level experiment plans. Runnable experiment
  code belongs in `code/experiments/` after the code component is active.
- `memory/boards/experiments.yaml` stores canonical experiment objects and links
  them to claims, evidence, risks, and actions.

Do not leave research decisions only in chat. Before handoff, update the touched
boards, `memory/change-control.yaml` when project-shape changes occurred,
`memory/current-status.md`, and run validation.
