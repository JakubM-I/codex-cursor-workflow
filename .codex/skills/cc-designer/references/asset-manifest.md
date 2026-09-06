# Asset Manifest Contract

`cc-designer` owns `docs/project/asset-manifest.md`. The manifest is the durable handoff for every visual asset that the approved product needs, including the explicit conclusion that a category is not needed.

It does not choose an implementation library or replace a license review for third-party material. It makes asset ownership, readiness, provenance, and delivery timing visible before Cursor receives UI work.

## Frontmatter

```yaml
---
artifact: asset-manifest
version: 1
status: draft
stage: design
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related:
  - docs/project/design-brief.md
  - docs/project/screen-spec.md
  - docs/project/design-system.md
---
```

Allowed `status` values:

* `draft` - asset needs or ownership are still being defined;
* `ready-for-asset-decision` - the approved design can be reviewed and the user must choose whether to prepare outstanding assets now or defer them;
* `ready-for-implementation` - every required asset is available, explicitly deferred to a named earlier task, or explicitly not needed;
* `superseded` - a newer manifest replaces this one.

## Required Body

```md
# Asset Manifest: <Project Name>

## Asset Strategy

<Whether the product uses a logo, icon set, imagery, illustration, custom fonts, brand files, or no custom assets; distinguish representative mockup assets from final deliverables.>

## Asset Inventory

| ID | Asset | Purpose and screens | Source / owner | Format and variants | License / usage note | Status | Required by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | <Asset> | <Use> | <User / generated / third party / not needed> | <SVG, PNG, etc.> | <Known constraint> | <ready / provisional / deferred / not-needed> | <Milestone or task> |

## Delivery Decision

<Record the user's decision: prepare now, provide files, source licensed material, or defer to a named asset-preparation task before UI implementation.>

## Handoff To Implementation

<Exact files or source locations Cursor receives; if deferred, name the prerequisite task and state that UI work must not substitute unapproved assets.>
```

## Rules

* Include logos, favicons, icons, illustrations, images, fonts, audio/video, and any design-defining placeholder that must later be replaced.
* An icon library may be listed as a candidate or source only; Architecture selects the implementation package when that remains a stack decision.
* Record provenance and license or usage constraints for every third-party asset.
* A mockup may use a provisional asset, but the inventory must say so.
* After the user approves the design direction, ask whether outstanding assets should be prepared now, supplied by the user, sourced with approved rights, or deferred to a named prerequisite task.
* Do not create, download, upload, license, or publish assets without the user's appropriate authorization.
