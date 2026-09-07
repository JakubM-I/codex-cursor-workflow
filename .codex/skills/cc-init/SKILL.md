---
name: cc-init
description: Initialize a new project workspace for the Codex-Cursor workflow. Use when the user says they are starting or initiating a new project and provides a short project description. Creates a minimal AGENTS.md, initializes Git with main as the stable base, then creates and switches to dev for workflow work.
argument-hint: "[short project description]"
---

# CC Init

Initialize the target project workspace for the Codex-Cursor workflow.

This skill is for the first project stage. It creates the minimal local entry point, project-status index, and git baseline needed before project discovery. It does not gather the full brief, choose a stack, create a design, or plan implementation.

Init may prepare baseline workflow materials that are intended to be available across later stages, such as shared skills already bundled with the workflow. It does not install or connect project-specific account-backed plugins. Tools such as Mobbin, MagicPath, Figma, Adobe, Canva, or other external design/research services are checked and requested by the stage that needs them, usually `cc-designer`.

## Input

Use the user's message as the project description. If the description is missing or too vague to create a one-sentence project entry point, ask for a short description before making changes.

## Actions

1. Identify the target project root.
2. Create or update `AGENTS.md` in the project root.
3. Create or preserve `docs/project/status.md`.
4. Initialize git if the project is not already a git repository.
5. Ensure the stable primary branch is named `main`.
6. After the Init checkpoint on `main`, create and switch to `dev` for subsequent workflow work.
7. Ensure baseline shared workflow materials are available when the workflow bundle includes them.
8. Close Init according to `.agents/artifacts/stage-closure.md`.
9. Report exactly what was created or changed.

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

Do not add tool-specific design instructions or plugin setup requirements to `AGENTS.md`. Later stage skills should decide which tools are needed.

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

For a new project, `main` is the stable base and `dev` is the active integration branch. Codex may commit stage checkpoints and accepted task checkpoints on `dev`, but it must never merge `dev` into `main`, push either branch, create a remote, or open a pull request. Those actions remain the user's responsibility.

If `.git/` does not exist:

1. Run `git init`.
2. Ensure the current branch is `main`.
3. Create the Init baseline commit on `main` after the workspace artifacts and status have been prepared.
4. Create `dev` from that commit and switch to it.

If git initializes with `master`, rename it to `main` with:

```bash
git branch -M main
```

If `.git/` already exists:

- do not reinitialize it;
- inspect the current branch;
- if the primary branch is `master` and there are no project-specific reasons to keep it, rename it to `main`;
- do not create, switch, merge, or rename branches automatically when the working tree is dirty, when an active branch other than `main` is in use, or when repository history makes the intended base uncertain; report the state and ask the user;
- if the repository is clean on `main` and `dev` already exists, switch to `dev`;
- if the repository is clean on `main` and `dev` does not exist, ask before creating it from `main`.

After successful initialization, read `.agents/artifacts/stage-closure.md`, create the Init baseline commit on `main`, then create and switch to `dev`. Do not create remotes, GitHub repositories, branches other than `dev`, or pull requests.

## Baseline Shared Materials

When the workflow bundle includes shared materials in `.agents/`, preserve or copy them as part of setting up the target project. This keeps later stages from depending on chat history for reusable guidance.

The baseline set currently includes:

```text
.agents/artifacts/project-status.md
.agents/artifacts/stage-closure.md
.agents/scripts/validate-project-artifacts.py
.agents/skills/make-interfaces-feel-better/
```

Do not overwrite substantial existing shared materials without asking. If a target project already has a different version of a shared skill, report the conflict and ask whether to preserve, merge, or replace it.

Account-backed plugins and user-authenticated tools are not baseline materials. `cc-init` should not install or connect them by default.

## Output

Finish with a concise summary:

- project root;
- whether `AGENTS.md` was created, updated, or left unchanged;
- whether `docs/project/status.md` was created, updated, or left unchanged;
- whether baseline shared workflow materials were present, copied, or left unchanged;
- whether git was initialized or already existed;
- resulting `main` and active branch;
- Init commit SHA on `main`, or the exact blocker that prevented stage closure;
- anything intentionally left for later stages.
