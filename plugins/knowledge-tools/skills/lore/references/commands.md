# Lore Commands Reference

Quick reference for all Lore CLI commands.

## Search Commands

### lore-search

Search indexed knowledge across domains.

**Syntax:**
```bash
lore-search <domain> <query>
```

**Domains:**
- `development` - Search development projects (name, description, tech stack)
- `tasks` - Search flux tasks and ideas (description, project)
- `events` - Search events by project or type
- `blogs` - Search blog posts (title, topics, content preview)
- `commits` - Search git commit history (message, project, author)

**Examples:**
```bash
lore-search development python
lore-search tasks authentication
lore-search events lore
lore-search commits "fix bug"
lore-search blogs kubernetes
```

**Behavior:**
- Case-insensitive matching
- Searches multiple fields per domain
- Returns formatted results

## Indexing Commands

### lore-index-all

Rebuild all indices.

**Syntax:**
```bash
lore-index-all
```

Rebuilds:
- development.jsonl
- tasks.jsonl
- by-project.json
- recent.json
- blogs.jsonl
- commits.jsonl
- personal.jsonl

### Individual Index Commands

**lore-index-development**
```bash
lore-index-development
```
Scans PROJECT_SUMMARY.md files in development directories.

**lore-index-tasks**
```bash
lore-index-tasks
```
Indexes flux tasks and ideas.

**lore-index-events**
```bash
lore-index-events
```
Processes event log into indices.

**lore-index-blogs**
```bash
lore-index-blogs
```
Indexes blog posts with frontmatter metadata.

**lore-index-commits**
```bash
lore-index-commits
```
Indexes git commit history from all repos.

**lore-index-personal**
```bash
lore-index-personal
```
Indexes people, interests, and habits.

## Graph Commands

### lore-graph schema

Show graph schema (node and edge types).

**Syntax:**
```bash
lore-graph schema
```

**Output:**
- Node types with properties
- Edge types with relationships
- Example queries

### lore-graph query

Execute Cypher query.

**Syntax:**
```bash
lore-graph query <cypher>
lore-graph query --json <cypher>
lore-graph query --jsonl <cypher>
lore-graph query --csv <cypher>
```

**Options:**
- `--json` - Output as JSON array
- `--jsonl` - Output as JSON lines
- `--csv` - Output as CSV (default)

**Examples:**
```bash
lore-graph query "MATCH (t:Tech) RETURN t.name ORDER BY t.name"
lore-graph query --json "MATCH (p:Project) RETURN p.name"
lore-graph query "MATCH (p:Project)-[:USES]->(t:Tech {name: 'Python'}) RETURN p.name"
```

### lore-build-graph

Build knowledge graph from indices.

**Syntax:**
```bash
lore-build-graph
```

Creates:
- Person, Project, Tech, Blog, Commit nodes
- WORKED_ON, USES, WROTE, AUTHORED, BELONGS_TO, DISCUSSES edges

Run after indexing to update graph with latest data.

## Event Logging Functions

### lore_task_complete

Log task completion with full details.

**Syntax:**
```bash
lore_task_complete <project> <task_name> <problem> <solution> <code_snippet> \
  <discoveries> <deviations> <reusable_pattern> <keywords> <tech_used> <difficulty_notes>
```

**Example:**
```bash
lore_task_complete \
  "myproject" \
  "implement auth" \
  "Users needed authentication" \
  "Added JWT-based auth with refresh tokens" \
  "const token = jwt.sign({userId}, secret, {expiresIn: '1h'})" \
  "Refresh tokens prevent frequent re-login,Token rotation improves security" \
  "Added refresh token endpoint not in original plan" \
  "JWT with refresh token pattern - reusable for any stateless auth" \
  "auth jwt security tokens stateless" \
  "jsonwebtoken,express-jwt" \
  "Straightforward implementation, well-documented libraries"
```

### lore_flux_capture

Capture task, idea, or learning.

**Syntax:**
```bash
lore_flux_capture <item> [type] [tags]
```

**Examples:**
```bash
lore_flux_capture "Add dark mode to dashboard" "idea" "ui,enhancement"
lore_flux_capture "Write tests for API endpoints"
lore_flux_capture "Read about Event Sourcing" "learning" "architecture"
```

### lore_note

Quick note capture.

**Syntax:**
```bash
lore_note <content> [tags] [context]
```

**Examples:**
```bash
lore_note "PostgreSQL EXPLAIN ANALYZE shows index not being used"
lore_note "Bash parameter expansion \${var#prefix} removes prefix" "bash,shell"
lore_note "Team prefers functional approach" "architecture,team" "Code review"
```

## Personal Data Commands

### lore-person

Manage people in your network.

**Add person:**
```bash
lore-person add <name> --relationship <relationship> [--notes <notes>]
```

**List people:**
```bash
lore-person list
```

**Examples:**
```bash
lore-person add "Alice" --relationship "friend"
lore-person add "Bob" --relationship "colleague" --notes "Met at conference"
lore-person list
```

### lore-interest

Track interests.

**Add interest:**
```bash
lore-interest add <interest_name>
```

**List interests:**
```bash
lore-interest list
```

**Examples:**
```bash
lore-interest add "woodworking"
lore-interest add "kubernetes"
lore-interest list
```

### lore-habit

Track habits.

**Add habit:**
```bash
lore-habit add <habit_name> --frequency <frequency>
```

**List habits:**
```bash
lore-habit list
```

**Examples:**
```bash
lore-habit add "morning walk" --frequency "daily"
lore-habit add "weekly review" --frequency "weekly"
lore-habit list
```

## File Locations

**Config:**
```
~/.config/lore/config
```

**Event log:**
```
~/.local/share/lore/log.jsonl
```

**Indices:**
```
~/.cache/lore/indices/
├── development.jsonl
├── tasks.jsonl
├── by-project.json
├── recent.json
├── blogs.jsonl
├── commits.jsonl
└── personal.jsonl
```

**Graph database:**
```
~/.local/share/lore/graph.db
```

**Personal data:**
```
~/.local/share/lore/personal/
├── people.json
├── interests.json
└── habits.json
```

## Common Workflows

**After task completion:**
```bash
lore_task_complete "project" "task" "problem" "solution" "code" \
  "discoveries" "deviations" "pattern" "keywords" "tech" "notes"
lore-index-all
```

**After adding personal data:**
```bash
lore-person add "Name" --relationship "type"
lore-index-personal
lore-build-graph
```

**Searching knowledge:**
```bash
lore-search development python
lore-search commits authentication
lore-graph query "MATCH (p:Project)-[:USES]->(t:Tech) RETURN p.name, t.name"
```

**Maintaining indices:**
```bash
lore-index-all
lore-build-graph
```
