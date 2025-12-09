# Exemplar: CLI Wrapper Skill

**Pattern:** CLI Wrapper
**Source:** prismis/SKILL.md
**Lines:** 54
**Use when:** Wrapping a single CLI tool with intent mapping

---

## Structure Analysis

- Frontmatter with explicit USE WHEN triggers
- Overview section (1-2 sentences)
- Instructions with IMPORTANT warnings
- Workflow (numbered steps)
- Common Operations (code blocks)

---

## Full Exemplar

```yaml
---
name: prismis
description: Query your Prismis content database via prismis-cli. Semantic search across saved articles, filter by priority (high/medium/low), view reading statistics, list unread entries, and retrieve specific content. USE WHEN user says "use prismis", "query prismis", "search prismis", "prismis articles", "prismis stats", "prismis unread", or searching saved articles.
allowed-tools: Bash
---
```

```markdown
# Prismis

## Overview

Query and access your Prismis content database for research and reference.

## Instructions

**IMPORTANT:** Use `prismis-cli --help` and `prismis-cli [command] --help`. DO NOT assume syntax.

- All commands support `--json` output for structured data
- Default to JSON output for parsing results
- Search uses semantic embeddings for relevance
- Limit results appropriately (default varies by command)

## Workflow

1. Determine operation needed (search/list/stats/export/get)
2. RUN `prismis-cli [command] --help` if unclear
3. Execute command with `--json` flag
4. Parse and present results clearly

## Common Operations

**Search** - use `--compact` first, then get articles of interest:
```bash
prismis-cli search "topic" --compact --limit 10 --json
prismis-cli get [entry-id] --raw      # article content
prismis-cli get [entry-id] --json     # full analysis (insights, patterns, quotes)
```

**List entries:**
```bash
prismis-cli list --limit 25 --json
prismis-cli list --priority high --json
prismis-cli list --unread --limit 10 --json
```

**Statistics:**
```bash
prismis-cli statistics --json
```

**Export:**
```bash
prismis-cli export --format json
```
```

---

## Key Patterns

1. **Tool-namespaced triggers:** "use prismis", "query prismis" - prevents collision with generic terms
2. **IMPORTANT warning:** Critical behavior note at top of Instructions
3. **Workflow:** Simple numbered steps for execution flow
4. **Code blocks:** Actual commands, not pseudo-code
5. **Compact:** ~54 lines total - no bloat
