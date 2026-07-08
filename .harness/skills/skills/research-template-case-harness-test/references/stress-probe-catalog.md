# Stress Probe Catalog

Use this catalog after the generated research-project case has a clean
baseline. Run destructive probes only in disposable copies or throwaway
branches. Keep each probe focused enough that a pass/fail result identifies one
template contract.

## Core Probe Matrix

| Area | Mutation | Expected behavior |
| --- | --- | --- |
| Template mode | Change `.harness/manifest.yaml` from `complete` to another mode. | `rph validate .` should fail. |
| Component activation | Mark `code`, `paper`, or `reference` inactive while leaving complete-template files present. | Validator should reject required active components. |
| Missing component file | Remove a required code, paper, or reference scaffold file. | Validator should report the missing active component file. |
| Evidence link drift | Promote a claim to supported while pointing at a missing evidence id. | Validator should reject the missing link. |
| Claim-evidence reciprocity | Let `EVD-*.supports_claims` name a claim that does not include the evidence in `evidence_basis.supporting`, or the inverse. | Validator should reject asymmetric support links. |
| Contradiction reciprocity | Let `EVD-*.contradicts_claims` and `CLM-*.evidence_basis.contradicting` disagree. | Validator should reject asymmetric contradiction links. |
| Risk-action reciprocity | Let `RSK-*.actions` and `ACT-*.targets.risks` disagree. | Validator should reject asymmetric mitigation/action links. |
| Risk-claim reciprocity | Let `RSK-*.claims` and `CLM-*.reviewer_risks` disagree. | Validator should reject asymmetric review-risk links. |
| Evidence provenance | Add evidence without provenance, visibility, or inspection path. | Validator or case review should flag missing provenance. |
| Source visibility | Use a private source in a paper-facing claim without visibility policy. | Source visibility board or review should block promotion. |
| Schema version drift | Remove or change `schema_version` in a core YAML file or board. | Validator should reject unsupported or missing schema versions. |
| Experiment closure | Mark an experiment complete without commit, config, metric source, or artifact pointer. | Case review should classify as harness gap if validator misses it. |
| Artifact index | Reference a table, figure, checkpoint, or run output without an index entry. | Artifact review or future validator should catch the drift. |
| Paper claim drift | Add a paper-facing claim not represented in `memory/boards/claims.yaml`. | Paper review should block or create an upstream validator proposal. |
| Generated/private leakage | Commit paths covered by root `.gitignore` protected patterns. | Gitignore and review should prevent leakage. |
| Human gate bypass | Change venue, main claim, baseline, metric, or release surface without a gate record. | Change-control or human-gate review should fail. |
| Anatomy drift | Move a directory or ownership boundary without updating `ANATOMY.md`. | Anatomy drift control should catch the mismatch. |
| Skill routing | Ask for cross-component work without reading `harness-router` or relevant component entrypoints. | Handoff should classify routing friction if agents miss required state. |
| Blueprint repairability | Delete or corrupt a file under `.harness/blueprints/<component>/<variant>/`, especially Python entrypoints. | Validator should reject missing blueprint files or Python syntax errors. |
| Available component drift | Remove or rename `reviewer`, `rebuttal`, or `artifact` in `harness.yaml` or `.harness/manifest.yaml`. | Validator should reject missing available components and manifest/harness drift. |
| Reapplication safety | Re-run component activation over edited files without `--force`. | Script should refuse unsafe overwrites. |
| Branch CD boundary | Push template changes to a non-template branch and expect public template sync. | Workflow should not sync unless branch policy allows it. |
| Case repo remote boundary | Remove `.git`, unset `origin`, change the case branch, or leave the case HEAD different from the eval manifest. | Case-root eval should reject unverifiable local/remote state. |

## Report Format

Use this shape for each probe:

````markdown
### P<N>: <short name>

Mutation:
- `<path>`: <field or fragment changed>

Expected:
- <contract that should be enforced>

Commands:
```bash
<validator command>
<component check>
```

Actual:
- <exit code and key diagnostic>

Classification:
- upstream harness gap | generated template gap | case ledger debt |
  documentation friction | accepted regression fixture

Follow-up:
- <PR, issue, case cleanup, or no action>
````

## Interpreting Results

- Caught cleanly: keep as a regression idea or no-op.
- Caught with noisy diagnostics: propose diagnostic grouping only if noise hides
  the primary failure.
- Missed by component review but caught by `rph validate .`: decide whether the
  component check advertises itself as an independent gate.
- Missed by both review and validator: create an upstream harness PR or a
  precise proposal.
- Fails on a valid migrated case: classify as false positive, then fix upstream
  or narrow the case ledger.
