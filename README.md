# Voidwire Skills

<div align="center">

**Claude Code plugins for building artifacts, engineering prompts, and querying personal knowledge**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

**Voidwire Skills** extends Claude Code with production-ready plugins. Learn to build skills and commands with battle-tested patterns. Engineer better prompts with proven principles. Query your personal knowledge bases without leaving the conversation.

Some plugins are general-purpose tools anyone can use. Others integrate with personal infrastructure (noted below).

## Quick Start

```bash
# Add the marketplace (one time)
/plugin marketplace add nickpending/skills

# Install what you need
/plugin install artifact-foundations@voidwire-skills  # Reference patterns
/plugin install artifact-builder@voidwire-skills      # Build skills/commands
/plugin install prompt-tools@voidwire-skills          # Prompt engineering
```

That's it. Skills trigger automatically based on what you're doing.

## Plugins

### artifact-foundations

Reference patterns for building Claude Code skills, commands, and prompts. The knowledge base that powers artifact-builder.

**What's inside:**
- **skill-foundations** — Structure rules, four archetypes (CLI Wrapper, Workflow Router, Knowledge Injection, Foundations), real exemplars
- **command-foundations** — Structure rules, four archetypes (Minimal, Priming, Workflow, Orchestration), real exemplars
- **prompt-foundations** — Anthropic best practices, conditionals, roles, output formats, execution patterns

**Example usage:**
```
"How should I structure a skill that wraps a CLI tool?"
→ Loads skill-foundations, explains CLI Wrapper archetype with exemplar

"What's the difference between a Workflow and Orchestration command?"
→ Loads command-foundations, compares archetypes with examples
```

### artifact-builder

Build and improve Claude Code skills and commands with guided workflows.

**What's inside:**
- **skill-builder** — Create, improve, and validate skills with archetype selection
- **command-builder** — Create, improve, and validate commands with archetype selection

**Example usage:**
```
"Create a skill that queries my todo app"
→ Asks clarifying questions, selects CLI Wrapper archetype, generates SKILL.md

"Improve my existing skill - it's not triggering correctly"
→ Analyzes SKILL.md, identifies description issues, rewrites with proper USE WHEN pattern
```

### prompt-tools

Create and improve prompts using prompt engineering best practices.

**Commands:**
- `/create-prompt [purpose]` — Build a well-structured prompt from scratch
- `/improve-prompt [text or path]` — Analyze and improve an existing prompt

**Example usage:**
```
/create-prompt summarize technical papers for non-experts
→ Gathers requirements, applies principles, outputs complete prompt

/improve-prompt "You are helpful. Summarize this."
→ Identifies issues (vague role, no output format), rewrites with improvements
```

### homenet-tools

Discover and map your home network via nmap, SSH, and DNS.

**What's inside:**
- **homenet-discovery** — Multi-method network discovery with topology diagrams

**Example usage:**
```
"What devices are on my network?"
→ Runs nmap scan, consolidates results, generates topology diagram

"Map my homelab"
→ Discovers services, SSH connections, DNS records, outputs inventory
```

**Prerequisites:** nmap, python3, SSH keys (optional)

### knowledge-tools

Query personal knowledge bases and content databases.

**What's inside:**
- **lore** — Query indexed knowledge fabric (projects, commits, books, movies, people)
- **prismis** — Query article database (semantic search, priority filtering, reading stats)

**Example usage:**
```
"What projects have I worked on involving React?"
→ Queries lore, returns matching projects with context

"Search prismis for articles about local-first architecture"
→ Semantic search across saved articles, returns matches with priority
```

**Prerequisites:**
- [lore](https://github.com/nickpending/lore) CLI (coming soon)
- [prismis-cli](https://github.com/nickpending/prismis) for article queries

## Why Plugins?

**The problem:** Claude Code skills and commands are powerful, but there's no easy way to share them. You build something useful, it lives in `~/.claude/`, and nobody else benefits.

**The solution:** Plugins package skills and commands for distribution. Install from a marketplace, get working tools immediately. Learn patterns from real implementations, not documentation.

**The philosophy:** Good tools should spread. Reference implementations teach better than specs.

## Building Your Own

Install `artifact-foundations` and ask Claude about the patterns:

```
"I want to build a skill that does X"
→ Claude loads foundations, recommends archetype, guides implementation

"What makes a good skill description?"
→ Claude explains USE WHEN pattern, shows examples from foundations
```

Then use `artifact-builder` to generate and validate your work.

## License

[MIT](LICENSE)

---

<div align="center">

**Stop reinventing. Start building on patterns that work.**

</div>
