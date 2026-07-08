---
description: Run the project harness validator and summarize failures
allowed-tools: Bash(rph validate:*), Bash(python -m research_project_harness validate:*)
---

Run `rph validate .` (or `python -m research_project_harness validate .` if
`rph` is not installed). Summarize errors and warnings grouped by code, and
list the exact next fix for each `ERROR`-level message. Do not attempt fixes
unless asked.
