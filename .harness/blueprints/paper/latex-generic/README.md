# Paper Component

This component owns paper source, venue-specific formatting, paper-facing
figures and tables, compile backend policy, and source visibility.

## Layout

```text
README.md
AGENTS.md
CLAUDE.md
.gitignore
main.tex
macros.tex
venue_preamble.tex
sections/
  title.tex
  abstract.tex
  intro.tex
  related.tex
  method.tex
  exp.tex
  conclusion.tex
  limitations.tex
  acknowledgement.tex
  appendix.tex
figures/
tables/
bib/refs.bib
.agent/worktree-status.md
```

## Compile Backend

Record the durable compile backend for this paper or worktree:

- `local`
- `Overleaf-GitHub`
- `CI`
- `unknown`

Do not record machine-specific TeX paths in committed docs.

## Source Visibility

Track whether the active paper source is agent-private, author-visible,
anonymous-submission, public-preprint, camera-ready-public, or publisher
artifact. Public or author-visible branches must not include private paths,
reviewer strategy, raw CSVs, internal provenance ledgers, or agent-only notes.

`main.tex` should stay stable across venue mode changes. Put venue package and
submission/camera-ready toggles in `venue_preamble.tex`.
