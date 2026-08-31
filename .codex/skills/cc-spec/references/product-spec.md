# Product Specification Contract

`cc-spec` owns `docs/project/product-spec.md`. The artifact describes the product as a coherent whole: what should exist, who it serves, how it should feel operationally, and what counts as product success. It is not a functional detail dump, design brief, architecture document, or implementation plan.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: product-spec
version: 1
status: draft
stage: product-functional-spec
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/brief.md
---
```

Allowed `status` values:

* `draft` - product definition is in progress or non-blocking questions remain;
* `ready-for-design-and-architecture` - the product shape is clear enough for design and technical architecture;
* `superseded` - another product specification has replaced this one.

`sources` lists user-provided documents, links, repositories, interviews, screenshots, inspiration, or other authoritative inputs that materially informed the specification. `related` should include the brief and the functional specification once both exist.

## Required Body

```md
# Product Specification: <Project Name>

## Product Summary

<A concise description of the product, primary users, and intended outcome.>

## Product Context

<Why this product should exist, which problem or opportunity it addresses, and what current situation it changes.>

## Users And Roles

<Primary users, secondary users, roles, responsibilities, motivations, and relevant context.>

## Product Principles

- <Decision principle or priority that should guide future tradeoffs.>

## First-Version Scope

### In Scope

- <Product area or capability included in the first coherent version.>

### Out Of Scope

- <Adjacent product area explicitly excluded or deferred.>

## Product Areas

### <Area Name>

<What this area exists for and how users experience it at product level.>

## Product Lifecycle

<How a user, object, project, record, or workflow moves through the product over time.>

## Success Criteria

- <Product-level success criterion or observable outcome.>

## Constraints And Dependencies

- <Only known product, business, legal, operational, content, account, asset, or external constraints.>

## References And Inspiration

- <Reference, its role, and what to adopt or avoid.>

## Assumptions To Validate

- <Unconfirmed claim, why it matters, and how it could be validated when known.>

## Open Product Decisions

- <Decision, why it affects product behavior or downstream work, and owner when known.>

## Handoff To Functional Specification

<The product boundaries and priorities that functional behavior must follow.>

## Handoff To Design And Architecture

<Design and architecture constraints created by the product shape, without selecting visual or technical solutions.>
```

Omit empty optional detail only when the question was genuinely considered and does not apply. Prefer `No external dependencies identified yet` over removing a section that later stages expect to check.

## Writing Rules

* Keep this document at product level. Put detailed capabilities, flows, states, data behavior, and acceptance criteria in `docs/project/functional-spec.md`.
* Distinguish confirmed facts from assumptions.
* Keep scope boundaries explicit. A deferred item is not a failure; it protects the first version.
* Preserve the user's language for important domain concepts when it improves clarity.
* Record product decisions that downstream stages must not silently reinterpret.
* Do not insert stack choices, schemas, components, routes, API contracts, implementation tasks, estimates, or delivery dates unless they are confirmed product constraints.

## Readiness Check

Set `status: ready-for-design-and-architecture` only when all of these are true:

- [ ] The product summary names the product's purpose and intended outcome.
- [ ] Users, roles, and relevant context are clear enough to reason about behavior.
- [ ] Product principles or priorities support tradeoffs.
- [ ] First-version scope and out-of-scope boundaries are understandable.
- [ ] Main product areas and lifecycle are described at product level.
- [ ] Success criteria are observable enough to guide later validation.
- [ ] Known constraints, references, assumptions, and open decisions are visible.
- [ ] No unresolved decision would materially change the product's core shape.
