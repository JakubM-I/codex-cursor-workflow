# External Stage Review Contract

An external stage review is an independent, read-only critique run automatically after an owner prepares a reviewable stage draft. It produces a durable report; it never edits project artifacts, project status, or external services.

The stage owner launches the configured reviewer through its CLI, gives it only the relevant artifact paths and review instruction, captures its output, and creates the report. The owner then records a compact trace in `docs/project/status.md` and leaves the stage `in-progress`.

## Reviewer Map

| Stage | Owner | Automatic reviewer | Focus |
| --- | --- | --- | --- |
| Brief | Codex | Claude Code CLI | business risks, assumptions, contradictions, and difficult questions |
| Product / Functional Specification | Codex | Claude Code CLI | requirements logic, flows, states, and scope |
| Designer | Claude Code | Gemini CLI | design system, visual assets, and consistency with the brief |
| Architect | Codex | Codex subagent | unchanged in-process architecture review |
| Implementation Plan | Codex | Claude Code CLI | milestone order, dependencies, and validation gates |
| Project Verification | Codex | Codex subagent | unchanged in-process verification review |

## Report Location And Format

Save each report at:

```text
docs/project/reviews/<stage>-review-<YYYY-MM-DD>.md
```

If a same-day repeat is needed, append `-2`, `-3`, and so on. The report must use this shape:

```md
---
artifact: stage-review
version: 1
status: awaiting-owner-review
stage: <brief | product-functional-spec | design | implementation-plan>
reviewer: <claude-code | gemini>
reviewer_cli: <claude | gemini>
review_depth: <light | standard | deep>
created: YYYY-MM-DD
sources:
  - <reviewed artifact path>
related:
  - docs/project/status.md
---

# <Stage> External Review

## Review Context

- Owner: <stage owner and skill>
- Reviewer instruction: <agent-definition path>
- Scope and exclusions: <what the reviewer received>
- CLI result: <completed | unavailable | failed>
- Limitation: <if the CLI could not establish an authenticated review>

## Findings

### Must Fix

- <Only an evidence-backed contradiction, missing required criterion, or safety-critical gap.>

### Owner Assessment Required

- <Finding, evidence, impact, and suggested route.>

### User Decision Required

- <Finding, decision, and tradeoff.>

### Defer Or Route

- <Finding and owning later/upstream stage.>

### Clear Areas

- <Only actually reviewed areas with no material issue.>

## Handoff To Owner

Resume <owner skill> with <this report's repository-relative path>. You can add notes or limits for the fixes.
```

## Resume With A Report

The stage owner fills in the handoff line with the actual skill name and report path and repeats it in the handoff to the user. The same line serves as the next action in project status. The user can reuse it as-is or append notes. Naming the owner skill and the report is enough to invoke the default behavior. For example:

```text
Resume cc-brief with docs/project/reviews/brief-review-2026-11-07.md. Focus on the success criteria first.
```

On this invocation, resume the existing stage. Read the report, project status, and current versions of the relevant artifacts before editing. Confirm that the report belongs to this stage and that its evidence still applies. Treat reviewer findings as evidence to assess. Follow the user's additional notes as scope and priority for the correction pass.

By default, assess each material finding and apply verified, in-scope fixes that preserve agreed decisions. Record what was applied, rejected with a reason, deferred or routed, or left for the user's decision. Ask before changing a material decision or expanding scope. A confirmed, unresolved `Must Fix` blocks closure. If a finding is unsupported or already addressed, record the evidence for that disposition. After material revisions, run a fresh external review and return its new report for manual handoff.

## CLI And Handoff Rules

1. Run `.agents/scripts/check-reviewer-clis.sh` during Init and before the first required external review when the prior result is stale or missing.
2. A version check proves only that a CLI executable is available. It does not prove login, account entitlement, model access, or a successful real review.
3. Use the current reviewer's agent definition as the review instruction and name the exact artifacts to read. Do not give the reviewer write authority or ask it to run project-changing commands.
4. Capture CLI output. If the CLI is unavailable, unauthenticated, or fails, write the limitation in the report and block the review gate; do not silently substitute a same-model self-review.
5. After a successful report, update the current stage row's Notes with the report link and reviewer, set Next action to the filled-in resume line, and append a one-line Recent Updates entry. Keep detailed findings in the report.
