# Voidwire Skills

<div align="center">

**Production-ready Claude Code plugins for artifact authoring, network discovery, and personal data tools**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## Installation

```bash
# Add marketplace
/plugin marketplace add nickpending/skills

# Install plugins
/plugin install artifact-builder@voidwire-skills
/plugin install homenet-tools@voidwire-skills
/plugin install knowledge-tools@voidwire-skills
```

## Plugins

### artifact-builder

Build and improve Claude Code skills and commands with archetype-based guidance.

**Skills included:**
- **skill-builder** — Create skills with archetype selection (CLI Wrapper, Workflow Router, Knowledge Injection, Foundations)
- **command-builder** — Create commands with archetype selection (Minimal, Priming, Workflow, Orchestration)

**Triggers:** "create skill", "build command", "improve skill", "validate command"

### homenet-tools

Discover and map your home network via nmap, SSH, and DNS.

**Skills included:**
- **homenet-discovery** — Multi-method network discovery with topology diagrams

**Triggers:** "map network", "discover homelab", "what's on my network"

**Prerequisites:** nmap, python3, SSH keys (optional)

### knowledge-tools

Query personal knowledge bases and content databases.

**Skills included:**
- **lore** — Query indexed knowledge fabric (projects, commits, books, movies, people)
- **prismis** — Query article database (semantic search, priority filtering, reading stats)

**Triggers:** "what projects", "find commits", "search prismis", "reading stats"

**Prerequisites:** lore CLI, prismis-cli

## Structure

```
plugins/
├── artifact-builder/
│   └── skills/
│       ├── skill-builder/
│       └── command-builder/
├── homenet-tools/
│   └── skills/
│       └── homenet-discovery/
└── knowledge-tools/
    └── skills/
        ├── lore/
        └── prismis/
```

## Dependencies

artifact-builder skills use foundations from `~/.claude/skills/`:
- skill-foundations
- command-foundations
- prompt-foundations

## License

MIT
