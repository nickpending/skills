# Graph Query Patterns

Common Cypher query patterns for exploring Lore's knowledge graph.

## Graph Schema

### Node Types

- **Person:** `{ name }`
- **Project:** `{ name, description }`
- **Tech:** `{ name }`
- **Blog:** `{ title, date }`
- **Commit:** `{ sha, message, date }`

### Edge Types

- **WORKED_ON:** Person → Project
- **USES:** Project → Tech
- **WROTE:** Person → Blog
- **AUTHORED:** Person → Commit
- **BELONGS_TO:** Commit → Project
- **DISCUSSES:** Blog → Tech

## Technology Queries

### List All Technologies

```cypher
MATCH (t:Tech)
RETURN t.name AS technology
ORDER BY technology
```

### Technologies You've Worked With

```cypher
MATCH (p:Person)-[:WORKED_ON]->(proj:Project)-[:USES]->(t:Tech)
RETURN DISTINCT t.name AS technology
ORDER BY technology
```

### Count Projects Per Technology

```cypher
MATCH (p:Project)-[:USES]->(t:Tech)
RETURN t.name AS technology, count(p) AS project_count
ORDER BY project_count DESC
```

## Project Queries

### Projects Using Specific Technology

```cypher
MATCH (p:Project)-[:USES]->(t:Tech {name: 'Python'})
RETURN p.name AS project, p.description AS description
```

### Project Technology Stack

```cypher
MATCH (p:Project {name: 'lore'})-[:USES]->(t:Tech)
RETURN t.name AS technology
ORDER BY technology
```

### Related Projects by Shared Tech

```cypher
MATCH (p1:Project {name:'lore'})-[:USES]->(t:Tech)<-[:USES]-(p2:Project)
RETURN p2.name AS related_project, count(t) AS shared_tech
ORDER BY shared_tech DESC
```

### All Projects

```cypher
MATCH (p:Project)
RETURN p.name AS project, p.description AS description
ORDER BY project
```

## Commit Queries

### Commits by Project

```cypher
MATCH (p:Person)-[:AUTHORED]->(c:Commit)-[:BELONGS_TO]->(proj:Project)
RETURN proj.name AS project, count(c) AS commits
ORDER BY commits DESC
```

### Recent Commits

```cypher
MATCH (c:Commit)
RETURN c.message AS message, c.date AS date
ORDER BY c.date DESC
LIMIT 10
```

### Commits for Specific Project

```cypher
MATCH (c:Commit)-[:BELONGS_TO]->(p:Project {name: 'lore'})
RETURN c.sha AS sha, c.message AS message, c.date AS date
ORDER BY c.date DESC
```

## Blog Queries

### All Blog Posts

```cypher
MATCH (b:Blog)
RETURN b.title AS title, b.date AS date
ORDER BY b.date DESC
```

### Blogs Discussing Technology

```cypher
MATCH (b:Blog)-[:DISCUSSES]->(t:Tech {name: 'Python'})
RETURN b.title AS title, b.date AS date
ORDER BY b.date DESC
```

### Technologies Discussed in Blogs

```cypher
MATCH (b:Blog)-[:DISCUSSES]->(t:Tech)
RETURN t.name AS technology, count(b) AS blog_count
ORDER BY blog_count DESC
```

## Personal Network Queries

### People in Network

```cypher
MATCH (p:Person)
RETURN p.name AS person
ORDER BY person
```

### Projects Worked On

```cypher
MATCH (p:Person)-[:WORKED_ON]->(proj:Project)
RETURN proj.name AS project
ORDER BY project
```

### Authorship

```cypher
MATCH (p:Person)-[:AUTHORED]->(c:Commit)
RETURN p.name AS author, count(c) AS total_commits
ORDER BY total_commits DESC
```

## Complex Queries

### Technology Co-occurrence

```cypher
MATCH (t1:Tech)<-[:USES]-(p:Project)-[:USES]->(t2:Tech)
WHERE t1.name < t2.name
RETURN t1.name AS tech1, t2.name AS tech2, count(p) AS projects_together
ORDER BY projects_together DESC
LIMIT 20
```

### Most Active Projects (by commits)

```cypher
MATCH (c:Commit)-[:BELONGS_TO]->(p:Project)
RETURN p.name AS project, count(c) AS commits
ORDER BY commits DESC
LIMIT 10
```

### Technology Breadth

```cypher
MATCH (p:Project)-[:USES]->(t:Tech)
RETURN p.name AS project, count(t) AS tech_count
ORDER BY tech_count DESC
```

### Blog Coverage

```cypher
MATCH (p:Person)-[:WROTE]->(b:Blog)-[:DISCUSSES]->(t:Tech)
RETURN t.name AS technology, count(b) AS blog_posts
ORDER BY blog_posts DESC
```

## Output Formats

### CSV (default)

```bash
lore-graph query "MATCH (t:Tech) RETURN t.name"
```

Returns:
```
t.name
Python
TypeScript
Rust
```

### JSON Array

```bash
lore-graph query --json "MATCH (t:Tech) RETURN t.name"
```

Returns:
```json
[
  {"t.name": "Python"},
  {"t.name": "TypeScript"},
  {"t.name": "Rust"}
]
```

### JSON Lines

```bash
lore-graph query --jsonl "MATCH (t:Tech) RETURN t.name"
```

Returns:
```json
{"t.name": "Python"}
{"t.name": "TypeScript"}
{"t.name": "Rust"}
```

## Query Tips

**Case sensitivity:**
- Node labels are case-sensitive: `Tech` not `tech`
- Property names are case-sensitive: `name` not `Name`
- String matching is case-sensitive: `{name: 'Python'}` not `'python'`

**Filtering:**
- Use WHERE for complex conditions
- Use inline properties for exact matches: `{name: 'Python'}`

**Ordering:**
- Always use ORDER BY for consistent results
- Add LIMIT for large result sets

**Counting:**
- Use count() for aggregations
- count(n) counts nodes, count(*) counts rows

**Distinct:**
- Use DISTINCT to remove duplicates
- Especially useful with MATCH patterns that can duplicate results
