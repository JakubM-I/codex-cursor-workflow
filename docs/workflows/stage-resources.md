# Stage Resources

This document is a working inventory of tools, skills, prompts, checklists, scripts, hooks, subagents, and supporting materials used across the project-creation workflow.

It is intentionally provisional. Its purpose is to help design the system while the workflow is still evolving. It may later be simplified, split into agent-specific skill files, or removed.

Current scope: project creation from zero through the implementation plan.

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
* `docs/` for human-readable workflow documents and project artifacts.

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
* `docs/sources/` working notes and direct source repositories, when relevant and available;
* later, if justified: deterministic checks for required frontmatter and acceptance criteria IDs.

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

Do ustalenia: `project-designer`.

Supporting resources:

* Do ustalenia: MagicPath workflow;
* Do ustalenia: Mobbin inspiration research;
* Do ustalenia: visual direction checklist;
* Do ustalenia: screen inventory template;
* Do ustalenia: component inventory checklist;
* Do ustalenia: accessibility and responsive checklist;
* Do ustalenia: design subagents, if useful.

Input artifacts:

* project brief;
* functional specification;
* user inspiration or brand references;
* technical constraints already known, if any.

Output artifacts:

* design direction or design brief;
* screen/view list;
* component and interaction notes;
* visual references or generated design artifacts, when used;
* design constraints for architecture and planning.

Frontmatter or metadata needs:

* likely yes for design briefs and screen specs;
* tool-specific outputs may have their own metadata formats.

Open decisions:

* decide whether Designer should run before Architect by default;
* decide how MagicPath and inspiration tools should be invoked;
* decide how design outputs are referenced by Architect and Plan.

### Architect

Purpose:

Define the technical architecture after product and design direction are known.

Intended owner:

Codex, with user approval for major tradeoffs.

Primary skill or prompt:

Do ustalenia: `project-architect`.

Supporting resources:

* Do ustalenia: stack selection checklist;
* Do ustalenia: architecture decision format;
* Do ustalenia: data model checklist;
* Do ustalenia: testing strategy checklist;
* Do ustalenia: deployment and hosting checklist;
* Do ustalenia: security and privacy checklist;
* Do ustalenia: architecture/security/performance subagents for larger projects.

Input artifacts:

* project brief;
* functional specification;
* design direction;
* user constraints;
* required integrations or services.

Output artifacts:

* technical architecture specification;
* stack decision or stack constraints;
* data and integration plan;
* validation and test strategy;
* technical risks and assumptions.

Frontmatter or metadata needs:

* yes: `type`, `status`, `created`, `updated`, `stage`, `source`, `related`, `stack`, `tags`.

Open decisions:

* decide whether stack selection can ever happen before Designer;
* decide which architecture decisions require explicit user approval;
* decide whether test strategy belongs here or in Plan.

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
* conversion from implementation-plan stage to Cursor task specification;
* Cursor implementation workflow;
* verification workflow;
* code review workflow;
* fix guidance and fix loops;
* completion and knowledge capture.
