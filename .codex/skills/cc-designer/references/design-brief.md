# Design Brief Contract

`cc-designer` owns `docs/project/design-brief.md`. The artifact describes the product's UX and visual direction as a coherent experience: what it should feel like, which references informed it, what tradeoffs guide design choices, and what constraints downstream architecture and planning must respect.

It is not a functional specification, technical architecture, implementation plan, or final production component library.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: design-brief
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
---
```

Allowed `status` values:

* `draft` - design direction is in progress or non-blocking questions remain;
* `ready-for-user-review` - Codex's proposed design direction is ready for the user to inspect in the artifacts or visual workspace;
* `approved-for-architecture` - the user has approved the UX and visual direction and it is clear enough for architecture and implementation planning;
* `superseded` - another design brief has replaced this one.

`sources` lists user-provided assets, screenshots, links, Mobbin references, MagicPath project links, generated assets, interviews, or other inputs that materially informed the design. `related` should include the product and functional specifications and the other design artifacts once they exist.

## Required Body

```md
# Design Brief: <Project Name>

## Design Summary

<A concise description of the intended experience, visual character, and primary UX outcome.>

## Experience Principles

- <Design principle or priority that should guide layout, interaction, and visual tradeoffs.>

## Audience And Use Context

<Who uses the product, where, with what intent, and what this implies for design.>

## Platform And Viewport Assumptions

- <Target platforms, viewport ranges, input modes, density expectations, and responsive priorities.>

## Visual Direction

### Personality

<The desired feel in concrete terms, tied to product goals and audience.>

### Typography

<Type hierarchy direction and readability expectations without requiring a final font unless decided.>

### Color

<Palette direction, contrast expectations, semantic color needs, and any brand constraints.>

### Spacing, Density, And Layout Rhythm

<How spacious, dense, editorial, operational, immersive, or compact the product should feel.>

### Imagery, Iconography, And Surfaces

<How images, icons, cards, panels, borders, shadows, and surface hierarchy should work.>

### Motion And Feedback

<When motion helps, when it should be restrained, and which interactions need feedback.>

## UX Structure

<The main navigation model, information architecture, and how users move through the product.>

## References And Inspiration

- <Reference name/link, what to adopt, what to avoid, and whether it is inspiration or a required reference.>

## Accessibility And Inclusive Design

- <Contrast, keyboard, touch target, reduced motion, readability, error recovery, localization, or assistive technology expectations.>

## Design Tooling And Deliverables

- <Tools used or planned, user actions needed, links to workspaces, and ownership of visual deliverables.>

## Assumptions To Validate

- <Unconfirmed design assumption, why it matters, and how it could be validated.>

## Open Design Decisions

- <Decision, why it affects design or downstream work, and owner when known.>

## Handoff To Screen Spec

<What the screen inventory and layout notes must follow.>

## Handoff To Design System

<What the component and token direction must follow.>

## Handoff To Architecture

<Design constraints that may affect stack, rendering, data, performance, accessibility, or integrations without choosing the technical solution.>
```

Omit empty optional detail only when the question was genuinely considered and does not apply. Prefer an explicit `Not applicable` note when a later stage could otherwise mistake omission for oversight.

## Writing Rules

* Tie visual choices to product goals, users, and flows.
* Use concrete design qualities instead of vague labels such as `modern`, `clean`, or `premium` without explanation.
* Distinguish confirmed brand direction from recommended direction and assumptions.
* Record what to adopt and avoid from references; do not copy another product wholesale.
* Do not select frontend frameworks, UI packages, database structures, routes, API contracts, or implementation tasks.
* Do not require a visual design tool unless the work actually needs that tool's output.

## Readiness Check

Set `status: ready-for-user-review` only when all of these are true:

- [ ] The design summary states the intended experience and visual direction.
- [ ] Experience principles support later tradeoffs.
- [ ] Audience and use context are reflected in density, layout, and interaction choices.
- [ ] Platform, viewport, and input assumptions are visible.
- [ ] Visual direction covers typography, color, spacing, imagery/iconography/surfaces, and motion where relevant.
- [ ] References explain what to adopt and avoid.
- [ ] Accessibility and responsive expectations are explicit.
- [ ] Tooling and deliverable ownership are clear enough to continue.
- [ ] No unresolved decision would materially change the design direction or downstream architecture constraints.

Set `status: approved-for-architecture` only after the readiness check passes and the user explicitly approves the design direction after reviewing the artifacts or chosen visual workspace.
