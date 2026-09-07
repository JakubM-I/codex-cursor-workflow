# Task Verification Guide

Verify the Task Spec's acceptance criteria at the level promised by its Codex Verification Plan. Cursor's report and self-checks are useful input, but never sufficient evidence by themselves.

Use this order:

1. Read the Cursor report and compare its changed files, declared temporary arrangements, and observations with the actual repository state.
2. Check scope conformance before correctness: identify unexpected source areas, undocumented dependencies, incomplete temporary arrangements, and work that attempts to close a later task.
3. Turn the architecture/specification scenarios named by the Task Spec into executable Codex evidence where needed. Codex owns E2E, acceptance, browser/runtime, visual, accessibility, integration, and release checks. Persist a new test only when it is useful regression coverage; otherwise keep a reproducible probe or manual script in the verification record.
4. Run the required evidence, including an inspectable visual comparison for UI work when the task cites an approved visual reference.

An unavailable browser, account, fixture, device, or runner is an environment blocker. Record its exact setup action and owner; do not ask Cursor to install tooling, author acceptance coverage, or perform the final runtime proof unless the frozen task explicitly assigns a narrow exception.

## Evidence

Use the checks that fit the task and its project instructions: automated tests, type or static checks, targeted runtime inspection, integration checks, manual scenario proof, accessibility or design review, and source review. Keep the work focused on the current task; do not turn verification into unrelated cleanup or a new feature audit.

For every failed or unproven criterion, state:

* the criterion and evidence observed;
* affected file, behavior, or environment when known;
* the required correction or missing input; and
* whether the issue is inside the frozen task scope or must be routed upstream.

For visual UI work, compare representative required viewports and states with the cited design evidence. Functional selectors, DOM shape, source inspection, and no-overflow assertions are not proof of visual fidelity on their own.

## Correction Request Format

`cc-task-verify` records corrections for user approval in the task's Codex Delivery History and the delivery log:

```md
### Verification Result — M-001-TASK-001 / revision 1

- Outcome: changes-required
- Evidence: <command or inspection and result>
- Required correction: <precise behavior or code correction>
- Unchanged scope: <what Cursor must not alter>
- Verification after revision: <how Codex will check the correction>
```

After user approval, `cc-task-spec` turns this record into revision 2 of the Task Spec. The new revision must preserve the original scope unless an upstream artifact has been corrected first.
