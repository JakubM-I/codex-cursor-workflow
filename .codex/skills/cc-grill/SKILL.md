---
name: cc-grill
description: Pressure-test a project idea, plan, or product decision through a structured interview. Use when cc-brief or the user needs to expose assumptions, resolve dependent decisions, compare credible directions, or test whether the stated solution addresses the real problem.
argument-hint: "[idea, plan, or decision to pressure-test]"
---

# CC Grill

Run a focused discovery interview that turns an ambiguous idea into explicit decisions, assumptions, and open questions.

This is a supporting Codex skill. It does not own a project artifact, create documentation, choose a technical solution, or start implementation. The calling stage owns any durable output.

## Start With What Is Already Known

Use the user's message and relevant project materials as the starting point. Separate:

* confirmed facts from user-provided or authoritative sources;
* facts that can be checked in the available environment;
* assumptions that still need confirmation;
* decisions that belong to the user.

Find available facts yourself before asking the user for them. Do not infer product priorities, user needs, business rules, or constraints from code or naming.

## Build And Work The Decision Map

Map the discussion as a decision tree. A decision may reveal dependent questions, but do not ask a dependent question before its prerequisite is settled.

Work in short rounds. In each round, ask the current frontier: the material questions whose prerequisites are known. Ask at most three independent questions together. Use one question when the decision is consequential, emotionally nuanced, or likely to need follow-up.

For every question:

1. state the decision in plain language;
2. explain why it matters to the project;
3. offer concrete options when the option space is clear;
4. mark one option as recommended and give the reason;
5. leave room for the user to choose a different direction.

Use open questions when options would prematurely narrow the user's thinking. Do not use a long questionnaire or ask questions merely because a template contains a field.

## Pressure-Test The Direction

As the map fills in, test only the lenses relevant to the idea:

* **Evidence**: what shows that the problem or need is real?
* **Specificity**: can the desired outcome be recognized in practice?
* **Counterfactual**: what happens if the project is not built or the change is not made?
* **Solution attachment**: are we defending a chosen solution instead of solving the problem?
* **Scope and durability**: is the first version bounded, and does it create enough lasting value for its cost?
* **Integration**: do the user's answers create a conflict or an unstated requirement when combined?

Present contradictions, hidden tradeoffs, and alternative framings as observations. Do not turn a challenge into a requirement without the user's agreement. Offer two or three approaches only when more than one is genuinely credible; otherwise recommend the clear direction directly.

## Stop Conditions And Handoff

End when every material branch is either:

* settled by the user;
* recorded by the calling stage as an explicit assumption;
* deferred to a named later stage; or
* identified as a blocking decision.

Return a compact handoff to the calling stage:

* settled decisions;
* assumptions to validate;
* contradictions or risks surfaced;
* blocking decisions and deferred questions;
* recommended next action.

When called by `cc-brief`, return the result to that skill so it can update `docs/project/brief.md`. Do not write the brief yourself.
