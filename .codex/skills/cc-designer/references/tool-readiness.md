# Tool Readiness Contract

`cc-designer` uses this reference before starting tool-backed design work. Its purpose is to make design-tool setup explicit without making Init heavy or requiring tools that the current project does not need.

## Tool Setup Principle

Use a two-layer model:

* **Baseline workflow materials** are part of the project bootstrap when available. This includes shared skills such as `.agents/skills/make-interfaces-feel-better/`.
* **Project-specific tools** are checked at the start of Designer. This includes account-backed plugins, visual workspaces, design platforms, and inspiration services such as Mobbin, MagicPath, Figma, Adobe, or Canva.

Do not block design work on a tool that is merely nice to have. Do block completion when the user chose a visual-review workflow and has not yet reviewed or approved the resulting design.

## Readiness Pass

At the start of Designer:

1. Read the brief, product specification, and functional specification.
2. Identify which design activities are actually needed: reference research, visual workspace, generated assets, design-system planning, prototype/mockup review, or final artifact writing.
3. Create a short tool plan with three groups:
   * **Required for this stage** - without it, the requested design process cannot be completed.
   * **Recommended** - useful enough to ask for, but not blocking.
   * **Not needed now** - plausible tools intentionally skipped.
4. Check available skills and tools before asking the user.
5. Ask the user whether Codex should install/connect available missing plugins or whether the user will add them manually and confirm readiness.

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

Use MagicPath when the design stage needs collaborative visual iteration or when the user wants to inspect and adjust the proposed design in a visual workspace.

MagicPath readiness may require several separate things:

* a Codex plugin or connector, if one is available in the user's environment;
* a MagicPath-specific skill or instructions supplied by the connector during setup;
* user login in the MagicPath session;
* a new or existing MagicPath project opened in the internal browser;
* enough project context copied or handed to the workspace to create the visual design;
* explicit user review and approval after the design is visible.

Operational flow:

1. Check whether a MagicPath plugin, connector, MCP tool, or MagicPath-provided skill is available.
2. If MagicPath requires installation or connection, ask the user to approve installing/connecting it through Codex, or to do it manually and confirm when ready.
3. After the connection is available, read any MagicPath-provided skill or setup instructions before using it.
4. Open MagicPath in the internal browser when browser control is available, or ask the user to open it there manually.
5. Ask the user to log in if needed.
6. Ask the user to create or open the project workspace.
7. Use the brief, product spec, functional spec, Mobbin/reference findings, and design direction to create or update the visual workspace.
8. Ask the user to review the design in MagicPath and either approve it or request changes.
9. Record the MagicPath project link or reference in `docs/project/design-brief.md` when available.
10. Keep Designer `in-progress` until the user explicitly approves the design direction.

If no MagicPath integration is available, do not invent one. Continue with structured artifacts and any available screenshots, generated visuals, or browser-based manual collaboration. Record the limitation in the design brief under tooling and deliverables.

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
* After explicit user approval, set design artifacts to `approved-for-architecture`, mark Designer `complete`, and move current stage to Architect.

Do not use Codex's own design review, a successful tool run, or a MagicPath project existing as a substitute for user approval.
