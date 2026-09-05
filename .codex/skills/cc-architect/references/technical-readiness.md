# Technical Readiness Contract

`cc-architect` uses this reference before finalizing implementation-enabling technical choices. Its purpose is to make missing capabilities, accounts, services, repositories, and tools explicit without turning architecture into setup work.

## Readiness Principle

Use a practical two-layer model:

* **Project evidence** comes first: brief, product and functional specs, approved design artifacts, user constraints, source repositories or starter projects referenced by the project, and existing conventions in the target project.
* **Implementation-enabling tooling** is checked during Architecture because the useful set depends on the selected stack, integrations, deployment target, auth model, and test strategy.

Do not block architecture on a tool that is merely nice to have. Do block completion when a missing decision, account, credential, source repository, or service would materially change stack selection, integration feasibility, auth design, deployment plan, or implementation sequencing.

## Source Repository Pass

When source repositories or reference implementations are available:

1. Identify which repositories are authoritative sources, inspiration, or reusable templates.
2. Inspect project structure, package manifests, config files, CI/deployment files, tests, auth code, data schemas, API boundaries, and docs where present.
3. Extract conventions that should inform the architecture: stack, module layout, naming, integration patterns, test commands, deployment assumptions, environment variables, and operational constraints.
4. Distinguish reusable patterns from project-specific details that should not be copied.
5. Record source repositories in `sources` and cite the relevant architectural takeaways in the artifact.

If a source repository cannot be accessed, record that limitation and ask the user only when its contents are needed to make a safe architecture decision.

## Tool Readiness Pass

At the start of Architecture or before finalization:

1. Read the available project artifacts and source repositories.
2. Identify technical activities that are actually needed: stack research, framework setup, database planning, API/integration work, auth setup, deployment, testing, observability, design-system implementation, or AI/model use.
3. Create a short tool plan with three groups:
   * **Required for implementation** - without it, the selected architecture cannot be implemented or validated as planned.
   * **Recommended** - useful enough to ask for, but not blocking.
   * **Not needed now** - plausible tools intentionally skipped.
4. Check available skills, plugins, CLIs, SDKs, and local project scripts before asking the user.
5. Ask whether Codex should install/connect available missing plugins or whether the user will add them manually and confirm readiness.

Keep the question project-specific. Do not present a generic marketplace checklist.

## Installation And Connection Boundaries

Codex may propose installing or connecting tools only when they materially help the current architecture or upcoming implementation.

Examples:

* GitHub plugin for repository inspection, issue/task coordination, or future PR work.
* Figma, Mobbin, Adobe, or Canva only when design assets remain relevant to implementation handoff.
* Netlify, Cloudflare, Vercel, Supabase, Firebase, or similar services only when deployment, backend, auth, storage, or edge requirements justify them and corresponding tools are available.
* Airtable, Notion, Google Drive, Slack, Jira, Linear, or similar tools only when the product or workflow depends on those systems.
* Model, AI gateway, or data-provider plugins only when AI features, external data, or current provider capabilities matter.

Do not install plugins, provision infrastructure, create repositories, configure billing, store secrets, or mutate external services without explicit user authorization and available tool support. When Codex cannot install or connect a needed tool, ask the user to do it manually and confirm readiness.

## Status Handling

Tool readiness affects project status:

* Keep Architect `in-progress` while a required decision or required tool/account is unresolved.
* If a required external account, credential, source repository, plugin, or service is missing, set the blocker to that exact missing action.
* If the architecture is sound but an implementation tool is merely recommended, record it as a recommendation and do not block completion.
* Do not mark Architecture complete until required tooling and source availability questions are either resolved, explicitly deferred, or represented as risks that do not change the architecture.
