---
artifact: task-notes
version: 1
status: complete
created: 2026-09-05
updated: 2026-09-05
related:
  - docs/tasks/TASK-001-cc-plan-smoke-test.md
  - .agents/scripts/validate-project-artifacts.py
  - .agents/artifacts/project-status.md
  - .codex/skills/cc-init/SKILL.md
  - .codex/skills/cc-brief/SKILL.md
  - .codex/skills/cc-spec/SKILL.md
  - .codex/skills/cc-designer/SKILL.md
  - .codex/skills/cc-architect/SKILL.md
  - .codex/skills/cc-plan/SKILL.md
---

# Stage Smoke Tests

## Purpose

Run local structural smoke tests for the greenfield workflow stages before testing the full workflow on an example project.

This complements the earlier isolated `cc-plan` smoke test by checking the artifact handoff shapes for Init, Brief, Product / Functional Specification, Designer, Architect, and the full pre-task-specification state.

## Test Fixture

Temporary fixtures were generated under:

```text
/private/tmp/cc-stage-smoke-tests-2026-09-05
```

The fixture project was a local-first parent practice tracker, matching the earlier implementation-plan smoke test closely enough to compare stage outputs.

## Positive Tests

The shared validator passed these stage snapshots:

```text
[PASS] 01-init
[PASS] 02-brief-ready
[PASS] 03-spec-ready
[PASS] 04-design-review-gate
[PASS] 05-design-approved
[PASS] 06-architecture-ready
[PASS] 07-full-plan-ready
```

Coverage:

* Init: minimal `AGENTS.md` and `docs/project/status.md` with Brief as current stage.
* Brief: `docs/project/brief.md` with `status: ready-for-functional-spec`.
* Product / Functional Specification: `docs/project/product-spec.md` and `docs/project/functional-spec.md` with `status: ready-for-design-and-architecture`.
* Designer review gate: design artifacts at `ready-for-user-review`, status still on Design, and blocker set to user design approval.
* Designer approved gate: design artifacts at `approved-for-architecture` and current stage moved to Architecture.
* Architect: `docs/project/technical-architecture.md` with nested `stack:` metadata and `status: ready-for-implementation-planning`.
* Full plan-ready state: all current greenfield artifacts present, cross-linked, and the implementation plan ready for task specification.

## Negative Tests

The shared validator rejected these intended failures:

```text
[FAIL] neg-brief-bad-status
- docs/project/brief.md: `status` has unsupported value `ready-for-design`; expected one of: draft, ready-for-functional-spec, superseded

[FAIL] neg-spec-missing-related
- docs/project/product-spec.md: related artifact does not exist: docs/project/missing-functional-spec.md

[FAIL] neg-design-duplicate-screen-id
- docs/project/screen-spec.md:79: duplicate stable ID `S-001` also appears at docs/project/screen-spec.md:21

[FAIL] neg-architecture-missing-stack
- docs/project/technical-architecture.md: missing frontmatter field `stack`
```

These checks confirm that the validator catches unsupported artifact statuses, broken `related` links, duplicate stable ID definitions, and missing required architecture metadata.

## Instruction And Script Checks

Skill and agent frontmatter parse check:

```text
ruby -e 'require "yaml"; require "date"; ...' .codex/skills/**/*.md .codex/agents/*.md .agents/artifacts/*.md docs/tasks/*.md
passed
```

Validator syntax check:

```text
python3 -c 'import ast, pathlib; ast.parse(pathlib.Path(".agents/scripts/validate-project-artifacts.py").read_text())'
passed
```

`python3 -m py_compile .agents/scripts/validate-project-artifacts.py` was not used as the final syntax check because it attempted to create `__pycache__` inside `.agents/scripts/` and hit local sandbox permissions. The `ast.parse` check is read-only and passed.

## Manual Contract Review

The local tests distinguish two kinds of gates:

* deterministic structure gates, handled by `.agents/scripts/validate-project-artifacts.py`;
* stage judgment and user-approval gates, handled by the stage skills.

The Designer approval gate is the clearest example. The validator accepts both `ready-for-user-review` and `approved-for-architecture` because both are legal artifact states. The stage skill remains responsible for not moving from review to approved without explicit user approval.

## Assessment

The current greenfield stage artifact contracts are structurally consistent enough to run a full workflow test on an example project.

No validator changes were needed during this test pass.

## Recommended Next Test

Run the complete sequence on a fresh example project:

```text
cc-init -> cc-brief -> cc-spec -> cc-designer -> cc-architect -> cc-plan
```

Pay special attention to:

* whether each stage updates only its own row in `docs/project/status.md`;
* whether stage-owner skills route missing readiness back to the correct prior stage;
* whether Designer pauses at user approval instead of silently approving its own artifacts;
* whether Architect records implementation-enabling tooling without installing or connecting services unless the user authorizes it;
* whether Plan can choose the first Cursor task-specification candidate without inventing product, design, or architecture decisions.
