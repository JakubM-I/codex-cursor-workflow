# AI Development Workflow

This document describes the first part of a reusable workflow for building a new software project with Codex, Cursor, and the user.

Current scope: project creation from zero, from initialization to an implementation plan. Existing-project onboarding, task-level implementation specs, Cursor execution, verification, review, and fix loops will be designed later.

This document is a design document for building the reusable workflow system. It is not currently part of the minimal runtime that must be copied into every target project. The portable runtime is expected to live primarily in `.agents/`, `.codex/`, and `.cursor/`, plus project artifacts generated under `docs/project/` inside each target project. If workflow documentation is copied into a target project later, it should be copied intentionally as reference material, not treated as a required input for every stage skill.

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

Init creates the minimal entry point. Once Brief is ready, Brief adds a compact project snapshot with the intended outcome, primary user, v1 boundary, key exclusion, and links to the current project artifacts. It must not duplicate the brief or accumulate implementation rules.

Use structured artifacts when they will be reused by later stages. If a file needs to be discovered, filtered, resumed, validated, or routed by agents, give it appropriate frontmatter or metadata.

Use lightweight text diagrams when they clarify relationships that are hard to read in prose. Prefer Mermaid blocks in Markdown because they are versionable, reviewable in diffs, and readable by agents. Do not require diagrams for obvious or linear material; add them when order, state, dependency, data flow, ownership, or system boundaries could otherwise be misunderstood.

Each project has a compact workflow index at `docs/project/status.md`. Init creates it. Stage-owner skills update their own row, the current stage, blockers, next action, and a short recent-update trail. Detailed history remains in stage artifacts and git; supporting skills do not update the index directly.

Use deterministic scripts, hooks, or validations when a gate should not depend only on model memory.

A lightweight shared validator may check project artifact frontmatter, statuses, related links, and stable IDs. It is not a replacement for stage judgment or user approval; it catches structural drift before later agents consume the artifacts.

Every closed stage is a Git checkpoint. After its readiness, validation, and any required user approval, its owner commits only its owned artifacts and `docs/project/status.md`, then reports the short SHA to the user. A stage remains open when its checkpoint cannot be committed.

## Material Layers

Recommended material layers:

* `.agents/` - shared instructions, checklists, skills, scripts, and reusable conventions.
* `.codex/` - Codex-specific stage skills, analysis prompts, subagent definitions, orchestration, review prompts, and supporting materials.
* `.cursor/` - Cursor-specific implementation rules, coding prompts, editor-native rules, and implementation support.
* `docs/` - in this workflow-system repository, human-readable workflow design documentation and local source notes; in target projects, generated project artifacts, plans, task records, reviews, and knowledge records.

Use the narrowest layer that fits. Shared materials belong in `.agents/`. Codex orchestration belongs in `.codex/`. Cursor implementation guidance belongs in `.cursor/`.

System skills created for this workflow should use the `cc-` prefix and a short action-oriented name, for example `cc-init`.

A working inventory of tools, skills, prompts, and supporting materials assigned to workflow stages may be tracked in this repository in:

```text
docs/workflows/stage-resources.md
```

That inventory is a planning aid for designing the system. It can be changed, simplified, or removed as the workflow matures, and it is not a required production artifact for target projects.

## Project Workflow Stages

### Stage 1: Init

Purpose:

Initialize a new project workspace for the Codex-Cursor workflow.

Possible responsibilities:

* create or update a minimal `AGENTS.md` entry point;
* initialize git;
* ensure the primary branch is named `main`;
* create the minimal project-status index at `docs/project/status.md`;
* prepare optional scripts, hooks, repo metadata, or remote repository setup in later versions.

The first version of this stage should stay conservative: create the minimal `AGENTS.md` entry point, project-status index, and initialize git with `main`. It should not gather the whole project brief, decide the technical architecture, create a remote repository, or plan implementation.

Output:

* initialized project workspace;
* minimal project entry point or context index;
* project-status index with Brief as the next stage;
* git repository with `main` as the primary branch;
* initial Git checkpoint;
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

This stage uses a standard discovery baseline even for simple projects. It may use conversational pressure testing, inspiration research, or "grill me" style questioning, and should ask in small rounds of one to three related decisions when the user is needed. A round is only a conversational cadence, not a total question budget: continue with dependent rounds until each applicable discovery area is confirmed, explicitly deferred, or visible as an assumption. Simplicity reduces unnecessary exploration, not the need to cover user, outcome, scope, constraints, and references.

Output:

* project brief;
* goals and non-goals;
* open questions and assumptions.

The Brief owns the project direction and its boundaries. It may capture capability hypotheses, but detailed features, user flows, states, and product acceptance criteria belong to Product / Functional Specification.

Exit condition:

There is enough product context to describe the desired functionality.

### Stage 3: Product / Functional Specification

Purpose:

Turn the brief into a structured product description and a behavior-level functional specification.

This stage should focus on what should exist, how the product should behave, and how users move through the product. It should not choose a technical stack, define architecture, create detailed visual design, or plan implementation tasks.

The product specification may include:

* product summary and intended outcome;
* users, roles, and contexts;
* product principles and priorities;
* first-version scope and explicit non-goals;
* main product areas or surfaces;
* product lifecycle or operating model;
* product-level success criteria;
* assumptions, risks, and open product decisions.

The functional specification may include:

* core features;
* user roles or user types;
* main user flows;
* optional Mermaid diagrams for non-trivial flows, state transitions, or dependencies;
* screens or interaction areas;
* important states and edge cases;
* data the product must create, display, import, export, or preserve;
* notifications, integrations, collaboration, or admin behavior when relevant;
* acceptance criteria at the product level.

The stage should be collaborative and proactive. Codex should not only generate documents from the brief: it should inspect relevant source material, propose product framing, ask focused questions, challenge unclear or risky choices, recommend options when useful, and record unresolved assumptions instead of silently inventing decisions.

Before completion, the stage should run a requirements review. Codex first classifies complexity as `light`, `standard`, or `deep`, then uses an independent requirements critic at that depth. The default critic configuration is `gpt-5.6-luna` with `medium` reasoning effort, with escalation only when `deep` complexity or high consequence justifies it. The critic does not edit artifacts or decide product direction. Codex applies minor clarity fixes, asks the user to approve material product decisions, routes design, architecture, or implementation concerns to later stages, and records only a compact review trace in project status.

Output:

* product specification;
* functional specification;
* resolved and unresolved product decisions;
* list of functionality that later stages must account for.

Exit condition:

The product shape and behavior are clear enough for design and technical architecture work.

### Stage 4: Designer

Purpose:

Define the visual and UX direction for the product.

At the start of Designer, the user selects one mode: reference research, full visual design, or an explicit documentation-only opt-out. A new user-facing interface defaults to full visual design. The agent must not silently decide that references, mockups, or visual tooling are unnecessary.

Designer is the first stage where account-backed design tools are normally expected. Baseline shared UI skills can be included during Init or repository bootstrap, while project-specific plugins and design accounts should be checked at the start of Designer. Codex should present the useful tool set, identify what is missing, and ask whether Codex should install/connect available plugins or whether the user will add tools manually and confirm readiness.

Mobbin is the preferred source for real UI and UX references when available. MagicPath is treated as a collaborative visual workspace for full visual design: the user may be asked to log in, open or create the project, review the proposed design, and either approve it or request changes. Tools required by the selected mode must be installed or connected before that mode can proceed; if they are unavailable, the user chooses another tool or explicitly changes mode.

The design stage should focus on:

* visual direction;
* UX structure;
* screen inventory;
* optional Mermaid diagrams for screen maps, navigation, or cross-screen flows when they reduce ambiguity;
* layout patterns;
* component needs;
* interaction patterns;
* accessibility and responsive expectations;
* design constraints that affect implementation.

Output:

* design brief;
* screen or view specification;
* design-system direction, including component and interaction notes;
* `asset-manifest.md`, covering logos, icons, imagery, fonts, provisional mockup assets, provenance, and delivery timing;
* references or generated design assets, when used;
* design constraints for architecture and planning.

Exit condition:

The user has approved the design direction after reviewing the selected-mode evidence. Full visual design requires reviewable mockups or a visual workspace, including core layouts and layout-changing states. The asset manifest must either provide required assets or defer each one to a named prerequisite before the relevant UI task.

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
* developer tooling, skills, plugins, accounts, credentials, and setup prerequisites;
* risks, constraints, and tradeoffs.

Architecture artifacts should use Mermaid diagrams when they clarify system components, data ownership, integration flow, event flow, deployment shape, or security boundaries. Diagrams should stay at architecture level and should not become exhaustive generated schemas or low-level code maps.

Stack should not be chosen too early unless the user has already fixed it. Design and functional requirements may affect technical decisions.

The stage should be collaborative and evidence-driven. In a target project, Codex should inspect the brief, product specification, functional specification, approved design artifacts, and available source repositories before asking the user for decisions. Source repositories, starter projects, existing systems, and templates should be mined for practical conventions such as stack, structure, tests, deployment, auth, data handling, and integration patterns, while avoiding project-specific assumptions that do not belong in the new project.

Architect should explain uncertain or high-impact technical choices in plain language, recommend a direction when the evidence is strong, and ask the user to decide when a choice affects cost, ownership, privacy, security, deployment, maintainability, or external accounts. It should also identify missing implementation capabilities in relation to the chosen stack: required or useful skills, plugins, CLIs, SDKs, services, accounts, credentials, and repository access. When Codex can install or connect a useful missing tool, it should ask whether the user wants Codex to do that or whether the user will do it manually and confirm readiness.

Output:

* technical architecture specification;
* stack decision or stack constraints;
* testing and validation approach;
* deployment and operations assumptions;
* required and recommended tools, skills, plugins, accounts, credentials, and source repositories;
* known technical risks and assumptions.

Exit condition:

There is enough product, design, and technical context to plan implementation phases.

### Stage 6: Implementation Plan

Purpose:

Break the project into ordered implementation stages that can later be converted into concrete Cursor tasks.

The implementation plan should stay at the project-stage level. It should not become a full list of low-level coding tasks unless a candidate slice is needed to understand sequencing. Detailed Cursor task packets belong to a later workflow part.

This stage answers:

* in what order the system should be built;
* which milestones depend on earlier milestones, tools, accounts, source repositories, data, auth, integrations, or deployment setup;
* which product capabilities, flows, acceptance criteria, design constraints, and architecture decisions each milestone must account for;
* where validation, review, and launch-readiness gates belong;
* which milestone or slice should become the first Cursor-ready task specification.

Implementation plans should include a dependency map. For simple projects a short list is enough; for multi-stage or dependency-heavy plans, use a Mermaid flowchart to show milestone order, prerequisites, blockers, and validation gates.

The stage should be collaborative and evidence-driven. Codex should inspect the project artifacts, technical architecture, and available source repositories or reference implementations before asking planning questions. Source repositories and prior delivery notes should be mined for practical sequencing patterns such as setup order, module boundaries, scaffolding, test layering, migrations, integration prerequisites, deployment gates, and milestone sizing. They are inspiration and evidence, not templates to copy blindly.

Codex should recommend an order when the evidence is strong, explain tradeoffs in plain language, and ask the user to decide when sequencing affects launch strategy, delivery risk, cost, account ownership, external services, sensitive data, deployment, or what should become usable first. Non-blocking unknowns should be recorded as assumptions or open planning decisions instead of being silently invented.

Each implementation stage should include:

* stage name;
* goal;
* scope;
* expected result;
* dependencies or prerequisites;
* traceability to acceptance criteria, functional areas, design constraints, and architecture decisions, when useful;
* validation or acceptance notes;
* notes for later task specification.

Example stage format:

```md
### M-010 - Eksport I Import Postepow

Goal:

Zabezpieczyc dane przed utrata.

Scope:

- eksport postepow do pliku JSON;
- import wczesniej wyeksportowanego pliku;
- potwierdzenie przed nadpisaniem obecnych postepow;
- komunikat przy niezgodnym pliku.

Expected Result:

- rodzic moze zrobic kopie zapasowa;
- import odtwarza lokalny zapis;
- eksport nie zawiera bazy cwiczen.

Dependencies And Prerequisites:

- lokalny model danych postepow jest juz ustalony;
- aplikacja ma ekran ustawien lub inne miejsce na akcje eksportu/importu.

Validation Notes:

- eksportowany plik mozna zaimportowac ponownie;
- import nie nadpisuje danych bez potwierdzenia;
- bledny plik daje zrozumialy komunikat.
```

Before completion, the stage should run a planning review. Codex first classifies planning complexity as `light`, `standard`, or `deep`, then uses an independent planning critic at that depth when available. The default critic configuration is `gpt-5.6-luna` with `medium` reasoning effort, with escalation only when `deep` complexity or high consequence justifies it. The critic does not edit artifacts or decide sequencing. Codex applies minor clarity fixes, asks the user to approve material planning changes, routes upstream gaps to the owning stage, and records only a compact review trace in project status.

Output:

* ordered implementation plan;
* project milestones with goals, scope, expected results, dependencies, validation notes, and task-specification notes;
* dependency map and prerequisite list;
* validation and review gates;
* first Cursor task-specification candidate;
* enough context to start creating task-level implementation specifications without reloading the whole project history.

Exit condition:

The project has a coherent implementation roadmap. The next workflow part can create detailed task specifications for Cursor.

## Future Workflow Parts

The following areas are intentionally outside the current scope and will be designed later:

* onboarding or analysis of an existing project;
* conversion of an implementation-plan stage into one or more Cursor task specifications, including a task packet contract with required context, optional context, acceptance criteria, relevant design and architecture constraints, and explicit decision boundaries;
* Cursor implementation workflow, including how Cursor should consume task packets without reloading the full project history;
* verification workflow, including runtime proof mapped back to acceptance criteria and design constraints;
* code review workflow, including independent review against the original Codex contract and not only diff quality;
* fix guidance and fix loops, including bounded Codex-to-Cursor fix packets and criteria for routing back to specification, design, or architecture;
* completion and knowledge capture.

## Source of Truth

Use this priority order when instructions conflict:

1. User's latest instruction.
2. Current project state.
3. Local project entry point and referenced project documents.
4. Stage artifact currently being produced.
5. Reusable workflow documents.

Workflow documents guide the process. They do not replace stage-specific skills, project-specific context, or user decisions.
