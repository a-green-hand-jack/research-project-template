# Workflow Recipe Policy

Cookbook practices are repo-local experimental recipes. They must be harvested
from traces, tested, and periodically retired or promoted.

## Recipe States

```text
candidate: trace-backed idea, not a default rule
provisional: has eval tasks and at least one successful retest
stable: cross-task evidence and current-practice adoption
deprecated: failed retest, product drift, or superseded by a simpler recipe
```

## Required Fields

Each durable recipe should include:

```yaml
id:
title:
status:
observed:
  date:
  product:
  version:
claim:
preconditions: []
steps: []
evidence:
  traces: []
  commits: []
evals: []
metrics: []
counterexamples: []
expires_at:
```

Do not promote a recipe from chat memory alone.
