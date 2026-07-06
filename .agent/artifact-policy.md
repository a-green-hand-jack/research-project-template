# Artifact Policy

Large, expensive, or paper-facing research assets must be indexed, not remembered
only in chat or session notes.

## Asset Classes

- raw runs and logs
- checkpoints and model exports
- datasets and processed splits
- figures and tables
- derived metric views
- artifact release bundles

## Required Fields

Each important asset should record:

- logical id
- owner action, experiment, or branch
- git commit
- config path
- data split or source
- storage path or URI
- checksum or version when practical
- inspection command
- status: active, superseded, archived, blocked, or unknown
- linked claims, evidence, or deliverables

## Hygiene

Do not commit large bytes unless the project explicitly allows it. Preserve
indexes, provenance, and inspection commands in git.
