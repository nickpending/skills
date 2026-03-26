---
name: skill-builder
description: Build and improve Claude Code skills. USE WHEN user says "create skill", "build skill", "new skill", "make skill", "improve skill", "update skill", "fix skill", "optimize skill", "migrate skill", or any request to create/modify/fix skills.
argument-hint: create|improve|validate|migrate [skill-path]
---

# Skill Builder

Build Claude Code skills through conversational workflows.

## Determine Action

Parse `$0` for the action keyword.

| `$0` | Workflow |
|------|----------|
| create | `workflows/create.md` |
| improve | `workflows/improve.md` |
| validate | `workflows/validate.md` |
| migrate | `workflows/migrate.md` |

## Execute

1. **READ** the workflow file matched by `$0`
2. **Follow** workflow instructions exactly

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

**Create a CLI wrapper skill:**
```
/skill-builder create
> "I want a skill to wrap the lore CLI"
> Selects CLI Wrapper archetype from skill-foundations
> Creates ~/.claude/skills/lore/SKILL.md with allowed-tools, argument-hint
```

**Validate a broken skill:**
```
/skill-builder validate ~/.claude/skills/visual/SKILL.md
> Checks frontmatter against skill-foundations structure.md
> Reports: missing argument-hint, no Examples section
> Offers automated fixes
```

