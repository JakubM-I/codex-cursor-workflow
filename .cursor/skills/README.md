# Cursor Skills

This directory is reserved for Cursor-oriented skills and implementation support material.

Current implementation guidance lives in `../rules/implement-task-spec.mdc`. It tells Cursor how to consume a Codex-authored task contract, keep scope narrow, run only permitted lightweight self-checks, and hand results back without claiming acceptance.

Potential future skills should support that boundary, not move Codex-owned verification, review, or project-record maintenance into Cursor.

Cursor's native rule files may remain in `.cursor/rules/`.
