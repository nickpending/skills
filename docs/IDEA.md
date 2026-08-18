---
type: project
domain: technical
status: active
started: 2025-10-30
---
# Skills - Core Idea

**Variables**: Variables in CAPS are injected by hooks (see HTML comments above), `{vars}` are runtime values (find/calculate them), `[vars]` are template placeholders (substitute them).

## The Problem

**What specific problem does this solve?**

Claude Code skills are valuable procedural knowledge packages, but they're isolated and difficult to share. Every skill created is trapped in one location - whether personal (`~/.claude/skills/`) or project-specific (`.claude/skills/`). There's no systematic way to package, distribute, and maintain a collection of reusable skills across projects and teams.

Additionally, creating skills and slash commands is inconsistent and context-heavy. Without templates and guided workflows, each new skill or command drifts in structure, quality, and adherence to patterns. This makes maintenance harder and reduces reliability.

**Who has this problem?**

- Developers using Claude Code who want to share their skills with teammates
- Teams that need consistent workflows across projects
- Anyone creating multiple skills or slash commands who wants to maintain quality and consistency
- Users who want to distribute skills publicly or across their own projects

**How do they solve it today?**

Currently, users manually copy skill directories between projects or maintain personal skills that aren't shared. For distribution, they might:
- Copy files manually between `.claude/skills/` directories
- Create git repositories for individual skills
- Package skills as plugins but without a central marketplace
- Recreate similar skills from scratch for each project

This is error-prone, leads to version drift, and makes it hard to maintain consistency across a portfolio of skills.

## The Solution

**Core Value Proposition**

A curated collection of production-ready Claude Code skills packaged as plugins, with tools to create new skills that follow consistent patterns and quality standards.

**Key Differentiators**

- **Plugin architecture** - Skills packaged for easy installation via Claude Code's plugin system
- **Quality templates** - Guided workflows for creating skills and slash commands with consistent structure
- **Proven patterns** - Each skill demonstrates best practices from real-world usage
- **Developer tools** - Skills to help build more skills (meta-tooling for skill creation)

## System Flow (Initial Sketch)

1. **Development** - Create skills following established patterns (using builder skills when applicable)
2. **Packaging** - Package skills into plugin format with proper structure and metadata
3. **Distribution** - Make plugins available via local marketplace or git repository
4. **Installation** - Users install plugins via `/plugin` commands
5. **Usage** - Skills activate automatically based on description matching, slash commands available via `/command-name`

## User Experience Vision

**Primary User Journey**

1. **Discover** - User finds the skills plugin marketplace
2. **Install** - User runs `/plugin marketplace add` and `/plugin install` for desired skills
3. **Use** - Skills activate automatically when user asks for relevant functionality

**Core User Workflows**

- **Installing existing skills** - Add marketplace, browse plugins, install what's needed
- **Creating new skills** - Use skill-builder to create consistent, well-structured skills
- **Creating slash commands** - Use command-builder to create momentum-compatible slash commands
- **Maintaining skills** - Update skills in dev marketplace, test, package, distribute

**Success Criteria**

- Skills install cleanly and work immediately after plugin installation
- New skills created with builder tools follow consistent patterns
- Skills are discoverable via clear descriptions and trigger phrases
- Skills demonstrate working functionality with real examples

## MVP Definition

**What is the absolute minimum viable version?**

A working plugin marketplace containing the homenet skill that can be installed and used immediately, plus the foundation for creating new skills with consistent structure.

**MVP Scope**

- **Plugin structure** - Working `.claude-plugin/` structure with marketplace.json
- **homenet skill** - Converted to plugin format, tested, documented
- **Installation workflow** - Local marketplace that can be added and installed from
- **Documentation** - README explaining how to install and use plugins

**MVP Constraints**

- Local marketplace only (no public hosting initially)
- Manual packaging process (can automate later)
- Small initial skill collection (expand after proving model)

**Post-MVP Evolution**

- Add slash command builder skill
- Add more domain-specific skills as needed
- Create automated packaging/validation tools
- Consider public marketplace distribution

## Features Status

**Status Legend:**

- 📋 **Planned** - Feature defined and ready for iteration planning
- 🔄 **In Progress** - Feature currently being developed
- ✅ **Built** - Feature completed and shipped

**Current Features:**

- ✅ **homenet skill** - Network discovery and documentation skill (converted to plugin)
- 📋 **slash command builder** - Guided workflow for creating consistent momentum slash commands
- 📋 **skill validator** - Automated validation of skill structure and patterns
- 📋 **plugin packager** - Automated packaging of skills into distributable plugins

## Technical Approach

**Architecture Decision**

- [x] **Composed Tool Ecosystem** - Multiple skills with clean interfaces

**Why this approach?**

Skills are inherently modular - each one is a self-contained capability. The plugin system supports this modularity by allowing skills to be independently installed, enabled, and disabled. This matches how users actually work: they want specific capabilities without being forced to adopt everything.

**Dependencies & Prerequisites**

- Claude Code with plugin system support
- Git for marketplace distribution (local or remote)
- File system access for plugin installation

**Integration Requirements**

- Claude Code plugin API (`.claude-plugin/plugin.json` format)
- Marketplace structure (`.claude-plugin/marketplace.json`)
- Skills follow standard SKILL.md frontmatter format

**Data Requirements**

- Plugin metadata (name, description, version, author)
- Skill metadata (name, description, trigger phrases)
- Marketplace catalog (list of available plugins)

**Key Technical Constraints**

- Must follow Claude Code plugin conventions
- Skills must be discoverable via description matching
- Plugin structure must support both local and git-based distribution

## Technical Architecture (Tentative)

**Data Design (Draft)**

```
skills-marketplace/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog
├── homenet/                       # Individual plugins
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       └── homenet/
│           └── SKILL.md
├── command-builder/
│   └── skills/
│       └── command-builder/
│           └── SKILL.md
└── README.md
```

**Component Architecture (Working Model)**

Each plugin contains:
- Metadata (`.claude-plugin/plugin.json`)
- Skills (`skills/skill-name/SKILL.md`)
- Optional resources (scripts, references, assets within skill directories)

**Integration Points (Planned)**

- Claude Code plugin system via `/plugin` commands
- Git repositories for marketplace hosting
- Local file system for development marketplace

**Tool/Technology Stack (Current Thinking)**

- Markdown for skill documentation (SKILL.md)
- JSON for plugin/marketplace metadata
- Python scripts for validation/packaging (if needed)
- Git for version control and distribution

## Implementation Strategy (Subject to Change)

**Iteration Priorities (Draft)**

1. **Validate plugin structure** - Ensure homenet skill works as plugin
2. **Create marketplace** - Set up local marketplace structure
3. **Build command-builder skill** - Second skill to validate pattern
4. **Add validation tools** - Automated checks for skill quality
5. **Documentation** - Usage guides and skill creation guidelines

**Deployment/Operations (Initial Thoughts)**

- Development marketplace: local directory for testing
- Distribution: git repository users can add via `/plugin marketplace add`
- Updates: users pull latest from git, reinstall plugins

**Data Flow (Conceptual)**

1. User adds marketplace → Claude Code discovers available plugins
2. User installs plugin → Files copied to plugin directory
3. User triggers skill via natural language → Description matching activates skill
4. Skill executes → SKILL.md loaded, instructions followed

## Learning and Evolution

**Key Learnings**

- homenet conversion to plugin proved the structure works
- Skills need clear, specific descriptions with trigger phrases to activate properly
- Progressive disclosure (metadata → SKILL.md → resources) keeps context efficient

**Evolution Notes**

- Started as "how do I share the homenet skill" conversation
- Evolved into "skills as plugins" distribution model
- Recognized need for builder skills to maintain consistency

## Open Questions

**User/Market Questions**

- Should this be a public marketplace or personal collection?
- What other skills would provide immediate value?
- How to balance general skills vs momentum-specific skills?

**Technical Questions**

- Should validation be automated or manual?
- How to handle skill versioning and updates?
- What's the best packaging workflow?

**Operational Questions**

- Where should the marketplace be hosted (local, GitHub, other)?
- How to maintain consistency across skill updates?
- What's the contribution/review process for new skills?

## Success Metrics

**Primary Metrics**

- Skills install cleanly without errors
- Skills activate when expected based on descriptions
- New skills can be created following established patterns

**Learning Metrics**

- User feedback on skill quality and usefulness
- Issues encountered during installation/usage
- Common patterns that emerge across multiple skills

## Risks and Assumptions

**Key Assumptions**

- Plugin system is stable and will remain Claude Code's distribution method
- Description-based skill discovery works reliably
- Users prefer modular skills over monolithic collections

**Primary Risks**

- Plugin API changes could break existing skills
- Description matching might not reliably trigger skills
- Marketplace structure might not scale to many plugins

**Mitigation Strategies**

- Follow Claude Code plugin conventions exactly
- Test skills with various trigger phrases
- Keep marketplace structure simple and flexible
- Version plugins to allow rollback if needed

---

## Current Status

**Built:**
- homenet skill converted to plugin format in `~/development/projects/skills/homenet`

**Next:**
- Create proper marketplace structure
- Build slash command builder skill
- Document installation and usage workflow
