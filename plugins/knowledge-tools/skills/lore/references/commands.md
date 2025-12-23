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

**Sources:** commits, tasks, obsidian, personal, captures, explorations, blogs, readmes, development, events

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
```

## lore list

List entries from a domain.

**Syntax:**
```bash
lore list <domain>                  # List domain entries
lore list --domains                 # List available domains
```

**Domains:** development, tasks, events, blogs, commits, explorations, readmes, obsidian, captures, books, movies, podcasts, interests, people, habits

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
lore list --domains
```

## lore capture

Capture knowledge for future retrieval.

### lore capture task

Log task completion with full details.

**Syntax:**
```bash
lore capture task --project=<name> --name=<task> --problem=<desc> --solution=<desc>
```

**Required options:**
| Option | Description |
|--------|-------------|
| `--project` | Project name |
| `--name` | Task name |
| `--problem` | Problem solved |
| `--solution` | Solution pattern |

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

**Syntax:**
```bash
lore capture knowledge --context=<name> --text=<insight> --type=<type>
```

**Required options:**
| Option | Description |
|--------|-------------|
| `--context` | Context or project name |
| `--text` | Insight text |
| `--type` | Type: decision, learning, gotcha, preference |

**Example:**
```bash
lore capture knowledge \
  --context="lore" \
  --text="Unified CLI simplifies discoverability" \
  --type=learning
```

### lore capture note

Quick note capture.

**Syntax:**
```bash
lore capture note --text=<content> [--tags=<tags>] [--context=<ctx>]
```

**Options:**
| Option | Description |
|--------|-------------|
| `--text` | Note content (required) |
| `--tags` | Comma-separated tags |
| `--context` | Optional context |

**Example:**
```bash
lore capture note --text="PostgreSQL EXPLAIN ANALYZE shows index not being used"
lore capture note --text="Bash \${var#prefix} removes prefix" --tags="bash,shell"
```

## lore-graph

Query the knowledge graph using Cypher.

**Syntax:**
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

**Syntax:**
```bash
lore-index-all
```

