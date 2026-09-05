---
name: cc-architect
description: Define a project's technical architecture after brief, product/functional specification, and design are ready. Use when the project needs stack decisions, application structure, data direction, integrations, auth, testing, deployment, tooling readiness, or technical risk analysis before implementation planning.
argument-hint: "[project artifacts, stack constraints, source repo paths, integration notes, or technical decisions]"
---

# CC Architect

Turn approved product, functional, and design direction into a durable technical architecture for implementation planning.

This is a technical decision stage. It decides or documents the stack, application structure, data model direction, integration approach, authentication and authorization boundaries, validation strategy, deployment assumptions, required tooling, and known technical risks. It does not create implementation tasks, write production code, or override unresolved product or design decisions.

## Inputs And Context

Read `.agents/artifacts/project-status.md` and `docs/project/status.md` when they exist. At the start of this stage, mark Architect as `in-progress` unless the project is already blocked or paused. Do not change another stage's row except when recording a completed handoff from this stage.

Read these project artifacts before asking questions or writing architecture artifacts:

```text
docs/project/brief.md
docs/project/product-spec.md
docs/project/functional-spec.md
docs/project/design-brief.md
docs/project/screen-spec.md
docs/project/design-system.md
```

If product, functional, or design artifacts are missing, blocked, or not approved for architecture, explain the gap and route back to the owning stage. If the user has already fixed a stack or platform constraint, preserve it unless it conflicts with a material requirement; then surface the conflict and ask for a decision.

When source repositories, starter projects, examples, templates, or existing systems are referenced by the project artifacts or provided by the user, inspect them directly and extract as much practical architecture guidance as possible: conventions, package choices, deployment patterns, testing setup, data handling, auth model, integration boundaries, and operational constraints. Treat source repositories as stronger evidence than generic preferences, but do not copy project-specific assumptions that do not belong in the new project.

## Collaboration Model

Work as a technical architect and decision partner, not as a template filler.

Develop the architecture through inspection, option narrowing, and focused user interaction:

* derive technical requirements from product behavior, acceptance criteria, screen structure, design-system constraints, data expectations, and integration needs;
* identify ambiguous choices that affect cost, delivery speed, security, data safety, maintainability, hosting, or future implementation tasks;
* explain tradeoffs in plain language before asking the user to choose;
* recommend a direction when the evidence is strong, while recording why alternatives were not chosen;
* ask small rounds of questions, usually one material architecture decision at a time;
* record non-blocking unknowns as assumptions, constraints, or risks instead of inventing certainty.

Do not ask a generic architecture questionnaire. Inspect available artifacts and repositories first, then ask only questions whose answers would materially change the architecture.

## Tooling, Skills, And Plugin Readiness

Architecture is the stage where implementation-enabling tools become explicit.

Before finalizing the architecture, read [the technical readiness contract](references/technical-readiness.md). Identify:

* skills, plugins, CLIs, SDKs, frameworks, services, accounts, credentials, or environments required to implement the selected stack;
* helpful but optional tools that could speed up implementation, research, testing, deployment, or integration work;
* tools that are plausible but intentionally not needed for the chosen architecture.

When a useful skill or plugin is missing and can be installed or connected through Codex, tell the user what it would help with and ask whether Codex should install/connect it or whether the user will do it manually and confirm readiness. Do not install, connect, provision, deploy, or mutate external services without the user's authorization and the available tool support.

If a tool is unavailable, record the limitation and continue with the best available local workflow when the architecture can still proceed. Do not pretend an integration, account, repository, or service exists.

## Architecture Areas

Cover the areas that matter for the project. Do not force irrelevant sections, but do not skip a material concern just because earlier artifacts were short.

Define:

* stack and major technical choices;
* application structure and module boundaries;
* runtime, rendering, client/server, offline, realtime, or background-job approach when relevant;
* data model direction, persistence, migrations, ownership, retention, import/export, and backup considerations;
* integrations, external APIs, webhooks, files, email, payments, analytics, AI services, or other service boundaries;
* authentication, authorization, roles, permissions, sessions, identity providers, and security boundaries when relevant;
* API, contract, or event direction at a planning level;
* validation, test strategy, review gates, local checks, and observability;
* build, deployment, hosting, environments, secrets, configuration, and release assumptions;
* developer tooling, missing skills, missing plugins, and setup prerequisites;
* risks, constraints, tradeoffs, assumptions, and decisions that need user approval.

## Artifact Ownership

This skill owns:

```text
docs/project/technical-architecture.md
```

It also maintains the Architect row and project-level fields in `docs/project/status.md` according to the shared project-status contract. It does not write product specs, design artifacts, implementation plans, Cursor task specs, or production code.

Before writing or revising the architecture artifact, read:

* [the technical architecture contract](references/technical-architecture.md);
* [the technical readiness contract](references/technical-readiness.md);
* [the architecture review contract](references/architecture-review.md).

These references define required frontmatter, headings, status values, readiness checks, tool handling, and review expectations.

## Architecture Review

Before marking the stage ready, run an architecture readiness review.

Classify architecture complexity as `light`, `standard`, or `deep` based on product consequence, user roles, data sensitivity, integrations, auth complexity, migration risk, deployment complexity, compliance needs, performance risk, source-repository uncertainty, and number of major open decisions.

Review the architecture against:

* alignment with the brief, product spec, functional spec, and approved design artifacts;
* stack fit for the required behavior and design constraints;
* data safety, auth, permissions, and privacy expectations;
* integration feasibility and external-service readiness;
* testing, validation, deployment, and observability coverage;
* implementation readiness for the next planning stage;
* risks, assumptions, and user-owned decisions.

Use `.codex/agents/architecture-critic.md` when an independent reviewer is available and the project is `standard` or `deep`. For `deep` projects, add focused security, performance, deployment, or data review only when the risk justifies it and such reviewers are available. If subagent execution is unavailable, perform the same review as a clearly separated self-review and report that limitation. The reviewer is read-only and does not update artifacts or project status.

When a project artifact validator is available, run it before moving the architecture artifact to `ready-for-implementation-planning`. Treat validator failures as corrections for the owning stage artifact, not as permission to rewrite unrelated documents.

Apply only small clarity fixes automatically. Ask the user before changing stack family, hosting provider, database category, auth provider, integration provider, cost posture, security posture, or other major technical tradeoffs.

## Completion

Write or update the technical architecture when the project is clear enough for implementation planning to sequence work without inventing major technical decisions. The artifact may remain `draft` when non-blocking assumptions remain visible.

Do not mark the stage complete while a missing decision would materially change:

* the stack or runtime model;
* the application structure or ownership boundaries;
* the data model, storage, or migration direction;
* authentication, permissions, security, or privacy behavior;
* a required integration or external service;
* deployment, hosting, environment, or secret handling;
* the test and validation strategy needed for acceptance criteria.

When the stage is ready, mark the architecture artifact as `ready-for-implementation-planning`, mark Architect as `complete`, set Implementation Plan as the current stage, link the architecture artifact in the stage register, and append one concise status update. Finish with a concise summary of:

* the technical architecture path and status;
* the selected stack or stack constraints;
* key data, integration, auth, test, and deployment decisions;
* required or recommended tools, skills, plugins, accounts, or credentials;
* blocking decisions or assumptions, if any;
* the suggested next stage: Implementation Plan.
