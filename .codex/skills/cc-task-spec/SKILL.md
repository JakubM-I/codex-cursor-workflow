---
name: cc-task-spec
description: Turn the next implementation-plan slice into a bounded Cursor task specification, then coordinate Codex-owned verification and delivery follow-up. Use after an implementation plan is ready; do not use to create every future task spec in advance.
argument-hint: "[milestone ID, delivery insight, implementation report, or task path]"
---

# CC Task Spec

Convert only the next ready implementation slice into a precise Cursor contract and manage its delivery loop. This skill is intentionally just-in-time: the implementation plan is the durable roadmap; a task specification is the current, code-level instruction for Cursor.

Codex owns the task contract, verification, review, delivery records, and updates to project artifacts. Cursor owns only the bounded implementation and the lightweight self-checks explicitly permitted in the task.

## Inputs And Readiness

Read `.agents/artifacts/project-status.md`, `.agents/artifacts/task-delivery.md`, `.agents/artifacts/delivery-log.md`, `docs/project/status.md`, `docs/project/implementation-plan.md`, and `docs/project/delivery-log.md` when they exist.

Before creating a task, inspect the selected milestone, the current repository state, upstream artifacts referenced by that milestone, and every open delivery-log implication that could affect it. Do not create detailed specifications for later milestones merely because their roadmap entries exist.

The implementation plan must be `ready-for-task-specification`. The selected milestone must have its prerequisites met and must not depend on an unresolved product, design, architecture, security, account, or deployment decision. Route such a gap to its owner instead of asking Cursor to invent it.

## Create The Contract

Read [the task specification contract](references/task-specification.md) before writing or materially revising a task. Create it at `docs/tasks/TASK-<number>-<short-name>.md` using the next stable task ID.

Make the scope the smallest coherent slice that can be implemented and verified. One milestone may produce several task specifications. Include only the source context Cursor genuinely needs; links and precise sections are preferable to pasting the whole project history.

List allowed Cursor self-checks separately from Codex verification. A task must never imply that Cursor owns acceptance, broad tests, integration checks, runtime proof, independent review, project-status updates, or project documentation.

Set a new task to `ready-for-cursor` only after its implementation boundaries, acceptance criteria, constraints, decision boundaries, and Codex verification plan are explicit. Update project status to `task-specification` or `implementation` as appropriate, without duplicating the task contents there.

## Process An Implementation Handoff

After Cursor returns its implementation report, record the attempt in the task history and set the task status to `verification-in-progress`. Run the verification defined by the task: targeted and broader tests as appropriate, static checks, runtime inspection, integration checks, review against the original specification, and any project-specific checks required by `AGENTS.md`.

Read [the delivery-loop contract](references/delivery-loop.md) before deciding the outcome. Do not accept a task based solely on Cursor's report or a passing self-check.

When verification finds a code-level issue inside the frozen scope, write a focused revision, increment `revision`, set `changes-required`, and give Cursor the corrected contract. When the evidence reveals a material change to scope, acceptance criteria, product behavior, design, architecture, security, cost, accounts, deployment, or release strategy, first update or route to the owning project artifact and obtain user approval when required. Then prepare the next task revision from that corrected source of truth.

## Close The Delivery Step

For an accepted, blocked, or materially revised attempt, append a concise record to `docs/project/delivery-log.md` according to `.agents/artifacts/delivery-log.md`. Mark every implication as `none`, `pending`, or `applied`.

Before creating another task, resolve relevant pending implications. Apply a delivery-derived correction to the implementation plan when it changes milestone scope, order, dependencies, risks, or validation gates. Apply it to the owning product, design, or architecture artifact when it changes that artifact's decision. Mark the source change as delivery-derived and preserve its reason.

Run `.agents/scripts/validate-project-artifacts.py` before reporting a task accepted or ready for Cursor when that validator is available. Keep Git and user-approval handling consistent with the target project's `AGENTS.md` and closure contracts; do not infer authority for commits, external changes, or approval-sensitive decisions.

Finish by stating the task outcome, verification evidence, unresolved limitations, downstream implications, source artifacts changed, and next action.
