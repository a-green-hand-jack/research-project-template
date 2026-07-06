# Paper Component

Activation status: inactive.

This placeholder marks where the paper component will live. Activate it when the
project is ready for sustained paper drafting or venue-specific source files.

```bash
python .harness/scripts/activate-component.py paper --variant latex-generic
```

Run the command from the project root.

The full scaffold is already stored in
`.harness/blueprints/paper/latex-generic/`. Activation copies that scaffold here
and marks `paper` active in `.harness/manifest.yaml` and `harness.yaml`.

## Activated Shape

```text
paper/
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

When active, this component owns:

- LaTeX source, sections, bibliography, figures, and tables;
- paper-facing claims and narrative projection;
- venue mode, compile backend, anonymity, and source visibility policy;
- arXiv, camera-ready, and author-visible source cleanup.

Paper-facing claims must trace back to `memory/boards/claims.yaml` and
supporting evidence. Do not hide internal result provenance only in TeX comments.

Venue-specific variants can be added later under `.harness/blueprints/paper/`.
The generic variant keeps `main.tex` stable and puts venue mode or style-file
changes in `venue_preamble.tex`.
