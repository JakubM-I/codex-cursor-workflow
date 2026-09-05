---
name: cc-plan
description: Create a stage-level implementation roadmap after technical architecture is ready. Use when a project needs ordered milestones, feature sequencing, dependencies, validation gates, and readiness for later Cursor task specifications without breaking work into low-level tasks.
argument-hint: "[project artifacts, architecture path, source repo paths, constraints, or planning notes]"
---

# CC Plan

Turn approved product, design, and architecture artifacts into a durable implementation roadmap.

This is a sequencing stage. It decides the order in which the system should be built, the major milestones or feature groups, the dependencies between them, the validation gates that matter, and the handoff shape for later Cursor task specifications. It does not write production code, create detailed task packets, override architecture, or turn the roadmap into a full backlog.

## Inputs And Context

Read `.agents/artifacts/project-status.md` and `docs/project/status.md` when they exist. At the start of this stage, mark Implementation Plan as `in-progress` unless the project is already blocked or paused. Do not change another stage's row except when recording a completed handoff from this stage.

Read these project artifacts before asking questions or writing the plan:

```text
docs/project/brief.md
docs/project/product-spec.md
docs/project/functional-spec.md
docs/project/design-brief.md
docs/project/screen-spec.md
docs/project/design-system.md
docs/project/technical-architecture.md
```

If the technical architecture is missing, blocked, or not `ready-for-implementation-planning`, explain the gap and route back to `cc-architect`. If product or design artifacts are missing or not approved enough for planning, route back to the owning stage instead of inventing missing decisions.

When source repositories, starter projects, examples, templates, existing systems, or previous delivery notes are referenced by the project artifacts or provided by the user, inspect them directly where practical. Extract implementation sequencing guidance such as setup order, module boundaries, bootstrapping steps, test layering, migration order, integration prerequisites, deployment constraints, and useful milestone patterns. Treat source repositories as evidence and inspiration, not as instructions to copy project-specific assumptions.

## Collaboration Model

Work as a delivery planning partner, not as a backlog generator.

Develop the roadmap through artifact inspection, source-repository analysis, option narrowing, and focused user interaction:

* derive milestone candidates from capabilities, user flows, screens, architecture boundaries, data dependencies, integrations, and validation strategy;
* identify dependency chains, risky prerequisites, and work that must happen before useful product slices can be built;
* recommend an order when the evidence is strong, and explain tradeoffs in plain language;
* ask the user to decide when sequencing affects launch strategy, delivery risk, cost, external accounts, scope priority, or what should be usable first;
* keep questions small, usually one material planning decision at a time;
* record non-blocking unknowns as assumptions, risks, or open planning decisions instead of pretending the plan is final.

Do not ask a generic project-management questionnaire. Read the artifacts and source material first, then ask only questions whose answers would materially change milestone order, scope, or readiness.

## Planning Areas

Cover the planning areas that matter for the project. Do not force irrelevant sections, but do not skip a dependency just because it feels operational rather than product-facing.

Define:

* implementation strategy and delivery depth;
* milestone order and rationale;
* feature grouping at project-stage level;
* foundational setup, scaffolding, data, auth, integrations, UI shell, core flows, verification, deployment, and launch-readiness work when relevant;
* dependencies and prerequisites for each milestone;
* acceptance criteria, design constraints, and architecture decisions each milestone must account for;
* validation gates and evidence expected before moving on;
* risks, assumptions, open planning decisions, and user-owned choices;
* which milestone or slice should become the first Cursor-ready task specification.

Keep the plan coarse. A milestone may mention candidate task slices when this clarifies sequencing, but do not decompose every milestone into implementation tasks. Detailed Cursor task packets belong to a later workflow stage.

## Artifact Ownership

This skill owns:

```text
docs/project/implementation-plan.md
```

It also maintains the Implementation Plan row and project-level fields in `docs/project/status.md` according to the shared project-status contract. It does not write product specs, design artifacts, architecture, Cursor task specs, implementation code, review reports, or fix packets.

Before writing or revising the plan, read:

* [the implementation plan contract](references/implementation-plan.md);
* [the planning review contract](references/planning-review.md).

These references define required frontmatter, milestone format, status values, readiness checks, and planning review expectations.

## Planning Review

Before marking the stage ready, run an implementation planning review.

Classify planning complexity as `light`, `standard`, or `deep` based on number of milestones, dependency depth, user roles, data sensitivity, auth and integration risk, deployment complexity, design-system complexity, migration risk, source-repository uncertainty, and consequence of sequencing mistakes.

Review the plan against:

* alignment with brief, product spec, functional spec, approved design artifacts, and technical architecture;
* whether milestones are ordered by real dependencies rather than narrative convenience;
* whether foundational setup enables useful vertical slices instead of becoming an endless platform phase;
* whether acceptance criteria, design constraints, architecture decisions, and validation gates are traceable;
* whether each milestone is coarse enough for roadmap planning but clear enough for later Cursor task specifications;
* whether missing accounts, credentials, source repositories, tools, or decisions are visible;
* whether the next stage can safely create the first task packet without inventing plan, architecture, or product decisions.

Use `.codex/agents/planning-critic.md` when an independent reviewer is available and the project is `standard` or `deep`. If subagent execution is unavailable, perform the same review as a clearly separated self-review and report that limitation. The reviewer is read-only and does not update artifacts or project status.

When a project artifact validator is available, run it before moving the plan artifact to `ready-for-task-specification`. Treat validator failures as corrections for the owning stage artifact, not as permission to rewrite unrelated documents.

Apply only small clarity fixes automatically. Ask the user before changing milestone order, first usable slice, launch scope, risk posture, or sequencing choices tied to cost, accounts, data safety, deployment, or external services.

## Completion

Write or update the implementation plan when the project can be sequenced without inventing major product, design, or architecture decisions. The artifact may remain `draft` when non-blocking assumptions remain visible.

Do not mark the stage complete while a missing decision would materially change:

* milestone order;
* the first usable product slice;
* foundational setup or scaffolding strategy;
* data, auth, integration, deployment, or migration sequencing;
* validation gates needed before later work;
* which milestone should become the first Cursor task specification.

When the stage is ready, mark the plan artifact as `ready-for-task-specification`, mark Implementation Plan as `complete`, set the project current stage to `complete` for the current greenfield planning scope, link the plan artifact in the stage register, and append one concise status update. Finish with a concise summary of:

* the implementation plan path and status;
* the recommended milestone sequence;
* the first Cursor task-specification candidate;
* key dependencies, prerequisites, and validation gates;
* blocking decisions or assumptions, if any;
* the suggested next workflow area: task specification for Cursor.
