# Project Status Contract

`docs/project/status.md` is the compact, current index of a project's workflow position. It helps the user, Codex, and later Cursor resume work without reading every project artifact.

It is not a replacement for stage artifacts, task records, review reports, or git history. Those remain the source of truth for their own detail. The status file records only the current position, links, blockers, and a short trail of material transitions.

## Creation And Maintenance

`cc-init` creates this file. Every stage-owner skill reads it before starting work and updates it before handing off to the next stage.

Supporting skills, exploratory subagents, validators, and checklists do not update it directly. They return findings to the stage-owner skill, which decides whether the state changed.

When updating the file:

* preserve completed-stage rows and prior update entries;
* update only the current stage's row, the project-level current state, blockers, next action, and the recent update list;
* link to the stage artifact instead of duplicating its content;
* append one concise entry for a material transition, pause, unblock, or completion;
* keep the most recent ten update entries. Older detail remains available through git and the linked artifacts.

Do not mark a stage complete unless its own exit condition is satisfied. A project can be `active` while its current stage is `in-progress` or `blocked`.

## Frontmatter

```yaml
---
artifact: project-status
version: 1
project_status: active
current_stage: brief
created: YYYY-MM-DD
updated: YYYY-MM-DD
related: []
---
```

Allowed `project_status` values:

* `active`;
* `paused`;
* `blocked`;
* `complete`;
* `superseded`.

Canonical `current_stage` values for the current greenfield workflow:

* `init`;
* `brief`;
* `product-functional-spec`;
* `design`;
* `architecture`;
* `implementation-plan`;
* `complete`.

Allowed stage-row statuses:

* `not-started`;
* `in-progress`;
* `blocked`;
* `complete`;
* `skipped`.

## Initial File

`cc-init` creates this initial file after creating the minimal project entry point:

```md
---
artifact: project-status
version: 1
project_status: active
current_stage: brief
created: YYYY-MM-DD
updated: YYYY-MM-DD
related:
  - AGENTS.md
---

# Project Status

## Current State

- Current stage: Brief
- Next action: Start `cc-brief` with the available project idea or notes.
- Blockers: None identified.

## Stage Register

| Stage | Status | Artifact | Updated | Notes |
| --- | --- | --- | --- | --- |
| Init | complete | `AGENTS.md` | YYYY-MM-DD | Workspace initialized. |
| Brief | not-started | - | - | - |
| Product / Functional Specification | not-started | - | - | - |
| Designer | not-started | - | - | - |
| Architect | not-started | - | - | - |
| Implementation Plan | not-started | - | - | - |

## Recent Updates

- YYYY-MM-DD - Init completed. Brief is the next stage.
```

## Stage Update Example

When `cc-brief` produces a ready brief, it updates the relevant values rather than recreating the file:

```md
## Current State

- Current stage: Product / Functional Specification
- Next action: Define product shape and behavior from `docs/project/brief.md`.
- Blockers: None identified.

## Stage Register

| Stage | Status | Artifact | Updated | Notes |
| --- | --- | --- | --- | --- |
| Init | complete | `AGENTS.md` | 2026-08-31 | Workspace initialized. |
| Brief | complete | `docs/project/brief.md` | 2026-08-31 | Ready for product and functional specification. |
| Product / Functional Specification | not-started | - | - | - |
| Designer | not-started | - | - | - |
| Architect | not-started | - | - | - |
| Implementation Plan | not-started | - | - | - |

## Recent Updates

- 2026-08-31 - Brief completed and linked. Product / Functional Specification is the next stage.
- 2026-08-31 - Init completed. Brief is the next stage.
```

When `cc-spec` produces both product-definition artifacts, it may link both in the same stage row:

```md
## Current State

- Current stage: Designer
- Next action: Define UX and visual direction from `docs/project/product-spec.md` and `docs/project/functional-spec.md`.
- Blockers: None identified.

## Stage Register

| Stage | Status | Artifact | Updated | Notes |
| --- | --- | --- | --- | --- |
| Init | complete | `AGENTS.md` | 2026-08-31 | Workspace initialized. |
| Brief | complete | `docs/project/brief.md` | 2026-08-31 | Ready for product and functional specification. |
| Product / Functional Specification | complete | `docs/project/product-spec.md`; `docs/project/functional-spec.md` | 2026-08-31 | Ready after standard requirements review. |
| Designer | not-started | - | - | - |
| Architect | not-started | - | - | - |
| Implementation Plan | not-started | - | - | - |

## Recent Updates

- 2026-08-31 - Product and functional specifications completed after standard requirements review. Designer is the next stage.
- 2026-08-31 - Brief completed and linked. Product / Functional Specification is the next stage.
- 2026-08-31 - Init completed. Brief is the next stage.
```
