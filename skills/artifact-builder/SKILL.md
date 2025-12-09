---
name: artifact-builder
description: Build and improve Claude Code slash commands, skills, and agents. USE WHEN user says "create skill", "build skill", "new skill", "make skill", "improve skill", "update skill", "fix skill", "optimize skill", "create command", "build command", "new command", "make command", "improve command", "migrate skill", "migrate command", or any request to create/modify/fix Claude Code artifacts.
---

# Artifact Builder

Build Claude Code artifacts (skills and slash commands) through conversational workflows.

## Determine Action

**From user's message, identify:**

| Intent | Keywords | Workflow |
|--------|----------|----------|
| Create new | "create", "build", "make", "new" | `workflows/create.md` |
| Improve existing | "improve", "optimize", "refactor", "tighten" | `workflows/improve.md` |
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

## Skill Exemplars

| Pattern | Lines | Reference |
|---------|-------|-----------|
| CLI wrapper | 54 | `references/exemplar-skill-cli-wrapper.md` |
| Multi-command CLI | 154 | `references/exemplar-skill-multi-command.md` |
| Workflow router | 132 | `references/exemplar-skill-workflow-router.md` |
| Procedural | 638 | `references/exemplar-skill-procedural.md` |
| Knowledge injection | 42 | `references/exemplar-skill-knowledge-injection.md` |

## Command Exemplars

| Pattern | Lines | Reference |
|---------|-------|-----------|
| Minimal procedural | 18 | `references/exemplar-command-minimal.md` |
| Priming | 53 | `references/exemplar-command-priming.md` |
| Workflow | 24 | `references/exemplar-command-workflow.md` |
| Multi-phase orchestration | 126 | `references/exemplar-command-orchestration.md` |

## Writing References

For prompt writing patterns, tool selection, and command syntax:

**RUN** `/prime-references prompting`
