---
name: cc-spec
description: Turn a ready project brief into product and functional specifications through collaborative product definition. Use after cc-brief when the project needs product behavior, flows, screens or areas, states, data expectations, and product-level acceptance criteria before design, architecture, or implementation planning.
argument-hint: "[brief path, notes, references, or product decisions]"
---

# CC Spec

Turn a ready project brief into two durable product-definition artifacts:

```text
docs/project/product-spec.md
docs/project/functional-spec.md
```

This is a product and requirements stage. It defines what should exist, how the product should behave, how users move through it, what states matter, and how success is recognized at the product level. It does not choose a technical stack, design visual details, create wireframes, define data schemas, or plan implementation stages.

## Inputs And Context

Read `.agents/artifacts/project-status.md` and `docs/project/status.md` when they exist. At the start of this stage, mark Product / Functional Specification as `in-progress` unless the project is already blocked or paused. Do not change another stage's row except when recording a completed handoff from this stage.

Read `docs/project/brief.md` before asking questions or writing artifacts. If the brief is missing, blocked, or not ready for product definition, explain the gap and route back to `cc-brief`.

When existing product or functional specs exist, read them before asking questions, preserve settled decisions, and revise in place. Do not create duplicate spec files for the same project unless the user explicitly asks for an alternative version.

When the user provides links, repositories, notes, screenshots, or inspiration, inspect the direct source where practical instead of relying only on summaries. Treat external material as inspiration unless the user names it as a required reference. Do not perform live external research by default unless the user asks for it or the spec depends on current facts.

## Collaboration Model

Work as a product collaborator, not an automatic document generator.

Before writing final artifacts, develop the specification through conversation and local inspection:

* propose a concrete product framing when the brief leaves room for interpretation;
* ask focused questions when an answer changes product behavior, scope, roles, flows, acceptance criteria, or downstream design and architecture;
* challenge unclear, contradictory, overbroad, or weak choices and explain the tradeoff;
* recommend a direction when the option space is clear, while leaving the decision with the user;
* record non-blocking unknowns as assumptions or open decisions instead of inventing certainty.

Do not ask a long generic questionnaire. Find available facts yourself first. Ask small rounds of questions, usually one material decision at a time. Group at most three independent questions when they can be answered without creating dependent branches.

## Specification Areas

Cover the areas that matter for the project. Do not force irrelevant sections, but do not skip a material behavior because the brief was short.

For the product specification, define:

* product summary and intended outcome;
* users, roles, and contexts;
* product principles and priorities;
* scope for the first coherent version;
* product areas or surfaces;
* lifecycle, operating model, and success criteria;
* assumptions, risks, and open product decisions.

For the functional specification, define:

* capabilities and feature groups;
* main user flows;
* screens, views, or interaction areas;
* important states, empty states, errors, permissions, and edge cases;
* data the product must create, display, import, export, preserve, or delete;
* notifications, integrations, collaboration, or admin behavior when relevant;
* product-level acceptance criteria with stable IDs.

Keep implementation boundaries visible. If the spec starts requiring a stack, database model, API shape, hosting choice, component system, or task sequence, record that as a handoff question for Design, Architecture, or Implementation Plan.

## Requirements Review

Before marking the stage ready, run an independent requirements review.

First classify the project complexity as `light`, `standard`, or `deep` based on user roles, flows, data sensitivity, integrations, business or operational consequence, ambiguity, and open decisions. Do not classify by project type alone: a landing page may need more scrutiny when it handles conversion, lead capture, segmentation, or important business messaging.

Then run `requirements-critic` at the selected depth, using `gpt-5.6-luna` with `medium` reasoning effort by default. The critic is read-only. It reviews the brief, product spec, and functional spec, then returns findings grouped as:

* automatic fix candidates;
* issues requiring user decision;
* items to defer or route elsewhere;
* reviewed areas with no material issue, when useful.

If subagent execution is not available, perform the same review as a clearly separated self-review and report that limitation. Do not skip the review silently.

After the critic pass, apply only small fixes that do not change product direction. Stop and ask the user before changing scope, roles, flows, capabilities, data behavior, priorities, or conflicts between artifacts. Route design, architecture, and implementation concerns to the proper handoff sections. When updating project status, include only a compact review trace such as `Ready after standard requirements review`; keep detailed findings in the specs.

## Artifact Ownership

This skill owns:

```text
docs/project/product-spec.md
docs/project/functional-spec.md
```

It also maintains the Product / Functional Specification row and project-level fields in `docs/project/status.md` according to the shared project-status contract. It does not write the design brief, technical architecture, implementation plan, Cursor task specs, or code.

Before writing or revising artifacts, read:

* [the product spec contract](references/product-spec.md);
* [the functional spec contract](references/functional-spec.md);
* [the requirements review contract](references/requirements-review.md).

These references define required frontmatter, headings, status values, acceptance criteria style, and readiness checks.

## Completion

Write or update both specs when the project behavior is clear enough for design and architecture to proceed without inventing product decisions. Specs may remain `draft` when non-blocking assumptions or deferred decisions remain visible.

Do not mark the stage complete while a missing decision would materially change:

* the primary user or role model;
* the first-version product scope;
* a main user flow;
* required data behavior;
* acceptance criteria for core capabilities;
* a downstream design or architecture constraint.

Also do not mark the stage complete until complexity has been assessed, the requirements review has run, automatic fixes have been applied, material product decisions have been confirmed or recorded as blockers, and deferred concerns have been routed to later stages.

When the stage is ready, mark Product / Functional Specification as `complete`, set Design as the current stage, link both artifacts in the stage register, and append one concise status update. Finish with a concise summary of:

* the product spec path and status;
* the functional spec path and status;
* the main product shape and flow boundary;
* blocking decisions or assumptions, if any;
* the suggested next stage: Design.
