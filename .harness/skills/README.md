# Project-Local Skills

Install this local skill pack from the project root:

```bash
npx skills add ./.harness/skills -a codex claude-code -y
```

These skills are intentionally small project-local operating instructions. They
route agents through the harness contract and local activation workflow.

Core skills:

- `harness-router`: enter the project through component state and boards.
- `component-activator`: activate `reference`, `code`, or `paper`.
- `claim-evidence-review`: promote claims only with evidence and visibility.
- `experiment-workflow`: close the loop from claim to experiment to evidence.
- `paper-writing`: edit paper text from traceable evidence.
- `artifact-indexing`: index large or paper-facing assets.
- `anatomy-drift-control`: keep structural maps synchronized.
- `session-boundary-control`: checkpoint, branch, compact, or hand off cleanly.
- `worktree-pr-flow`: isolate non-trivial or parallel edits.
- `subagent-routing`: choose child-agent budget by task shape.
- `interactive-plan-doc`: create durable human-agent plans.
- `recipe-harvesting`: turn repeated workflows into tested cookbook recipes.
- `research-template-case-harness-test`: replay real research cases against
  this template and feed durable gaps back to the upstream harness branch.
