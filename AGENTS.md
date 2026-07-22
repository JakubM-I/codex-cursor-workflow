# Repository Guidelines

## Project Scope

This Shopify theme is based on Eurus. The main work is preparing new custom page sections plus supporting elements: blocks, snippets, JavaScript, CSS, schema settings, and translations. Existing BLG examples include `sections/blg-media-with-text.liquid`, `sections/blg-faq-with-text-panel.liquid`, `sections/blg-media-with-text-group.liquid`, and `blocks/blg-media-with-text-item.liquid`. Do not treat this as a Shopify app or connected store project.

## Project Structure & Module Organization

Create custom sections in `sections/`. Put reusable Liquid fragments in `snippets/`, blocks in `blocks/`, and JavaScript or SVG files in `assets/`. Keep section or block-specific CSS primarily inside the Liquid file with `{%- style -%}` / `{% style %}` or `{% stylesheet %}` when that matches the existing pattern. Use CSS assets only for shared or clearly separate styles. Global settings are in `config/`; translations live in `locales/`.

Keep related files named consistently. If a section needs styles or scripts, reuse the feature name:

- `sections/blg-media-with-text-group.liquid`
- `assets/blg-media-with-text-group.js`

## Native Shopify Theme Safety

The most important rule: do not edit native Shopify or base Eurus theme elements directly. Work only on copies that can be freely changed.

When copying an existing section, block, snippet, or asset, first reproduce it 1:1 with all functions, settings, blocks, presets, responsive behavior, dark/RTL handling, and dependencies. Rename the copy with the BLG prefix, then modify or extend that BLG copy. Leave original files intact.

## Naming Conventions

Every new file, section, block, snippet, asset, schema group, or related technical element must start with the `blg-` prefix. Use kebab-case filenames, for example `blg-media-with-text-group.liquid`.

Visible names in the Shopify panel should start with `BLG`, then use a normal human-readable name. Do not mechanically duplicate the filename. For example:

```json
"name": "BLG Media with text group"
```

Follow project conventions: two-space indentation, Liquid whitespace control, inline section styles scoped by `section.id` or `block.id`, descriptive schema IDs, and deferred scripts when loaded from Liquid.

## Local Validation

This project is not directly connected to Shopify. Do not run a store preview, test the whole theme, push to Shopify, or rely on `shopify theme dev`.

Testing is local and code-focused:

- inspect Liquid syntax and schema JSON validity;
- verify asset, snippet, and section references;
- compare copied BLG elements against the source to ensure no functions were dropped unintentionally;
- check that copied elements use BLG names consistently;
- review CSS/JS selectors for collisions with native theme code;
- confirm no native theme files were edited accidentally.

Use `rg`, `sed`, JSON validation tools, or `shopify theme check` only when useful locally.

## Git Workflow

Agents must not create commits, pull requests, pushes, branches, rebases, or other git workflow actions. Git is handled manually by the user.

It is acceptable to inspect git state or history, for example `git status --short`, but do not stage or modify history.

## Agent-Specific Instructions

When adding or modifying BLG elements, keep changes scoped and aligned with the existing theme style. Prefer copying and adapting Eurus patterns over inventing new architecture. Before finishing, summarize changed BLG files and local checks.

When Shopify documentation or specification details are needed, use the Context7 MCP source for Shopify docs before making assumptions.

## AI Working Modes

This repository supports different AI-assisted working modes, including standalone implementation, analysis and specification, implementation from an existing task specification, and code review.

The active working mode is determined by the user's current instruction. Do not assign a permanent role to Codex, Cursor, or another coding agent.

Detailed workflows, task handoff conventions, and task specification structure are described in:

* `docs/workflows/ai-development.md`
