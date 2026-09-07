# Project Verification Artifact Contract

Read this reference before creating or updating a project verification report, remediation plan, or final revalidation result.

## Project Verification Report

Store the report at `docs/project/project-verification-report.md`.

```yaml
---
artifact: project-verification-report
version: 1
status: draft
stage: project-verification
verification_mode: initial
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
tags: []
---
```

Allowed `status` values: `draft`, `awaiting-user-decision`, `remediation-in-progress`, `revalidation-in-progress`, `ready-for-user-acceptance`, `completed`, `blocked`, `superseded`.

Allowed `verification_mode` values: `initial`, `targeted-revalidation`, `final-revalidation`.

Use this body shape:

```md
# Project Verification Report

## Verification Scope And Limitations

- Scope: <artifacts, flows, risks, viewports, integrations, and environments assessed.>
- Not verified: <unavailable evidence, with owner and required setup; or `None`.>

## Traceability And Evidence

| Source | Required proof | Evidence | Result | Limitation |
| --- | --- | --- | --- | --- |
| <AC, design reference, risk, or delivery implication> | <observable proof> | <command, review, screenshot, manual script, or report> | pass / fail / unproven | <None or limitation> |

## Findings

### PV-001 - <Short title>

- Classification: defect | unproven-criterion | design-mismatch | integration-risk | delivery-inconsistency | user-feedback
- Source and affected area: <artifact/reference and project area>
- Evidence: <reproducible result or review observation>
- Impact: blocking | high | medium | low
- Recommended route: remediation | upstream-decision | defer | no-action
- User decision: pending | approved | deferred | rejected
- Remediation status: open | planned | in-progress | ready-for-revalidation | closed | blocked | deferred
- Related remediation tasks: <R task refs or `None`.>

## Independent Review

- Scope and reviewer: <review coverage and independent reviewer or separated self-review.>
- Findings: <PV IDs or `None`.>
- Limitation: <None or why independent review was unavailable.>

## Revalidation History

- <Date and scope: evidence, findings closed/reopened, and remaining limitation.>

## Final Decision

- Outcome: <awaiting user decision | needs further remediation | ready for user acceptance | completed | blocked>
- Required user action: <decision, final acceptance, or `None`.>
```

Do not claim that an unrun check passed. Put visual comparison evidence in the traceability table or the finding itself. Findings stay in the report after closure so later users can reconstruct the decision.

## Remediation Plan

Store the plan at `docs/project/remediation-plan.md`.

```yaml
---
artifact: remediation-plan
version: 1
status: draft
stage: remediation
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
tags: []
---
```

Allowed `status` values: `draft`, `awaiting-user-decision`, `approved`, `in-progress`, `revalidation-needed`, `complete`, `blocked`, `superseded`.

Use this body shape:

```md
# Remediation Plan

## Decision Record

- Approved findings: <PV IDs.>
- Deferred or rejected findings: <PV IDs and user rationale.>
- Upstream decisions required: <artifact and owner, or `None`.>

## Remediation Phase Map

### R-001 - <Phase name>

- Goal: <risk-reducing outcome.>
- Findings: PV-001, PV-002
- Dependencies: <phase, decision, environment, or `None`.>
- Retest boundary: <project area that `cc-project-verify` must revalidate.>
- Delivery status: not-started | in-progress | ready-for-revalidation | complete | blocked
- Task map status: not-created | active | complete | blocked

## Cross-Phase Constraints

- <Regression boundary, release constraint, or `None`.>

## Completion Rule

Every approved finding is closed by project-level revalidation or is explicitly deferred by the user. No phase has an unresolved blocking dependency.
```

`cc-project-verify` creates the phase map. `cc-remediation-task-spec` later adds a compact task delivery register under the active phase; it must not replace the phase map or create detailed packets for future work.
