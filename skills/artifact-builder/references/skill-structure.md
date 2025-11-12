# Skill Structure

Skill-specific structure and organizational patterns. See `skill-types.md` for type selection, `writing-fundamentals.md` for writing patterns.

## Anatomy

Directory with SKILL.md + optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional, type-dependent)
    ├── workflows/      - Step-by-step procedures (workflow skills)
    ├── scripts/        - Executable code (tool skills)
    ├── references/     - Documentation (domain/reference skills)
    └── assets/         - Templates, files (template skills)
```

## YAML Requirements

```yaml
---
name: skill-name
description: What the skill does and when to use it. Use third-person.
---
```

**Description format:**
- What it does + "Use when" + natural scenarios
- Natural language (not literal trigger phrases)
- No implementation details
- Specific enough to prevent false triggers
- General enough to catch relevant use cases

**Examples:**
```yaml
# Good
description: Build and improve skills through conversational discovery. Use when creating skills, improving skills, optimizing skills, understanding skill patterns, or refactoring skills.

# Bad
description: A skill for skills  # Too vague
description: Use when user says "create skill"  # Literal phrases
```

## Content Requirements

Depends on skill type (see `skill-types.md`):
- **Workflow:** Router pattern with workflow checklist
- **Tool:** Script inventory and usage guide
- **Domain:** Reference map and search hints
- **Template:** Asset catalog and customization guide
- **Reference:** Documentation organization

**Target length:** <200 lines routers, <250 lines direct-execution

## Bundled Resources

### Directory Organization

Structure communicates purpose:

**Workflow-heavy:**
```
skill-name/
├── SKILL.md (router)
├── workflows/ (primary)
└── references/ (supporting)
```

**Tool-heavy:**
```
skill-name/
├── SKILL.md (script guide)
├── scripts/ (primary)
└── references/ (API docs)
```

**Reference-heavy:**
```
skill-name/
├── SKILL.md (doc map)
└── references/ (primary)
```

See `skill-types.md` for per-type bundled resource guidance.

### File Naming

- Descriptive action verbs (new.md, improve.md, migrate.md)
- One level deep from SKILL.md (flat structure required)
- Clear navigation paths

### Search Optimization

For large references (>10k words), provide grep hints in SKILL.md:

```markdown
To find users table schema:
grep "users table" references/database-schemas.md
```

## Progressive Disclosure

Three-level loading manages context efficiently:

**Level 1: Metadata (Always Loaded)**
- YAML frontmatter only (~100 words)
- Loaded at startup for all skills
- Determines skill triggering

**Level 2: SKILL.md Body (Loaded on Trigger)**
- Full SKILL.md content (<5k words)
- Navigation map and core instructions
- Router pattern for workflow skills
- Loaded only when skill matches

**Level 3: Bundled Resources (Loaded as Needed)**
- Individual workflow/reference/script files
- Loaded when specific resource needed
- 200-300 lines per file
- Scripts can execute without loading

**Benefits:**
- Context efficiency: ~7k words vs loading everything upfront
- Faster trigger evaluation
- More room for codebase context
- Scripts execute without context cost

## File Size Management

**Target lengths:**
- SKILL.md router: <200 lines
- SKILL.md direct: <250 lines
- Workflows: 200-300 lines (400 max)
- References: 200-300 lines each
- Scripts/assets: No hard limit

**Why:**
- Context scanning efficiency drops beyond 400 lines
- Decision-making slows with large files
- Navigation becomes harder

**When to split:**
- Workflow >400 lines → Extract phases to sub-workflows
- Reference >400 lines → Split by topic
- Multiple capabilities → Separate workflow files
- Repeated patterns → Extract to reference

**Example split:**

Before (500 lines):
```
workflows/
└── do-everything.md
```

After (focused):
```
workflows/
├── main.md (150 lines - routing)
├── phase-1-setup.md (200 lines)
├── phase-2-execution.md (250 lines)
└── phase-3-cleanup.md (150 lines)
```

## Information Architecture

**Principle:** Right information at right time

**SKILL.md answers:**
- What does this skill do?
- When should it be used?
- How to navigate to specific capabilities?

**SKILL.md does NOT contain:**
- Lengthy examples (→ references/)
- Complete API docs (→ references/)
- Detailed procedures (→ workflows/)
- Large code blocks (→ scripts/)

**References contain:**
- Deep dives on topics
- Comprehensive examples
- Technical specifications
- Domain knowledge

**Avoid duplication:** Information in SKILL.md OR references, not both. Prefer references for detailed content.

## Common Patterns

### Router Pattern (Workflow Skills)

```markdown
## Workflow

- [ ] Determine scenario
- [ ] Load appropriate workflow
- [ ] Execute workflow

## Execute ALL steps in sequence

### Step 1: Determine Scenario

ASK user about intent
DECIDE which workflow needed

### Step 2: Load Workflow

READ workflows/[scenario].md

### Step 3: Execute

FOLLOW workflow exactly as written
```

Clean navigation, focused workflows, easy to extend.

### Script Catalog Pattern (Tool Skills)

```markdown
## Available Operations

### Operation Name
```bash
python scripts/operation.py input.ext output.ext --flag
```

## Usage

Determine operation needed
RUN appropriate script with parameters
HANDLE errors if script fails
```

Clear inventory, direct usage, low overhead.

### Reference Map Pattern (Domain Skills)

```markdown
## Available Documentation

- `references/topic-a.md` - Description
- `references/topic-b.md` - Description

## Usage

Determine what information needed
READ appropriate reference file
APPLY knowledge to user's task

## Search Hints

Find X: grep "pattern" references/file.md
```

Quick lookup, efficient loading, clear navigation.

## Summary Checklist

**Structure:**
- [ ] SKILL.md with valid YAML frontmatter
- [ ] Description specific and trigger-appropriate
- [ ] Bundled resources organized by type
- [ ] File sizes within targets
- [ ] Clear navigation in SKILL.md

**Content:**
- [ ] Follows writing patterns (see `writing-fundamentals.md`)
- [ ] Execution language if workflow skill (see `writing-fundamentals.md`)
- [ ] No duplication between SKILL.md and references
- [ ] Examples and details in appropriate files
- [ ] Search hints for large references

**Usability:**
- [ ] Clear what skill does and when to use
- [ ] Easy to find specific capabilities
- [ ] Resources load on-demand efficiently
- [ ] Test cases documented
- [ ] Maintenance patterns established

Well-structured skills are discoverable, efficient, and maintainable.

## Templates

- `templates/skills/workflow-skill.md` - Router pattern with workflows
- `templates/skills/tool-skill.md` - Script catalog pattern
- `templates/skills/domain-skill.md` - Reference map pattern
- `templates/skills/template-skill.md` - Asset catalog pattern
- `templates/skills/reference-skill.md` - Documentation organization

Copy structure, customize placeholders, remove unused sections.
