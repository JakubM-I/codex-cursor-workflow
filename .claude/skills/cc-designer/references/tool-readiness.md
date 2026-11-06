# Tool Readiness Contract

`cc-designer` uses this reference before starting tool-backed design work. Its purpose is to make design-tool setup explicit without making Init heavy or requiring tools that the current project does not need.

## Tool Setup Principle

Use a two-layer model:

* **Baseline workflow materials** are part of the project bootstrap when available. This includes shared skills such as `.agents/skills/make-interfaces-feel-better/`.
* **Project-specific tools** are checked at the start of Designer. This includes account-backed plugins, visual workspaces, design platforms, and inspiration services such as Mobbin, MagicPath, Figma, Adobe, or Canva.

Do not block design work on a tool that is merely nice to have. Do block the selected design mode when its required tool is unavailable, and do not silently downgrade that mode. Documentation-only is available only as an explicit user opt-out from references and visual validation.

## Readiness Pass

At the start of Designer:

1. Read the brief, product specification, and functional specification.
2. Present the three design modes: Reference research, Full visual design, and Documentation-only. Record the user's choice before creating the design direction.
3. Identify the activities required by that mode: reference research, visual workspace, generated assets, design-system planning, prototype/mockup review, or final artifact writing.
4. Create a short tool plan with three groups:
   * **Required for this stage** - without it, the requested design process cannot be completed.
   * **Recommended** - useful enough to ask for, but not blocking.
   * **Not needed now** - plausible tools intentionally skipped.
5. Check available skills and tools before asking the user.
6. Ask the user whether Claude Code should install/connect available missing plugins or whether the user will add them manually and confirm readiness.

Keep the question focused on the current project. Do not present a generic marketplace checklist.

## Mobbin

Use Mobbin when available and the project benefits from real UI references.

Search from concrete product needs:

* screens from `docs/project/functional-spec.md`;
* multi-step flows such as onboarding, checkout, search, creation, editing, review, or approval;
* web sections such as hero, pricing, dashboard, settings, editor, empty state, or admin area.

Inspect returned images before summarizing. In user-facing reference lists, cite each Mobbin result with its canonical Mobbin link.

If Mobbin is missing and would materially improve the work, ask whether the user wants to install/connect it or continue with other references.

## MagicPath

Use MagicPath when the user selects Full visual design and chooses it as the collaborative visual workspace.

1. Check the MagicPath integration available in Claude Code and read its setup and tool instructions. If connection or authentication is required, ask the user to complete the needed step. The user can sign in through their regular browser.
2. Verify the intended workspace and the integration's project and canvas capabilities. Reuse the confirmed project when one already exists. For a new project, create it through the integration when it exposes that operation. If the integration can edit an existing project but cannot create one, ask the user to create it in their MagicPath dashboard and share its link.
3. Use the brief, product spec, functional spec, reference findings, and design direction to create or iterate the designs on the remote canvas through the integration. Start when the connection and target project are ready. Opening a browser tab is optional for the user and independent of Claude Code's work.
4. Record the project link in `docs/project/design-brief.md` and share it with the user for review in their regular browser. If the integration returns only a project reference, provide that reference and the dashboard location instead. Keep Designer `in-progress` until the user explicitly approves the design direction.

If the integration is unavailable or cannot edit the canvas, offer another available visual workspace or ask the user to choose another design mode. Record the limitation and the user's decision in the design brief.

## Other Design Tools

Use Figma, Adobe, Canva, generated images, or other tools only when they match the current deliverable.

Examples:

* Figma is useful when the project needs a collaborative design source of truth or existing Figma assets.
* Adobe or Canva can help with brand, marketing, social, or template-based visual assets.
* Generated images can help with mood, art direction, bitmap mockups, illustrations, or asset direction.

Treat UI libraries and component systems as architecture inputs unless the user or existing project has already selected the stack. Designer may recommend qualities a library should have, but Architecture owns the final technical selection.

## Status Handling

Tool setup and visual review affect project status:

* During setup or design iteration, keep Designer `in-progress`.
* If a required tool or login is missing, set the blocker to that exact missing action.
* When artifacts are ready but awaiting user review, set the design artifacts to `ready-for-user-review` and keep Designer `in-progress`.
* After explicit user approval, resolve the asset-delivery decision in `docs/project/asset-manifest.md`. Only then set design artifacts to `approved-for-architecture`, mark Designer `complete`, and move current stage to Architect.

Do not use Claude Code's own design review, a successful tool run, or a MagicPath project existing as a substitute for user approval.
