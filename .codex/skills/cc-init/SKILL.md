---
name: cc-init
description: Initialize a new project workspace for the Codex-Cursor workflow. Use when the user says they are starting or initiating a new project and provides a short project description. Creates a minimal AGENTS.md and initializes git with main as the primary branch.
argument-hint: "[short project description]"
---

# CC Init

Initialize the target project workspace for the Codex-Cursor workflow.

This skill is for the first project stage. It creates the minimal local entry point, project-status index, and git baseline needed before project discovery. It does not gather the full brief, choose a stack, create a design, or plan implementation.

## Input

Use the user's message as the project description. If the description is missing or too vague to create a one-sentence project entry point, ask for a short description before making changes.

## Actions

1. Identify the target project root.
2. Create or update `AGENTS.md` in the project root.
3. Create or preserve `docs/project/status.md`.
4. Initialize git if the project is not already a git repository.
5. Ensure the primary branch is named `main`.
6. Report exactly what was created or changed.

## AGENTS.md Contract

The generated `AGENTS.md` should be intentionally minimal. It is a project entry point, not the full workflow system.

It should include:

```md
# Project Instructions

## Project

<one-sentence project description>

## Context

Use the Codex-Cursor workflow materials in this repository to decide which project context is needed for the current stage.

Project details, requirements, architecture, design, plans, and task specifications should be created and linked as the workflow progresses.
```

Do not add stack, commands, git workflow, implementation rules, validation rules, feature lists, architecture, or full project documentation to `AGENTS.md` during init.

If `AGENTS.md` already exists:

- preserve existing user-written project information when it does not conflict with this minimal contract;
- do not overwrite substantial existing content without asking;
- if the file looks unrelated or already detailed, summarize the situation and ask whether to replace, merge, or leave it unchanged.

## Project Status Contract

Read `.agents/artifacts/project-status.md` before creating or updating `docs/project/status.md`.

Create `docs/project/` and the initial status file after the minimal project entry point has been established. Set Init to `complete`, set the project to `active`, and set Brief as the current next stage.

If `docs/project/status.md` already exists:

- preserve it and inspect its current state;
- do not recreate the stage register or overwrite its history;
- update only the Init row when this invocation materially changes initialization state;
- report any conflict between the existing status and the project state instead of silently correcting it.

## Git Contract

If `.git/` does not exist:

1. Run `git init`.
2. Ensure the current branch is `main`.

If git initializes with `master`, rename it to `main` with:

```bash
git branch -M main
```

If `.git/` already exists:

- do not reinitialize it;
- inspect the current branch;
- if the primary branch is `master` and there are no project-specific reasons to keep it, rename it to `main`;
- if another branch is active, do not rename it automatically. Report the branch and ask before changing it.

Do not create commits, remotes, GitHub repositories, branches other than `main`, or pull requests in this version of the skill.

## Output

Finish with a concise summary:

- project root;
- whether `AGENTS.md` was created, updated, or left unchanged;
- whether `docs/project/status.md` was created, updated, or left unchanged;
- whether git was initialized or already existed;
- resulting current branch;
- anything intentionally left for later stages.
