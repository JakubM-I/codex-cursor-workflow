---
name: cc-brief
description: Discover and pressure-test a new project's product direction through structured dialogue. Use after cc-init when the user provides a project idea, notes, or references and needs a durable project brief before product and functional specification, design, architecture, or implementation planning.
argument-hint: "[project idea, notes, or reference paths]"
---

# CC Brief

Turn the user's early project idea into a clear, durable project brief through conversation.

This is a discovery stage. It establishes why the project should exist, for whom, what outcome it should create, and the boundaries that protect its scope. It does not choose a stack, design screens, define detailed product behavior, write acceptance criteria, or plan implementation.

## Inputs And Context

Use the invocation, existing project entry point, and project materials already available in the repository as starting context. Treat user-provided or authoritative project documents as the source for product and business facts.

Read `.agents/artifacts/project-status.md` and `docs/project/status.md` when they exist. At the start of this stage, mark Brief as `in-progress` unless the project is already blocked or paused. Do not change another stage's row.

Do not infer target users, priorities, commercial constraints, legal obligations, or business rules from technical files, names, or conventions. Record anything not confirmed by the user or an authoritative source as an assumption.

When the user provides links, notes, or inspiration, inspect only material relevant to the idea. Do not perform live external research by default. Ask before it if the user has not already requested or authorized it.

## Conversation Flow

First, summarize the current understanding in plain language. Identify what is known, what is assumed, and which missing answers would materially change the project direction.

Classify the discovery depth from the current ambiguity and consequence:

* **Light** - a bounded idea with few material decisions; clarify only what the next stage needs.
* **Standard** - a typical new project with several connected product decisions; use `cc-grill` to pressure-test the direction.
* **Deep** - a strategic, high-risk, or highly ambiguous project; use `cc-grill`, explore credible alternative directions, and do not hide blocking decisions.

Use `cc-grill` whenever the user asks to pressure-test the idea or when the project is Standard or Deep. Treat its output as discussion support, not as a second artifact. This skill remains responsible for the brief.

Then guide the conversation through the applicable areas below. Cover each area deliberately, but do not force irrelevant questions or restart areas already settled by the user:

1. **Purpose and problem**: what is being built, what problem exists now, why it matters, and what change would make the project worthwhile.
2. **Users and context**: who experiences the problem, their situation, needs, motivations, and any distinct user groups.
3. **Desired outcome and priorities**: how success will be recognized, what matters most, and which tradeoffs the user is willing to make.
4. **Product direction**: the smallest credible shape of the solution and the capabilities it may need. Keep these as capability hypotheses, not a detailed feature specification.
5. **Scope boundaries**: what belongs in the first version, what is explicitly out of scope, and what should be deferred.
6. **Constraints and dependencies**: time, budget, compliance, data, integrations, assets, accounts, operational, or other constraints when they apply.
7. **References and inspiration**: examples to learn from, qualities to adopt or avoid, and whether they are inspiration or a required reference.
8. **Assumptions and decisions**: claims needing validation, contradictions, risks, and unresolved decisions that block a sound next stage.

Ask focused questions in small rounds. Prefer one decision at a time; group closely related questions only when that genuinely reduces turns. Explain why a question matters when its relevance is not obvious.

Pressure-test the idea as it becomes clear. Surface contradictions, vague success language, unbounded scope, missing users, unowned constraints, or a solution that does not address the stated problem. Present these as observations and options, not invented requirements. Do not silently settle material product decisions.

## Artifact Ownership

This skill owns one project artifact:

```text
docs/project/brief.md
```

It also maintains the Brief row and project-level fields in `docs/project/status.md` according to the shared project-status contract. It does not rewrite other stages' rows or own the status file's detailed history.

Create `docs/project/` only when the brief is ready to be saved. If a brief already exists, read it before asking questions, preserve settled information, and revise it in place. Do not create a separate functional specification, design brief, architecture document, implementation plan, task packet, or code.

Read [the project brief contract](references/project-brief.md) before writing or revising the artifact. It defines required frontmatter, headings, status values, and the readiness check.

## Completion

Write or update the brief when the dialogue has enough information for the next product-definition stage. A brief may remain `draft` when non-blocking assumptions or questions are still open. Do not claim it is ready for product and functional specification while a decision that changes the core user, problem, scope, or success outcome remains unresolved.

When the brief remains `draft`, keep Brief as `in-progress` or `blocked`, record only material blockers, and name the next discovery action. When it becomes `ready-for-functional-spec`, mark Brief as `complete`, set Product / Functional Specification as the current stage, link the brief in the stage register, and append one concise update entry.

Finish with a concise summary of:

* the resulting brief path and status;
* the central project direction and scope boundary;
* any blocking decisions or assumptions to validate;
* the suggested next stage: Product / Functional Specification.
