# Lore Commands Reference

Complete reference for the Lore CLI.

## lore search

Search indexed knowledge across sources.

**Syntax:**
```bash
lore search <query>                 # Search all sources
lore search <source> <query>        # Search specific source
lore search --sources               # List available sources with counts
```

**Indexed Sources:**
| Source | Description |
|--------|-------------|
| blogs | Blog posts and articles |
| captures | Quick captures and notes |
| commits | Git commit history |
| development | Active development projects |
| events | Calendar events and meetings |
| explorations | Technical explorations |
| obsidian | Obsidian vault notes |
| personal | Personal data (books, movies, etc.) |
| readmes | Project README files |
| sessions | Claude Code session transcripts |
| tasks | Logged development tasks |

**Passthrough Sources:**
| Source | Description |
|--------|-------------|
| prismis | Semantic search via prismis daemon (requires prismis-daemon running) |

**Options:**
| Option | Description |
|--------|-------------|
| `--limit <n>` | Maximum results (default: 20) |
| `--since <date>` | Filter by date: today, yesterday, this-week, or YYYY-MM-DD |

**Examples:**
```bash
lore search "authentication"
lore search commits "fix bug"
lore search blogs "kubernetes"
lore search development "python" --limit 5
lore search tasks "auth" --since this-week
lore search prismis "security patterns"
```

## lore list

List entries from a domain.

**Syntax:**
```bash
lore list <domain>                  # List domain entries
lore list --domains                 # List available domains
```

**Domains:**
| Domain | Description |
|--------|-------------|
| blogs | Blog posts |
| books | Books read |
| captures | Quick captures |
| commits | Git commits |
| development | Development projects |
| events | Calendar events |
| explorations | Technical explorations |
| habits | Tracked habits |
| interests | Personal interests |
| movies | Movies watched |
| obsidian | Obsidian notes |
| people | People/contacts |
| personal | Personal data aggregate |
| podcasts | Podcasts listened |
| readmes | Project READMEs |
| sessions | Claude Code sessions |
| tasks | Development tasks |

**Options:**
| Option | Description |
|--------|-------------|
| `--limit <n>` | Maximum entries |
| `--format <fmt>` | Output format: json (default), jsonl, human |

**Examples:**
```bash
lore list development
lore list blogs --format human
lore list commits --limit 10
lore list books --format jsonl
```

## lore capture

Capture knowledge for future retrieval.

### lore capture task

Log task completion with full details.

```bash
lore capture task --project=<name> --name=<task> --problem=<desc> --solution=<desc>
```

| Option | Required | Description |
|--------|----------|-------------|
| `--project` | Yes | Project name |
| `--name` | Yes | Task name |
| `--problem` | Yes | Problem solved |
| `--solution` | Yes | Solution pattern |

**Example:**
```bash
lore capture task \
  --project="myproject" \
  --name="implement auth" \
  --problem="Users needed authentication" \
  --solution="Added JWT-based auth with refresh tokens"
```

### lore capture knowledge

Log an insight or learning.

```bash
lore capture knowledge --context=<name> --text=<insight> --type=<type>
```

| Option | Required | Description |
|--------|----------|-------------|
| `--context` | Yes | Context or project name |
| `--text` | Yes | Insight text |
| `--type` | Yes | Type: decision, learning, gotcha, preference |

**Example:**
```bash
lore capture knowledge \
  --context="lore" \
  --text="Unified CLI simplifies discoverability" \
  --type=learning
```

### lore capture note

Quick note capture.

```bash
lore capture note --text=<content> [--tags=<tags>] [--context=<ctx>]
```

| Option | Required | Description |
|--------|----------|-------------|
| `--text` | Yes | Note content |
| `--tags` | No | Comma-separated tags |
| `--context` | No | Optional context |

**Example:**
```bash
lore capture note --text="PostgreSQL EXPLAIN ANALYZE shows index not being used"
lore capture note --text="Bash \${var#prefix} removes prefix" --tags="bash,shell"
```

## lore-graph

Query the knowledge graph using Cypher.

```bash
lore-graph schema                   # Show graph schema
lore-graph query "<cypher>"         # Execute Cypher query
lore-graph query --json "<cypher>"  # Output as JSON array
lore-graph query --jsonl "<cypher>" # Output as JSON lines
lore-graph query --csv "<cypher>"   # Output as CSV (default)
```

**Examples:**
```bash
lore-graph schema
lore-graph query "MATCH (t:Tech) RETURN t.name ORDER BY t.name"
lore-graph query --json "MATCH (p:Project) RETURN p.name"
```

See `graph-patterns.md` for common Cypher patterns.

## lore-index-all

Rebuild all indices. Run after significant data changes.

```bash
lore-index-all
```
