---
name: cc-stage-review
description: Run the configured independent CLI reviewer for a prepared Brief, Product and Functional Specification, Designer, or Implementation Plan stage; save a read-only review report and route it to the user and stage owner.
argument-hint: "[stage, review depth, artifact paths]"
---

# CC Stage Review

Run one configured external review without changing the reviewed project artifacts.

Read `.agents/artifacts/stage-review.md` and `docs/project/status.md` before acting. Confirm the supplied stage is one of `brief`, `product-functional-spec`, `design`, or `implementation-plan`, and use the reviewer and agent-definition path from the Reviewer Map.

## Execution

1. Read the reviewer runtime evidence in project status. If readiness is missing, stale, failed, or for a different model, run `bash .agents/scripts/check-reviewer-clis.sh --cli <claude | agy>` with the selected model flag when needed. Update the runtime evidence. If readiness fails, write a blocked review report with the known setup action and return to the owner.
2. Build a prompt containing the agent-definition path, review depth, exact artifact paths, explicit exclusions, and: `Read only. Return findings in the External Stage Review Contract format. Do not modify files or use write-capable tools.`
3. Invoke the configured CLI in non-interactive prompt mode. Use `claude -p <prompt>` for Claude Code reviews. For Designer, use `agy --mode plan --model gemini-4-neon-high -p <prompt>` and supply `.antigravity/agents/design-critic.md` in the prompt. Select `gemini-4-neon-xhigh` for justified deep reviews according to that instruction. Confirm model availability through `agy models` before the first review or when availability changes. Inspect `agy --help` for the installed version's supported flags. Capture the requested model and any model reported by the CLI in the report.
4. Capture the output and create the report at the contract path. The stage owner, not the reviewer, writes the report file and status trace.
5. Keep the stage `in-progress`. Give the user the filled-in resume line from the report contract and record it as the next action. Leave assessment and corrections for the owner's manual resume.

## Manual Owner Handoff

The owner follows [Resume With A Report](../../artifacts/stage-review.md#resume-with-a-report) when the user supplies the report path. Additional user notes are optional.
