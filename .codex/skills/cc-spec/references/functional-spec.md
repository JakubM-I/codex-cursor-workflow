# Functional Specification Contract

`cc-spec` owns `docs/project/functional-spec.md`. The artifact describes product behavior in enough detail for design, architecture, implementation planning, and later Cursor task specifications. It is not a technical architecture, UI design system, or implementation task list.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: functional-spec
version: 1
status: draft
stage: product-functional-spec
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/brief.md
  - docs/project/product-spec.md
---
```

Allowed `status` values:

* `draft` - functional definition is in progress or non-blocking questions remain;
* `ready-for-design-and-architecture` - the behavior is clear enough for design and technical architecture;
* `superseded` - another functional specification has replaced this one.

`sources` lists user-provided documents, links, repositories, interviews, screenshots, inspiration, or other authoritative inputs that materially informed the specification. `related` should include the brief and product specification.

## Required Body

```md
# Functional Specification: <Project Name>

## Functional Summary

<A concise behavior-focused description of what the product must let users do.>

## Roles And Permissions

<User types, access boundaries, ownership, collaboration, moderation, or admin behavior when relevant.>

## Capabilities

### F-001 - <Capability Name>

Description:

<What the capability does for the user.>

Users:

- <Role or user type.>

Behavior:

- <Expected product behavior.>

States And Edge Cases:

- <Important state, empty state, error, permission case, or exception.>

Acceptance Criteria:

- AC-001 - <Observable product-level criterion.>

## Main User Flows

### Flow-001 - <Flow Name>

Goal:

<What the user is trying to accomplish.>

Steps:

1. <User-visible step or system response.>

Success Result:

<What is true when the flow succeeds.>

Failure And Recovery:

- <Likely failure, blocked state, or recovery path.>

## Screens Or Interaction Areas

### <Screen Or Area Name>

Purpose:

<Why this screen or area exists.>

Primary Actions:

- <User action.>

Visible Information:

- <Information, object, status, or control visible to the user.>

States:

- <Empty, loading, error, disabled, completed, archived, pending, or other state.>

## Data Expectations

- <Data the product must create, display, import, export, preserve, update, delete, or protect.>

## Notifications, Integrations, And External Touchpoints

- <Only behavior-level expectations. Put provider choices and API details in Architecture.>

## Cross-Cutting Behavior

- <Search, filtering, history, auditability, accessibility expectations, localization, privacy, offline behavior, or other behavior that spans features.>

## Product-Level Acceptance Criteria

- AC-001 - <Criterion that later planning, implementation, verification, and review can reference.>

## Out Of Scope For Functionality

- <Feature or behavior explicitly excluded or deferred.>

## Assumptions To Validate

- <Unconfirmed functional assumption and why it matters.>

## Open Functional Decisions

- <Decision, why it affects behavior, and owner when known.>

## Handoff To Design

<Behavior, flows, screens, and states that design must account for.>

## Handoff To Architecture

<Behavioral requirements that may affect architecture, without choosing the technical solution.>
```

Omit sections only when genuinely irrelevant. Keep explicit `Not applicable` notes when a later stage could otherwise mistake omission for oversight.

## Acceptance Criteria Rules

* Use stable IDs in the form `AC-001`, `AC-002`, and so on.
* Criteria should be observable from product behavior. Avoid implementation language.
* Criteria may appear under capabilities and in the product-level list. Keep IDs unique across the file.
* If a criterion depends on an unresolved decision, mark it as provisional instead of hiding the dependency.
* Later implementation plans and Cursor task specs should reference these IDs where useful.

## Writing Rules

* Define behavior before screens when possible. Screens should serve flows, not replace them.
* Include edge cases that would materially affect UX, trust, data safety, or acceptance.
* Capture data expectations at product level without inventing schemas or storage details.
* Do not select tools, frameworks, database structures, providers, endpoints, component libraries, or implementation sequence.
* Challenge feature requests that conflict with the brief, product spec, or first-version scope. Record the agreed resolution.

## Readiness Check

Set `status: ready-for-design-and-architecture` only when all of these are true:

- [ ] Core capabilities are described with users, behavior, states, and acceptance criteria.
- [ ] Main user flows are clear enough to design and reason about.
- [ ] Screens or interaction areas cover the expected flows without becoming visual design.
- [ ] Important empty states, errors, permissions, and edge cases are visible.
- [ ] Product data expectations are clear at behavior level.
- [ ] Cross-cutting behavior is captured when relevant.
- [ ] Out-of-scope functionality is explicit.
- [ ] Open decisions and assumptions are visible.
- [ ] No unresolved decision would materially change core behavior or acceptance criteria.
