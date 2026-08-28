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

`.codex/skills/project-init/SKILL.md`.

Supporting resources:

* minimal `AGENTS.md` entrypoint contract defined in `project-init`;
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
* base folders needed by the workflow, when introduced in later versions.

Frontmatter or metadata needs:

* likely none for `AGENTS.md`;
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

Do ustalenia: `project-brief`.

Supporting resources:

* Do ustalenia: project goals checklist;
* Do ustalenia: audience and user needs checklist;
* Do ustalenia: non-goals checklist;
* Do ustalenia: assumptions checklist;
* Do ustalenia: pressure-test or grill-me style skill;
* Do ustalenia: inspiration/research support.

Input artifacts:

* user idea;
* rough notes;
* references or inspiration links, when provided.

Output artifacts:

* project brief;
* goals and non-goals;
* initial feature/function list;
* assumptions and open questions.

Frontmatter or metadata needs:

* likely yes: `type`, `status`, `created`, `updated`, `source`, `stage`, `tags`.

Open decisions:

* decide whether the brief is one file or several focused files;
* decide how much questioning belongs here before moving to functional specification.

### Functional Specification

Purpose:

Define what the project should do before design and technical architecture.

Intended owner:

Codex, with user approval.

Primary skill or prompt:

Do ustalenia: `functional-spec`.

Supporting resources:

* Do ustalenia: feature definition checklist;
* Do ustalenia: user-flow checklist;
* Do ustalenia: edge-case checklist;
* Do ustalenia: acceptance criteria format;
* Do ustalenia: subagent for requirements pressure testing.

Input artifacts:

* project brief;
* user decisions;
* reference materials, when relevant.

Output artifacts:

* functional specification;
* feature list;
* user flows;
* product-level acceptance criteria;
* unresolved product questions.

Frontmatter or metadata needs:

* yes: `type`, `status`, `created`, `updated`, `source`, `stage`, `related`, `tags`.

Open decisions:

* decide whether this stage should produce one product spec or split specs by feature area;
* decide how detailed screen/user-flow descriptions should be before Designer.

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
