# Cursor Skills

This directory is reserved for Cursor-oriented skills and implementation support material.

Current implementation guidance lives in `../rules/implement-task-spec.mdc`. It tells Cursor how to consume a Codex-authored task contract, keep scope narrow, run only permitted lightweight self-checks, and hand results back without claiming acceptance.

`../rules/implement-remediation-task-spec.mdc` provides the equivalent boundary for a Codex-authored remediation packet. It is separate because remediation work originates in approved project-verification findings rather than implementation-plan milestones.

Potential future skills should support that boundary, not move Codex-owned verification, review, or project-record maintenance into Cursor.

Cursor's native rule files may remain in `.cursor/rules/`.
