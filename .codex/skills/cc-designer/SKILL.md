---
name: cc-designer
description: Define a project's UX and visual direction after product and functional specification. Use when the project needs screen structure, interaction model, inspiration research, design system direction, component inventory, or design-tool handoff before technical architecture or implementation planning.
argument-hint: "[product/functional spec paths, design notes, brand references, or tool preferences]"
---

# CC Designer

Turn ready product and functional specifications into durable UX and visual-design artifacts.

This is a design-planning stage. It defines how the product experience should be structured, feel, and behave visually. It may use external design tools, visual inspiration, screenshots, generated references, and shared UI-polish guidance. It does not choose the technical stack, create production code, plan implementation tasks, or make final brand decisions the user has not approved.

## Inputs And Context

Read `.agents/artifacts/project-status.md` and `docs/project/status.md` when they exist. At the start of this stage, mark Designer as `in-progress` unless the project is already blocked or paused. Do not change another stage's row except when recording a completed handoff from this stage.

Read these project artifacts before asking questions or writing design artifacts:

```text
docs/project/brief.md
docs/project/product-spec.md
docs/project/functional-spec.md
```

If product or functional specifications are missing, blocked, or not ready for design, explain the gap and route back to `cc-spec`. If existing design artifacts exist, read them before asking questions, preserve settled decisions, and revise in place instead of creating duplicates.

Treat user-provided brand files, screenshots, references, and tool outputs as direct inputs. Treat external examples as inspiration unless the user names them as a required reference.

## Tool And Plugin Readiness

Designer is the first stage that normally needs account-backed creative and research tools. Tool setup is mandatory; the selected design mode determines which tools must be connected. Use a hybrid installation model:

* baseline shared skills that are part of the workflow, especially `.agents/skills/make-interfaces-feel-better/`, should be included during Init or repository bootstrap when available;
* project-specific external tools and account-backed plugins should be checked at the start of Designer, because the needed set depends on product type, platform, and user preference.

At the start of the stage, inspect available tools and ask the user to choose one design mode. Do not silently choose a documentation-only path:

* **Reference research** - inspect and compare relevant UI references, then produce design artifacts without an original visual workspace. Requires an appropriate reference tool.
* **Full visual design** - inspect references, create or iterate a visual design, and obtain visual approval. This is the default for a new user-facing interface. Requires a reference tool and a visual workspace such as MagicPath, Figma, or an equivalent available tool.
* **Documentation-only** - no references and no visual design. This is an explicit user opt-out; record that later implementation will not have pre-code visual validation.

Present the required, recommended, and intentionally unneeded tools for the selected mode. Ask the user whether Codex should install/connect available missing tools or whether the user will add them manually and confirm readiness. If a required tool for the selected mode is unavailable, keep Designer blocked until the user connects it or explicitly chooses another mode.

Preferred tool routing:

* **Mobbin** - use for real UI and UX references when available. Search specific screens, flows, or website sections from the functional spec. Inspect returned images before summarizing them. Cite Mobbin links in any user-facing reference list.
* **MagicPath** - use as a collaborative visual workspace when the user selects the full visual-design mode and MagicPath is the chosen tool. Since it may require the user's browser session and login, pause at the right moment and ask the user to log in, open or create the project, and confirm that Codex should continue from that workspace.
* **Generated visual references and assets** - use when the project needs mood, art direction, bitmap mockups, logos, icons, illustrations, or other asset direction that is not well covered by existing product references.
* **Figma, Adobe, Canva, or similar tools** - use only when available and appropriate for the requested deliverable. Do not require a tool because it is popular; require it only when the work benefits from that tool's actual output.

If a tool is unavailable, record the limitation. Do not pretend a manual visual workspace has been created or downgrade a selected mode without the user's explicit decision.

## Collaboration Model

Work as a UX and visual-design collaborator, not as a template filler.

Develop the design direction through inspection, reference gathering, and focused conversation:

* derive design requirements from the brief, product spec, functional spec, user roles, flows, states, and acceptance criteria;
* identify which screens, flows, and interaction areas need visual decisions;
* gather references for similar patterns when this would improve the result;
* compare references by usable design qualities, not vague style labels;
* recommend a direction when the option space is clear;
* ask the user to decide when a choice affects brand personality, target feel, major layout model, workflow density, or design-tool ownership;
* record unresolved but non-blocking design assumptions rather than inventing certainty.

Use `.codex/agents/design-researcher.md` when the project needs independent reference gathering, especially for Mobbin searches, competitor/inspiration comparison, or multiple possible UX patterns. The researcher is read-only and returns evidence to `cc-designer`; it does not write design artifacts or choose the final direction.

Ask small rounds of questions. Prefer one material design decision at a time. Group at most three independent questions when they can be answered without creating dependent branches.

## Design Areas

Cover the areas that matter for the product. Do not force irrelevant sections, but do not skip a material surface just because the product spec was short.

Define:

* UX principles and experience qualities;
* platform and viewport assumptions;
* screen or view inventory;
* primary navigation and information architecture;
* key layouts and content hierarchy;
* interaction patterns, transitions, feedback, and state behavior;
* visual direction, including typography, color, spacing, density, imagery, iconography, surfaces, and motion;
* component inventory and component states;
* accessibility, responsive behavior, and usability constraints;
* design constraints that Architecture and Implementation Plan must account for.

For **Full visual design**, create visual evidence that makes the proposed layout reviewable before implementation. Cover the primary desktop and mobile (when relevant) viewports plus the key task states or flows that would materially affect the layout. A visual workspace, linked static prototype, or rendered mockups are valid; a text-only screen specification is not.

Use `.agents/skills/make-interfaces-feel-better/` as the default UI-polish lens when it is present. It should influence typography, surfaces, animation restraint, icon treatment, hit areas, and final design review. It should not override the product's brand direction, accessibility needs, or established design system.

When using `make-interfaces-feel-better`, use the full skill directory, including its supporting files such as `typography.md`, `surfaces.md`, `animations.md`, `icons.md`, and `performance.md`. Read the relevant supporting file before applying detailed guidance in that category.

## Artifact Ownership

This skill owns:

```text
docs/project/design-brief.md
docs/project/screen-spec.md
docs/project/design-system.md
docs/project/asset-manifest.md
```

It also maintains the Designer row and project-level fields in `docs/project/status.md` according to the shared project-status contract. It does not write the technical architecture, implementation plan, Cursor task specs, or production code.

Before writing or revising artifacts, read:

* [the tool readiness contract](references/tool-readiness.md);
* [the design brief contract](references/design-brief.md);
* [the screen spec contract](references/screen-spec.md);
* [the design system contract](references/design-system.md).
* [the asset manifest contract](references/asset-manifest.md).

These references define required frontmatter, headings, status values, and readiness checks.

For very small projects, the three artifacts may remain concise. Do not collapse them into one file unless the user explicitly asks for a lighter artifact set; later stages benefit from being able to read visual direction, screen structure, and component rules independently.

## Design Review

Before marking the stage ready, run a design readiness review.

Classify design complexity as `light`, `standard`, or `deep` based on number of screens, user roles, workflow density, visual ambiguity, brand consequence, accessibility risk, responsive complexity, and interaction/state complexity.

Review the design artifacts against:

* alignment with the brief and product/functional specs;
* coverage of main flows, screens, states, and edge cases;
* consistency of layout, hierarchy, components, and interaction patterns;
* accessibility and responsive expectations;
* clear handoff constraints for architecture and planning;
* UI polish using `.agents/skills/make-interfaces-feel-better/` when present.
* the selected design mode, its reference or visual evidence, and asset-manifest completeness.

Use `.codex/agents/design-critic.md` when an independent reviewer is available and the project is `standard` or `deep`. If subagent execution is unavailable, perform the same review as a clearly separated self-review and report that limitation. The reviewer is read-only and does not update artifacts or project status.

When a project artifact validator is available, run it before moving design artifacts to `ready-for-user-review` or `approved-for-architecture`. Treat validator failures as corrections for the owning stage artifacts, not as permission to rewrite unrelated documents.

Apply only small clarity fixes automatically. Ask the user before changing brand direction, primary layout model, navigation model, density, motion personality, or design-tool deliverable ownership.

## User Review And Approval

Designer requires an explicit user approval gate before completion.

When the design artifacts, selected-mode evidence, and asset manifest are ready for review, keep the Designer stage `in-progress` and update `docs/project/status.md` with:

* Current stage: Designer
* Next action: User reviews the design direction, selected-mode evidence, and asset strategy.
* Blockers: Awaiting user design approval, or a specific design decision if one is missing.
* Designer row: `in-progress`, linked to the current design artifacts, with a note such as `Ready for user design review`.

For Full visual design, ask the user to review the visual workspace or mockups and explicitly approve or request changes to the proposed layout, visual direction, and responsive behavior. Record the workspace link or visual-evidence reference in the design artifacts. A generic instruction to proceed is not design approval.

After the user approves the design direction, ask whether outstanding assets in `asset-manifest.md` should be prepared now, supplied by the user, sourced with approved rights, or deferred to a named prerequisite task before UI implementation. Record the decision and do not create or source assets without the necessary authorization.

When the user requests changes, revise the relevant design artifacts and visual workspace notes, then return to user review. Do not treat the design-critic verdict or Codex's own review as a substitute for user approval.

## Completion

Write or update the design artifacts when the product experience is clear enough for architecture to account for the intended UX and visual system. Artifacts may remain `draft` when non-blocking assumptions remain visible.

Do not mark the stage complete while a missing decision would materially change:

* the main navigation or screen structure;
* the visual direction or brand personality;
* a core interaction pattern;
* accessibility or responsive behavior;
* component system expectations;
* design constraints that affect architecture.

Also do not mark the stage complete until the user explicitly approves the design direction after reviewing the selected-mode evidence and, for Full visual design, the visual workspace or mockups. The asset manifest must be `ready-for-implementation`, with each asset ready, not needed, or deferred to a named prerequisite task.

When the stage is approved, mark the design artifacts as `approved-for-architecture`, mark Designer as `complete`, set Architect as the current stage, link all design artifacts in the stage register, append one concise status update, then close Designer according to `.agents/artifacts/stage-closure.md`. Finish with a concise summary of:

* the design brief path and status;
* the screen spec path and status;
* the design system path and status;
* the asset manifest path and delivery decision;
* the chosen visual/UX direction;
* references or tool outputs used;
* blocking decisions or assumptions, if any;
* the suggested next stage: Architect.
