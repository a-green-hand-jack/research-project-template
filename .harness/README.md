# Project Harness Runtime

`.harness/` is the project-local agent/runtime layer.

It is not durable research memory. Durable research state belongs in `memory/`,
component docs, and production artifacts. This directory stores the local
capabilities and policies that let agents activate components, validate the
project, and recover project structure without depending on an external skill
repository.

## Contents

- `manifest.yaml` records template version, component activation state, skill
  install policy, and validator registry paths.
- `lifecycle.yaml` defines progressive phases from idea to submission.
- `blueprints/` contains offline scaffolds for components that are activated
  later.
- `scripts/activate-component.py` copies a blueprint into the project and marks
  the component active.
- `skills/` contains the project-local skill pack installable by `npx skills`.
- `validators/` records project-local validator hooks and future custom checks.
- `private/` is ignored local-only space for machine notes and private
  overrides.
