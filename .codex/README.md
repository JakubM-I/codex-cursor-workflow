# Codex Materials

This directory is for Codex-specific materials.

Use it for stage skills, analysis prompts, subagent definitions, review prompts, verification workflows, and supporting references intended primarily for Codex.

Keep shared material in `.agents/` instead.

Current supporting agents:

- `agents/design-researcher.md` - read-only UI/UX reference research used by `cc-designer`.
- `agents/architecture-critic.md` - read-only technical architecture review used by `cc-architect`.
- `agents/project-verification-critic.md` - read-only project-wide implementation and consistency review used by `cc-project-verify` when warranted.

Current task-delivery skill:

- `skills/cc-task-spec/` - creates a milestone task map and prepares the current Cursor task contract.
- `skills/cc-task-verify/` - owns Codex verification, delivery records, task acceptance, and milestone bookkeeping.
- `skills/cc-project-verify/` - owns project-wide verification, remediation planning, and final revalidation.
- `skills/cc-remediation-task-spec/` and `skills/cc-remediation-verify/` - own the separate remediation delivery loop.
