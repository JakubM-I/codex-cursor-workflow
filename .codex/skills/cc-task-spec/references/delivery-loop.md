# Delivery Loop

Use this reference after Cursor hands back code or when delivery evidence changes the next task.

## Codex Verification

Start from the task's original acceptance criteria and Codex verification plan, not from the diff alone. Verify in proportion to the risk and the project instructions. Evidence can include automated tests, targeted runtime inspection, integration checks, manual scenario proof, static analysis, design or accessibility review, and independent code review.

State limitations precisely. A task can be accepted with a documented environment limitation only when that limitation does not leave an acceptance criterion unproven; otherwise it remains blocked or changes-required.

## Outcome Routing

| Evidence | Codex action |
| --- | --- |
| Criteria met, no material concern | Mark accepted; append delivery record; prepare the next ready slice. |
| Defect within frozen task scope | Revise the same task narrowly, increment revision, and return it to Cursor. |
| Task lacks a needed decision | Mark blocked and route to the decision owner. |
| Delivery changes a future milestone's practical approach | Record a pending downstream implication and amend the plan before the affected task is written. |
| Delivery invalidates product, design, architecture, security, deployment, cost, or acceptance assumptions | Update or route to the owning artifact; obtain user approval when its contract requires it. |

## Evidence And Records

Keep raw test output in the appropriate project-native place when it is needed. In the task delivery history and delivery log, record only reproducible commands or concise evidence, their result, and meaningful limitations.

Do not erase a failed attempt. Preserve its task revision, reason, and the resulting decision so later task authors can distinguish a deliberate correction from an accidental regression.
