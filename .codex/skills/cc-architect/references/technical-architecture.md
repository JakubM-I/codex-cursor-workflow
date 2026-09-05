# Technical Architecture Contract

`cc-architect` owns `docs/project/technical-architecture.md`. The artifact describes the technical shape of the project in enough detail for implementation planning and later Cursor task specifications.

It is not a product specification, design document, exhaustive schema migration, deployment runbook, or low-level task list.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: technical-architecture
version: 1
status: draft
stage: architecture
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
stack:
  application: []
  data: []
  infrastructure: []
  testing: []
tags: []
---
```

Allowed `status` values:

* `draft` - architecture is in progress or non-blocking questions remain;
* `ready-for-implementation-planning` - technical direction is settled enough to plan implementation phases;
* `blocked` - architecture cannot proceed until a missing decision, source, tool, account, or constraint is resolved;
* `superseded` - another architecture artifact has replaced this one.

`sources` lists project artifacts, source repositories, user-provided links, service docs, examples, decisions, or other authoritative inputs that materially informed the architecture. `related` should include upstream product and design artifacts. `stack` summarizes the selected stack or constrained options for quick routing by later agents.

## Required Body

```md
# Technical Architecture: <Project Name>

## Architecture Summary

<A concise description of the selected technical direction and why it fits the product and design requirements.>

## Source Repository Findings

- <Repository or other source, what was inspected, and which architectural patterns or constraints should be reused or avoided.>

## Technical Requirements Derived From Product And Design

- <Requirement, source artifact or acceptance criterion, and architecture implication.>

## Stack Decision

### Selected Stack

- <Layer or concern>: <technology, service, framework, or constrained option>.

### Rationale

- <Reason tied to product behavior, design constraints, team capability, cost, deployment, risk, or maintainability.>

### Alternatives Considered

- <Alternative, why it was rejected or deferred.>

## Application Structure

<Major modules, boundaries, ownership areas, client/server split, routing direction, background jobs, realtime/offline behavior, and how the structure supports future Cursor tasks.>

## Data Architecture

<Core entities, ownership, relationships, persistence direction, migrations, import/export, retention, backup, privacy, and data integrity expectations at architecture level.>

## API, Contracts, And Integration Boundaries

<Internal APIs, external APIs, webhooks, files, queues, events, third-party services, rate limits, failure handling, and provider assumptions.>

## Authentication, Authorization, And Security

<Identity model, roles, permissions, sessions, secrets, sensitive data, threat assumptions, auditability, and security boundaries.>

## UX And Design-System Implementation Constraints

<Technical implications of approved screen structure, responsiveness, accessibility, component needs, media/assets, performance, motion, and design-system expectations.>

## Validation, Testing, And Quality Strategy

- <Test layer or validation check, what it proves, when it runs, and which acceptance criteria or risks it covers.>

## Deployment, Environments, And Operations

<Hosting, environments, build and release approach, configuration, secrets, migrations, monitoring, logging, analytics, backups, and operational ownership.>

## Developer Tooling And Setup

- <Required or recommended CLI, SDK, plugin, skill, service account, credential, local dependency, script, or workflow prerequisite.>

## Architecture Decisions

| ID | Decision | Status | Rationale | Owner |
| --- | --- | --- | --- | --- |
| ADR-001 | <Decision> | proposed | <Why this is the recommended choice.> | <Codex/user/team> |

## Risks And Tradeoffs

- <Risk, likelihood or impact when known, mitigation, and owner.>

## Assumptions To Validate

- <Unconfirmed technical assumption, why it matters, and how it can be validated.>

## Open Technical Decisions

- <Decision, why it affects architecture or implementation planning, and owner when known.>

## Handoff To Implementation Plan

<Implementation sequencing constraints, prerequisites, validation gates, and areas that should become project-level implementation stages.>
```

Omit sections only when genuinely irrelevant. Keep explicit `Not applicable` notes when a later stage could otherwise mistake omission for oversight.

## Writing Rules

* Tie technical choices to product behavior, acceptance criteria, approved design constraints, source repository evidence, and user constraints.
* Distinguish confirmed decisions from recommendations, assumptions, and open questions.
* Keep architecture at planning level: name major modules and data direction, but do not write complete schemas, endpoint specs, or low-level task lists unless the architecture decision requires that precision.
* Include testing and deployment strategy here because implementation planning needs to sequence validation and environment work.
* Do not use tool popularity as a reason. Explain fit, tradeoffs, implementation cost, and risk.
* Do not choose external services, auth providers, hosting, paid tools, or data providers silently when the choice affects cost, ownership, privacy, or account setup.

## Readiness Check

Set `status: ready-for-implementation-planning` only when all of these are true:

- [ ] Stack direction is selected or bounded with clear rationale.
- [ ] Application structure and major boundaries are understandable.
- [ ] Data architecture covers core entities, persistence, integrity, and retention concerns that matter.
- [ ] Required integrations and external service boundaries are visible.
- [ ] Auth, permissions, security, and privacy are covered or explicitly not applicable.
- [ ] Design-system and screen constraints that affect implementation are accounted for.
- [ ] Testing, validation, deployment, environment, and operations strategy are clear enough to plan work.
- [ ] Required tools, skills, plugins, accounts, credentials, and source repositories are listed with readiness status.
- [ ] Risks, assumptions, and open decisions are visible.
- [ ] No unresolved decision would materially change stack, data, auth, integration, deployment, or validation strategy.
