---
name: lore
description: Query personal knowledge fabric across projects, commits, tasks, blogs, and captures. USE WHEN user says "use lore", "search lore", "what projects", "what did I work on", "find commits", "search my knowledge", "list my tasks", "what have I written", or searching past work and project history.
allowed-tools: Read, Bash
---

# Lore

Query and capture indexed knowledge across development, commits, tasks, events, and personal data.

**IMPORTANT:** If uncertain about syntax, run `lore --help`.

## Commands

```bash
lore search [source] <query>    # Search knowledge
lore list <domain>              # List entries
lore capture <type>             # Capture knowledge
lore-graph schema|query         # Graph queries
```

## Intent Routing

| User wants | Command |
|------------|---------|
| Search across everything | `lore search "query"` |
| Search specific source | `lore search <source> "query"` |
| List domain entries | `lore list <domain>` |
| See what sources exist | `lore search --sources` |
| See what domains exist | `lore list --domains` |
| Graph schema | `lore-graph schema` |
| Cypher query | `lore-graph query "<cypher>"` |
| Capture insight | `lore capture knowledge --context=X --text="Y" --type=learning` |
| Capture task | `lore capture task --project=X --name="Y" --problem="Z" --solution="W"` |
| Quick note | `lore capture note --text="X"` |

## Sources & Domains

**Search sources:** commits, tasks, obsidian, personal, captures, explorations, blogs, readmes, development, events

**List domains:** development, tasks, events, blogs, commits, explorations, readmes, obsidian, captures, books, movies, podcasts, interests, people, habits

## Common Patterns

```bash
# Find projects using a technology
lore search development "python"

# Recent commits about a topic
lore search commits "authentication"

# List all blog posts
lore list blogs

# What technologies have I used?
lore-graph query "MATCH (p:Project)-[:USES]->(t:Tech) RETURN DISTINCT t.name"

# Projects related by shared tech
lore-graph query "MATCH (p1:Project {name:'X'})-[:USES]->(t:Tech)<-[:USES]-(p2:Project) RETURN p2.name, count(t) AS shared ORDER BY shared DESC"
```

## Options

**Search:**
- `--limit <n>` — Max results (default: 20)
- `--since <date>` — Filter by date (today, yesterday, this-week, YYYY-MM-DD)

**List:**
- `--limit <n>` — Max entries
- `--format <fmt>` — json (default), jsonl, human

## References

- `references/commands.md` — Full command reference
- `references/graph-patterns.md` — Cypher query patterns
