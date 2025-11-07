# Skills

<div align="center">

**Production-ready Claude Code skills for building workflows, commands, and automation**

[GitHub](https://github.com/nickpending/skills) | [Issues](https://github.com/nickpending/skills/issues)

[![Status](https://img.shields.io/badge/Status-Active-green?style=flat)](#)
[![Built for](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet?style=flat)](https://claude.ai/download)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

Three specialized skills for building and automating Claude Code workflows: create skills, build slash commands, and discover network infrastructure.

## Installation

```bash
# In Claude Code
/plugin marketplace add nickpending/skills

# Install skills individually:
/plugin install slash-builder@voidwire-skills
/plugin install skill-builder@voidwire-skills
/plugin install homenet-discovery@voidwire-skills
```

## What's Inside

### slash-builder

Interactive builder for creating and optimizing Claude Code slash commands. Guides through conversational workflows for building new commands, migrating old formats to current standards, and improving existing commands.

**Triggers:** "create slash command", "migrate command", "improve command"

**Features:**
- Conversational command building with template selection
- Migration from old formats with conflict resolution
- Token efficiency optimization and clarity improvements
- Built-in validation via `validate_command.py`
- Momentum workflow and generic command support

**Outputs:**
- Validated command markdown files
- Template-based structure (Momentum or generic)
- Syntax validation and execution language patterns

### skill-builder

Type-aware skill creation and improvement through conversational discovery. Handles five skill types (workflow, tool, domain, template, reference) with specialized guidance for each.

**Triggers:** "create skill", "build skill", "improve skill"

**Features:**
- Conversational skill building from examples
- Type detection (workflow/tool/domain/template/reference)
- Type-specific resource planning and structure
- Momentum integration with mode awareness (optional)
- Built-in validation and packaging scripts

**Outputs:**
- Complete skill directories with SKILL.md
- Type-appropriate bundled resources (workflows, scripts, references, assets)
- Validated structure following WORKFLOW-EXECUTION-SPEC
- Packaged zip files ready for distribution

**Tools:**
- `scripts/validate_skill.py` - Structure and frontmatter validation
- `scripts/package_skill.py` - Zip packaging with validation

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
├── slash-builder/         # Slash command builder
│   ├── SKILL.md          # Router (94 lines)
│   ├── workflows/        # new.md, migrate.md, improve.md
│   ├── references/       # Templates and patterns
│   └── scripts/          # validate_command.py
├── skill-builder/        # Skill creation and improvement
│   ├── SKILL.md          # Router (102 lines)
│   ├── workflows/        # new.md (432 lines), improve.md (401 lines)
│   ├── references/       # skill-types.md, skill-structure.md, momentum-integration.md
│   └── scripts/          # validate_skill.py, package_skill.py
└── homenet-discovery/    # Network discovery
    ├── SKILL.md          # Router (129 lines)
    ├── workflows/        # discover.md (418 lines), update.md (298 lines)
    ├── references/       # setup-guides.md
    ├── scripts/          # discovery and parsing scripts
    ├── parsers/          # proxmox, opnsense, unifi parsers
    └── templates/        # output format templates
```

### Validation & Packaging

```bash
# Validate skill structure
python3 skills/skill-builder/scripts/validate_skill.py <skill-dir>

# Package skill as distributable zip (outputs to /tmp)
python3 skills/skill-builder/scripts/package_skill.py <skill-dir>

# Validate slash command
python3 skills/slash-builder/scripts/validate_command.py <command.md>
```

### Key Specifications

- **WORKFLOW-EXECUTION-SPEC.md** - Execution language patterns for workflows
- Router pattern: SKILL.md <200 lines, delegates to focused workflows
- Progressive disclosure: metadata → SKILL.md → workflows/references loaded on-demand
- File size targets: workflows 200-400 lines, references 200-300 lines

## Usage

Skills trigger automatically based on natural language requests matching their descriptions. Both builder skills use conversational workflows to guide creation through discovery, planning, and implementation phases.

Each skill follows XDG directory structure and produces model-friendly output following execution language patterns.

## Contributing

Skills follow established patterns documented in WORKFLOW-EXECUTION-SPEC.md. Use skill-builder to create new skills with consistent structure and quality.

## License

MIT
