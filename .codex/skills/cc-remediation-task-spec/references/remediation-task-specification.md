# Remediation Task Specification Contract

Read this reference before creating or revising a remediation packet.

## Frontmatter

```yaml
---
artifact: cursor-remediation-task-spec
version: 1
status: draft
stage: remediation-task-specification
task_id: TASK-001
task_ref: R-001-TASK-001
revision: 1
remediation_phase: R-001
finding_ids:
  - PV-001
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
depends_on: []
tags: []
---
```

Allowed `status` values: `draft`, `ready-for-cursor`, `implementation-reported`, `verification-in-progress`, `changes-required`, `accepted`, `blocked`, `superseded`.

## Required Body

```md
# R-001-TASK-001 - <Task Name>

## Objective

<The smallest observable correction this task must make.>

## Findings And Evidence

- PV-001: <finding statement, evidence, and source link.>

## Scope

In scope:

- <Required correction.>

Out of scope:

- <Explicit non-goal.>

## Completion Boundary And Dependencies

- This task is complete when: <task-local outcome; it does not itself close the project finding.>
- Permitted source areas: <known files/directories.>
- Forbidden changes: <known exclusions.>
- Dependencies: <task refs, decision, environment, or `None`.>

## Context And Constraints

- <Only the report, source artifact, visual reference, and code facts needed by Cursor.>
- Cursor must escalate: <missing decision or ambiguity it cannot resolve.>

## Required Correction Behavior

- <Observable corrected behavior and regression boundary.>

## Acceptance Criteria

- PV-001: <observable task-level proof that the correction is present.>

## Allowed Cursor Self-Checks

- <Exact lightweight check, or `None`.>

## Codex Remediation Verification Plan

- Finding evidence to recheck: <exact failed/unproven evidence.>
- Checks `cc-remediation-verify` will run: <targeted test, runtime proof, visual comparison, or inspection.>
- Project revalidation trigger: <when and what `cc-project-verify` must recheck.>
- Environment readiness: <runner/device/account/fixture and owner, or `Not applicable`.>

## Cursor Handoff Format

- Task reference and revision.
- Files changed.
- Findings and criteria addressed.
- Self-checks run and results.
- Deviations, conflicts, and regression risks.

## Revision History

- Revision 1 — YYYY-MM-DD: Initial remediation contract.

## Codex Remediation Verification History

- <Added by `cc-remediation-verify`.>
```

## Phase Task Delivery Register

Add this beneath the active phase in `docs/project/remediation-plan.md`:

```md
Remediation Task Delivery Register:

- R-001-TASK-001 — <short correction>; findings: PV-001; depends on: `None`; status: ready-for-cursor
- R-001-TASK-002 — <short correction>; findings: PV-002; depends on: R-001-TASK-001; status: planned
- Completion rule: every listed task is accepted and every phase finding is ready for project-level revalidation.
```

The register maps work for one remediation phase only. A detailed packet is created only for the current ready task.

## Ready-For-Cursor Check

- [ ] Each named finding is approved and has evidence.
- [ ] The task is a small correction, not a project-wide cleanup request.
- [ ] Source context is limited to the correction and its regression boundary.
- [ ] Scope, non-goals, dependencies, and decision boundaries are explicit.
- [ ] Cursor self-checks are separated from Codex evidence.
- [ ] The individual retest and the later project revalidation trigger are explicit.
