---
name: subagent-routing
description: Choose child-agent budget, paths, and evidence requirements from repo-local routing policy before delegation.
allowed-tools: Read, Glob
---

# Subagent Routing

Use this skill before launching child agents for non-trivial work.

1. Read `.agent/model-routing-policy.md`.
2. Classify risk, blast radius, uncertainty, context pollution, reversibility,
   and evidence standard.
3. Produce a launch packet with agent type, budget tier, owned paths, forbidden
   paths, evidence required, and stop/escalate condition.
4. After the child returns, record whether the chosen tier was too high, too
   low, or appropriate when that feedback matters.

Main-agent quality may be high. Child-agent budget should be task-shaped.
