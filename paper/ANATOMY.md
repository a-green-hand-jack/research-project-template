# Paper Component Anatomy

This component owns paper source, paper-facing narrative, figures, tables, and
submission hygiene.

## Entry Surfaces

- `AGENTS.md` records paper-specific agent rules.
- `CLAUDE.md` is the Claude Code adapter for paper work.
- `main.tex` is the LaTeX root.
- `venue_preamble.tex` records venue-specific formatting.
- `macros.tex` owns reusable macros.

## Components

- `sections/` owns paper body text.
- `figures/` owns figure source notes and lightweight tracked assets.
- `tables/` owns table source notes and lightweight tracked assets.
- `bib/refs.bib` owns references.
- `.agent/` owns paper-local worktree status and paper-writing contracts.

## State

Every paper-facing empirical claim should trace to `memory/boards/claims.yaml`
and `memory/boards/evidence.yaml`. Visibility-sensitive sources must pass
`memory/boards/source-visibility.yaml`.

## Same-Change Rule

When paper text changes claims, citations, figures, tables, or artifact
references, update the corresponding board object or mark the text TODO.
