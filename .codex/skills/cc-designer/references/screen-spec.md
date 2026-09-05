# Screen Spec Contract

`cc-designer` owns `docs/project/screen-spec.md`. The artifact translates product behavior into a screen, view, or interaction-area inventory with layout purpose, information hierarchy, states, and cross-screen flow notes.

It is not a full visual mockup, component library, route map, technical architecture, or implementation task list.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: screen-spec
version: 1
status: draft
stage: design
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/brief.md
  - docs/project/product-spec.md
  - docs/project/functional-spec.md
  - docs/project/design-brief.md
---
```

Allowed `status` values:

* `draft` - screen structure is in progress or non-blocking questions remain;
* `ready-for-user-review` - Codex's proposed screen structure is ready for the user to inspect in the artifacts or visual workspace;
* `approved-for-architecture` - the user has approved the screen structure and states and they are clear enough for architecture and planning;
* `superseded` - another screen spec has replaced this one.

## Required Body

```md
# Screen Spec: <Project Name>

## Screen Inventory Summary

<A concise overview of the product's screens, views, or interaction areas and how they support the main flows.>

## Navigation And Information Architecture

<Primary navigation model, hierarchy, entry points, and cross-screen movement.>

## Screen Map

| ID | Screen Or Area | Purpose | Primary Users | Related Flows | Status |
| --- | --- | --- | --- | --- | --- |
| S-001 | <Name> | <Why it exists> | <Role/user> | Flow-001 | draft |

## Screens And States

### S-001 - <Screen Or Area Name>

Purpose:

<Why this screen exists in the product experience.>

Primary Users:

- <Role or user type.>

Related Product Areas, Features, And Flows:

- <Product area, F-001 capability, Flow-001, or AC-001 criterion.>

Layout And Hierarchy:

- <Main regions, content priority, visual grouping, and responsive changes.>

Primary Actions:

- <Action, control, or decision point.>

Visible Information:

- <Information, status, object, affordance, or feedback visible to the user.>

States:

- <Default, empty, loading, error, disabled, permission, completed, archived, pending, or other relevant state.>

Interaction Notes:

- <Important hover, focus, active, selection, drag, modal, navigation, transition, confirmation, or recovery behavior.>

Responsive Notes:

- <How this screen adapts across target viewports and input modes.>

Accessibility Notes:

- <Keyboard, focus, semantic structure, contrast, touch target, reduced motion, or assistive technology expectations.>

References:

- <Reference link or tool output and what it informed.>

Open Questions:

- <Question or decision that affects this screen.>

## Cross-Screen Patterns

- <Shared navigation, filtering, search, command patterns, empty states, error recovery, progressive disclosure, or content hierarchy.>

## Deferred Or Out-Of-Scope Screens

- <Screen or area intentionally excluded from the first version.>

## Handoff To Design System

<Components, tokens, and states implied by the screens.>

## Handoff To Architecture

<Screen-level constraints that may affect routing, rendering, data loading, performance, offline behavior, accessibility, or integrations without choosing the technical solution.>
```

Keep IDs stable once referenced by later artifacts. Use `S-001`, `S-002`, and so on for screens or interaction areas.

## Writing Rules

* Base screens on product flows and behavior, not on a generic app template.
* Include states that affect usability, trust, accessibility, or acceptance criteria.
* Make responsive behavior explicit enough that architecture can account for it.
* Record inspiration as reference evidence, not as a command to clone another product.
* Do not invent URLs, routes, components, schemas, services, or task order.

## Readiness Check

Set `status: ready-for-user-review` only when all of these are true:

- [ ] Main screens or interaction areas cover the product's core flows.
- [ ] Navigation and information architecture are understandable.
- [ ] Each core screen has purpose, users, related flows, layout hierarchy, actions, visible information, and states.
- [ ] Cross-screen patterns are visible.
- [ ] Responsive and accessibility notes cover material risks.
- [ ] Deferred or out-of-scope screens are explicit.
- [ ] No unresolved screen decision would materially change architecture or implementation planning.

Set `status: approved-for-architecture` only after the readiness check passes and the user explicitly approves the screen structure after reviewing the artifacts or chosen visual workspace.
