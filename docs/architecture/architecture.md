---
type: architecture
subtype: overview
project: "skills"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture]
---

# skills Architecture

> A Claude Code plugin marketplace providing production-ready skills, commands, and foundations for artifact authoring, network discovery, and personal data tools. Distributed as a single marketplace (`voidwire-skills`) containing multiple plugins, each with their own skills.

## Principles

- **Foundations-driven:** Builder skills delegate to foundations at runtime via INVOKE — foundations are the source of truth for structure, archetypes, and patterns.
- **Archetype-based:** Every skill follows a recognized archetype (CLI Wrapper, Workflow Router, Forked Workflow, Forked Validator, Knowledge Injection, Foundations) with tested feature recipes.
- **Self-dogfooding:** Builder skills must be exemplar-compliant with the standards they enforce on others.
- **Plugin isolation:** Each plugin is independently versioned and self-contained. Cross-plugin dependencies are via skill invocation, not file references.

## Components

| Component | Purpose | Detail |
|-----------|---------|--------|
| artifact-foundations | Reference patterns for skills, commands, and prompts | [components/artifact-foundations.md](components/artifact-foundations.md) |
| artifact-builder | Build and improve skills and commands using foundations | [components/artifact-builder.md](components/artifact-builder.md) |
| homenet-tools | Home network discovery and topology mapping | — |
| prompt-tools | Prompt creation and improvement | — |

## Key Decisions

See [decisions.md](decisions.md) for the full decision log.

## Boundaries

See [boundaries.md](boundaries.md) for interface contracts.
