# Architecture Review Contract

`cc-architect` uses this reference before marking Architecture complete. The review checks whether the technical direction is coherent, implementable, and aligned with upstream artifacts.

## Complexity Classification

Classify architecture complexity before review:

* **Light** - small scope, low data sensitivity, few integrations, simple auth or no auth, straightforward deployment, limited source-repository ambiguity.
* **Standard** - typical product with several modules, meaningful state, design-system expectations, some integrations or auth, and non-trivial validation needs.
* **Deep** - sensitive data, payments, healthcare/finance/legal implications, complex permissions, realtime/collaboration, migrations, multiple external services, high availability, AI/provider risk, compliance, or major uncertainty in source repositories.

Do not classify by product category alone. A small product can be deep when data, auth, or consequence is high.

## Review Inputs

Review against:

```text
docs/project/brief.md
docs/project/product-spec.md
docs/project/functional-spec.md
docs/project/design-brief.md
docs/project/screen-spec.md
docs/project/design-system.md
docs/project/technical-architecture.md
source repositories or reference implementations, when available
```

## Review Areas

Check:

* stack fit for product behavior, team constraints, design-system needs, deployment, cost, and maintainability;
* application boundaries, module ownership, and future task decomposition;
* data model direction, data integrity, migrations, import/export, backup, retention, and privacy;
* auth, authorization, sessions, permissions, secrets, and sensitive data handling;
* integration feasibility, failure handling, rate limits, service ownership, and provider lock-in;
* performance, accessibility, responsive behavior, media/assets, and design-system implementation constraints;
* testing layers, acceptance-criteria coverage, local validation commands, review gates, and observability;
* deployment, environment, secrets, configuration, release, rollback, and operational assumptions;
* missing tools, plugins, accounts, credentials, CLIs, SDKs, and source repositories;
* risks, tradeoffs, assumptions, and open decisions.

## Finding Groups

Return findings grouped as:

* **Automatic clarity fixes** - wording, traceability, missing rationale, or small consistency issues that do not change technical direction.
* **Needs user decision** - choices that affect stack, cost, ownership, privacy, auth, data, integration, deployment, or delivery strategy.
* **Needs source or tool readiness** - missing repository access, account, credential, plugin, skill, CLI, SDK, or service setup.
* **Defer to Implementation Plan** - sequencing details or task boundaries that do not change architecture.
* **No material issue** - reviewed areas that are adequate, when useful.

## Handling Findings

Apply automatic clarity fixes directly. Ask the user before changing any material technical decision.

If a finding exposes a missing upstream product or design decision, route it back to the owning stage instead of hiding it inside Architecture.

If a finding is an implementation sequencing concern, keep Architecture complete when the technical direction is sound and record the concern in `Handoff To Implementation Plan`.

Do not let a review pass, source-repository inspection, or tool-readiness check substitute for explicit user approval of major tradeoffs when those tradeoffs affect cost, account ownership, data sensitivity, or long-term maintainability.
