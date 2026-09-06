# Task Verification Guide

Verify the Task Spec's acceptance criteria at the level promised by its Codex Verification Plan. Cursor's report and self-checks are useful input, but never sufficient evidence by themselves.

## Evidence

Use the checks that fit the task and its project instructions: automated tests, type or static checks, targeted runtime inspection, integration checks, manual scenario proof, accessibility or design review, and source review. Keep the work focused on the current task; do not turn verification into unrelated cleanup or a new feature audit.

For every failed or unproven criterion, state:

* the criterion and evidence observed;
* affected file, behavior, or environment when known;
* the required correction or missing input; and
* whether the issue is inside the frozen task scope or must be routed upstream.

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
