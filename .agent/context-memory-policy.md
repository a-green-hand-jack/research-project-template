# Context And Memory Policy

Chat context is short-term working memory. The repository is the system of
record.

## Layers

```text
chat/thread        immediate reasoning and coordination
memory/sessions/  bounded handoffs and session epilogues
research-artifact/staging/
                   unverified AI observations and tentative claims
memory/boards/    durable project graph used by agents
component docs     code, paper, reference, artifact, review, and release notes
```

## Rules

- Do not leave decisions, experiment results, or paper-facing claims only in
  chat.
- AI observations start in staging or low-certainty board states.
- Supported claims require evidence links, provenance, caveats, and visibility.
- Long logs and full papers should be summarized from paths, run ids, or
  bounded excerpts, not pasted into the main thread.
- Before compact, clear, or handoff, update `memory/current-status.md` or a
  session note with exact next steps and validation status.

## Fresh Context Triggers

Use a new session, plan, review pass, or worktree when:

- exploration turns into implementation
- implementation turns into final verification or paper promotion
- repeated failures are polluting the current reasoning context
- independent work has distinct ownership boundaries
- a remote, expensive, public, or irreversible action is under consideration
