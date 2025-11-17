---
name: lore
description: Query personal knowledge fabric indexed across development projects, tasks, events, blogs, commits, and personal data. Use when searching past work, exploring project relationships, logging discoveries, managing personal network data, or investigating commit history and technology usage patterns.
allowed-tools: Read, Bash
model: haiku
---

# Lore

## Overview

Query and manage your indexed knowledge across development, commits, tasks, events, and personal data.

**IMPORTANT:** Use `--help` with all lore commands to see current options. DO NOT assume command structure.

## Commands

**List:**
```bash
lore-list {domain}
```
Domains: development, tasks, events, blogs, commits, explorations, readmes, books, movies, podcasts, interests, people, habits

**Search:**
```bash
lore-search {domain} {query}
```
Domains: development, tasks, events, blogs, commits, personal

**Graph:**
```bash
lore-graph schema
lore-graph query "{cypher}"
```

**Index:**
```bash
lore-index-all
lore-index-{domain}
lore-index-personal && lore-build-graph  # After personal data changes
```

**Personal:**
```bash
lore-person add "{name}" --relationship "{type}" [--notes "{text}"]
lore-person list

lore-interest add "{topic}"
lore-interest remove "{topic}"
lore-interest list

lore-habit add "{habit}" [--frequency "{freq}"]
lore-habit list
```

## Intent Mapping

**Development Projects:**
- "what projects", "show my projects", "list projects" → `lore-list development`
- "find Python projects", "projects using Redis" → `lore-search development python`

**Tasks:**
- "show my tasks", "what tasks exist" → `lore-list tasks`
- "tasks about auth", "find lore tasks" → `lore-search tasks auth`

**Events:**
- "show events", "what events happened" → `lore-list events`
- "events for lore project" → `lore-search events lore`

**Blogs:**
- "list blog posts", "what have I written" → `lore-list blogs`
- "blogs about kubernetes", "find python posts" → `lore-search blogs kubernetes`

**Commits:**
- "show commits", "recent commits" → `lore-list commits`
- "commits by author", "commits about auth" → `lore-search commits nickpending`

**Explorations:**
- "show explorations", "what explorations exist" → `lore-list explorations`

**READMEs:**
- "list readmes", "show project readmes" → `lore-list readmes`

**Books:**
- "what books have I read", "show my books" → `lore-list books`

**Movies:**
- "what movies", "show movies I've watched" → `lore-list movies`

**Podcasts:**
- "show podcasts", "what podcasts do I listen to" → `lore-list podcasts`

**People:**
- "show my network", "list people", "who do I know" → `lore-list people` or `lore-person list`
- "add person Alice" → `lore-person add "Alice" --relationship "friend"` → reindex

**Interests:**
- "what are my interests", "show interests" → `lore-list interests` or `lore-interest list`
- "add interest woodworking" → `lore-interest add "woodworking"` → reindex
- "remove interest X" → `lore-interest remove "X"` → reindex

**Habits:**
- "show my habits", "what habits do I track" → `lore-list habits` or `lore-habit list`
- "add habit morning walk" → `lore-habit add "morning walk" --frequency "daily"` → reindex

**Personal (search across all):**
- "search personal data for X" → `lore-search personal X`

**Graph queries:**
- "what technologies", "show all tech" → `MATCH (t:Tech) RETURN t.name ORDER BY t.name`
- "technologies I've used" → `MATCH (p:Person)-[:WORKED_ON]->(proj:Project)-[:USES]->(t:Tech) RETURN DISTINCT t.name`
- "related projects", "projects similar to X" → Related projects query
- "show schema", "what's in the graph" → `lore-graph schema`

**Indexing:**
- "re-index", "rebuild indices", "refresh data", "update indices" → `lore-index-all`

## Common Cypher

List technologies:
```cypher
MATCH (t:Tech) RETURN t.name ORDER BY t.name
```

Projects using tech:
```cypher
MATCH (p:Project)-[:USES]->(t:Tech {name: 'Python'}) RETURN p.name
```

Related projects by shared tech:
```cypher
MATCH (p1:Project {name:'X'})-[:USES]->(t:Tech)<-[:USES]-(p2:Project)
RETURN p2.name, count(t) AS shared ORDER BY shared DESC
```

Technologies you've used:
```cypher
MATCH (p:Person)-[:WORKED_ON]->(proj:Project)-[:USES]->(t:Tech)
RETURN DISTINCT t.name ORDER BY t.name
```

More patterns: `references/graph-patterns.md`

## Schema

Nodes: Person, Project, Tech, Blog, Commit, Interest, Habit, Book, Movie, Podcast
Edges: WORKED_ON, USES, WROTE, AUTHORED, BELONGS_TO, DISCUSSES

## Execution

Parse intent → construct command → execute → return output

Multi-domain: Run per domain, consolidate
After personal changes: Always reindex with `lore-index-personal && lore-build-graph`
