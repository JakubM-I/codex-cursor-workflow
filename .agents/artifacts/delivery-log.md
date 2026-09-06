# Delivery Log Contract

`docs/project/delivery-log.md` is the durable, append-only record of accepted tasks, blocked attempts, material revisions, and implementation-derived project corrections. It is maintained by Codex, not Cursor.

It is not a replacement for a task specification, test output, review report, implementation plan, or Git history. It records only the outcome and the consequences that a later task author must know.

## Frontmatter

```yaml
---
artifact: delivery-log
version: 1
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
related:
  - docs/project/implementation-plan.md
---
```

Allowed `status` values are `active`, `complete`, and `superseded`.

## Record Format

```md
## DL-001 - TASK-001 / revision 1

- Milestone: M-001
- Outcome: accepted | changes-required | blocked
- Date: YYYY-MM-DD
- Verification evidence: <commands, review evidence, and limitations>
- Delivery decision: <accepted scope or exact reason for non-acceptance>
- Deviations: <None, or concise factual deviation>
- Downstream implications: none | pending | applied
- Impact and action: <affected milestone or artifact, required correction, and owner>
- Next action: <next task, focused revision, or user decision>
```

Use `DL-001`-style IDs. Keep enough evidence to explain a later decision, not raw command transcripts. When an implementation insight changes a source artifact, name that artifact and state that the amendment came from delivery.
