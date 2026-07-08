---
name: research-template-case-harness-test
description: Use a real research project case to stress-test the complete research-project-template, record template friction, and turn durable findings into upstream research-project-harness changes on the research-project-template branch.
allowed-tools: Read, Glob, Bash, Write
---

# Research Template Case Harness Test

Use this skill when testing `research-project-template` with a concrete paper,
repo, benchmark, dataset, or reproduction case, replaying a case after template
sync, or converting template friction into upstream harness changes.

For destructive probe ideas, read
`.harness/skills/skills/research-template-case-harness-test/references/stress-probe-catalog.md`
after the case has a clean baseline.

## Repository Roles

- Generated template or case repo: the project created from
  `a-green-hand-jack/research-project-template`.
- Upstream harness repo: `research-project-harness`.
- Persistent template, validator, workflow, or CI fixes belong upstream on the
  `research-project-template` branch, not as hand edits in the generated case.
- Case-specific claims, evidence, runs, paper edits, source cards, reports, and
  replay notes belong in the generated case repo.

## Inputs

- A concrete case source: existing repo, paper, arXiv id, benchmark, dataset,
  experiment log, or project brief.
- Existing template surfaces: `harness.yaml`, `.harness/`, `.agent/`,
  `memory/`, `human/`, `reference/`, `code/`, `paper/`, and component docs.
- Upstream harness checkout when proposing validator or template fixes.

## Declared Outputs

- `memory/boards/`
- `memory/current-status.md`
- `human/inbox/README.md`
- `human/reviews/results/`
- `reference/`
- `code/`
- `paper/`
- `docs/audits/`
- `docs/experiments/`
- `plans/`

## Validators

Run the smallest useful check during migration, then the full profile before
claiming a baseline:

```bash
rph validate .
```

If the case exercises runnable code or paper build paths, also run the relevant
component tests, linters, experiment dry runs, or LaTeX build commands and
record the exact commands in `human/reviews/results/` or `docs/audits/`.

## Workflow

1. Orient: confirm `pwd`, `git status -sb`, remotes, current branch, and the
   generated-template sync base.
2. Read `AGENTS.md`, `harness.yaml`, `.harness/manifest.yaml`,
   `memory/current-status.md`, and `ANATOMY.md`.
3. Create or select a case branch such as `case/<source>-template-replay`.
4. Import the case mechanically first. Preserve source provenance in
   `reference/`, `memory/boards/provenance.yaml`, and component notes before
   promoting facts.
5. Populate the smallest honest state needed for the case: claims, evidence,
   risks, actions, decisions, source visibility, experiment objects, artifact
   indexes, and paper locations.
6. Run `rph validate .` and relevant component checks. Commit a clean baseline
   separately from stress reports.
7. Stress only disposable copies or throwaway branches. For each probe, record
   mutation, expected contract, commands, actual diagnostics, classification,
   and follow-up.
8. For an upstream gap, work in `research-project-harness` from
   `origin/research-project-template`, fix the validator, template source,
   docs, tests, or workflow, validate, commit, and open a PR with base
   `research-project-template`.
9. After upstream merge and generated-template sync, replay the original case
   and append the result to the case report.

## Report Shape

Write case reports under `docs/audits/` or `human/reviews/results/`:

````markdown
# Template Case Harness Report

Case:
Baseline:
Commands:
Findings:
Upstream candidates:
Replay result:
Remaining debt:
````

Classify each finding as one of:

- upstream harness gap
- generated template gap
- case ledger debt
- documentation friction
- accepted regression fixture

## Completion Contract

- Baseline contract: the case validates with `rph validate .`, or each blocker
  has command output and an owner.
- Probe contract: destructive mutations happen only in disposable copies or
  throwaway branches.
- Fact contract: claims, numbers, citations, source summaries, and paper text
  are backed by repository evidence, not chat memory.
- Upstream contract: persistent fixes target `research-project-harness` branch
  `research-project-template`.
- Handoff contract: the final note names changed files, validators run,
  unresolved case debt, and any upstream PR or proposal.
