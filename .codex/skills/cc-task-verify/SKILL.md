---
name: cc-task-verify
description: Verify a Cursor-implemented task against its Task Spec, record the evidence, and accept it or issue a precise correction request. Use after Cursor reports implementation; do not create or revise Cursor instructions.
argument-hint: "[task ID, task path, or Cursor implementation report]"
---

# CC Task Verify

Verify the current implementation against the original Task Spec. This skill owns engineering verification, review, evidence, task acceptance, and milestone bookkeeping. It does not write a new Cursor contract: if corrections are needed, the user approves them and `cc-task-spec` creates the next revision.

## Inputs

Read `AGENTS.md`, the referenced `docs/tasks/M-<milestone>-<slug>/M-<milestone>-TASK-<number>-<slug>.md`, `.agents/artifacts/task-delivery.md`, `.agents/artifacts/delivery-log.md`, `docs/project/implementation-plan.md`, `docs/project/delivery-log.md`, and the current implementation. Read only the upstream project artifacts needed to interpret the task's acceptance criteria and constraints.

Confirm that Cursor's task revision is `ready-for-cursor` or `implementation-reported`. If the actual repository state cannot be attributed to the task because of unrelated changes, identify that boundary before testing or reviewing.

## Verification

Read [the verification guide](references/task-verification.md) before assessing the implementation. Run the task's Codex Verification Plan and any required project checks from `AGENTS.md`. Review against the frozen task contract, not merely against the diff or Cursor's self-check report.

Record the commands or other reproducible evidence, result, and limitations. Do not claim proof for an acceptance criterion that the evidence does not cover.

## Outcomes

Choose exactly one outcome:

* **accepted** — every applicable criterion is supported by evidence and no blocker remains. Update the task status and its Codex Delivery History, append the delivery-log record, and update its Task Delivery Register entry to `accepted`.
* **changes-required** — a code-level correction is needed within the frozen scope. Set the task status to `changes-required`; write a precise, evidence-backed correction request in its Codex Delivery History and the delivery log. Stop for user approval. Do not revise the contract yourself.
* **blocked** — missing access, environment, decision, prerequisite, or unprovable criterion prevents a reliable result. Set the task to `blocked`, record the smallest needed action and owner, and do not accept it.

If the evidence reveals a material change to product, design, architecture, security, cost, accounts, deployment, or release scope, mark the task blocked or changes-required as appropriate and route it to the owning artifact and user. Do not silently turn it into an implementation correction.

## Milestone Bookkeeping

After accepting a task, inspect its milestone Task Delivery Register. If another listed task remains, leave the milestone `in-progress` and name the next action: `cc-task-spec` for that task.

If every listed task is accepted, mark the milestone `complete` and append its concise completion note to the delivery log. This is not a new end-to-end or global test: it only confirms completion of the task map and absence of an open implication blocking the next milestone.

Run `.agents/scripts/validate-project-artifacts.py` when available before reporting the final outcome. Finish with the outcome, evidence, limitations, required user approval or next task, milestone state, and any downstream implications.
