# Research Project

This repository is an agent-native research project control root. It is designed
to give agents the complete control plane from the first commit: research memory,
human collaboration, reference intake, runnable code, paper source, artifacts,
skills, policies, and validators.

The durable project state lives in `memory/`. The local agent runtime,
component blueprints, validator registry, and project-local skills live in
`.harness/`. Stable agent policy lives in `.agent/`, and structural routing
lives in `ANATOMY.md`. Claude Code subagents, permissions, hooks, commands,
and the statusline live in `.claude/`, so the boundaries described in
`.agent/action-boundary.md` are mechanically enforced, not just documented.

## First Session

1. Fill `PROJECT.md` with the research target, venue or milestone, and current
   definition of done.
2. Update `harness.yaml` and `memory/current-status.md`.
3. Check `memory/change-control.yaml` for goal or scope changes that need
   synchronized edits.
4. Add initial claims, risks, actions, and source visibility entries under
   `memory/boards/`.
5. Put human constraints or approvals that should outlive chat in `human/`.
6. Validate the project.

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
human/             human briefs, reviews, decisions, and inbox
research-artifact/ staging, trace, problem logic, and narrative workspace
docs/              project-level designs, experiment plans, updates, audits
plans/             human-agent plans for ambiguous or staged work
code/              runnable code, experiments, evaluation, infra, tests
paper/             paper source, figures, tables, bibliography, writing state
reference/         source library, cards, processing status, project-use notes
reviewer/          simulated review state
rebuttal/          real reviews and response planning
artifact/          artifact evaluation and release handoff
.agent/            stable agent policy and cookbook promotion rules
.harness/          project-local agent runtime, skills, blueprints, validators
.claude/           Claude Code subagents, permissions, hooks, commands, statusline
ANATOMY.md         structural router for ownership, state, and component boundaries
```

`code/`, `paper/`, and `reference/` are scaffolded from the start. Use only the
parts relevant to the task, but do not create duplicate top-level experiment,
paper, or literature directories.

## Blueprint Reapplication

The project keeps the source blueprints under `.harness/blueprints/` so a
component can be re-applied or repaired intentionally:

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

The default skill pack includes routing, component reapplication, claim/evidence
review, experiment workflow, paper writing, artifact indexing, anatomy drift
control, session boundary control, worktree PR flow, subagent routing,
interactive planning, and recipe harvesting.

## Claude Code Subagents, Permissions, Hooks, And Statusline

`.claude/agents/` holds isolated-context subagents for this project:
`repo-researcher`, `feature-worker`, `test-runner`, `experiment-monitor`,
`checkpoint-writer`, `subagent-router-agent`, `session-boundary-agent`,
`artifact-librarian`, and `branch-reporter`. Each has a narrow `tools:` scope
and a written boundary; see `.claude/agents/README.md`.

`.claude/settings.json` turns `.agent/action-boundary.md` into enforced
permissions (deny/ask/allow) instead of prose the agent might skip, wires a
`PreToolUse` hook (`.claude/hooks/pre_tool_guard.py`) that blocks `sudo`,
recursive force-delete, piping a download into a shell, force/main pushes,
and direct edits to protected paths (`code/data/`, `code/checkpoints/`,
`code/wandb/`, `reference/sources/raw|private/`, `.harness/private/`), and a
`PreCompact` hook (`.claude/hooks/pre_compact_memory_check.py`) that reminds
the agent to update `memory/current-status.md` before compacting.

`.claude/statusline.py` shows model, git branch, worktree status, and
session cost so session-boundary decisions happen before context runs out.

Codex has no equivalent subagent/hook/settings layer today; treat
`.agent/model-routing-policy.md` and `.agent/action-boundary.md` as the
routing/boundary source of truth there.

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
