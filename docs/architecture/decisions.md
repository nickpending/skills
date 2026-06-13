---
type: architecture
subtype: decisions
project: "skills"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture, decisions]
---

# Decisions

Architectural decisions and their rationale. Most recent first.

## Prefer $0 dispatch over freeform keyword matching for workflow routers

**Context:** skill-builder and command-builder used freeform keyword synonym matching (create/build/make/new → create workflow). This was fragile and redundant when argument-hint already provides discoverability.
**Choice:** Switch to `$0` positional dispatch with `argument-hint: create|improve|validate|migrate [path]`.
**Why:** argument-hint handles discoverability, $0 handles routing cleanly. No need for synonym soup when hints exist.

## Builders delegate to foundations via INVOKE, not duplication

**Context:** Builder skills need foundations knowledge (archetypes, structure rules, feature recipes) to do their job.
**Choice:** INVOKE foundations at runtime rather than duplicating content in builder workflows.
**Why:** Foundations updates flow through automatically without requiring builder changes. Only inline recipe shortcuts in create.md risk minor staleness.

## TaskCreate enforcement for multi-step workflows

**Context:** Models skip steps in multi-step flows when there's no explicit gate. Builder workflows (create, improve, migrate) each have 5+ sequential steps.
**Choice:** Add TaskCreate gate instructions to multi-step workflows. Excluded validate.md (read-only checks have lower skip-risk).
**Why:** TaskCreate is behavioral enforcement, not progress tracking. Models follow through more reliably when each gate requires explicit task completion.

## knowledge-tools removed — superseded by Sable built-ins

**Context:** knowledge-tools plugin provided lore and prismis skills. Sable now includes these as built-in capabilities.
**Choice:** Remove knowledge-tools from marketplace and delete the plugin directory.
**Why:** Redundant. Sable built-ins are authoritative and always available.
