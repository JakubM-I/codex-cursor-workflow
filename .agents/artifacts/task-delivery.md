# Task Delivery Contract

Task delivery is a repeatable implementation loop after the implementation plan is ready. A task is not accepted merely because Cursor reports that it wrote code.

## Responsibility Boundary

| Activity | Owner |
| --- | --- |
| Choose the next slice and write or revise the task specification | Codex |
| Implement the bounded code change | Cursor |
| Lightweight, explicitly permitted self-checks | Cursor |
| Acceptance tests, integration and runtime checks, independent review, and evidence assessment | Codex |
| Update task history, delivery log, project status, plan, and upstream artifacts | Codex |
| Approve material product, design, architecture, cost, security, or launch changes | User |

Cursor may report a conflict or a delivery insight, but it must not silently resolve a decision owned by Codex or the user.

## Delivery Loop

1. Codex reads the current project state, relevant upstream artifacts, the implementation plan, and unresolved delivery-log implications.
2. Codex creates one Cursor-ready task specification for the next smallest verifiable slice. A milestone may require more than one task.
3. Cursor implements only that contract and returns its implementation report.
4. Codex records the handoff, runs the verification specified for the task, and reviews the change against the original contract.
5. Codex either accepts the task, sends a focused revised task specification for the same scope, or routes a material issue to the owning project artifact and user when approval is needed.
6. Codex appends a delivery record, records downstream implications, and updates the plan or source artifact before preparing the next task whenever an implication is material.

## Task Contract And Revision

`docs/tasks/TASK-*.md` is the implementation contract. Its scope, acceptance criteria, and decision boundaries are frozen when its status becomes `ready-for-cursor`.

Codex alone may revise an unaccepted task. It increments `revision`, adds a compact revision note, and records why the next Cursor attempt needs a different contract. It must not overwrite the original intent without preserving that reason. A changed scope, product decision, architecture, design direction, or acceptance criterion is not a routine revision: update the owning artifact first and obtain user approval when that artifact requires it.

## Acceptance And Follow-Up

Codex accepts a task only when the required verification evidence supports every applicable acceptance criterion and no unresolved blocker remains. A passing lightweight Cursor self-check is useful evidence, not acceptance.

For each accepted, blocked, or materially revised task, Codex appends a record to `docs/project/delivery-log.md` with:

* task ID, revision, milestone, status, and date;
* verification evidence and remaining limitations;
* deviations and decisions actually made;
* downstream implications marked `none`, `pending`, or `applied`; and
* the next action and any required user decision.

Before the next task specification, Codex reads open `pending` implications. It applies them to the relevant future milestone, task context, or owning source artifact; it does not rely on conversation memory.
