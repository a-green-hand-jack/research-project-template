# Reference Component Anatomy

This component owns source intake, source cards, source processing status, and
project-use notes.

## Entry Surfaces

- `README.md` explains the source library boundary.
- `.agent/source-index.md` records source inventory.
- `.agent/processing-status.md` records ingestion and summarization progress.
- `.agent/metadata-gaps.md` records missing bibliographic or provenance data.

## Components

- `sources/` stores source pointers or small source metadata.
- `papers/` stores paper-specific notes or links.
- `cards/` stores structured source cards.
- `summaries/` stores source summaries.
- `notes/` stores transient reading notes.
- `project-use/` records how a source is used by this project.

## State

Source-derived claims must flow through evidence and provenance boards before
becoming supported project claims.

## Same-Change Rule

When a source supports, contradicts, or scopes a claim, update the relevant
claim, evidence, provenance, and visibility records.
