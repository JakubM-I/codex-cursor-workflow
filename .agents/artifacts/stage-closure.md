# Stage Closure Contract

Project stages produce durable checkpoints. A stage is not closed merely because its Markdown artifacts are written: its owning skill must complete the applicable review, validation, user-decision, and version-control work.

This contract is intended for target projects that use this workflow. More restrictive repository instructions take precedence.

## Default Branch Strategy

For a newly initialized workflow project, `main` is the stable baseline and `dev` is the active integration branch.

- `cc-init` creates the Init checkpoint on `main`, then creates and switches to `dev`.
- Later stage checkpoints and accepted task checkpoints are created on `dev`.
- Codex and Cursor never merge `dev` into `main`, push, create a remote, or create a pull request unless the user explicitly asks. The user owns publishing and branch-integration decisions.
- For an existing repository, do not infer that its active branch, merge policy, or default branch may be changed. Inspect it and ask when the default strategy conflicts with its established workflow.

## Closure Rules

Before reporting a stage as closed, its owner must:

1. satisfy that stage's own readiness and approval requirements;
2. update only its owned stage row and the project-level fields in `docs/project/status.md`;
3. run the applicable local validation;
4. inspect Git status and identify only the files owned by that stage; and
5. create one commit on the active workflow branch containing those stage-owned files and `docs/project/status.md`.

For Init, the commit follows successful workspace initialization on `main`; `cc-init` then creates and switches to `dev`. For stages with an explicit user approval gate, the commit follows that approval. Other stages commit when their documented exit condition is met.

Use a concise stage-scoped commit message, for example `chore: initialize project workflow`, `docs: complete project brief`, or `docs: approve design direction`. Never use `git add -A`, include unrelated user changes, amend a prior commit, rewrite history, create a remote, push, or create a pull request.

If Git author identity, repository state, or another Git prerequisite prevents the commit, restore or keep the stage as `in-progress`, record the exact blocker in `docs/project/status.md`, and ask for the smallest action needed to resolve it. Do not report the stage as fully closed without its commit.

## Status Trace

The completion note in `docs/project/status.md` identifies the closed stage and its artifacts. The closing skill reports the resulting short commit SHA to the user; Git history remains the authoritative commit trace. This avoids a second status-only commit merely to write the SHA back into the committed status file.
