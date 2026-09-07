---
name: cc-task-spec
description: Turn a ready implementation-plan milestone into a lightweight task map and prepare its next bounded Cursor task specification. Use after an implementation plan is ready; do not use to create every future detailed task spec in advance.
argument-hint: "[milestone ID, next task ID, or user-approved correction request]"
---

# CC Task Spec

Turn a ready milestone into a lightweight task map, then create only its next precise Cursor contract. This skill is intentionally just-in-time: the implementation plan is the durable roadmap; a task specification is the current, code-level instruction for Cursor.

Codex owns the task contract and its revision. `cc-task-verify` owns verification, review, delivery records, and acceptance. Cursor owns only the bounded implementation and the lightweight self-checks explicitly permitted in the task.

## Inputs And Readiness

Read `.agents/artifacts/project-status.md`, `.agents/artifacts/task-delivery.md`, `.agents/artifacts/delivery-log.md`, `docs/project/status.md`, `docs/project/implementation-plan.md`, and `docs/project/delivery-log.md` when they exist.

Before creating a task, inspect the selected milestone, the current repository state, the exact upstream artifacts and visual references needed by that slice, the architecture's test-ownership matrix and capability matrix, and every open delivery-log implication that could affect it. Do not create detailed specifications for later tasks merely because their task-map entries exist.

The implementation plan must be `ready-for-task-specification`. The selected milestone must have its prerequisites met and must not depend on an unresolved product, design, architecture, security, account, or deployment decision. Route such a gap to its owner instead of asking Cursor to invent it.

## Initialize Or Continue A Milestone

When the user starts a milestone for the first time, create its **Task Delivery Register** in `docs/project/implementation-plan.md` according to [the task specification contract](references/task-specification.md). It contains the planned full task references, short objectives, dependencies, delivery state, and the rule for completing the milestone.

This is a lightweight map, not several Cursor prompts. Reserve stable task IDs in the map when useful, but make their visible reference `M-<milestone>-TASK-<number>`. Write a complete `docs/tasks/M-<milestone>-<slug>/M-<milestone>-TASK-<number>-<slug>.md` only for the first ready task. Later task specifications are written after the preceding task is accepted and its relevant delivery implications have been applied.

When the user asks to continue a milestone, read its delivery register, task outcomes, and open implications. Create the next ready task specification or, after the user accepts a verified correction request, revise the identified task. Do not decide verification outcomes, mark a task accepted, or close a milestone; route those actions to `cc-task-verify`.

## Create Or Revise The Contract

Read [the task specification contract](references/task-specification.md) before writing or materially revising a task. Create it at `docs/tasks/M-<milestone>-<slug>/M-<milestone>-TASK-<number>-<slug>.md` using the milestone ID and next stable task ID.

Make the scope the smallest coherent slice that can be implemented and verified. One milestone may produce several task specifications. Define the task's completion boundary separately from wider feature completion, especially when later tasks provide integration, visual polish, or dependent flows. Include only the source context Cursor genuinely needs; links and precise sections are preferable to pasting the whole project history.

For each task, state permitted source areas, forbidden areas, known later dependencies, and any approved temporary arrangement. Do not tell Cursor to infer a missing design, architecture, integration, or test decision. For UI work, cite the approved visual reference and the exact view/state it governs; if no inspectable reference exists for a material visual decision, route back to Designer instead of asking Cursor to choose it.

List allowed Cursor self-checks separately from Codex verification. Reproduce the architecture's test ownership for this slice: Codex owns acceptance scenarios, E2E, browser/runtime, accessibility, visual, integration, and release evidence. Cursor may own only the narrow checks explicitly named in the task. A task must never imply that Cursor owns acceptance, broad tests, integration checks, runtime proof, independent review, project-status updates, or project documentation.

Set a new or revised task to `ready-for-cursor` only after its implementation boundaries, acceptance criteria, constraints, decision boundaries, and Codex verification plan are explicit. For a correction, preserve the prior contract, increment `revision`, and add a focused revision note saying exactly what Cursor must correct and what remains unchanged. Update project status to `task-specification` or `implementation` as appropriate, without duplicating the task contents there.

Before handing the task to Cursor, run `.agents/scripts/validate-project-artifacts.py` when available. Keep Git and user-approval handling consistent with the target project's `AGENTS.md` and closure contracts; do not infer authority for commits, external changes, or approval-sensitive decisions.

Finish by stating the milestone task map, the current task path and revision, its preconditions, and the next action: Cursor implementation or `cc-task-verify` after Cursor returns.
