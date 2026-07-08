# Paper Agent Guide

This file is the paper-component entry point. Root `memory/boards/` remains the
durable claim/evidence source of truth.

## Rules

- Paper-facing claims must link back to root claim and evidence objects.
- Keep figure/table captions separate from internal provenance notes.
- Store raw CSVs, plotting scripts, and internal result descriptions outside
  author-visible paper source unless cleaned for release.
- If `tex-fmt` is used, run check mode first and format only when requested.
- Use Overleaf or CI logs as compile evidence when that is the configured
  backend.
