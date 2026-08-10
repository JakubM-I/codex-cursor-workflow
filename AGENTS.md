# Repository Guidelines

## Project Scope

This repository is a workspace for designing a reusable AI-assisted development workflow for cooperation between Codex and Cursor.

The goal is to prepare instructions, task templates, review guidelines, skills, and supporting workflow documents that can later be copied or adapted into other software projects.

This repository's `AGENTS.md` is local to this repository. In future target projects, `AGENTS.md` should describe that specific project, its technology stack, repository structure, validation commands, and local constraints.

Keep workflow materials general unless the user explicitly asks to create a project-specific or stack-specific variant.

## Project Structure & Module Organization

Workflow documentation lives in `docs/workflows/`.

Task handoff specifications for work on this repository should be created in `docs/tasks/` when needed. Use concise, descriptive filenames, for example:

```text
TASK-001-short-feature-name.md
```

Keep workflow documents focused on reusable collaboration rules. Avoid adding extra process structure before it is actually useful.

## Documentation Conventions

Write instructions so they can apply to different technology stacks.

Prefer:

- clear separation between this local `AGENTS.md` and reusable workflow materials;
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

## Agent-Specific Instructions

When preparing a task specification for this repository, inspect the relevant instruction files first and write guidance that another coding agent can follow without relying on the original conversation.

When implementing from a specification, verify that the specification still matches the current repository state before changing files.

When reviewing, prioritize missing requirements, contradictions, unclear handoff steps, unsafe assumptions, stack-specific leakage, and missing validation guidance. Do not modify reviewed files unless explicitly asked to apply fixes.

Before finishing, summarize changed files and local checks.

## AI Working Modes

This repository supports different AI-assisted working modes, including standalone documentation changes, analysis and specification, implementation from an existing task specification, and review.

The active working mode is determined by the user's current instruction. Do not assign a permanent role to Codex, Cursor, or another coding agent.

Detailed workflows, task handoff conventions, and task specification structure are described in:

* `docs/workflows/ai-development.md`
