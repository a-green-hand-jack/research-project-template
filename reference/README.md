# Reference Component

Activation status: inactive.

This placeholder marks where project-local sources and source cards will live.
Activate it when the project needs a durable source library.

```bash
python ../.harness/scripts/activate-component.py reference --variant source-library
```

When active, this component owns:

- raw or private source files under `sources/` and `papers/`;
- copyright-safe source cards under `cards/`;
- project implications under `project-use/`;
- processing status and scan/read trajectories under `.agent/`.

Do not copy long raw source text into public memory. Link durable claims and
evidence to sanitized cards or project-use notes.
