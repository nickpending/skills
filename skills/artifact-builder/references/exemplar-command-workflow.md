# Exemplar: Workflow Command

**Pattern:** Workflow
**Source:** big-3-super-agent/.claude/commands/build.md
**Lines:** 24
**Use when:** Variables, conditional logic, structured execution with report

---

## Structure Analysis

- Frontmatter with description, argument-hint, allowed-tools, model
- Variables section (maps $ARGUMENTS)
- Workflow section (conditional + steps)
- Report section (output format)

---

## Full Exemplar

```yaml
---
description: Build the codebase based on the plan
argument-hint: [path-to-plan]
allowed-tools: Read, Write, Bash
model: claude-sonnet-4-5-20250929
---
```

```markdown
# Build

Follow the `Workflow` to implement the `PATH_TO_PLAN` then `Report` the completed work.

## Variables

PATH_TO_PLAN: $ARGUMENTS

## Workflow

- If no `PATH_TO_PLAN` is provided, STOP immediately and ask the user to provide it.
- Read the plan at `PATH_TO_PLAN`. Think hard about the plan and implement it into the codebase.

## Report

- Summarize the work you've just done in a concise bullet point list.
- Report the files and total lines changed with `git diff --stat`
```

---

## Key Patterns

1. **argument-hint:** Shows expected arguments in help
2. **Variables section:** Maps `$ARGUMENTS` to meaningful name
3. **model override:** Forces specific model (sonnet for implementation)
4. **Conditional logic:** "If no X, STOP and ask"
5. **Report format:** Specific output expectations (bullet list, git diff)
6. **Compact:** 24 lines - structured but minimal

---

## Frontmatter Options

| Field | Purpose | Example |
|-------|---------|---------|
| `description` | What command does (required) | "Build the codebase based on the plan" |
| `allowed-tools` | Tool restrictions | "Read, Write, Bash" |
| `model` | Force specific model | "claude-sonnet-4-5-20250929" |
| `argument-hint` | Help text for args | "[path-to-plan]" |
