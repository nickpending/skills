---
type: architecture
subtype: component-detail
project: "skills"
component: "artifact-foundations"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture, components]
---

# artifact-foundations

**Purpose:** Reference content for building Claude Code skills, commands, and prompts — archetypes, structure rules, and exemplars.

## Current State

Three foundations skills, version 1.1.1:

- **skill-foundations** — structure.md (frontmatter, directory, features), archetypes.md (6 archetypes with templates), decisions.md (feature decisions, recipes, TaskCreate enforcement), plus 4 exemplars
- **command-foundations** — structure.md, archetypes.md (4 archetypes: minimal, priming, workflow, orchestration), plus exemplars
- **prompt-foundations** — principles.md, conditionals.md, roles.md, output-guidance.md, execution-patterns.md, writing-patterns.md, primitives.md (7 reference docs routed by a content table)

Each foundations skill carries a `## Content Routing` table that maps intent to the file to load on INVOKE. Frontmatter is `name` + `description` only — there is no `disable-model-invocation` field on these skills (they are still auto-discoverable; the routing table is what scopes which doc a consumer reads).

## Design

Foundations are Foundations archetype skills — pure reference content, no execution logic. They load only when explicitly INVOKEd by other skills. Content routing tables tell the invoker which file to read based on intent.

Key design decision: foundations are consumed at runtime, not at build time. This means updates to foundations automatically improve all consumers without requiring consumer changes.

## Connections

- **Consumed by:** artifact-builder (skill-builder, command-builder), prompt-tools
- **No dependencies** — foundations are self-contained reference material
