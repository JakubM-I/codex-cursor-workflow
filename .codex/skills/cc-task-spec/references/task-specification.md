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

`revision` starts at `1` and is incremented only by Codex before a new Cursor implementation attempt. `milestone` references one implementation-plan milestone. `sources` identifies the artifacts, repository facts, prior delivery records, and user decisions used to prepare this exact task.

## Required Body

```md
# TASK-001 - <Task Name>

## Objective

<The observable outcome this small slice must create.>

## Scope

In scope:

- <Required change.>

Out of scope:

- <Explicit non-goal that Cursor must not add.>

## Context And Source Of Truth

- <Exact source file, artifact, decision, or prior delivery record and the relevant section.>

## Preconditions And Current State

- <What must already exist or be true before implementation.>

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

## Codex Verification Plan

- <Tests, runtime proof, review, integration check, accessibility check, or inspection Codex will perform.>

## Cursor Handoff Format

- Files changed.
- Behavior implemented and criteria addressed.
- Self-checks run and results.
- Deviations, risks, assumptions, conflicts, and downstream observations.

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
- TASK-001 — <short objective>; depends on: <task IDs or `None`>; status: ready-for-cursor
- TASK-002 — <short objective>; depends on: TASK-001; status: planned
- Completion rule: every listed task is accepted and no delivery-log implication blocks the next milestone.
```

The register may reserve task IDs and describe their small objectives, but it must not become a collection of detailed Cursor instructions. Create the full specification for only the current ready task. If delivery exposes a genuinely necessary additional task, add it to the register with the reason before preparing its detailed specification.

Completing a milestone does not require a separate end-to-end or global test merely because it is the last task. `cc-task-verify` marks it complete after every listed task is accepted and no open implication blocks the next milestone. Broader product or release testing belongs to a later, explicitly defined validation stage.

## Ready-For-Cursor Check

- [ ] The task implements one coherent, verifiable slice of one ready milestone.
- [ ] Preconditions and source context are specific enough to avoid reloading unrelated project history.
- [ ] Scope and non-goals prevent opportunistic expansion.
- [ ] All behavior and edge cases needed for acceptance are explicit.
- [ ] Decision boundaries say what Cursor may decide and must escalate.
- [ ] Cursor self-checks are lightweight and explicitly separated from Codex verification.
- [ ] Codex verification can produce evidence for every acceptance criterion.
- [ ] Dependencies, assets, accounts, credentials, and prior delivery implications are ready or explicitly block the task.
