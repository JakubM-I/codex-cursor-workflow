# Design System Contract

`cc-designer` owns `docs/project/design-system.md`. The artifact defines the product's design-system direction: tokens, components, interaction states, accessibility constraints, and polish rules that later architecture and implementation planning must preserve.

It is not a production component implementation, package decision, CSS framework choice, or exhaustive brand manual.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: design-system
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
  - docs/project/screen-spec.md
---
```

Allowed `status` values:

* `draft` - design-system direction is in progress or non-blocking questions remain;
* `ready-for-user-review` - Codex's proposed design-system direction is ready for the user to inspect in the artifacts or visual workspace;
* `approved-for-architecture` - the user has approved the design-system direction and tokens, components, states, and constraints are clear enough for architecture and planning;
* `superseded` - another design-system artifact has replaced this one.

## Required Body

```md
# Design System: <Project Name>

## System Summary

<A concise description of the visual system, component philosophy, and how it supports the product experience.>

## Design Principles

- <Reusable rule that should guide component and visual decisions.>

## Token Direction

### Color

- <Core, semantic, status, and surface color direction with contrast expectations.>

### Typography

- <Type scale, hierarchy, numeric behavior, wrapping, line height, and readability expectations.>

### Spacing And Layout

- <Spacing scale, layout rhythm, grid or container expectations, density, and responsive rules.>

### Radius, Borders, Shadows, And Surfaces

- <Surface hierarchy, radius approach, borders, shadows, image outlines, and elevation.>

### Motion

- <Durations, easing, transition types, reduced-motion behavior, and where motion is allowed.>

### Iconography And Imagery

- <Icon style, stroke/fill behavior, image treatment, illustration/photo direction, and asset constraints.>

## Component Inventory

| Component | Purpose | Variants | Required States | Notes |
| --- | --- | --- | --- | --- |
| <Component> | <Why it exists> | <Variants> | <Default/hover/focus/active/loading/disabled/error/etc.> | <Design notes> |

## Core Components

### <Component Name>

Purpose:

<What this component enables in the product.>

Usage:

- <Where and when to use it.>

Variants:

- <Variant and intent.>

States:

- <Default, hover, focus, active, selected, loading, disabled, error, empty, expanded, collapsed, or other relevant state.>

Accessibility:

- <Name, role, keyboard behavior, focus, contrast, hit area, or assistive technology expectation.>

Responsive Behavior:

- <How it adapts across viewports and input modes.>

Implementation Constraints:

- <Design expectation architecture must account for, without choosing the implementation.>

## Interaction Patterns

- <Reusable pattern for feedback, confirmation, disclosure, selection, navigation, filtering, editing, drag, or modal behavior.>

## Accessibility Rules

- <Contrast, focus, keyboard, semantic, touch target, reduced motion, error messaging, and readability rules.>

## UI Polish Rules

- <Project-specific polish expectations, informed by `.agents/skills/make-interfaces-feel-better/` when available.>

## Optional Library Or Framework Considerations

- <When a component library may help and which qualities it must preserve, without selecting one unless the user or architecture already decided.>

## Assumptions To Validate

- <Unconfirmed design-system assumption and why it matters.>

## Open Design-System Decisions

- <Decision, why it affects design or downstream work, and owner when known.>

## Handoff To Architecture

<Design-system constraints that may affect stack, styling approach, rendering, accessibility, performance, assets, or package selection without deciding the stack.>

## Handoff To Implementation Plan

<Component, state, and polish expectations that should be reflected in implementation sequencing and later Cursor task specs.>
```

## Writing Rules

* Define design intent and constraints before naming libraries.
* Do not select a component library or CSS framework unless the user has already chosen it or the project has an existing stack.
* Use library recommendations as architecture inputs, not final architecture decisions.
* Include component states and accessibility requirements that later implementation must not forget.
* Keep visual-system rules specific enough to guide implementation, but not so specific that they become unapproved code.
* When `.agents/skills/make-interfaces-feel-better/` exists, incorporate its relevant polish principles without copying its full checklist into this artifact.

## Readiness Check

Set `status: ready-for-user-review` only when all of these are true:

- [ ] Token direction covers color, typography, spacing/layout, surfaces, motion, iconography, and imagery where relevant.
- [ ] Core components and variants are identified.
- [ ] Required states are listed for important components.
- [ ] Accessibility rules are explicit.
- [ ] UI-polish expectations are captured at the system level.
- [ ] Optional library considerations are framed as constraints or candidates, not hidden stack choices.
- [ ] No unresolved design-system decision would materially change architecture or implementation planning.

Set `status: approved-for-architecture` only after the readiness check passes and the user explicitly approves the design-system direction after reviewing the artifacts or chosen visual workspace.
