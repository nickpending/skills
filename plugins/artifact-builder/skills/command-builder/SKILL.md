---
name: command-builder
description: Build and improve Claude Code slash commands. USE WHEN user says "create command", "build command", "new command", "make command", "improve command", "fix command", "migrate command", or any request to create/modify/fix slash commands.
argument-hint: create|improve|validate|migrate [command-path]
---

# Command Builder

Build Claude Code slash commands through conversational workflows.

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

- **Conversational**: Discuss, don't interrogate. Offer examples from exemplars.
- **Exemplar-driven**: Point to working artifacts as references, not abstract templates.
- **Quality-focused**: Token efficiency, clarity, established patterns.
- **Teaching another AI**: You're writing instructions for AI consumption - be specific and unambiguous.

## Command Architecture

**INVOKE** `command-foundations` for:
- Structure requirements (frontmatter, preprocessing syntax)
- Archetypes (decision tree, body patterns)
- Exemplars (working examples per archetype)

**INVOKE** `prompt-foundations` for:
- Prompting principles (clarity, examples, XML tags)
- Directive patterns (IF-THEN, roles, output guidance)
- Writing style (model-consumable, not human-readable)

## Examples

**Create a commit command:**
```
/command-builder create
> "I want a command to commit my changes with conventional format"
> Selects minimal archetype from command-foundations
> Creates ~/.claude/commands/commit.md with !`git status` injection
```

**Improve a verbose command:**
```
/command-builder improve ~/.claude/commands/deploy.md
> Analyzes against command-foundations and prompt-foundations
> Reports: 40% token reduction possible, redundant sections
> Proposes changes, waits for approval
```
