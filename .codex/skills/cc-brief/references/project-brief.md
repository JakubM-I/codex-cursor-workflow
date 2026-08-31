# Project Brief Contract

`cc-brief` owns `docs/project/brief.md`. The artifact captures discovery and project direction. It is not a functional specification, technical architecture, design brief, or implementation plan.

## Frontmatter

Use this minimal frontmatter. Dates use `YYYY-MM-DD`.

```yaml
---
artifact: project-brief
version: 1
status: draft
stage: brief
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
---
```

Allowed `status` values:

* `draft` - discovery is in progress or non-blocking questions remain;
* `ready-for-functional-spec` - the core direction is sufficiently settled for product and functional specification;
* `superseded` - another brief has replaced this one.

`sources` lists user-provided documents, links, interviews, or other authoritative inputs that materially informed the brief. `related` is empty until another project artifact needs to be linked.

## Required Body

```md
# Project Brief: <Project Name>

## Project Summary

<A short description of the intended product and its primary outcome.>

## Problem And Opportunity

<The current problem, why it matters, and the opportunity to improve it.>

## Target Users And Context

<Primary users, relevant secondary users, their situation, needs, and motivations.>

## Desired Outcomes And Priorities

<What success looks like, what matters most, and important tradeoffs.>

## Initial Product Direction

<The smallest credible solution shape and capability hypotheses. This is not a detailed feature list.>

## Scope Boundaries

### In Scope

- <Project-level area included in the first version.>

### Out Of Scope

- <Adjacent area explicitly excluded or deferred.>

## Constraints And Dependencies

- <Only constraints or dependencies that are known and relevant.>

## References And Inspiration

- <Reference, its role, and what to adopt or avoid.>

## Assumptions To Validate

- <Unconfirmed claim, why it matters, and how it could be validated when known.>

## Open Decisions

- <Decision, why it blocks or affects the next stage, and the owner when known.>

## Handoff To Product / Functional Specification

<The product questions the next stage must turn into functional behavior, flows, and detailed capabilities.>
```

Omit empty optional sections only when the omission would not hide an unknown. For example, write `No external dependencies identified yet` instead of omitting the section when the question was considered but no dependency is known. Keep unknowns in **Assumptions To Validate** or **Open Decisions**, never as confident facts.

## Writing Rules

* Distinguish confirmed facts from assumptions. Use direct language such as `The user confirmed...` only when a source supports it.
* Describe outcomes and user needs before solution ideas.
* Keep capabilities at project-direction level. Detailed functions, user flows, roles, states, edge cases, and product acceptance criteria belong to Product / Functional Specification.
* Name explicit non-goals. They are scope protection, not a failure to plan.
* Keep references traceable. Do not copy private credentials, personal data, or sensitive material into the brief.
* Do not insert technical choices, frameworks, data schemas, screens, components, implementation tasks, or delivery dates unless they are a confirmed project constraint. Route their definition to later stages.

## Readiness Check

Set `status: ready-for-functional-spec` only when all of these are true:

- [ ] The project summary names a meaningful intended outcome.
- [ ] The primary user and the problem or need are clear enough to reason about behavior.
- [ ] Desired outcomes or priorities provide a basis for future tradeoffs.
- [ ] The initial product direction is bounded without becoming a feature specification.
- [ ] In-scope and out-of-scope areas make the first version's boundary understandable.
- [ ] Known constraints, references, assumptions, and open decisions are visible.
- [ ] No unresolved decision changes the core user, problem, scope, or success outcome.

If a core decision is unresolved, keep the brief as `draft`, explain the blocker, and continue discovery with the user.
