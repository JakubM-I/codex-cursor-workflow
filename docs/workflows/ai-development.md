# AI Development Workflow

This document describes the first part of a reusable workflow for building a new software project with Codex, Cursor, and the user.

Current scope: project creation from zero, from initialization to an implementation plan. Existing-project onboarding, task-level implementation specs, Cursor execution, verification, review, and fix loops will be designed later.

The workflow is intended to be portable. The whole workflow system may be copied into another repository and adapted there. In every repository, the user's latest instruction and current project state remain the source of truth.

## Core Idea

The workflow is organized as project stages. Each stage should eventually have a dedicated skill or entry point.

The preferred collaboration model is:

* Codex guides project discovery, product definition, design direction, technical architecture, and implementation planning.
* Cursor implements concrete tasks later, after the project plan has been converted into task-level specifications.
* The user provides goals, decisions, priorities, feedback, accounts, assets, and final approval.

This document stops at the project implementation plan. It does not yet define the detailed Cursor task workflow.

## Operating Principles

Use the smallest amount of process that creates clarity.

Do not force every agent to read every project document. Each stage or skill should decide which context is needed for its purpose.

Keep `AGENTS.md` minimal in target projects. Treat it as an entry point or context index, not as the main workflow engine.

Use structured artifacts when they will be reused by later stages. If a file needs to be discovered, filtered, resumed, validated, or routed by agents, give it appropriate frontmatter or metadata.

Use deterministic scripts, hooks, or validations when a gate should not depend only on model memory.

## Material Layers

Recommended material layers:

* `.agents/` - shared instructions, checklists, skills, scripts, and reusable conventions.
* `.codex/` - Codex-specific stage skills, analysis prompts, subagent definitions, orchestration, review prompts, and supporting materials.
* `.cursor/` - Cursor-specific implementation rules, coding prompts, editor-native rules, and implementation support.
* `docs/` - human-readable workflow documentation, project artifacts, plans, and task records.

Use the narrowest layer that fits. Shared materials belong in `.agents/`. Codex orchestration belongs in `.codex/`. Cursor implementation guidance belongs in `.cursor/`.

A working inventory of tools, skills, prompts, and supporting materials assigned to workflow stages may be tracked in:

```text
docs/workflows/stage-resources.md
```

That inventory is a planning aid. It can be changed, simplified, or removed as the workflow matures.

## Project Workflow Stages

### Stage 1: Init

Purpose:

Initialize a new project workspace for the Codex-Cursor workflow.

Possible responsibilities:

* create or update a minimal `AGENTS.md` entry point;
* create the base workflow/project documentation folders when needed;
* initialize git when the user wants it;
* prepare optional scripts, hooks, or repo metadata;
* optionally create or connect a remote repository when the user explicitly asks for it.

The first version of this stage should stay conservative. It should not gather the whole project brief or decide the technical architecture.

Output:

* initialized project workspace;
* minimal project entry point or context index;
* clear note of what was created and what remains unset.

Exit condition:

The project workspace is ready for project discovery.

### Stage 2: Brief

Purpose:

Collect and pressure-test the core project idea before product or technical decisions are locked.

The brief should answer:

* what is being built;
* who it is for;
* what problem it solves;
* what the most important outcomes are;
* what is explicitly out of scope;
* what assumptions need validation;
* what inputs, assets, accounts, or external references may be needed.

This stage may use conversational pressure testing, inspiration research, or "grill me" style questioning. It should ask for one decision at a time when the user is needed.

Output:

* project brief;
* goals and non-goals;
* initial feature/function list;
* open questions and assumptions.

Exit condition:

There is enough product context to describe the desired functionality.

### Stage 3: Functional Specification

Purpose:

Turn the brief into a structured description of what the project should do.

The functional specification should focus on product behavior, not implementation details.

It may include:

* core features;
* user roles or user types;
* main user flows;
* screens or interaction areas;
* important states and edge cases;
* data the product must create, display, import, export, or preserve;
* acceptance criteria at the product level.

Output:

* functional specification;
* resolved and unresolved product decisions;
* list of functionality that later stages must account for.

Exit condition:

The product behavior is clear enough for design and technical architecture work.

### Stage 4: Designer

Purpose:

Define the visual and UX direction for the product.

This stage may use design tools, UI inspiration sources, visual references, mockup tools, or design-specific skills. Examples include MagicPath, Mobbin, generated visual references, or project-specific design systems when available.

The design stage should focus on:

* visual direction;
* UX structure;
* screen inventory;
* layout patterns;
* component needs;
* interaction patterns;
* accessibility and responsive expectations;
* design constraints that affect implementation.

Output:

* design direction or design brief;
* screen or view list;
* component and interaction notes;
* references or generated design assets, when used;
* design constraints for architecture and planning.

Exit condition:

The technical architecture can account for the intended product experience.

### Stage 5: Architect

Purpose:

Define the technical shape of the project based on the brief, functional specification, and design direction.

The architect stage should decide or document:

* stack and major technical choices;
* application structure;
* data model direction;
* integrations and external services;
* authentication or permissions, when relevant;
* validation and test strategy;
* build, deployment, or hosting assumptions;
* risks, constraints, and tradeoffs.

Stack should not be chosen too early unless the user has already fixed it. Design and functional requirements may affect technical decisions.

Output:

* technical architecture specification;
* stack decision or stack constraints;
* testing and validation approach;
* known technical risks and assumptions.

Exit condition:

There is enough product, design, and technical context to plan implementation phases.

### Stage 6: Implementation Plan

Purpose:

Break the project into ordered implementation stages that can later be converted into concrete Cursor tasks.

The implementation plan should stay at the project-stage level. It should not become a full list of low-level coding tasks unless that detail is needed to understand sequencing.

Each implementation stage should include:

* stage name;
* goal;
* scope;
* expected result;
* dependencies or prerequisites;
* validation or acceptance notes, when useful.

Example stage format:

```md
## Etap 10 - Eksport I Import Postepow

Cel:

Zabezpieczyc dane przed utrata.

Zakres:

- eksport postepow do pliku JSON;
- import wczesniej wyeksportowanego pliku;
- potwierdzenie przed nadpisaniem obecnych postepow;
- komunikat przy niezgodnym pliku.

Rezultat:

- rodzic moze zrobic kopie zapasowa;
- import odtwarza lokalny zapis;
- eksport nie zawiera bazy cwiczen.
```

Output:

* ordered implementation plan;
* project stages with goals, scope, and expected results;
* dependencies and prerequisites;
* enough context to start creating task-level implementation specifications.

Exit condition:

The project has a coherent implementation roadmap. The next workflow part can create detailed task specifications for Cursor.

## Future Workflow Parts

The following areas are intentionally outside the current scope and will be designed later:

* onboarding or analysis of an existing project;
* conversion of an implementation-plan stage into one or more Cursor task specifications;
* Cursor implementation workflow;
* verification workflow;
* code review workflow;
* fix guidance and fix loops;
* completion and knowledge capture.

## Source of Truth

Use this priority order when instructions conflict:

1. User's latest instruction.
2. Current project state.
3. Local project entry point and referenced project documents.
4. Stage artifact currently being produced.
5. Reusable workflow documents.

Workflow documents guide the process. They do not replace stage-specific skills, project-specific context, or user decisions.
