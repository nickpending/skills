---
type: architecture
subtype: boundaries
project: "skills"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture, boundaries]
---

# Boundaries

Interface contracts between components and external systems.

## Foundations INVOKE Contract

**Between:** artifact-builder ↔ artifact-foundations
**Contract:** Builder SKILL.md declares `**INVOKE** skill-foundations for:` with intent list. Claude loads the foundations skill into context at runtime. Workflows reference already-loaded foundations content without re-invoking.
**Constraints:** Builders must not hardcode foundations content or file paths. Foundations must maintain stable content routing tables so INVOKE callers can find what they need.

## Marketplace Plugin Contract

**Between:** plugins ↔ `.claude-plugin/marketplace.json`
**Contract:** Each plugin has a name, description, version, source path, and category. Source path points to a directory containing the plugin's skills/commands.
**Constraints:** Version bumps required on changes (patch for fixes, minor for features, major for breaking). Plugin names are stable identifiers — renaming breaks installations.

## Skill Frontmatter Contract

**Between:** skills ↔ Claude Code runtime
**Contract:** SKILL.md frontmatter fields (`name`, `description`, `argument-hint`, `allowed-tools`, `context`, `model`, etc.) are parsed by Claude Code to control skill discovery, invocation, and execution behavior.
**Constraints:** Field semantics defined by Claude Code platform. skill-foundations `structure.md` documents current field reference. Breaking changes come from upstream (Claude Code), not from this project.
