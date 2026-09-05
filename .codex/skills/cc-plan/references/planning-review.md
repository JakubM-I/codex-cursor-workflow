# Planning Review Contract

`cc-plan` uses this reference before marking Implementation Plan complete. The review checks whether the roadmap is coherent, dependency-aware, and ready to be turned into focused Cursor task specifications.

## Complexity Classification

Classify planning complexity before review:

* **Light** - small project, few milestones, shallow dependencies, simple data, little or no auth, few integrations, straightforward deployment.
* **Standard** - normal product build with several modules, meaningful state, design-system expectations, some auth or integrations, and non-trivial validation needs.
* **Deep** - sensitive data, payments, compliance, complex permissions, realtime or collaboration, migrations, multiple external services, source-repository uncertainty, high availability, or costly sequencing mistakes.

Do not classify by product category alone. A small project can be deep when data safety, auth, money, or operational consequence is high.

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
docs/project/implementation-plan.md
source repositories or reference implementations, when available
```

## Review Areas

Check:

* alignment with project goals, first-version scope, user flows, acceptance criteria, approved design constraints, and architecture decisions;
* whether milestone order follows real dependencies and useful delivery slices;
* whether foundational setup is proportional and enables later product work;
* whether data, auth, integration, deployment, migration, and validation prerequisites are sequenced before dependent milestones;
* whether plan scope is coarse enough for roadmap planning and precise enough for later task-specification work;
* whether acceptance criteria, functional IDs, design constraints, architecture decisions, and validation gates are traceable;
* whether missing tools, plugins, accounts, credentials, source repositories, or user decisions are surfaced;
* whether the handoff to the first Cursor task specification is clear and bounded.

## Finding Groups

Return findings grouped as:

* **Automatic clarity fixes** - wording, traceability, duplicate milestone concern, missing rationale, or small consistency issues that do not change sequencing.
* **Needs user decision** - choices that affect milestone order, launch slice, delivery depth, cost, account ownership, external services, or risk posture.
* **Needs source or tool readiness** - missing repository access, plugin, skill, CLI, SDK, account, credential, service, or setup action.
* **Route back to upstream stage** - product, design, or architecture gaps that planning must not invent.
* **Defer to task specification** - valid low-level task details that should be handled later.
* **No material issue** - reviewed areas that are adequate, when useful.

## Handling Findings

Apply automatic clarity fixes directly. Ask the user before changing milestone order, first usable slice, launch-readiness threshold, or risk posture.

If a finding exposes a missing product, design, or architecture decision, route it back to the owning stage instead of hiding it inside the plan.

If a finding is task-level detail, keep the implementation plan coarse and record only enough handoff guidance for the future task-spec stage.

Do not let a review pass, source-repository inspection, or validation script substitute for explicit user approval when sequencing affects external cost, account ownership, sensitive data, deployment, or launch strategy.
