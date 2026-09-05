# Stage Resources

This document is a working inventory of tools, skills, prompts, checklists, scripts, hooks, subagents, and supporting materials used across the project-creation workflow.

It is intentionally provisional. Its purpose is to help design the system while the workflow is still evolving. It may later be simplified, split into agent-specific skill files, or removed.

Current scope: project creation from zero through the implementation plan.

This file is a design-time inventory for this workflow-system repository. It is not a production stage input and does not need to be copied into target projects. Target projects should rely on `.agents/`, `.codex/`, `.cursor/`, and generated `docs/project/` artifacts unless a future packaging step intentionally includes additional reference docs.

## How To Use This File

For each workflow stage, track:

* intended owner;
* primary skill or prompt;
* supporting skills, tools, subagents, scripts, hooks, or checklists;
* input artifacts;
* output artifacts;
* frontmatter or metadata needs;
* open decisions.

Use this file to decide where a material belongs:

* `.agents/` for shared materials used by more than one agent;
* `.codex/` for Codex-specific stage skills, analysis prompts, subagents, review prompts, and orchestration;
* `.cursor/` for Cursor-specific implementation rules, coding prompts, and editor-native rules;
* `docs/` for human-readable workflow design documents in this repository, and generated project artifacts or records inside target projects.

## Stage Resource Map

### Init

Purpose:

Initialize a new project workspace for the workflow system.

Intended owner:

Codex, with user approval for repository or remote actions.

Primary skill or prompt:

`.codex/skills/cc-init/SKILL.md`.

Supporting resources:

* minimal `AGENTS.md` entrypoint contract defined in `cc-init`;
* `.agents/artifacts/project-status.md` - shared project-status contract;
* `.agents/skills/make-interfaces-feel-better/` - full baseline shared UI-polish skill that target projects may receive during workflow bootstrap;
* `.agents/scripts/validate-project-artifacts.py` - lightweight local validator for project artifact frontmatter, statuses, related links, and stable IDs;
* Do ustalenia: project folder bootstrap script;
* Do ustalenia: git initialization script for later automation;
* Do ustalenia: GitHub repository creation script or checklist;
* Do ustalenia: safety checklist for destructive or remote actions.

Input artifacts:

* project name or working title;
* target project directory;
* user's preference for local-only, git, or remote repository setup.

Output artifacts:

* initialized project workspace;
* minimal project entry point or context index;
* git repository with `main` as the primary branch;
* `docs/project/status.md` with Brief as the next stage.

Frontmatter or metadata needs:

* likely none for `AGENTS.md`;
* required for `docs/project/status.md`: `artifact`, `version`, `project_status`, `current_stage`, `created`, `updated`, `related`;
* bootstrap logs or init reports may need metadata later.

Open decisions:

* decide how small the first `AGENTS.md` should be;
* decide which folders are created immediately and which are created on demand;
* decide whether shared baseline skills such as `make-interfaces-feel-better` are copied during `cc-init` itself or by a separate bootstrap step that Init invokes;
* decide whether GitHub setup is part of the default path or an explicit option.

### Brief

Purpose:

Collect and pressure-test the project idea.

Intended owner:

Codex, with user input.

Primary skill or prompt:

`.codex/skills/cc-brief/SKILL.md`.

Supporting resources:

* `cc-brief/references/project-brief.md` - artifact contract and readiness check;
* `.codex/skills/cc-grill/SKILL.md` - pressure-test support for Standard and Deep discovery;
* `.agents/artifacts/project-status.md` - shared project-status contract;
* later, if justified: focused use of `requirements-critic` for brief-level requirement risks;
* later, if justified and authorized: inspiration or market research support.

Input artifacts:

* user idea;
* rough notes;
* references or inspiration links, when provided.

Output artifacts:

* `docs/project/brief.md`;
* updated `docs/project/status.md`;
* project direction, goals, and non-goals;
* initial capability hypotheses;
* assumptions and open questions.

Frontmatter or metadata needs:

* required for `docs/project/brief.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`.

Open decisions:

* whether the brief needs a separate change log or revision history once projects become long-lived;
* whether Brief should ever use `requirements-critic`, or whether requirements criticism should remain owned by `cc-spec`.

### Product / Functional Specification

Purpose:

Define the product shape and product behavior before design and technical architecture.

Intended owner:

Codex, with user approval.

Primary skill or prompt:

`.codex/skills/cc-spec/SKILL.md`.

Supporting resources:

* `cc-spec/references/product-spec.md` - product specification contract and readiness check;
* `cc-spec/references/functional-spec.md` - functional specification contract, acceptance criteria style, and readiness check;
* `cc-spec/references/requirements-review.md` - complexity assessment, critic depth, and findings handling contract;
* `.codex/agents/requirements-critic.md` - read-only independent requirements review subagent used by `cc-spec`, defaulting to `gpt-5.6-luna` with `medium` reasoning effort;
* `.agents/artifacts/project-status.md` - shared project-status contract;
* source repositories, user-provided notes, or direct references when relevant and available;
* `.agents/scripts/validate-project-artifacts.py` - deterministic check for required frontmatter, allowed statuses, related links, and stable IDs.

Input artifacts:

* project brief;
* user decisions;
* reference materials, when relevant.

Output artifacts:

* `docs/project/product-spec.md`;
* `docs/project/functional-spec.md`;
* resolved and unresolved product decisions;
* feature groups, user flows, product-level acceptance criteria, and unresolved functional questions inside the functional specification.

Frontmatter or metadata needs:

* required for `docs/project/product-spec.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`;
* required for `docs/project/functional-spec.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`.

Open decisions:

* default to two artifacts: product specification and functional specification;
* decide later whether large projects need additional feature-area specs;
* decide how detailed screen/user-flow descriptions should be before Designer;
* decide whether requirements review findings should later be saved as a separate artifact for high-risk projects or remain inside the stage handoff.

### Designer

Purpose:

Define the product's UX and visual direction.

Intended owner:

Codex, using design tools and user feedback.

Primary skill or prompt:

`.codex/skills/cc-designer/SKILL.md`.

Supporting resources:

* `cc-designer/references/tool-readiness.md` - tool setup, MagicPath workflow, Mobbin routing, and user approval/status handling;
* `cc-designer/references/design-brief.md` - visual direction, UX principles, references, tooling, and handoff constraints;
* `cc-designer/references/screen-spec.md` - screen/view inventory, navigation, states, responsive notes, and flow coverage;
* `cc-designer/references/design-system.md` - token direction, component inventory, interaction patterns, accessibility rules, and UI polish expectations;
* `.agents/skills/make-interfaces-feel-better/` - full shared UI-polish lens for typography, surfaces, motion, icons, hit areas, and review;
* Mobbin plugin - preferred source for real UI screens, flows, and website section references when available;
* MagicPath - collaborative visual workspace when the user wants or needs visual iteration there; requires user login/project setup outside Codex when no direct integration is available;
* generated visual references or image tools, when useful for mood, art direction, bitmap mockups, or asset direction;
* optional tools such as Figma, Adobe, or Canva only when the project and available plugins justify them;
* `.codex/agents/design-researcher.md` - read-only UI/UX reference researcher for Mobbin, user-provided references, screenshots, and comparable patterns;
* `.codex/agents/design-critic.md` - read-only UX/design reviewer subagent for standard and deep design reviews, defaulting to `gpt-5.6-luna` with `medium` reasoning effort.

Input artifacts:

* project brief;
* product specification;
* functional specification;
* user inspiration or brand references;
* technical constraints already known, if any.

Output artifacts:

* `docs/project/design-brief.md`;
* `docs/project/screen-spec.md`;
* `docs/project/design-system.md`;
* visual references or generated design artifacts, when used;
* design constraints for architecture and planning.

Frontmatter or metadata needs:

* required for `docs/project/design-brief.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`;
* required for `docs/project/screen-spec.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`;
* required for `docs/project/design-system.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`;
* design artifact statuses include `draft`, `ready-for-user-review`, `approved-for-architecture`, and `superseded`;
* tool-specific outputs may have their own metadata formats, but project artifacts should link them instead of duplicating tool internals.

Open decisions:

* Designer runs before Architect by default unless the user has already fixed technical constraints that must be known first;
* use a hybrid installation model: baseline shared skills during Init/bootstrap, project-specific account-backed plugins at the start of Designer;
* Designer can prepare artifacts for review, but it only marks the stage complete after explicit user approval of the design direction, preferably after reviewing MagicPath or another visual representation when that flow is used;
* decide whether a lightweight single-artifact design mode is worth supporting for very small projects.

### Architect

Purpose:

Define the technical architecture after product and design direction are known.

Intended owner:

Codex, with user approval for major tradeoffs.

Primary skill or prompt:

`.codex/skills/cc-architect/SKILL.md`.

Supporting resources:

* `cc-architect/references/technical-architecture.md` - artifact contract, required architecture areas, frontmatter, status values, and readiness check;
* `cc-architect/references/technical-readiness.md` - source repository inspection, missing tools, skills, plugins, accounts, credentials, and installation/connection boundaries;
* `cc-architect/references/architecture-review.md` - complexity assessment, review areas, finding groups, and handling rules;
* source repositories, starter projects, examples, templates, and existing systems when available;
* available stack-specific skills or plugins, selected only when they materially help the project;
* available deployment, repository, design, data, auth, AI, or integration plugins when the selected architecture justifies them;
* `.codex/agents/architecture-critic.md` - read-only independent architecture review subagent used by `cc-architect`, defaulting to `gpt-5.6-luna` with `medium` reasoning effort;
* later, if justified: focused security, performance, or deployment reviewer subagents for larger projects.

Input artifacts:

* project brief;
* product specification;
* functional specification;
* approved design brief;
* approved screen spec;
* approved design system;
* user constraints;
* required integrations or services.

Output artifacts:

* technical architecture specification;
* stack decision or stack constraints;
* data and integration plan;
* authentication, authorization, and security plan when relevant;
* validation and test strategy;
* deployment and operations assumptions;
* required and recommended skills, plugins, accounts, credentials, tools, and source repositories;
* technical risks and assumptions.

Frontmatter or metadata needs:

* required for `docs/project/technical-architecture.md`: `artifact`, `version`, `status`, `stage`, `created`, `updated`, `sources`, `related`, `stack`, `tags`;
* architecture artifact statuses include `draft`, `ready-for-implementation-planning`, `blocked`, and `superseded`.

Open decisions:

* Designer remains the default predecessor because UX, screen, and design-system constraints affect stack and implementation choices; stack may be constrained earlier only when the user, organization, existing repository, or source system already fixed it;
* major architecture decisions that affect cost, account ownership, data sensitivity, security posture, hosting, auth, integration providers, or maintainability require explicit user approval;
* testing and validation strategy belongs in Architecture at strategy level, while exact sequencing and task-level commands belong in Implementation Plan and later Cursor task specs;
* use a hybrid tool model: inspect available source repositories first, then ask whether Codex should install/connect useful missing skills or plugins when tool support exists, or whether the user will install/connect them manually and confirm readiness.

### Implementation Plan

Purpose:

Break the project into ordered implementation stages.

Intended owner:

Codex, with user approval.

Primary skill or prompt:

Do ustalenia: `implementation-plan`.

Supporting resources:

* Do ustalenia: milestone breakdown template;
* Do ustalenia: dependency sequencing checklist;
* Do ustalenia: stage format template;
* Do ustalenia: risk and prerequisite checklist;
* Do ustalenia: validation/acceptance checklist.

Input artifacts:

* project brief;
* functional specification;
* design direction;
* technical architecture specification.

Output artifacts:

* ordered implementation plan;
* stages with goal, scope, result, dependencies, and acceptance notes;
* enough context to create task-level specifications later.

Frontmatter or metadata needs:

* yes: `type`, `status`, `created`, `updated`, `stage`, `source`, `related`, `tags`.

Open decisions:

* decide final format for implementation stages;
* decide whether stages should contain task candidates or only high-level scope;
* decide where the implementation plan should live.

## Later Workflow Areas

These areas are intentionally not designed in detail yet:

* existing project onboarding and current-state analysis;
* conversion from an implementation-plan stage into a Cursor-ready task packet, including required context, optional context, acceptance criteria IDs, relevant design and architecture constraints, decisions Cursor may make locally, and decisions Cursor must route back to Codex;
* Cursor implementation workflow, including how Cursor consumes task packets without needing the whole project history;
* verification workflow, including runtime checks mapped back to acceptance criteria and design constraints;
* code review workflow, including independent review against the original Codex contract rather than only general diff quality;
* fix guidance and fix loops, including focused fix packets from Codex to Cursor, bounded retries, and criteria for returning to specification, design, or architecture;
* completion and knowledge capture.
