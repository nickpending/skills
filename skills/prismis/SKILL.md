---
name: prismis
description: Query your Prismis content database via prismis-cli. Semantic search across saved articles, filter by priority (high/medium/low), view reading statistics, list unread entries, and retrieve specific content. USE WHEN user says "use prismis", "query prismis", "search prismis", "prismis articles", "prismis stats", "prismis unread", or searching saved articles.
allowed-tools: Bash
---

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

**Semantic search:**
```bash
prismis-cli search "topic or query" --limit 20 --json
```

**List recent entries:**
```bash
prismis-cli list --limit 50 --json
```

**Filter by priority:**
```bash
prismis-cli list --priority high --json
prismis-cli list --priority medium --json
prismis-cli list --priority low --json
```

**Show unread items:**
```bash
prismis-cli list --unread --limit 20 --json
```

**Display statistics:**
```bash
prismis-cli statistics --json
```

**Get specific entry:**
```bash
prismis-cli get [entry-id] --json
```

**Export data:**
```bash
prismis-cli export --format json
```
