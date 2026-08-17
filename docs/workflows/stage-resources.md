# Stage Resources

This document is a working inventory of tools, skills, prompts, checklists, and supporting materials used across the AI development workflow.

It is intentionally provisional. Its purpose is to help design the system while the workflow is still evolving. It may later be simplified, split into agent-specific skill files, or removed.

## How To Use This File

For each workflow stage, track:

* intended owner;
* primary skill or prompt;
* supporting skills, tools, or checklists;
* input artifacts;
* output artifacts;
* open decisions.

Use this file to decide where a material belongs:

* `.agents/` for shared materials used by more than one agent;
* `.codex/` for Codex-specific stage skills, analysis prompts, review prompts, and orchestration;
* `.cursor/` for Cursor-specific implementation rules, coding prompts, and editor-native rules;
* `docs/` for human-readable workflow documents and task records.

## Stage Resource Map

### Project Definition

Purpose:

Define the project before individual implementation tasks are created.

Intended owner:

Codex, with user input.

Primary skill or prompt:

Do ustalenia.

Supporting resources:

* Do ustalenia: project goals checklist;
* Do ustalenia: audience and user needs checklist;
* Do ustalenia: constraints and assumptions checklist.

Input artifacts:

* user idea or project brief;
* reference materials, when provided;
* existing repository, when the project is not starting from zero.

Output artifacts:

* project definition;
* goals and non-goals;
* initial assumptions and open questions.

Open decisions:

* decide whether this becomes a dedicated Codex skill;
* decide where the project definition artifact should live.

### Requirements And Feature Definition

Purpose:

Turn the project definition into functional requirements and feature boundaries.

Intended owner:

Codex, with user input.

Primary skill or prompt:

Do ustalenia.

Supporting resources:

* Do ustalenia: requirements checklist;
* Do ustalenia: feature description template;
* Do ustalenia: user flow checklist.

Input artifacts:

* project definition;
* user priorities;
* existing product or code context, when available.

Output artifacts:

* feature list;
* functional requirements;
* important user flows;
* unresolved product questions.

Open decisions:

* decide whether requirements and feature definition should be separate stages.

### Existing State Analysis

Purpose:

Analyze an existing repository or product state when the project is not starting from zero.

Intended owner:

Codex.

Primary skill or prompt:

Do ustalenia.

Supporting resources:

* Do ustalenia: repository inspection checklist;
* Do ustalenia: architecture summary checklist;
* Do ustalenia: risk and dependency checklist.

Input artifacts:

* local `AGENTS.md`;
* source files;
* tests;
* configuration;
* documentation;
* existing task specifications.

Output artifacts:

* current-state summary;
* relevant patterns and constraints;
* risks, dependencies, and validation options.

Open decisions:

* decide how this stage differs from later task-level codebase analysis.

### Project Workflow Planning

Purpose:

Break the project into phases, milestones, features, or implementation tasks.

Intended owner:

Codex, with user approval.

Primary skill or prompt:

Do ustalenia.

Supporting resources:

* Do ustalenia: roadmap planning checklist;
* Do ustalenia: milestone breakdown template;
* Do ustalenia: dependency sequencing checklist.

Input artifacts:

* project definition;
* requirements and feature definitions;
* existing state analysis, when applicable.

Output artifacts:

* project workflow or roadmap;
* ordered stages or tasks;
* dependencies and sequencing notes.

Open decisions:

* decide whether the roadmap belongs in `docs/tasks/`, `docs/workflows/`, or a separate project-planning location.

### Task Specification

Purpose:

Create a concrete implementation handoff for Cursor.

Intended owner:

Codex.

Primary skill or prompt:

Do ustalenia: `task-specification`.

Supporting resources:

* Do ustalenia: task specification template;
* Do ustalenia: validation checklist;
* Do ustalenia: scope and out-of-scope checklist.

Input artifacts:

* selected project phase, feature, or task;
* current repository state;
* local `AGENTS.md`;
* relevant project workflow documents.

Output artifacts:

* task specification in `docs/tasks/`;
* optional summary for the user.

Open decisions:

* define final task specification template.

### Implementation

Purpose:

Implement the accepted task specification.

Intended owner:

Cursor.

Primary skill or prompt:

Do ustalenia.

Supporting resources:

* `.cursor/rules/` for editor-native rules;
* Do ustalenia: implementation-from-spec guidance;
* Do ustalenia: validation reporting guidance.

Input artifacts:

* local `AGENTS.md`;
* task specification;
* current repository state.

Output artifacts:

* changed source files;
* implementation notes;
* validation results.

Open decisions:

* decide how Cursor-specific implementation material should reference shared `.agents/` resources.

### Verification

Purpose:

Check whether the implementation appears complete before formal review.

Intended owner:

Codex.

Primary skill or prompt:

Do ustalenia: `verification`.

Supporting resources:

* Do ustalenia: diff inspection checklist;
* Do ustalenia: validation evidence checklist;
* Do ustalenia: scope compliance checklist.

Input artifacts:

* task specification;
* implementation diff;
* validation output;
* local project instructions.

Output artifacts:

* verification summary;
* missing checks or deviations.

Open decisions:

* decide whether verification and review should stay separate stages.

### Review

Purpose:

Produce actionable findings for implementation issues.

Intended owner:

Codex.

Primary skill or prompt:

Do ustalenia: `code-review`.

Supporting resources:

* Do ustalenia: review finding format;
* Do ustalenia: severity definitions;
* Do ustalenia: regression checklist.

Input artifacts:

* original user request;
* task specification;
* implementation diff;
* current repository state;
* validation results.

Output artifacts:

* review findings;
* acceptance statement when no issues are found.

Open decisions:

* decide whether review findings should be written back into the task specification by default.

### Fix Guidance

Purpose:

Translate accepted review findings into focused correction instructions.

Intended owner:

Codex for guidance, Cursor for applying fixes.

Primary skill or prompt:

Do ustalenia: `fix-guidance`.

Supporting resources:

* Do ustalenia: fix instruction template;
* Do ustalenia: retest checklist.

Input artifacts:

* review findings;
* user decisions about accepted fixes;
* current repository state.

Output artifacts:

* focused fix instructions;
* updated validation expectations.

Open decisions:

* decide whether every review loop needs a separate fix-guidance artifact.

### Completion

Purpose:

Close the work with a concise record of outcome and validation.

Intended owner:

Codex.

Primary skill or prompt:

Do ustalenia: `completion-summary`.

Supporting resources:

* Do ustalenia: completion summary checklist;
* Do ustalenia: limitation reporting checklist.

Input artifacts:

* completed implementation;
* validation results;
* final review result;
* unresolved questions, if any.

Output artifacts:

* completion summary for the user;
* final task status update, when applicable.

Open decisions:

* decide whether completion status should update task files automatically or only on request.
