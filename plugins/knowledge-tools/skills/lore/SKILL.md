---
name: lore
description: Query personal knowledge fabric with semantic and text search across development projects, tasks, events, blogs, commits, and personal data. USE WHEN user says "use lore", "query lore", "search lore", "lore projects", "lore commits", "lore events", "lore blog posts", or searching past work and project history.
allowed-tools: Bash
---

# Lore

Query indexed knowledge across development history. Two search modes with different purposes.

## Choosing Search Mode

**Semantic (default)** — meaning-based retrieval:
- Exploratory questions: "what have I done with kubernetes?"
- Conceptual queries: "authentication patterns", "error handling approaches"
- Finding related work when you don't know exact terms
- Understanding context and background

**FTS5 (`--exact`)** — literal text matching:
- Specific code: function names, class names, variable names
- Exact phrases the user quotes
- Error messages, log patterns
- When semantic returns noise because term is common

**Decision rule:** Is the query about *meaning* or about *literal text*? Meaning → semantic. Literal → `--exact`.

## Search

```bash
lore search "authentication patterns"      # semantic
lore search --exact "def process_data"     # FTS5 literal
lore search commits "refactor auth"        # semantic, specific source
lore search --sources                      # list sources with counts
```

**Passthrough sources** (external systems):
```bash
lore search prismis "security patterns"    # prismis daemon
lore search atuin "docker build"           # shell history
```

## Other Operations

```bash
lore list development                      # domain entries
lore list --domains                        # available domains
lore capture knowledge --context=X --text="Y" --type=learning
lore capture teaching --domain=X --confidence=Y --text="Z"
lore-graph ask "what technologies does lore use?"
lore-graph related-to <project>            # projects sharing tech
```

