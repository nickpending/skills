---
name: prismis
description: Query your Prismis content database via prismis-cli. Semantic search across saved articles, filter by priority/source, view reading statistics, list unread entries, and retrieve specific content. USE WHEN user says "use prismis", "query prismis", "search prismis", "prismis articles", "prismis stats", "prismis unread", "prismis sources", or searching saved articles.
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

**Search** - use `--compact` first, then get articles of interest:
```bash
prismis-cli search "topic" --compact --json
prismis-cli search "topic" -s Anthropic --compact --json   # filter by source (substring)
prismis-cli get <id> --raw                                 # article content
prismis-cli get <id> --json                                # full analysis
```

**List entries:**
```bash
prismis-cli list --limit 25 --json
prismis-cli list -s Anthropic --since-hours 168 --json     # source + time filter
prismis-cli list --priority high --unread --json
```

**Parse with jq:**
```bash
prismis-cli search "topic" --compact --json | jq '.[].title'
prismis-cli search "topic" --compact --json | jq '.[] | {id, title, source_name}'
```

**Statistics:**
```bash
prismis-cli statistics --json
```

**Export:**
```bash
prismis-cli export --format json
```
