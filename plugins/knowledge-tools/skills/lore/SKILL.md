---
name: lore
description: Query personal knowledge fabric indexed across development projects, tasks, events, blogs, commits, and personal data. USE WHEN user says "use lore", "query lore", "search lore", "lore projects", "lore commits", "lore events", "lore blog posts", or searching past work and project history.
allowed-tools: Bash
---

# Lore

Query and capture indexed knowledge across your development history.

## Instructions

**IMPORTANT:** Run `lore --help` or `lore [command] --help` if uncertain about syntax.

- Default output is JSON — use `jq` for filtering
- Search sources and list domains differ — check `--sources` vs `--domains`
- `lore-graph` is separate for Cypher queries

## Workflow

1. Determine operation (search / list / capture / graph)
2. RUN appropriate command
3. Parse JSON output and present results

## Common Operations

**Search:**
```bash
lore search "query"                    # all sources
lore search commits "authentication"   # specific source
lore search --sources                  # list available sources
```

**List:**
```bash
lore list development                  # domain entries
lore list blogs --format human         # human-readable
lore list --domains                    # list available domains
```

**Capture:**
```bash
lore capture knowledge --context=X --text="Y" --type=learning
lore capture task --project=X --name="Y" --problem="Z" --solution="W"
lore capture note --text="X"
```

**Graph queries:**
```bash
lore-graph schema                      # show schema
lore-graph query "MATCH (t:Tech) RETURN t.name"
```

## References

- `references/commands.md` — Full command reference with options
- `references/graph-patterns.md` — Cypher query patterns
