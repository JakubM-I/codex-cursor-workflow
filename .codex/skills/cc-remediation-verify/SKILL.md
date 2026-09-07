---
name: cc-remediation-verify
description: Verify one Cursor-implemented remediation task, update its project findings and phase register, and route targeted revalidation or the next remediation task.
argument-hint: "[remediation task reference, task path, or Cursor implementation report]"
---

# CC Remediation Verify

Verify one remediation packet against its approved finding and correction contract. This skill is separate from `cc-task-verify`: acceptance proves the bounded correction only; `cc-project-verify` alone closes findings through project-level revalidation.

## Inputs

Read `AGENTS.md`, `.agents/artifacts/project-status.md`, `.agents/artifacts/project-verification.md`, the referenced remediation packet, `docs/project/project-verification-report.md`, `docs/project/remediation-plan.md`, and the current implementation. Read only the linked source artifacts necessary to assess the finding and regression boundary.

Confirm that the packet is `ready-for-cursor` or `implementation-reported`, and that the repository state can be attributed to it. Read [the remediation verification guide](references/remediation-verification.md) before assessing the change.

## Verification

Compare the actual change with the packet's scope before testing. Then run its targeted remediation verification plan. Recheck the original finding evidence and the named regression boundary; for visual work, inspect the cited viewports and states against approved visual evidence. Record reproducible commands, observations, and limitations.

Do not extend testing into a new project-wide audit. If the task's impact analysis says that a phase or project revalidation is needed, record that routing for `cc-project-verify` rather than claiming the project finding is closed.

## Outcomes And Records

Choose exactly one outcome:

* **accepted** — the bounded correction has evidence and no local blocker remains. Update the packet history and phase register. Mark each fully addressed finding `ready-for-revalidation`, not `closed`.
* **changes-required** — an in-scope correction is needed. Record a precise evidence-backed request in the packet and report, set the packet status accordingly, and stop for user approval. `cc-remediation-task-spec` prepares the next revision only after approval.
* **blocked** — missing access, environment, decision, or unprovable criterion prevents a reliable result. Record the smallest needed action and owner.

If every task in the active phase is accepted, set that phase to `ready-for-revalidation`, the plan to `revalidation-needed`, and route to `cc-project-verify`. Otherwise route to `cc-remediation-task-spec` for the next ready remediation task. Keep the project verification report and remediation plan consistent with the packet outcome.

Run `.agents/scripts/validate-project-artifacts.py` when available before reporting. Finish with the outcome, evidence, finding and phase states, limitation, and next skill.
