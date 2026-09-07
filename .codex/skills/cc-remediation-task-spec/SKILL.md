---
name: cc-remediation-task-spec
description: Turn one approved remediation phase into a lightweight task map and prepare its next bounded Cursor remediation task specification.
argument-hint: "[remediation phase ID, next task ID, or user-approved correction request]"
---

# CC Remediation Task Spec

Prepare the next bounded Cursor task for an approved remediation phase. This is intentionally separate from `cc-task-spec`: its source is an approved project-verification finding and remediation plan, not an implementation-plan milestone. Do not alter existing implementation Task Specs, milestone maps, or delivery records.

## Inputs And Readiness

Read `AGENTS.md`, `.agents/artifacts/project-status.md`, `.agents/artifacts/project-verification.md`, `docs/project/status.md`, `docs/project/project-verification-report.md`, `docs/project/remediation-plan.md`, the selected finding records, and the current repository state. Read only the upstream product, design, architecture, or delivery artifacts named by the selected finding or needed to define the change safely.

The remediation plan must be `approved` or `in-progress`. The selected `R-001` phase must have an approved finding, resolved prerequisites, and a task-map status that can progress. Do not turn a deferred finding or unresolved upstream decision into a Cursor task.

Before authoring, read [the remediation task contract](references/remediation-task-specification.md).

## Initialize Or Continue A Phase

When a phase starts, add its compact **Remediation Task Delivery Register** beneath that phase in `docs/project/remediation-plan.md`. Set the plan and phase to `in-progress` and the task-map status to `active`. The register maps the small task references needed for that one phase, dependencies, statuses, and the phase completion rule. It is not a restatement of the full project-verification report.

Write a complete packet only for the first ready task. After `cc-remediation-verify` accepts a task, read the phase register, its evidence, and the finding status; then prepare the next ready packet. After a user approves a correction request, revise only the identified remediation packet and increment its revision.

## Create Or Revise The Packet

Create the packet at `docs/remediation/R-<phase>-<slug>/R-<phase>-TASK-<number>-<slug>.md`. Make it the smallest coherent change that can resolve or advance a named `PV-*` finding without concealing a wider decision.

State the evidence-backed defect or approved feedback, required behavior, affected source areas, regression boundaries, and exact recheck that `cc-remediation-verify` will perform. Cite the approved visual reference for a visual finding. Preserve a clear out-of-scope boundary; a remediation packet must not become opportunistic cleanup.

Cursor may run only the explicitly listed lightweight self-checks. It must not update verification reports, remediation plans, task registers, project status, acceptance evidence, or upstream project documents. Set the packet to `ready-for-cursor` only when it has sufficient context and a concrete verification plan.

Run `.agents/scripts/validate-project-artifacts.py` when available. Finish by naming the phase map, current packet path and revision, findings addressed, and next handoff to Cursor or `cc-remediation-verify`.
