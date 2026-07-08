# Project Subagents

Execution layer — isolated read/write/test/monitor work:

- `repo-researcher.md`: read-only code/paper/reference/memory exploration.
- `feature-worker.md`: implement one bounded task in owned paths.
- `test-runner.md`: run an exact test/validation command and summarize.
- `experiment-monitor.md`: read-only health check of a run, log, or metric.
- `checkpoint-writer.md`: write `memory/current-status.md` before compact/handoff.

Maintenance/routing layer — keeps the main agent from relying on chat memory:

- `subagent-router-agent.md`: pick model/effort/tool budget before delegating.
- `session-boundary-agent.md`: decide checkpoint/branch/compact/clear/handoff.
- `artifact-librarian.md`: index datasets/checkpoints/tables/figures.
- `branch-reporter.md`: report branch/worktree state, read-only.

Each agent has a narrow `tools:` scope in its frontmatter and a written
boundary of what it must never do. If a workflow needs a new persistent
role, add it here through the same review path as any other repo-local
change — do not accumulate ad hoc roles only in chat.
