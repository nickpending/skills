---
name: prompt-foundations
description: General prompt engineering patterns and principles. USE WHEN writing prompts, improving prompts, designing LLM interactions, or creating skills/commands/agents. Covers Anthropic best practices, conditionals, roles, output formats.
---

# prompt-foundations

Universal prompt engineering patterns. Applies to:
- Claude Code artifacts (skills, commands, agents)
- System prompts
- API prompts
- Any LLM interaction

## Content Routing

| Intent | Load |
|--------|------|
| principles, best practices, fundamentals, checklist | `principles.md` |
| conditionals, IF-THEN, feature flags, branching | `conditionals.md` |
| role, persona, "You are", identity | `roles.md` |
| output format, response structure, guidance | `output-guidance.md` |
| execution, STOP points, checkpoints, procedural | `execution-patterns.md` |
| directives, MUST/NEVER, variables, token efficiency | `writing-patterns.md` |
| primitives, skill vs command vs agent vs hook | `primitives.md` |

## Quick Reference

**Core principles:** Be clear/direct, use examples, assign roles, use XML tags, enable reasoning

**Conditionals:** IF-THEN-EXAMPLES pattern for routing and feature toggles

**Role establishment:** "You are a/an [expert type]..." opener pattern

**Output guidance:** Explicit sections telling model how to format responses

**Execution language:** CAPS tools (READ, RUN, STOP), MUST/NEVER directives

**Token efficiency:** Remove filler, use bullets over prose, reference don't repeat

## Artifact-Specific Patterns

For patterns specific to each artifact type, use:
- `skill-foundations` - skill triggering, USE WHEN, Examples sections
- `command-foundations` - frontmatter, preprocessing, archetypes
- (future) `agent-foundations` - agent triggering, `<example>` blocks
