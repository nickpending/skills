---
name: skill-builder
description: Build and improve Claude Code skills. USE WHEN user says "create skill", "build skill", "new skill", "make skill", "improve skill", "update skill", "fix skill", "optimize skill", "migrate skill", or any request to create/modify/fix skills.
---

# Skill Builder

Build Claude Code skills through conversational workflows.

## Determine Action

**From user's message, identify:**

| Intent | Keywords | Workflow |
|--------|----------|----------|
| Create new | "create", "build", "make", "new" | `workflows/create.md` |
| Improve existing | "improve", "optimize", "refactor", "tighten" | `workflows/improve.md` |
| Validate structure | "validate", "check", "verify" | `workflows/validate.md` |
| Fix structure | "migrate", "fix format", "validation errors" | `workflows/migrate.md` |

## Execute

1. **Determine action** from user's request
2. **READ** the appropriate workflow file
3. **Follow** workflow instructions exactly

## Key Principles

- **Conversational**: Discuss, don't interrogate. Show examples, iterate on feedback.
- **Exemplar-driven**: Point to working artifacts as references, not abstract templates.
- **Quality-focused**: Token efficiency, clarity, established patterns.
- **Teaching another AI**: You're writing instructions for AI consumption - be specific and unambiguous.

## Skill Architecture

**INVOKE** `skill-foundations` for:
- Structure requirements (frontmatter, directory)
- Archetypes (decision tree, body patterns)
- Exemplars (working examples per archetype)

**INVOKE** `prompt-foundations` for:
- Prompting principles (clarity, examples, XML tags)
- Directive patterns (IF-THEN, roles, output guidance)
- Writing style (model-consumable, not human-readable)

## Examples

**Example 1: Create a CLI wrapper skill**
```
User: "Create a skill to wrap the lore CLI"
→ Invokes create workflow
→ Selects CLI wrapper archetype
→ Creates ~/.claude/skills/lore/
→ Sets up command routing table
```

**Example 2: Validate a broken skill**
```
User: "The visual skill won't trigger, check it"
→ Invokes validate workflow
→ Checks frontmatter and USE WHEN clause
→ Reports missing intent triggers
→ Offers automated fix
```

