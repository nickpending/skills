---
name: command-builder
description: Build and improve Claude Code slash commands. USE WHEN user says "create command", "build command", "new command", "make command", "improve command", "fix command", "migrate command", or any request to create/modify/fix slash commands.
---

# Command Builder

Build Claude Code slash commands through conversational workflows.

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

**Example 1: Create a simple commit command**
```
User: "Create a command to commit my changes"
-> Invokes create workflow
-> Selects minimal archetype
-> Creates ~/.claude/commands/commit.md
-> Uses !`git status` for context injection
```

**Example 2: Improve an existing command**
```
User: "This deploy command is too verbose, tighten it up"
-> Invokes improve workflow
-> Analyzes current token usage
-> Proposes reductions
-> Gets user approval before changes
```
