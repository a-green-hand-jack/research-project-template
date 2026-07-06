---
name: experiment-workflow
description: Plan, launch, monitor, and close ML experiments through claims, evidence, and artifact indexes.
allowed-tools: Read, Glob, Bash
---

# Experiment Workflow

Use this skill when planning, launching, monitoring, or closing an experiment.

## Phases

1. Map the target claim and evidence gap.
2. Create or update the experiment object in `memory/boards/experiments.yaml`.
3. Confirm commit, config, data split, baseline, metric, runtime estimate, and
   failure signals.
4. Get explicit approval before remote, expensive, or irreversible execution.
5. Monitor within a bounded window.
6. Write a run summary and update artifact indexes.
7. Propose evidence updates, including negative or contradicting results.
8. Run `rph validate .`.

Never promote a result to paper-facing status unless it has run id, commit,
config, metric source, artifact path, caveats, and visibility.
