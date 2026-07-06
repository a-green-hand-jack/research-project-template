---
name: recipe-harvesting
description: Convert repeated human-agent workflow traces into reviewable project-local cookbook recipes.
allowed-tools: Read, Glob, Write
---

# Recipe Harvesting

Use this skill to turn repeated successful or painful workflows into durable
repo-local recipes.

1. Read `.agent/workflow-recipe-policy.md`.
2. Inspect session traces, plan files, diffs, verification logs, and handoffs.
3. Propose a recipe only when it is linked to concrete evidence.
4. Record preconditions, steps, evidence, evals, metrics, counterexamples, and
   expiration date.
5. Keep candidates out of current practice until retested.
6. Record human acceptance or rejection as a decision or review note.

Do not promote a recipe from memory or intuition alone.
