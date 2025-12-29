# Command Structure

## Naming

- kebab-case filename (e.g., `fix-issue.md`)
- Filename becomes command name (`/fix-issue`)

## Frontmatter (YAML)

```yaml
---
description: What the command does (recommended)
allowed-tools: Tool restrictions (optional)
model: sonnet|opus|haiku (optional)
argument-hint: [expected args] (optional)
disable-model-invocation: true (optional)
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Recommended | Shown in /help, <60 chars best |
| `allowed-tools` | No | Used in 78% of official commands |
| `argument-hint` | No | Used in 33% of official commands |
| `model` | No | Rarely used in official examples |
| `disable-model-invocation` | No | Prevent programmatic calls |
| `hide-from-slash-command-tool` | No | Hide from discovery |

## Length Guidelines

| Metric | Best Practice |
|--------|---------------|
| Description | <60 chars |
| Body | 40-200 lines typical |

**Ranges by pattern:**
- Minimal: 17-40 lines
- Workflow: 40-200 lines
- Orchestration: 100-400+ lines

## Hard Limits

- **SlashCommand tool budget**: 15,000 chars — commands hidden from discovery if exceeded

## Preprocessing Syntax

| Syntax | Purpose |
|--------|---------|
| `!`\`command\` | Execute bash, inject output |
| `@path/to/file` | Include file contents |
| `$ARGUMENTS` | All arguments as string |
| `$1`, `$2`, etc. | Positional arguments |

## Body

Structure varies by archetype - see `archetypes.md`.
