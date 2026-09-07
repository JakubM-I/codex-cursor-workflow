# Cursor Task Specification Contract

`docs/tasks/M-<milestone>-<slug>/M-<milestone>-TASK-<number>-<slug>.md` is a bounded implementation contract prepared by Codex for Cursor. It is not a roadmap, backlog entry, change request without acceptance criteria, test report, or a substitute for project architecture.

For example, the first task of a Foundation milestone could be stored as `docs/tasks/M-001-foundation/M-001-TASK-001-initialize-project.md`. The milestone ID appears in both the folder and filename so a task remains identifiable when copied, linked, or listed outside its folder.

## Frontmatter

```yaml
---
artifact: cursor-task-spec
version: 1
status: draft
stage: task-specification
task_id: TASK-001
task_ref: M-001-TASK-001
revision: 1
milestone: M-001
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/implementation-plan.md
depends_on: []
tags: []
---
```

Allowed `status` values:

* `draft`;
* `ready-for-cursor`;
* `implementation-reported`;
* `verification-in-progress`;
* `changes-required`;
* `accepted`;
* `blocked`;
* `superseded`.

`task_ref` is the canonical human-visible reference used in task titles, Cursor handoffs, verification results, and delivery records. It must equal `<milestone>-<task_id>`, for example `M-001-TASK-001`. `revision` starts at `1` and is incremented only by Codex before a new Cursor implementation attempt. `milestone` references one implementation-plan milestone. `sources` identifies the artifacts, repository facts, prior delivery records, and user decisions used to prepare this exact task.

## Required Body

```md
# M-001-TASK-001 - <Task Name>

## Objective

<The observable outcome this small slice must create.>

## Scope

In scope:

- <Required change.>

Out of scope:

- <Explicit non-goal that Cursor must not add.>

## Completion Boundary And Dependencies

- This task is complete when: <its own observable completion condition.>
- Deliberately deferred: <later flow, integration, or polish not needed for this task, with owning task or milestone.>
- Permitted source areas: <directories/files or `Only those named below`.>
- Forbidden changes: <areas, documentation, dependencies, configuration, or `None beyond out-of-scope work`.>

## Context And Source Of Truth

- <Exact source file, artifact, decision, or prior delivery record and the relevant section.>

## Preconditions And Current State

- <What must already exist or be true before implementation.>

## Temporary Arrangements

- <`None`, or a declared fake, placeholder, adapter, seam, or temporary UI state: purpose, observable behavior, replacement task/owner, and removal condition.>

## Required Implementation Behavior

- <Concrete behavior, state handling, error handling, compatibility, or migration behavior.>

## Constraints And Decision Boundaries

- <Architecture, design, security, performance, data, naming, or compatibility constraint.>
- Cursor may decide: <small local implementation choice, or `None`.>
- Cursor must escalate: <decision it must not invent.>

## Acceptance Criteria

- <Source AC-001, or a clearly labelled task-local condition>: <Observable condition.>

## Allowed Cursor Self-Checks

- <Exact lightweight command or check; omit if no self-check is appropriate.>

Cursor must not write or run E2E, acceptance, browser/runtime, visual, accessibility, integration, or release coverage unless this section explicitly assigns one narrow self-check.

## Codex Verification Plan

- Acceptance scenario source: <architecture/spec scenario IDs or task-local observable scenarios.>
- Executable evidence Codex will create or update: <durable regression test, ephemeral probe, manual script, or `Not needed`, with reason.>
- Checks Codex will run: <tests, runtime proof, review, integration, accessibility, visual comparison, or inspection.>
- Environment readiness: <required runner, browser/device, account, fixture, command, and owner; or `Not applicable`.>

## Cursor Handoff Format

- Task reference: `M-001-TASK-001`.
- Files changed.
- Behavior implemented and criteria addressed.
- Self-checks run and results.
- Deviations, risks, assumptions, conflicts, and downstream observations.
- Temporary arrangements actually used and their named follow-up.

## Revision History

- Revision 1 — YYYY-MM-DD: Initial contract.

## Codex Delivery History

- <Added by Codex after Cursor handoff and verification. Link to delivery-log record.>
```

Do not fabricate an acceptance-criterion ID. When the upstream functional specification does not have one, write a task-local observable condition and explain the source link. File lists belong only when they are known constraints; do not force Cursor into guessed file changes.

## Milestone Task Delivery Register

When `cc-task-spec` starts a milestone, add this compact register below that milestone in `docs/project/implementation-plan.md`:

```md
Task Delivery Register:

- Delivery status: not-started | in-progress | complete | blocked
- M-001-TASK-001 — <short objective>; depends on: <task references or `None`>; status: ready-for-cursor
- M-001-TASK-002 — <short objective>; depends on: M-001-TASK-001; status: planned
- Completion rule: every listed task is accepted and no delivery-log implication blocks the next milestone.
```

The register may reserve full task references and describe their small objectives, but it must not become a collection of detailed Cursor instructions. Create the full specification for only the current ready task. If delivery exposes a genuinely necessary additional task, add it to the register with the reason before preparing its detailed specification.

Completing a milestone does not require a separate end-to-end or global test merely because it is the last task. `cc-task-verify` marks it complete after every listed task is accepted and no open implication blocks the next milestone. Broader product or release testing belongs to a later, explicitly defined validation stage.

## Ready-For-Cursor Check

- [ ] The task implements one coherent, verifiable slice of one ready milestone.
- [ ] Preconditions and source context are specific enough to avoid reloading unrelated project history.
- [ ] Scope and non-goals prevent opportunistic expansion.
- [ ] The completion boundary says why this slice is done even if wider work is deferred.
- [ ] Allowed and forbidden source areas, later dependencies, and any temporary arrangement are explicit.
- [ ] All behavior and edge cases needed for acceptance are explicit.
- [ ] Decision boundaries say what Cursor may decide and must escalate.
- [ ] Cursor self-checks are lightweight and explicitly separated from Codex verification.
- [ ] Test ownership, executable Codex evidence, and required runtime readiness are explicit.
- [ ] Codex verification can produce evidence for every acceptance criterion.
- [ ] Dependencies, assets, accounts, credentials, and prior delivery implications are ready or explicitly block the task.
