# Skills

<div align="center">

**Production-ready Claude Code skills for building workflows, commands, and automation**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

Production skills for building Claude Code artifacts and automating network discovery.

## Installation

```bash
# In Claude Code
/plugin marketplace add nickpending/skills

# Install skills individually:
/plugin install artifact-builder@voidwire-skills
/plugin install homenet-discovery@voidwire-skills
```

## What's Inside

### artifact-builder

Unified builder for creating and improving Claude Code slash commands and skills through conversational workflows. Handles both artifact types with type-aware guidance.

**Triggers:** "create command", "build skill", "improve command", "migrate skill"

**Features:**
- Conversational building with template selection
- Artifact type detection (command vs skill)
- Action routing (new/improve/migrate)
- Type-aware skill guidance (workflow/tool/domain/template/reference)
- Template library (3 command + 5 skill templates)
- Built-in validation scripts
- Momentum integration (optional)

**Outputs:**
- Commands: Validated markdown files with template structure
- Skills: Complete directories with SKILL.md + bundled resources
- Follows execution language patterns and progressive disclosure

**Tools:**
- `scripts/validate_command.py` - Command syntax validation
- `scripts/validate_skill.py` - Skill structure validation
- `scripts/package_skill.py` - Zip packaging for distribution

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

## Development

### Project Structure

```
skills/
├── artifact-builder/         # Unified command and skill builder
│   ├── SKILL.md             # Router (107 lines)
│   ├── workflows/           # {command,skill}-{new,migrate,improve}.md
│   ├── references/          # Structure docs, patterns, tool selection
│   ├── templates/
│   │   ├── commands/        # momentum-simple, momentum-complex, generic
│   │   └── skills/          # workflow, tool, domain, template, reference
│   └── scripts/             # Validation and packaging tools
└── homenet-discovery/       # Network discovery
    ├── SKILL.md             # Router (129 lines)
    ├── workflows/           # discover.md (418 lines), update.md (298 lines)
    ├── references/          # setup-guides.md
    ├── scripts/             # Discovery and parsing scripts
    ├── parsers/             # proxmox, opnsense, unifi parsers
    └── templates/           # Output format templates
```

### Validation & Packaging

```bash
# Validate skill structure
python3 skills/artifact-builder/scripts/validate_skill.py <skill-dir>

# Package skill as distributable zip (outputs to /tmp)
python3 skills/artifact-builder/scripts/package_skill.py <skill-dir>

# Validate slash command
python3 skills/artifact-builder/scripts/validate_command.py <command.md>
```

### Key Patterns

- Router pattern: SKILL.md <200 lines, delegates to focused workflows
- Progressive disclosure: metadata → SKILL.md → workflows/references loaded on-demand
- Execution language: CAPS tool names, STOP points, VERIFICATION sections
- File size targets: workflows 200-400 lines, references 200-300 lines
- Template-based: 8 templates for consistent structure

## Usage

Skills trigger automatically based on natural language matching their descriptions. Artifact-builder uses conversational workflows to guide creation through discovery, planning, and implementation phases.

Each skill follows progressive disclosure patterns and produces model-friendly output with clear execution language.

## Contributing

Skills follow established patterns documented in references. Use artifact-builder to create new skills with consistent structure and quality.

## License

MIT
