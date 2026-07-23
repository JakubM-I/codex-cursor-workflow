# AI Development Workflows

This document describes optional workflows for working with coding agents in this repository.

Permanent repository rules are defined in `AGENTS.md` and take precedence over this workflow document.

## Selecting a Working Mode

The working mode is determined by the user's current instruction.

Agents must not assume a permanent role based on the tool being used. Codex, Cursor, or another coding agent may analyze, implement, or review changes when explicitly instructed.

## Mode 1: Standalone Implementation

Use this mode when one agent is expected to complete the task independently.

Typical process:

1. Read `AGENTS.md`.
2. Inspect the relevant project files and existing patterns.
3. Analyze the requested change.
4. Implement the solution.
5. Perform applicable local validation.
6. Review the resulting changes.
7. Summarize modified files, completed checks, limitations, and assumptions.

A separate task specification is optional for small or clearly scoped tasks.

## Mode 2: Analysis and Task Specification

Use this mode when one agent prepares implementation guidance for another agent.

The analyzing agent should:

1. Read `AGENTS.md`.
2. Inspect the relevant code and documentation.
3. Identify existing project patterns.
4. Determine the required files, dependencies, risks, and edge cases.
5. Prepare a task specification in `docs/tasks/`.
6. Avoid modifying application code unless explicitly requested.

The specification should describe what needs to be implemented without duplicating permanent project rules from `AGENTS.md`.

## Mode 3: Implementation from a Task Specification

Use this mode when an agent receives a task prepared earlier.

The implementing agent should:

1. Read `AGENTS.md`.
2. Read the complete referenced task specification.
3. Inspect the current repository state.
4. Verify that the proposed solution still matches the actual code.
5. Implement only the defined scope.
6. Avoid unrelated refactoring.
7. Perform applicable local validation.
8. Report any deviations from the specification.

A task specification does not override repository safety rules or the actual state of the codebase.

When the specification conflicts with the repository, the agent should report the conflict rather than silently introducing an unrelated workaround.

## Mode 4: Review

Use this mode when an agent reviews work completed by another agent or by the user.

The reviewer should compare the implementation against:

* the original request;
* the referenced task specification, when present;
* `AGENTS.md`;
* existing project patterns.

Review findings should focus on:

* missing requirements;
* functional errors;
* behavioral regressions;
* unsafe or undocumented assumptions;
* unintended changes outside the requested scope;
* broken references, imports, or integration points;
* invalid syntax, schema, configuration, or data shape;
* missing or insufficient validation;
* incomplete handling of relevant edge cases.

Do not modify reviewed code unless explicitly asked to apply fixes.

## Collaborative Workflow

A typical Codex and Cursor workflow may look like this:

1. Codex analyzes the task.
2. Codex creates a specification in `docs/tasks/`.
3. The user reviews or accepts the specification.
4. Cursor implements the specification.
5. Codex reviews the implementation.
6. Cursor applies accepted fixes.

This is an optional workflow, not a permanent assignment of responsibilities.

Codex may also complete a task independently when instructed to do so.

## Task Handoff

Task specifications used for collaboration between agents are stored in:

```text
docs/tasks/
```

Suggested filename format:

```text
TASK-001-short-feature-name.md
```

The purpose of a task specification is to provide a clear implementation handoff. It should remain concise and include only information useful for implementing and reviewing the requested change.

A task specification is not intended to document the entire project or reproduce permanent rules from `AGENTS.md`.

## Recommended Task Structure

### Status

Indicate the current stage of the task.

Suggested values:

* `Draft`
* `Ready for implementation`
* `Implementation in progress`
* `Ready for review`
* `Changes requested`
* `Completed`

### Goal

Briefly describe what should be created or changed and what the expected result is.

Focus on the visible, functional, or developer-facing outcome rather than general project background.

### Target

Identify the main files, modules, components, services, tests, configuration, or documentation involved.

This may include:

* new files to create;
* existing files to modify;
* existing implementation patterns that should be used as references;
* optional supporting files needed for tests, configuration, styles, scripts, documentation, or data.

Do not list unrelated repository files.

Example:

```md
## Target

Create:

- `src/features/example/example-view.tsx`
- `src/features/example/example-view.test.tsx`

Based on:

- `src/features/nearby-feature/nearby-view.tsx`

Optional supporting files:

- `src/features/example/example-types.ts`
```

### Implementation

Describe the required solution in enough detail for another agent to implement it without relying on the original conversation.

Depending on the task, this section may describe:

* expected behavior;
* user-facing or developer-facing flows;
* data structures and interfaces;
* configuration changes;
* UI structure and responsive behavior;
* API or service interactions;
* state management;
* error, empty, and loading states;
* accessibility requirements;
* styling requirements;
* testing requirements;
* dependencies on other files or modules;
* behavior that must be preserved from existing implementation.

This is the main part of the task specification.

Prefer concrete implementation requirements over general suggestions. Do not prescribe unnecessary architecture when the task can be completed by following an existing project pattern.

### Validation

List only checks that are relevant to the requested implementation.

Typical checks may include:

* syntax, type, schema, or configuration validation;
* linting or formatting checks;
* unit, integration, or focused regression tests;
* manual checks for important user flows;
* verification that references, imports, routes, or registrations are correct;
* verification that existing behavior was not unintentionally removed;
* review that changed files stay within the requested scope;
* accessibility or responsive checks when relevant.

Validation in this repository is local and code-focused unless the user explicitly requests a different process.

### Implementation Notes

This section is completed by the implementing agent after the work is finished.

It should include:

* created or modified files;
* existing patterns or reference files used;
* completed local checks;
* differences from the proposed implementation;
* assumptions or limitations;
* behavior that could not be verified locally.

Keep this section factual and concise.

### Review Findings

This section is completed during review.

Findings should include:

* the affected file or part of the implementation;
* a clear description of the problem;
* why the problem matters;
* the required or suggested correction.

Suggested finding levels:

* `Blocker` - the implementation is unsafe, invalid, or cannot be accepted;
* `Major` - an important requirement or behavior is missing or incorrect;
* `Minor` - a limited issue that should be corrected;
* `Suggestion` - an optional improvement outside the acceptance requirement.

When no problems are found, state that the implementation matches the task specification within the limits of local validation.

## Optional Sections

Additional sections should be added only when they help explain a specific task.

### Current Behavior

Use this when modifying existing behavior and the current implementation needs to be explained before describing the change.

It is usually unnecessary when creating something new.

### Scope and Out of Scope

Use these sections when the task could easily expand into unrelated work or when specific parts of the existing implementation should not be copied or changed.

They are not required for straightforward changes.

### Open Questions or Assumptions

Use this when the task specification cannot determine an important behavior from the repository or provided requirements.

Do not add this section for minor implementation details that can be resolved by following existing project patterns.

## Minimal Task Template

```md
# TASK-001: Short feature name

## Status

Ready for implementation

## Goal

Describe the expected change or feature.

## Target

Create or modify:

- `path/to/target-file.ext`

Based on:

- `path/to/reference-file.ext`

## Implementation

Describe the required behavior, structure, interfaces, styling, tests, and existing behavior that must be preserved.

## Validation

- [ ] Relevant syntax, type, schema, or configuration checks pass.
- [ ] All references, imports, routes, or registrations are correct.
- [ ] Required behavior is covered by appropriate local checks.
- [ ] Existing behavior was not unintentionally removed.
- [ ] Changed files stay within the requested scope.

## Implementation Notes

Completed by the implementing agent.

## Review Findings

Completed by the reviewing agent.
```

The repository, `AGENTS.md`, current source files, and the user's latest instruction remain the source of truth.

A task specification is a handoff document. It does not replace inspecting the actual source before implementation.
