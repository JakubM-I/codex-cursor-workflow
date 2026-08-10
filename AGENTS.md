# Repository Guidelines

## Project Scope

This repository is a workspace for designing a reusable AI-assisted development workflow for cooperation between Codex and Cursor.

The goal is to prepare instructions, task templates, review guidelines, skills, and supporting workflow documents that can later be copied or adapted into other software projects.

This repository's `AGENTS.md` is only for working on this workflow-system repository. It is not the operational `AGENTS.md` that should be copied into future software projects.

In future projects, `AGENTS.md` should be written separately for that specific project, technology stack, repository structure, validation commands, and local constraints.

Keep workflow materials general unless the user explicitly asks to create a project-specific or stack-specific variant.

## Project Structure & Module Organization

Workflow documentation lives in `docs/workflows/`.

Shared agent materials live in `.agents/`.

Codex-specific materials live in `.codex/`.

Cursor-specific materials live in `.cursor/`.

Temporary task notes for work on this repository may be created in `docs/tasks/` when useful. Use concise, descriptive filenames, for example:

```text
TASK-001-short-feature-name.md
```

Keep workflow documents focused on reusable collaboration rules. Avoid adding extra process structure before it is actually useful.

Use the hidden agent directories only for agent/tool materials that are part of the designed system. Keep human-readable workflow documentation in `docs/`.

## Documentation Conventions

Write instructions so they can apply to different technology stacks.

Prefer:

- clear separation between this local `AGENTS.md` and reusable workflow materials;
- clear separation between shared, Codex-specific, and Cursor-specific materials;
- source files, modules, components, services, tests, configuration, and documentation as generic concepts;
- clear acceptance criteria and review findings.

Avoid:

- framework-specific terminology unless the current task requires it;
- assumptions about folder structure, build tools, deployment targets, admin panels, or hosting;
- references to a previous client, platform, theme, CMS, or naming prefix;
- wording that implies this repository is the eventual application project;
- unnecessary layers of templates, folders, or instructions about writing instructions;
- prescribing architecture before the existing code has been inspected.

## Local Validation

Validation is local and documentation-focused unless the user asks for a different workflow.

Use checks that match the material being edited, such as:

- Markdown readability and internal consistency;
- reference and link checks;
- review for framework, CMS, platform, or product assumptions;
- review for conflicts between this local `AGENTS.md` and reusable workflow materials;
- review of changed files for unintended scope expansion.

Do not assume that a preview server, external deployment, or full end-to-end test is relevant to this repository. When something cannot be verified locally, record that limitation in the implementation notes or review.

## Git Workflow

Agents must not create commits, pull requests, pushes, branches, rebases, or other git workflow actions. Git is handled manually by the user.

It is acceptable to inspect git state or history, for example `git status --short`, but do not stage or modify history.

## Working On This Repository

This repository is for creating and refining the workflow system itself.

When editing materials here:

- keep changes focused on the instruction system being discussed;
- avoid turning local repository rules into reusable workflow rules;
- avoid turning reusable workflow rules into local repository rules;
- prefer simple files and directories until a stronger structure is needed;
- preserve the distinction between shared, Codex-specific, and Cursor-specific materials;
- check for contradictions, unclear handoff steps, unsafe assumptions, stack-specific leakage, and missing validation guidance.

Before finishing, summarize changed files and local checks.

## Designed Workflow Materials

The reusable workflow being designed in this repository is described in:

* `docs/workflows/ai-development.md`

That document is part of the portable system. This `AGENTS.md` is not.
