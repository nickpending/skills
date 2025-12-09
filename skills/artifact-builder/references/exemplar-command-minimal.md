# Exemplar: Minimal Procedural Command

**Pattern:** Minimal Procedural
**Source:** Claude Code plugins/commit-commands/commands/commit.md
**Lines:** 18
**Use when:** Single task, immediate execution, no user interaction needed

---

## Structure Analysis

- Frontmatter with allowed-tools restriction
- Context section with !`backticks` for injection
- Your task section (single instruction)
- No Report section (action is self-evident)

---

## Full Exemplar

```yaml
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---
```

```markdown
## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit.

You have the capability to call multiple tools in a single response. Stage and create the commit using a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
```

---

## Key Patterns

1. **Tool restrictions:** `allowed-tools` limits to specific commands
2. **Context injection:** `!`backticks execute before model sees prompt
3. **Single task:** One clear instruction
4. **Constraint instructions:** "Do not use any other tools" - explicit boundaries
5. **No bloat:** 18 lines total - everything needed, nothing extra
6. **No Report:** Action is self-documenting (git commit output)

---

## Preprocessing Syntax

| Syntax | Purpose | Example |
|--------|---------|---------|
| `!`\`command\` | Execute command, inject output | `!`\`git status\` |
| `@file` | Include file contents | `@~/.ssh/config` |
| `$ARGUMENTS` | Command arguments | `/commit "message"` → `$ARGUMENTS` = "message" |
| `$1`, `$2` | Positional arguments | First and second args |
