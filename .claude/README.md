# Claude Code Project Assets

This directory holds Claude Code capabilities that are specific to this
project. They are repo-local so they are versioned, reviewed, and validated
with the rest of the project, instead of living in a user-global config.

- `agents/`: isolated-context subagents (own tool scope, own context window).
  Use these when a task should not pollute the main thread or needs a
  narrower tool/path scope. See `agents/README.md`.
- `settings.json`: permission allow/ask/deny lists and hook wiring that make
  `.agent/action-boundary.md` and `.agent/artifact-policy.md` mechanically
  enforced instead of prose-only.
- `hooks/`: the scripts `settings.json` wires into `PreToolUse`/`PreCompact`.
- `statusline.sh`: shows context/model/branch/worktree so session-boundary
  decisions happen before context is exhausted, not after.
- `commands/`: thin slash-command wrappers over the project skill pack in
  `.harness/skills/`.

Durable project state never lives here. It lives in `memory/`,
`research-artifact/`, component docs, or production artifacts. This
directory is machinery, not memory — see `.agent/context-memory-policy.md`.

For Codex, the same skill pack installs via
`npx skills add ./.harness/skills -a codex claude-code -y`, but Codex has no
equivalent to Claude Code subagents/hooks/settings.json today. If this
project is used from Codex, treat `.agent/model-routing-policy.md` and
`.agent/action-boundary.md` as the routing/boundary source of truth and
apply them manually until a Codex-native agent/hook layer exists.
