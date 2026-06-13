---
type: architecture
subtype: component-detail
project: "skills"
component: "artifact-builder"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture, components]
---

# artifact-builder

**Purpose:** Build and improve Claude Code skills and commands through conversational workflows using archetype-based guidance.

## Current State

Two builder skills, version 1.2.0:

- **skill-builder** — Workflow Router archetype. Routes via `$0` dispatch to create/improve/validate/migrate workflows. INVOKEs skill-foundations and prompt-foundations. Has `argument-hint: create|improve|validate|migrate [skill-path]`. TaskCreate gates on create, improve, migrate workflows.
- **command-builder** — Same pattern, routes to command workflows. INVOKEs command-foundations and prompt-foundations. Has `argument-hint: create|improve|validate|migrate [command-path]`.

Each builder has 4 workflows: create.md, improve.md, validate.md, migrate.md. skill-builder also ships `tools/` — `validate_skill.py`, `validate_command.py`, `package_skill.py` (Python helpers invoked by the validate/package workflows); command-builder has no `tools/`.

## Design

Builders are Workflow Router archetype skills running in main thread with full conversation context. They orchestrate skill/command creation through multi-step conversational workflows.

Key design principle: builders delegate to foundations at runtime via INVOKE, not by duplicating content. This means foundations updates flow through automatically. The only inline content is the archetype recipe shortcuts in create.md (for quick reference during creation).

TaskCreate enforcement added to create/improve/migrate workflows (3+ sequential steps). validate.md excluded — read-only checks have lower skip-risk.

## Connections

- **Depends on:** artifact-foundations (skill-foundations, command-foundations, prompt-foundations) via INVOKE
- **User-facing:** Both skills are user-invocable via `/skill-builder` and `/command-builder`
