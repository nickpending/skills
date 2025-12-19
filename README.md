# Skills

<div align="center">

**Production-ready Claude Code skills for building workflows, commands, and automation**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

Production skills for building Claude Code artifacts, automating network discovery, and querying personal knowledge bases.

## Installation

```bash
# In Claude Code
/plugin marketplace add nickpending/skills

# Install skills individually:
/plugin install skill-builder@voidwire-skills
/plugin install command-builder@voidwire-skills
/plugin install homenet-discovery@voidwire-skills
/plugin install lore@voidwire-skills
/plugin install prismis@voidwire-skills
```

## What's Inside

### skill-builder

Build and improve Claude Code skills with archetype-based guidance. Uses foundations pattern for consistent structure.

**Triggers:** "create skill", "build skill", "new skill", "improve skill"

**Features:**
- Archetype selection (CLI Wrapper, Workflow Router, Knowledge Injection, Foundations)
- Structure validation against skill-foundations
- Conversational workflows for create/validate/improve
- Prompt-foundations integration for writing patterns

**Outputs:**
- Complete skill directories with SKILL.md + workflows/references as needed
- Follows progressive disclosure and execution language patterns

### command-builder

Build and improve Claude Code slash commands with archetype-based guidance.

**Triggers:** "create command", "build command", "new command", "improve command"

**Features:**
- Archetype selection (Minimal, Priming, Workflow, Orchestration)
- Structure validation against command-foundations
- Preprocessing syntax guidance
- Prompt-foundations integration

**Outputs:**
- Validated markdown command files
- Proper frontmatter (description, allowed-tools, argument-hint)

### homenet-discovery

Automated home network discovery via nmap, SSH, and DNS. Creates machine-readable inventory with topology diagrams for infrastructure documentation.

**Triggers:** "map network", "discover homelab", "what's on my network"

**Features:**
- Multi-method discovery (nmap, SSH, DNS)
- Service detection and metadata extraction
- Topology diagram generation (Mermaid)
- Machine-readable inventory format

**Outputs:**
- Device inventory with services and metadata
- Network topology diagrams
- AI-friendly markdown documentation

**Prerequisites:** nmap, python3, SSH keys (optional), DNS access (optional)

### lore

Query your indexed personal knowledge fabric covering development projects, tasks, events, blogs, commits, and personal data. Simple tool skill for direct CLI command execution.

**Triggers:** "what projects", "find commits", "show tasks", "list books"

**Features:**
- List operations across all domains (development, tasks, events, blogs, commits, books, movies, etc.)
- Semantic search within domains
- Cypher graph queries for exploring relationships
- Personal data management (people, interests, habits)

**Outputs:**
- Filtered search results
- Complete domain listings
- Graph query results showing technology connections

**Prerequisites:** lore CLI tools installed and indexed

### prismis

Query your Prismis content database for semantic search, priority filtering, and reading statistics. Simple tool skill for direct prismis-cli access.

**Triggers:** "search prismis", "show priority articles", "reading stats"

**Features:**
- Semantic search across saved articles
- Priority filtering (high/medium/low)
- Reading statistics and unread tracking
- Content retrieval by ID

**Outputs:**
- Search results with relevance scores
- Filtered article lists
- Reading analytics

**Prerequisites:** prismis-cli installed with indexed content

## Development

### Project Structure

```
skills/
├── skill-builder/           # Skill creation with archetypes
│   ├── SKILL.md             # Router with INVOKE pattern
│   └── workflows/           # create.md, validate.md
├── command-builder/         # Command creation with archetypes
│   ├── SKILL.md             # Router with INVOKE pattern
│   └── workflows/           # create.md, validate.md
├── homenet-discovery/       # Network discovery
│   ├── SKILL.md             # Router
│   ├── workflows/           # discover.md, update.md
│   ├── references/          # setup-guides.md
│   ├── scripts/             # Discovery and parsing scripts
│   ├── parsers/             # proxmox, opnsense, unifi parsers
│   └── templates/           # Output format templates
├── lore/                    # Personal knowledge fabric queries
│   ├── SKILL.md             # Tool skill
│   └── references/          # Graph patterns, command reference
└── prismis/                 # Content database queries
    └── SKILL.md             # Tool skill
```

### Key Patterns

- **Router pattern:** SKILL.md <200 lines, delegates to focused workflows
- **INVOKE pattern:** SKILL.md invokes foundations, workflows reference loaded content
- **Progressive disclosure:** metadata → SKILL.md → workflows/references loaded on-demand
- **Execution language:** CAPS tool names, STOP points, VERIFICATION sections
- **Foundations:** skill-builder and command-builder use `*-foundations` skills for reference content

## Related Foundations

These skills work with foundations skills (installed separately):

- `skill-foundations` - Structure rules, archetypes, exemplars
- `command-foundations` - Command structure, archetypes, preprocessing
- `prompt-foundations` - Prompt engineering principles, patterns

## Usage

Skills trigger automatically based on natural language matching their descriptions. Builders use conversational workflows to guide creation through discovery, archetype selection, and implementation phases.

Each skill follows progressive disclosure patterns and produces model-friendly output with clear execution language.

## Contributing

Skills follow established patterns documented in foundations. Use skill-builder to create new skills with consistent structure and quality.

## License

MIT
