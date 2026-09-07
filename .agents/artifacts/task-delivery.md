# Task Delivery Contract

Task delivery is a repeatable implementation loop after the implementation plan is ready. A task is not accepted merely because Cursor reports that it wrote code.

## Responsibility Boundary

| Activity | Owner |
| --- | --- |
| Create a milestone task map and write or revise the current task specification | Codex via `cc-task-spec` |
| Implement the bounded code change | Cursor |
| Lightweight, explicitly permitted self-checks | Cursor |
| Acceptance-test design, executable acceptance/regression tests, integration and runtime checks, independent review, evidence assessment, and task acceptance | Codex via `cc-task-verify` |
| Update task history, delivery log, project status, plan, and upstream artifacts | Codex |
| Approve material product, design, architecture, cost, security, or launch changes | User |

Cursor may report a conflict or a delivery insight, but it must not silently resolve a decision owned by Codex or the user. A task is complete when its own frozen completion boundary is met; it is not incomplete merely because a later task is needed to complete a wider feature or user flow.

## Delivery Loop

1. `cc-task-spec` reads the current project state, relevant upstream artifacts, the implementation plan, and unresolved delivery-log implications.
2. On the first task of a milestone, it creates a lightweight task map for that milestone and one Cursor-ready task specification for its first smallest verifiable slice.
3. Cursor implements only that contract, uses only its permitted self-checks, and returns its implementation report.
4. `cc-task-verify` reviews the report as supporting evidence, checks the actual diff against scope, prepares or updates Codex-owned executable verification where needed, and reviews the change against the original contract.
5. It either accepts the task, returns a precise correction request for the user to approve, or routes a material issue to the owning project artifact and user when approval is needed.
6. After user approval of a correction request, `cc-task-spec` writes the focused revision for Cursor. After task acceptance, it prepares only the next ready task in the milestone map.
7. `cc-task-verify` records delivery implications and updates the plan or source artifact before the next task whenever an implication is material.

## Task Contract And Revision

`docs/tasks/M-<milestone>-<slug>/M-<milestone>-TASK-<number>-<slug>.md` is the implementation contract. Its scope, completion boundary, acceptance criteria, temporary arrangements, test ownership, and decision boundaries are frozen when its status becomes `ready-for-cursor`.

Every contract must make clear which project context Cursor may read, which source areas it may change, what it must leave untouched, and which integration work intentionally belongs to later tasks. A fake, placeholder, adapter, or other temporary arrangement is permitted only when the task names its purpose, observable behavior, replacement owner/task, and removal condition.

Codex revises an unaccepted task only after the user approves the verified correction request. `cc-task-spec` increments `revision`, adds a compact revision note, and records why the next Cursor attempt needs a different contract. It must not overwrite the original intent without preserving that reason. A changed scope, product decision, architecture, design direction, or acceptance criterion is not a routine revision: update the owning artifact first and obtain user approval when that artifact requires it.

## Acceptance And Follow-Up

Codex accepts a task only when the required verification evidence supports every applicable acceptance criterion and no unresolved blocker remains. A passing lightweight Cursor self-check and Cursor's implementation report are useful evidence, not acceptance. Codex owns executable E2E and other acceptance/regression coverage. Cursor may create or run a narrow test only when the Task Spec explicitly assigns that self-check; it never substitutes for Codex acceptance evidence.

For each accepted, blocked, or materially revised task, Codex appends a record to `docs/project/delivery-log.md` with:

* full task reference, revision, milestone, status, and date;
* verification evidence and remaining limitations;
* deviations and decisions actually made;
* downstream implications marked `none`, `pending`, or `applied`; and
* the next action and any required user decision.

Before the next task specification, Codex reads open `pending` implications. It applies them to the relevant future milestone, task context, or owning source artifact; it does not rely on conversation memory.

## Milestone Completion

A milestone remains `in-progress` while any task in its Task Delivery Register is planned, in progress, changes-required, or blocked. When `cc-task-verify` accepts the final listed task, it marks the milestone `complete` after checking only that every listed task is accepted and no open delivery-log implication blocks the next milestone.

This is a bookkeeping and traceability check, not an additional global, end-to-end, or release test. Such broader testing is performed only by a future, explicitly invoked validation workflow.
