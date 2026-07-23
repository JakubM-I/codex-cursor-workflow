# Repository Guidelines

## Project Scope

This repository defines and refines an AI-assisted development workflow for cooperation between Codex and Cursor.

The intended split of responsibilities is:

- Codex analyzes tasks, prepares implementation specifications, reviews completed code, and identifies required corrections.
- Cursor implements tasks based on the prepared specification.

These responsibilities describe the preferred collaboration model for this repository. The active working mode is still determined by the user's current instruction.

Keep the instructions general. Do not make repository rules depend on a specific framework, CMS, platform, hosting provider, or product unless the user explicitly asks for that in a future task.

## Project Structure & Module Organization

Workflow documentation lives in `docs/workflows/`.

Task handoff specifications should be created in `docs/tasks/` when needed. Use concise, descriptive filenames, for example:

```text
TASK-001-short-feature-name.md
```

Keep workflow documents focused on reusable collaboration rules. Avoid mixing project-specific implementation details into general process documentation.

## Documentation Conventions

Write instructions so they can apply to different technology stacks.

Prefer:

- source files, modules, components, services, tests, configuration, and documentation;
- existing project patterns;
- local validation appropriate to the repository;
- clear acceptance criteria and review findings.

Avoid:

- framework-specific terminology unless the current task requires it;
- assumptions about folder structure, build tools, deployment targets, or admin panels;
- references to a previous client, platform, theme, CMS, or naming prefix;
- prescribing architecture before the existing code has been inspected.

## Local Validation

Validation is local and code-focused unless the user asks for a different workflow.

Use checks that match the project being worked on, such as:

- syntax or type checks;
- linting or formatting checks;
- unit, integration, or focused regression tests;
- configuration validation;
- reference and import checks;
- review of changed files for unintended scope expansion.

Do not assume that a preview server, external deployment, or full end-to-end test is available. When something cannot be verified locally, record that limitation in the implementation notes or review.

## Git Workflow

Agents must not create commits, pull requests, pushes, branches, rebases, or other git workflow actions. Git is handled manually by the user.

It is acceptable to inspect git state or history, for example `git status --short`, but do not stage or modify history.

## Agent-Specific Instructions

When preparing a task specification, inspect the relevant repository files first and write implementation guidance that another coding agent can follow without relying on the original conversation.

When implementing from a specification, verify that the specification still matches the current repository state before changing code.

When reviewing, prioritize bugs, missing requirements, behavioral regressions, unsafe assumptions, and missing validation. Do not modify reviewed code unless explicitly asked to apply fixes.

Before finishing, summarize changed files and local checks.

## AI Working Modes

This repository supports different AI-assisted working modes, including standalone implementation, analysis and specification, implementation from an existing task specification, and code review.

The active working mode is determined by the user's current instruction. Do not assign a permanent role to Codex, Cursor, or another coding agent.

Detailed workflows, task handoff conventions, and task specification structure are described in:

* `docs/workflows/ai-development.md`
