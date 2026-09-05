---
artifact: task-notes
version: 1
status: complete
created: 2026-09-05
updated: 2026-09-05
related:
  - .codex/skills/cc-plan/SKILL.md
  - .codex/skills/cc-plan/references/implementation-plan.md
  - .codex/skills/cc-plan/references/planning-review.md
  - .codex/agents/planning-critic.md
  - .agents/scripts/validate-project-artifacts.py
---

# CC Plan Smoke Test

## Purpose

Run the first isolated test of the new Implementation Plan stage before a full greenfield workflow test across Init, Brief, Spec, Designer, Architect, and Plan.

The test focused on whether `cc-plan` can produce a realistic stage-level implementation roadmap from complete upstream artifacts, and whether the shared validator supports the new `implementation-plan` artifact.

## Test Fixture

Temporary target project:

```text
/private/tmp/cc-plan-e2e
```

Fixture artifacts:

```text
AGENTS.md
docs/project/status.md
docs/project/brief.md
docs/project/product-spec.md
docs/project/functional-spec.md
docs/project/design-brief.md
docs/project/screen-spec.md
docs/project/design-system.md
docs/project/technical-architecture.md
docs/project/implementation-plan.md
```

The sample project was a local-first parent practice tracker with:

* exercise library;
* daily practice logging;
* progress dashboard;
* JSON export/import backup;
* Vite React TypeScript architecture;
* localStorage persistence;
* Vitest and Playwright validation strategy.

## Positive Test

Generated a sample `docs/project/implementation-plan.md` with:

* `status: ready-for-task-specification`;
* `plan_depth: standard`;
* milestones `M-001` through `M-006`;
* dependency map;
* validation and review gates;
* tooling and setup prerequisites;
* launch-readiness notes;
* handoff to the first Cursor task specification.

Result:

```text
python3 .agents/scripts/validate-project-artifacts.py /private/tmp/cc-plan-e2e
Project artifact validation passed.
```

## Negative Tests

### Duplicate Milestone Definition

Temporary target project:

```text
/private/tmp/cc-plan-duplicate-test
```

Added a second `### M-001 - ...` heading.

Result:

```text
Project artifact validation failed:
- docs/project/implementation-plan.md:55: duplicate stable ID `M-001` also appears at docs/project/implementation-plan.md:49
```

This confirms the validator still catches duplicate stable ID definitions.

### Missing Architecture Artifact

Temporary target project:

```text
/private/tmp/cc-plan-missing-architecture-test
```

Moved `docs/project/technical-architecture.md` away while status and implementation plan still referenced it.

Result:

```text
Project artifact validation failed:
- docs/project/status.md: related artifact does not exist: docs/project/technical-architecture.md
- docs/project/implementation-plan.md: related artifact does not exist: docs/project/technical-architecture.md
```

This confirms broken `related` links are detected. `cc-plan` also explicitly says to route back to `cc-architect` when technical architecture is missing, blocked, or not `ready-for-implementation-planning`.

## Issues Found And Fixed

### Validator Treated ID References As Duplicate Definitions

Initial test failed because the validator scanned all stable ID occurrences. This made valid roadmap traceability look like duplicate definitions whenever `implementation-plan.md` referenced `AC-001`, `F-001`, `ADR-001`, or `M-001`.

Fix:

* validator now checks duplicate IDs only in definition contexts:
  * heading definitions such as `### M-001 - ...`;
  * acceptance criteria definitions such as `- AC-001 - ...`;
  * ADR table definitions such as `| ADR-001 | ... |`.

### Validator Did Not Tolerate Nested Frontmatter

Initial test also failed on the nested `stack:` map used by `technical-architecture.md`, even though that shape is part of the architecture contract.

Fix:

* validator now tolerates nested YAML-like frontmatter blocks well enough for known artifact metadata;
* top-level list fields such as `related` are still collected and validated.

### Fixture Status Was Internally Inconsistent

The generated test status body said `Current stage: Complete`, while frontmatter initially still said `current_stage: implementation-plan`.

Fix:

* fixture frontmatter was corrected to `project_status: complete` and `current_stage: complete` after the implementation plan completed.

## Other Checks

Frontmatter parse check:

```text
ruby -e 'require "yaml"; ...' .codex/skills/cc-plan/**/*.md .codex/agents/planning-critic.md
```

Result:

```text
passed
```

Python syntax check:

```text
python3 -c 'import ast, pathlib; ast.parse(pathlib.Path(".agents/scripts/validate-project-artifacts.py").read_text())'
```

Result:

```text
passed
```

Official `skill-creator` `quick_validate.py` was not rerun successfully because the local environment still lacks `PyYAML`, matching the earlier Architect-stage limitation.

## Assessment

The new Implementation Plan stage is usable enough for a fuller end-to-end workflow test.

The most valuable finding was not in `cc-plan` itself, but in the shared validator: implementation planning makes heavy use of cross-artifact stable ID references, so the validator must distinguish definitions from references. That is now fixed.

## Recommended Next Test

Create a fresh test target project and run the entire greenfield sequence:

```text
cc-init -> cc-brief -> cc-spec -> cc-designer -> cc-architect -> cc-plan
```

Focus especially on:

* whether each stage updates `docs/project/status.md` consistently;
* whether handoff statuses match the next stage's required input state;
* whether the final `implementation-plan.md` can identify a clean first `cc-task-spec` candidate without needing hidden product, design, or architecture decisions.
