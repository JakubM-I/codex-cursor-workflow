---
name: cc-stage-review
description: Run the configured independent CLI reviewer for a prepared Brief, Product and Functional Specification, Designer, or Implementation Plan stage; save a read-only review report and route it to the user and stage owner.
argument-hint: "[stage, review depth, artifact paths]"
---

# CC Stage Review

Run one configured external review without changing the reviewed project artifacts.

Read `.agents/artifacts/stage-review.md` and `docs/project/status.md` before acting. Confirm the supplied stage is one of `brief`, `product-functional-spec`, `design`, or `implementation-plan`, and use the reviewer and agent-definition path from the Reviewer Map.

## Execution

1. Check reviewer CLI availability with `bash .agents/scripts/check-reviewer-clis.sh`. If the configured CLI is unavailable, write a blocked review report and return to the owner; do not substitute another reviewer or a self-review.
2. Build a prompt containing the agent-definition path, review depth, exact artifact paths, explicit exclusions, and: `Read only. Return findings in the External Stage Review Contract format. Do not modify files or use write-capable tools.`
3. Invoke the configured CLI in non-interactive prompt mode. The normal forms are `claude -p <prompt>` and `gemini -p <prompt>`; inspect `--help` when the installed CLI requires a different documented non-interactive form.
4. Capture the output and create the report at the contract path. The stage owner, not the reviewer, writes the report file and status trace.
5. Keep the stage `in-progress`. Give the user the filled-in resume line from the report contract and record it as the next action. Leave assessment and corrections for the owner's manual resume.

## Manual Owner Handoff

The owner follows [Resume With A Report](../../artifacts/stage-review.md#resume-with-a-report) when the user supplies the report path. Additional user notes are optional.
