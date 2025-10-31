# Skills

<div align="center">

**Claude Code skills for workflow automation and network discovery**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

Two specialized skills: build slash commands interactively and map your home network infrastructure.

## Installation

```bash
# In Claude Code
/plugin marketplace add nickpending/skills
/plugin install voidwire-skills@voidwire-skills
```

## What's Inside

### slash-builder

Interactive builder for creating and updating Claude Code slash commands. Guides through discovery, planning, generation, and validation phases with built-in prompt engineering patterns.

**Triggers:** When you mention creating or updating slash commands

**Outputs:**
- Validated command files following Claude Code conventions
- Template-based generation (Momentum or generic patterns)
- Syntax validation and best practices

### homenet-discovery

Automated home network discovery via nmap, SSH, and DNS. Creates machine-readable inventory with topology diagrams for infrastructure documentation.

**Triggers:** When you mention network mapping, homelab discovery, or "what's on my network"

**Outputs:**
- Device inventory with services and metadata
- Network topology diagrams (Mermaid)
- AI-friendly markdown documentation

**Prerequisites:** nmap, python3, SSH keys (optional), DNS access (optional)

## Usage

Skills trigger automatically based on your requests. Both follow XDG directory structure and produce model-friendly output.

See individual skill directories for detailed workflows and implementation.
