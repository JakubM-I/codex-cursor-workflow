# AI Development Workflow

This document describes a reusable workflow for cooperation between Codex, Cursor, and the user.

It is intended to be portable. The whole `docs` directory may be copied into another repository and adapted there. In every repository, the local `AGENTS.md`, current source code, and the user's latest instruction remain the source of truth.

## Core Idea

The workflow is organized as a sequence of stages, not as a permanent role assignment.

The preferred collaboration model is:

* Codex performs analysis, planning, task specification, verification, review, and correction guidance.
* Cursor performs implementation based on the prepared task specification.
* The user decides priorities, accepts scope, resolves product questions, and chooses when to move between stages.

This division is intentional, but not absolute. A user may ask any agent to perform a different stage when needed.

## Workflow Architecture

Each stage should have a clear purpose, input, output, and exit condition. Over time, a dedicated skill can be created for each stage. A stage skill may call or rely on more specialized skills, but it should still produce the expected stage artifact.

Recommended material layers:

* `.agents/` - shared instructions, checklists, and skills useful to more than one agent.
* `.codex/` - Codex-specific stage skills, analysis prompts, review prompts, and supporting materials.
* `.cursor/` - Cursor-specific implementation rules, coding prompts, and editor-native rule files.
* `docs/` - human-readable workflow documentation, task specifications, and process records.

Use the narrowest layer that fits. For example, a general review checklist belongs in `.agents/`, but a Codex skill that orchestrates the review stage belongs in `.codex/`.

Suggested stage skills:

* `task-intake` - clarify the request and collect missing context.
* `codebase-analysis` - inspect relevant files and existing patterns.
* `implementation-plan` - define approach, scope, risks, and validation strategy.
* `task-specification` - create the handoff document for Cursor.
* `implementation-support` - help Cursor interpret the specification when needed.
* `verification` - inspect completed changes and run or define local checks.
* `code-review` - produce actionable findings.
* `fix-guidance` - translate review findings into correction instructions.
* `completion-summary` - summarize outcome, checks, limitations, and next steps.

Skill names are descriptive placeholders. A project may rename them or split them differently as the system evolves.

## Stage 1: Intake

Purpose:

Understand what the user wants and decide whether enough information exists to continue.

Input:

* user's request;
* current repository instructions;
* relevant existing task specification, when present.

Process:

1. Read the user's latest instruction carefully.
2. Identify the requested outcome, not only the requested action.
3. Check whether the request is for analysis, specification, implementation, review, fixes, or workflow design.
4. Ask only for information that is necessary and cannot be safely inferred from the repository.

Output:

* concise understanding of the requested outcome;
* list of known constraints;
* open questions or assumptions, only when needed.

Exit condition:

The next stage is clear, or the user has answered a blocking question.

## Stage 2: Codebase Analysis

Purpose:

Inspect the repository before prescribing changes.

Input:

* accepted request or task goal;
* local `AGENTS.md`;
* relevant source files, tests, configuration, documentation, and prior task specifications.

Process:

1. Read local project instructions first.
2. Inspect files related to the requested behavior.
3. Identify existing patterns, naming conventions, ownership boundaries, and validation commands.
4. Note dependencies, integration points, and likely risks.
5. Avoid making implementation changes during analysis unless the user explicitly asks for them.

Output:

* relevant files and patterns;
* constraints that implementation must respect;
* risks, unknowns, and validation options.

Exit condition:

There is enough repository context to create a plan or task specification.

## Stage 3: Planning

Purpose:

Choose a scoped approach before writing a task specification.

Input:

* intake summary;
* codebase analysis;
* project constraints.

Process:

1. Define the smallest useful scope that satisfies the request.
2. Decide which files should be created or modified.
3. Identify behavior that must be preserved.
4. Identify validation that should be performed locally.
5. Separate required work from optional improvements.

Output:

* implementation approach;
* scope and out-of-scope notes;
* validation strategy;
* assumptions or decisions that should be visible to the implementing agent.

Exit condition:

The approach is specific enough to hand off.

## Stage 4: Task Specification

Purpose:

Create a handoff document that Cursor can implement without relying on the original conversation.

Location:

```text
docs/tasks/
```

Suggested filename format:

```text
TASK-001-short-feature-name.md
```

Process:

1. Write the specification from the current repository state, not from memory.
2. Include only information useful for implementation and review.
3. Do not duplicate permanent project rules from `AGENTS.md`.
4. Prefer concrete requirements over broad advice.
5. Make validation expectations explicit.

Recommended task structure:

```md
# TASK-001: Short feature name

## Status

Ready for implementation

## Goal

Describe the expected result.

## Context

Summarize the relevant current behavior, files, patterns, and constraints.

## Scope

List what must be created or changed.

## Out of Scope

List nearby work that should not be done.

## Implementation Requirements

Describe the required behavior, structure, interfaces, styling, data handling, tests, and existing behavior that must be preserved.

## Validation

- [ ] Relevant syntax, type, schema, or configuration checks pass.
- [ ] Relevant tests or focused manual checks are completed.
- [ ] References, imports, routes, registrations, or generated artifacts are correct.
- [ ] Existing behavior was not unintentionally removed.
- [ ] Changed files stay within the requested scope.

## Implementation Notes

Completed by the implementing agent.

## Review Findings

Completed by the reviewing agent.
```

Output:

* task specification in `docs/tasks/`;
* optional short summary for the user.

Exit condition:

The task is ready for Cursor or another implementing agent.

## Stage 5: Implementation

Purpose:

Implement the accepted task specification.

Primary owner:

Cursor, unless the user explicitly assigns implementation to another agent.

Input:

* local `AGENTS.md`;
* referenced task specification;
* current repository state.

Process:

1. Read `AGENTS.md`.
2. Read the complete task specification.
3. Inspect the current files before editing.
4. Confirm that the specification still matches the repository.
5. Implement only the defined scope.
6. Avoid unrelated refactoring, renaming, cleanup, or architecture changes.
7. Run or document relevant validation.
8. Fill in `Implementation Notes` in the task specification when requested by the workflow or user.

Output:

* changed source files;
* completed implementation notes or summary;
* validation results and limitations.

Exit condition:

The implementation is ready for verification or review.

## Stage 6: Verification

Purpose:

Check whether the implementation appears complete before formal review.

Input:

* task specification;
* implementation diff;
* validation output;
* local project instructions.

Process:

1. Compare changed files against the task scope.
2. Check whether required validation was performed.
3. Identify missing evidence, skipped checks, or obvious deviations.
4. Decide whether the work can proceed to review or should return to implementation.

Output:

* verification summary;
* missing checks or deviations, if any.

Exit condition:

The implementation is ready for review, or concrete follow-up work is identified.

## Stage 7: Review

Purpose:

Find actionable issues in the completed implementation.

Primary owner:

Codex, unless the user explicitly assigns review to another agent.

Review against:

* original user request;
* task specification;
* local `AGENTS.md`;
* current repository state;
* existing project patterns.

Focus on:

* missing requirements;
* functional errors;
* behavioral regressions;
* unsafe or undocumented assumptions;
* unintended changes outside scope;
* broken references, imports, routes, registrations, or integration points;
* invalid syntax, schema, configuration, or data shape;
* missing or insufficient validation;
* incomplete handling of relevant edge cases.

Output format:

List findings first. For each finding include:

* severity: `Blocker`, `Major`, `Minor`, or `Suggestion`;
* affected file or code area;
* description of the issue;
* why it matters;
* required or suggested correction.

When no issues are found, state that clearly and mention remaining test gaps or limits of local validation.

Exit condition:

The task is accepted, or findings are ready for correction.

## Stage 8: Fix Loop

Purpose:

Turn review findings into focused implementation corrections.

Process:

1. Cursor applies accepted fixes.
2. Fixes stay limited to review findings and required follow-up.
3. Validation is repeated for the changed area.
4. Codex reviews again when needed.

Exit condition:

No blocking or major findings remain, or the user decides to stop.

## Stage 9: Completion

Purpose:

Close the task with a clear record of what changed and what was verified.

Completion summary should include:

* created or modified files;
* implemented behavior;
* completed validation;
* known limitations or checks that could not be run;
* unresolved questions, if any.

The summary should be concise and factual.

## Status Values

Task specifications may use these status values:

* `Draft`
* `Ready for implementation`
* `Implementation in progress`
* `Ready for verification`
* `Ready for review`
* `Changes requested`
* `Completed`

## Source of Truth

Use this priority order when instructions conflict:

1. User's latest instruction.
2. Local `AGENTS.md`.
3. Current repository state.
4. Referenced task specification.
5. Reusable workflow documents.

A task specification is a handoff artifact. It does not replace inspecting the actual source before implementation.
