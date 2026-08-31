# Requirements Review Contract

`cc-spec` uses an independent `requirements-critic` pass before marking product and functional specifications ready.

The purpose is to catch blind spots without turning the process into a second specification stage. The critic reviews and reports; `cc-spec` remains responsible for deciding what to change, what to ask the user, and what to defer.

## Complexity Assessment

Before invoking the critic, classify the review depth as `light`, `standard`, or `deep`.

Use `light` when most of these are true:

* one primary user type;
* one or two simple flows;
* low-risk content or data;
* no accounts, payments, permissions, or sensitive user data;
* no required external integrations;
* few screens or product areas;
* limited business or operational consequence if behavior is imperfect;
* few assumptions or open decisions.

Use `standard` when any meaningful complexity appears:

* more than one important flow;
* more than one user type or role;
* user-created or business-relevant data;
* forms, submissions, notifications, imports, exports, or integrations;
* several screens, sections, or product areas;
* the product supports a real business, educational, operational, or content workflow;
* acceptance criteria must coordinate multiple capabilities;
* assumptions exist but do not create high risk.

Use `deep` when one or more high-consequence signals appear:

* payments, accounts, permissions, private data, regulated data, or safety-sensitive behavior;
* business-critical, legal, reputational, financial, or operational risk;
* many dependent flows or roles;
* multiple systems or external services;
* ambiguous or conflicting goals;
* many open assumptions or decisions;
* failure modes that could harm users, data integrity, trust, or business operations.

Do not classify only by project type. A landing page can need `standard` review if it has lead capture, segmentation, conversion logic, or important business messaging. A small internal tool can need `deep` review if it handles sensitive data or irreversible actions.

Record the assessment in working notes or in the final summary when useful:

```text
Complexity: standard
Reasons:
- two user roles
- three main flows
- user-generated data
Critic depth: standard
```

## Always Run The Critic

Run `requirements-critic` for every `cc-spec` completion attempt.

Use `gpt-5.6-luna` with `medium` reasoning effort by default. This is the normal configuration for `light` and `standard` reviews, and it is also acceptable for many `deep` reviews. Raise the model or reasoning effort only when the complexity assessment shows high consequence, ambiguity, sensitive data, compliance concerns, or many dependent flows.

The depth changes the scope and expected effort:

* `light` - concise blindspot pass focused on goal, user, scope, core flow, states, and acceptance criteria.
* `standard` - full requirements pass across roles, capabilities, flows, screens, data, edge cases, non-goals, and hidden decisions.
* `deep` - rigorous pass including decision dependencies, risk, privacy, negative scenarios, conflict analysis, and readiness to unblock Design and Architecture.

If subagent execution is unavailable in the current environment, run the same review as a clearly separated self-review and report that limitation. Do not skip the review silently.

## Handling Critic Findings

Classify every material finding before editing:

### Automatic Fix

Apply directly when the correction improves clarity without changing product direction. Examples:

* unclear wording;
* duplicate or weakly named section;
* missing obvious empty state or error state implied by an agreed flow;
* acceptance criterion that needs sharper observable language;
* missing cross-reference between product and functional specs;
* formatting or ID consistency.

### Requires User Decision

Stop and ask the user when the finding would materially change or choose:

* first-version scope;
* a user role or permission model;
* a main flow or success path;
* a required capability;
* data retention, deletion, export, privacy, or ownership behavior;
* a business rule, priority, or conversion goal;
* conflict resolution between brief, product spec, and functional spec.

Ask focused questions. Explain the tradeoff and recommend an option when the answer space is clear.

### Defer Or Route Elsewhere

Do not resolve inside `cc-spec` when the finding belongs to:

* Design - layout, visual hierarchy, component choices, responsive details, brand direction;
* Architecture - stack, data model, APIs, providers, hosting, authentication mechanism, storage;
* Implementation Plan - sequencing, milestones, task breakdown, effort;
* later validation - research, analytics, user testing, legal review, production metrics.

Record the routing in the relevant handoff or open decisions section when it affects downstream work.

### Reject

Reject findings that expand scope without evidence, contradict confirmed user decisions, duplicate existing content, or add process overhead without improving the specification. A brief reason is enough.

## Completion Gate

Do not mark `cc-spec` complete until:

- [ ] complexity has been assessed;
- [ ] `requirements-critic` has run at the selected depth, or a self-review fallback has been reported;
- [ ] automatic fixes have been applied;
- [ ] material product decisions have been confirmed by the user or recorded as blockers;
- [ ] deferred items are routed to the correct later stage;
- [ ] product and functional spec readiness checks pass.

## Status Update

Record only a compact review trace in `docs/project/status.md`. The status file should show that the stage passed requirements review and at what depth, but it should not contain the full critic report or detailed fix list.

Good examples:

```text
Ready after standard requirements review.
```

```text
Product and functional specifications completed after deep requirements review. Designer is next.
```

Put material findings, assumptions, open decisions, or deferred concerns in the product and functional specs themselves.
