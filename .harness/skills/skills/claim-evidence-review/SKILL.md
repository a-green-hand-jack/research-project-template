---
name: claim-evidence-review
description: Review whether claims, evidence, visibility, and provenance are linked tightly enough for paper-facing use.
allowed-tools: Read, Glob, Bash
---

# Claim Evidence Review

Use this skill before upgrading a claim to `supported`, `paper-facing`, or
`final`.

1. Read `memory/boards/claims.yaml`, `memory/boards/evidence.yaml`,
   `memory/boards/provenance.yaml`, and `memory/boards/source-visibility.yaml`.
2. For each target claim, check falsification criteria, scope, assumptions,
   supporting evidence, contradicting evidence, reviewer risks, and paper
   locations.
3. Verify that paper-facing evidence has visibility and provenance.
4. Preserve caveats and negative results in `research-artifact/trace/`.
5. Record required follow-up actions in `memory/boards/actions.yaml`.
6. Run `rph validate .`.

Do not promote an AI observation directly into a supported claim without
evidence or human confirmation.
