# Agent Policy Index

These files are stable repo-local policy for agents. They are not research
evidence and they are not a substitute for `memory/boards/`.

- `anatomy-protocol.md`: how structural maps are maintained.
- `action-boundary.md`: which side effects need human approval.
- `context-memory-policy.md`: what belongs in chat, traces, staging, boards,
  and durable artifacts.
- `model-routing-policy.md`: how child-agent effort and context budgets are
  chosen.
- `artifact-policy.md`: how result, data, checkpoint, figure, and table assets
  are indexed.
- `human-gates.md`: how human approvals are represented and closed.
- `tool-skill-interface.md`: how project-local skills, tools, and validators
  interact.
- `session-boundary-protocol.md`: when to checkpoint, branch, compact, or move
  work to a fresh session.
- `worktree-policy.md`: how parallel implementation boundaries are chosen.
- `workflow-recipe-policy.md`: how cookbook practices are harvested, tested,
  promoted, or deprecated.
- `repo-documentation-topology.md`: where human docs, agent maps, structure
  maps, memory, and runtime files belong.
- `release-agent-boundary.md`: how to separate this outer development harness
  from any agent being built or released by the project.

If a behavior matters enough to become policy, add a validator, test, or
reviewable checklist where practical.
