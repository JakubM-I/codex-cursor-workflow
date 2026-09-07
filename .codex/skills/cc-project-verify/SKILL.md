---
name: cc-project-verify
description: Verify a completed project's cross-cutting behavior, design, architecture, and delivery evidence; report findings, plan approved remediation, and revalidate the resulting project.
argument-hint: "[verify project | continue after user decision | revalidate remediation]"
---

# CC Project Verify

Own the closing verification workflow after planned implementation delivery. This skill is not a replacement for `cc-task-verify`: it assesses the project as a whole, creates durable project findings, and owns the remediation roadmap. It does not prepare a detailed Cursor remediation packet or verify an individual Cursor implementation.

## Readiness And Inputs

Read `AGENTS.md`, `.agents/artifacts/project-status.md`, `.agents/artifacts/project-verification.md`, `docs/project/status.md`, the implementation plan, the delivery log, and the current repository state. Read the product, functional, design, architecture, and asset artifacts only to the extent needed to establish traceability and verification scope. Read `.agents/artifacts/stage-closure.md` when updating a target project's stage status.

For an initial audit, confirm that the planned delivery work is complete or that the user explicitly wants an early audit with known incomplete scope. Do not quietly treat milestone bookkeeping as project-wide proof.

For revalidation, read the prior report, remediation plan, the completed remediation packets, their verification histories, and the defined impact scope. Do not repeat the entire initial audit unless the evidence, a cross-cutting change, or the user requires it.

Before working, read [the project-verification contract](references/project-verification.md).

## Initial Verification And Review

Build a traceable verification scope from applicable acceptance criteria, approved visual references and states, architecture test ownership and risks, implementation-plan delivery expectations, and unresolved delivery-log implications. Use the smallest set of checks that can produce credible evidence; select integration, runtime, accessibility, visual, security, performance, deployment, and manual checks according to documented project risk rather than by a fixed universal checklist.

For UI work, compare the required viewport and states with approved design evidence. A passing selector, screenshot-free test, or source review is not visual-fidelity proof on its own.

Run an independent implementation and consistency review when the project complexity or consequence warrants it. Use `.codex/agents/project-verification-critic.md` as a read-only reviewer when available; otherwise perform a clearly labelled separated self-review and record that limitation. The review must distinguish an evidence-backed defect, an unproven criterion, a design mismatch, a delivery-process inconsistency, a risk, and subjective user feedback.

Create or update `docs/project/project-verification-report.md` using [the report contract](references/project-verification.md). Give each actionable finding a stable `PV-001`-style ID, source, evidence, impact, and recommended route. Do not invent a remediation decision or alter an upstream decision merely to close a finding.

## User Decision And Remediation Planning

If findings or feedback need a scope, priority, deferral, or material-decision choice, set the report to `awaiting-user-decision`, update project status, and stop. Present a concise decision list to the user; do not create remediation packets before approval.

After the user has approved the selected work, create or update `docs/project/remediation-plan.md` according to [the remediation-plan contract](references/project-verification.md). Group approved work into ordered `R-001`-style phases by risk, dependency, and retest boundary. Set the report to `remediation-in-progress` and the plan to `approved` or `in-progress` as work begins. Record deferred, rejected, and blocked findings explicitly. The plan is a phase roadmap, not a collection of Cursor prompts.

Set the next action to `cc-remediation-task-spec` for the first ready phase. Do not create a detailed remediation task here; that keeps project-wide audit context out of repeated task-authoring work.

## Revalidation And Completion

Run revalidation after a remediation phase is ready, a cross-cutting correction needs project-wide proof, or the user asks to close the project. Set the report to `revalidation-in-progress` and the plan to `revalidation-needed`, verify the closed findings and their declared impact areas, then update both artifacts.

Choose one outcome:

* `needs-further-remediation` — a finding persists, a regression appears, or new approved work is needed; set the report to `awaiting-user-decision` when scope changes, otherwise return it to `remediation-in-progress`.
* `ready-for-user-acceptance` — required revalidation evidence passes, the remediation plan is `complete`, and only the user's final acceptance remains.
* `completed` — the user accepts the final report, including any explicit deferrals and limitations.
* `blocked` — reliable verification cannot proceed because of a missing decision, environment, account, fixture, access, or other named prerequisite.

Run `.agents/scripts/validate-project-artifacts.py` when available before reporting an outcome. Follow the target project's Git and approval rules; do not infer authority for external actions.
