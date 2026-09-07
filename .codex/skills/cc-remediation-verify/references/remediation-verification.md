# Remediation Verification Guide

Acceptance of a remediation task is evidence that its bounded correction was made; it does not prove that the whole project or a `PV-*` finding is closed.

Use this order:

1. Compare Cursor's report and actual changed source areas against the remediation packet.
2. Reproduce or inspect the original finding evidence before relying on a newly passing check.
3. Run the task's stated targeted checks and regression boundary.
4. Record whether the findings are ready for project-level revalidation, still open, or blocked.

For every failed or unproven criterion, record the finding ID, observed evidence, affected area, minimal correction or input, and whether it remains inside the approved remediation scope. A newly discovered material product, design, architecture, security, cost, account, deployment, or launch issue requires user routing; do not silently absorb it into the packet.

Use this record in the packet and report:

```md
### Remediation Verification Result — R-001-TASK-001 / revision 1

- Outcome: accepted | changes-required | blocked
- Finding evidence: <reproduced evidence and result>
- Regression evidence: <check and result>
- Finding state: ready-for-revalidation | open | blocked
- Project revalidation trigger: <scope or `Not triggered yet`.>
- Required user action: <approval, decision, or `None`.>
```

When visual fidelity is part of the finding, named DOM structure or source inspection alone is insufficient: inspect the required visual references, viewports, and states.
