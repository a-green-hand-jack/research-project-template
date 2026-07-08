# Tool And Skill Interface

Project-local skills are workflow guides loaded into the main thread.
Subagents are isolated-context actors with their own tool scope. Hooks and
permissions are mechanical constraints. Validators are the executable source
of truth for deterministic checks. Do not collapse these into one layer.

## Project-Local Skills

The skill pack lives under `.harness/skills/` and may be installed with:

```bash
npx skills add ./.harness/skills -a codex claude-code -y
```

Use those skills to route common workflows, but write durable output into
`memory/`, `research-artifact/`, component docs, `human/`, or production
artifacts.

## Subagents, Permissions, And Hooks (Claude Code)

`.claude/agents/` holds isolated-context subagents (own tool scope, own
context window) for read-only research, bounded implementation, targeted
testing, experiment monitoring, checkpoint writing, subagent routing, session
boundary decisions, artifact indexing, and branch/worktree reporting. Use a
subagent instead of a skill when a task should not pollute the main thread,
or needs a narrower tool scope than the main agent has.

`.claude/settings.json` and `.claude/hooks/` make `action-boundary.md`
mechanical: dangerous commands and protected-path writes are denied or asked
for, not just documented. See `.agent/action-boundary.md`.

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
