# Implementation Plan Contract

`cc-plan` owns `docs/project/implementation-plan.md`. The artifact describes the project-level roadmap in enough detail for later Cursor task specifications.

It is not a backlog, sprint board, task packet, technical architecture, product specification, or code-generation prompt.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: implementation-plan
version: 1
status: draft
stage: implementation-plan
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/brief.md
  - docs/project/product-spec.md
  - docs/project/functional-spec.md
  - docs/project/design-brief.md
  - docs/project/screen-spec.md
  - docs/project/design-system.md
  - docs/project/technical-architecture.md
plan_depth: standard
tags: []
---
```

Allowed `status` values:

* `draft` - roadmap is in progress or non-blocking planning questions remain;
* `ready-for-task-specification` - roadmap is clear enough to create the first Cursor-ready task packet;
* `blocked` - planning cannot proceed until a missing decision, source, tool, account, or prerequisite is resolved;
* `superseded` - another implementation plan has replaced this one.

Allowed `plan_depth` values:

* `prototype` - fastest coherent path to a usable proof;
* `standard` - normal product build with validation gates and review;
* `high-assurance` - deeper staging for sensitive, costly, regulated, or operationally risky work.

`sources` lists project artifacts, source repositories, starter projects, user decisions, external references, or previous implementation notes that materially informed sequencing. `related` should include upstream artifacts, especially the technical architecture.

## Required Body

```md
# Implementation Plan: <Project Name>

## Plan Summary

<Concise description of the recommended build order and why this order fits the product, design, and architecture.>

## Source And Reference Findings

- <Repository, source, or note inspected, and which sequencing pattern or caution should be reused or avoided.>

## Planning Principles

- <Principle that affects ordering, scope, validation, or delivery depth.>

## Milestones

### M-001 - <Milestone Name>

Goal:

<What this milestone makes possible.>

Scope:

- <Project-stage level work included.>

Expected Result:

- <Observable product, technical, or workflow state after this milestone.>

Dependencies And Prerequisites:

- <Required upstream artifact, setup, decision, account, data, module, or previous milestone.>

Traceability:

- Acceptance criteria: <AC-001, AC-002, or `Not applicable`.>
- Functional areas: <F-001, Flow-001, screen names, or `Not applicable`.>
- Architecture decisions: <ADR-001 or `Not applicable`.>
- Design constraints: <Relevant design artifact section or `Not applicable`.>

Validation Notes:

- <What must be checked, demonstrated, reviewed, or recorded before moving on.>

Task-Specification Notes:

- <How this milestone should later be split into Cursor-ready task packets, if already visible at a coarse level.>

Risks Or Open Questions:

- <Risk, assumption, missing decision, or blocker tied to this milestone.>

## Dependency Map

- <Milestone or prerequisite> -> <Milestone that depends on it> because <reason>.

## Validation And Review Gates

- <Gate, what evidence it requires, and when it should run.>

## Tooling, Accounts, And Setup Prerequisites

- <Required or recommended skill, plugin, CLI, SDK, service account, credential, repository access, environment, or local setup action.>

## Launch Or Release Readiness

<What must be true before the first public/internal release, pilot, handoff, or demo.>

## Risks And Sequencing Tradeoffs

- <Risk or tradeoff, mitigation, and owner.>

## Assumptions To Validate

- <Unconfirmed planning assumption, why it matters, and how it can be validated.>

## Open Planning Decisions

- <Decision, why it affects sequencing, and owner when known.>

## Handoff To Task Specification

<Recommended first milestone or slice for task-spec creation, required context for that packet, and decisions Cursor must not invent.>
```

Omit sections only when genuinely irrelevant. Keep explicit `Not applicable` notes when a later stage could otherwise mistake omission for oversight.

## Milestone Rules

* Use stable milestone IDs in the form `M-001`, `M-002`, and so on.
* Milestones should be ordered by dependency and delivery value, not by document order in upstream specs.
* Prefer vertical product slices once the foundation is ready. Avoid a long foundation phase unless the architecture or risk profile makes it necessary.
* Each milestone should be large enough to explain a meaningful phase and small enough that a later task-spec stage can split it into one or more Cursor task packets.
* Include candidate task slices only when they clarify sequencing. Do not write task-level acceptance criteria, file lists, implementation prompts, or code instructions here.
* Link to stable IDs from functional specs and architecture when useful. Do not invent acceptance criteria or ADRs in the plan.

## Writing Rules

* Make dependencies explicit: data before UI when UI depends on persisted state, auth before protected flows, integrations before integration-dependent workflows, deployment setup before release validation.
* Distinguish confirmed decisions from recommendations, assumptions, open questions, and user-owned choices.
* Preserve architecture boundaries. If the plan requires changing stack, data model, auth, provider, deployment, or validation strategy, route back to `cc-architect`.
* Preserve product and design boundaries. If the plan requires changing scope, flows, screens, visual direction, or acceptance criteria, route back to the owning stage.
* Use source repositories as evidence for sequencing patterns, setup order, and validation strategy, not as a source of copied project assumptions.

## Readiness Check

Set `status: ready-for-task-specification` only when all of these are true:

- [ ] Milestones are ordered and have stable IDs.
- [ ] Each milestone has goal, scope, expected result, dependencies, validation notes, and task-specification notes.
- [ ] Dependency chains and prerequisites are visible.
- [ ] Acceptance criteria, functional areas, design constraints, and architecture decisions are referenced where useful.
- [ ] Required tools, accounts, credentials, repositories, setup actions, and readiness gaps are visible.
- [ ] Validation and review gates are clear enough to sequence implementation.
- [ ] Risks, assumptions, and open planning decisions are visible.
- [ ] The first Cursor task-specification candidate is identified.
- [ ] No unresolved decision would materially change milestone order, first usable slice, or validation strategy.
