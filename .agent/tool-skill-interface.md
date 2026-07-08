# Tool And Skill Interface

Project-local skills are workflow guides. Validators are the executable source
of truth for deterministic checks.

## Project-Local Skills

The skill pack lives under `.harness/skills/` and may be installed with:

```bash
npx skills add ./.harness/skills -a codex claude-code -y
```

Use those skills to route common workflows, but write durable output into
`memory/`, `research-artifact/`, component docs, `human/`, or production
artifacts.

## Validators

The default validator is:

```bash
rph validate .
```

If a skill describes an invariant, add a validator rule, test fixture, or
reviewable checklist where practical. Do not rely on natural-language skill text
for important safety or release boundaries.

## External Tools

External systems such as GitHub, clusters, cloud storage, email, and publishing
surfaces are side-effect boundaries. Use the smallest read-only query first and
open a human gate before mutating remote or public state.
