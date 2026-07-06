# Model Routing Policy

Child-agent budget is determined by task shape, not by role prestige.

## Routing Dimensions

Classify delegated work by:

- risk: low, medium, high
- blast radius: read-only, narrow edit, shared contract, release/evidence
- uncertainty: lookup, bounded implementation, open-ended reasoning
- context pollution: small files, large logs, many files, cross-repo
- reversibility: local reversible, local git only, remote or expensive side effect
- evidence standard: summary, test output, claim-grade proof

## Budget Tiers

```text
tier 0: local shell/search, no child agent
tier 1: fast read-only lookup or log summary
tier 2: bounded implementation or targeted test
tier 3: architecture, hard debugging, shared contract edits
tier 4: final verifier, paper-facing claim, release or artifact gate
```

Use the cheapest tier that can satisfy the evidence standard.

## Launch Packet

For non-trivial delegated work, record:

```text
agent_type:
task:
budget tier:
allowed paths:
forbidden paths:
evidence required:
stop / escalate condition:
```
