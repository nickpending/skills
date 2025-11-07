# Skill Structure Reference

Anatomy of skills, progressive disclosure patterns, and structural best practices.

## Anatomy of a Skill

Every skill follows this structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required)
│   │   ├── name: skill-name (required)
│   │   └── description: when to use (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional, type-dependent)
    ├── workflows/      - Step-by-step procedures (workflow skills)
    ├── scripts/        - Executable code (tool skills)
    ├── references/     - Documentation (domain/reference skills)
    └── assets/         - Templates, files (template skills)
```

### SKILL.md (Required)

**Purpose:** Entry point that loads when skill triggers

**YAML Frontmatter:**
```yaml
---
name: skill-name
description: What the skill does and when to use it. Use third-person.
---
```

**Description quality matters:**
- Determines when skill triggers (semantic matching only)
- Format: What it does + "Use when" + natural scenarios
- Natural language scenarios (not literal trigger phrases)
- No implementation details (routing handles that internally)
- Specific enough to prevent false triggers
- General enough to catch relevant use cases

**Good descriptions:**
```yaml
description: Build and improve Claude Code skills through conversational discovery. Use when creating skills, improving skills, optimizing skills, understanding skill patterns, or refactoring skills.

description: Build, migrate, and optimize Claude Code slash commands. Use when creating new commands, migrating old formats, fixing validation issues, or improving command clarity and efficiency.

description: Discovers home network devices via nmap, SSH, and DNS. Creates machine-readable inventory with topology diagrams. Use when mapping networks, discovering devices, creating network inventory, updating inventory, refreshing network data, tracking infrastructure changes, or documenting infrastructure.
```

**Bad descriptions:**
```yaml
description: A skill for skills  # Too vague

description: Use when user says "create skill"  # Literal phrases, not natural scenarios

description: Build skills. Handles workflow, tool, domain, template, and reference types with momentum integration.  # Implementation details confuse matching
```

**Content structure** depends on skill type:
- **Workflow skills:** Router pattern with workflow checklist
- **Tool skills:** Script inventory and usage guide
- **Domain skills:** Reference map and search hints
- **Template skills:** Asset catalog and customization guide
- **Reference skills:** Documentation organization

**Target length:** <200 lines for routers, <250 lines for direct-execution skills

### Bundled Resources (Optional)

#### workflows/ Directory

**When to include:** Workflow skills requiring multi-step procedures

**Structure:**
```
workflows/
├── primary-workflow.md
├── secondary-workflow.md
└── specialized-case.md
```

**File naming:** Descriptive action verbs (new.md, improve.md, migrate.md)

**Content requirements:**
- Execution language (CAPS tools, STOP points, VERIFICATION)
- Numbered steps with REQUIRED ACTIONS
- IF/THEN branches with explicit logic
- Clear dependencies between steps

**Target length:** 200-300 lines per workflow (400 max)

See WORKFLOW-EXECUTION-SPEC.md for complete patterns.

#### scripts/ Directory

**When to include:** Tool skills with deterministic operations

**Structure:**
```
scripts/
├── primary_operation.py
├── helper_function.py
└── utility.sh
```

**When to script:**
- Same code rewritten repeatedly
- Deterministic reliability required
- Complex operations prone to errors
- Performance-critical operations

**Script design:**
- Clear, documented parameters
- Proper error handling and exit codes
- Can run standalone or via skill
- Include usage examples in docstring

**Note:** Scripts may still need reading by Claude for patching or environment adjustments.

#### references/ Directory

**When to include:** Documentation Claude should reference while working

**Structure:**
```
references/
├── core-concepts.md
├── api-documentation.md
└── examples.md
```

**Content types:**
- Database schemas and relationships
- API specifications and endpoints
- Business rules and policies
- Domain terminology and concepts
- Detailed how-to guides

**Organization:**
- One topic per file (easier to load selectively)
- Clear section headers for grep hints
- Examples integrated with explanations
- Cross-references between related docs

**Target length:** 200-300 lines per reference file

**Avoid duplication:** Information in either SKILL.md OR references, not both. Prefer references for detailed content.

**Search optimization:** If files >10k words, include grep patterns in SKILL.md:
```markdown
To find schema for users table:
grep "users table" references/database-schemas.md
```

#### assets/ Directory

**When to include:** Files used in output, not loaded into context

**Structure:**
```
assets/
├── templates/
│   ├── base-template.html
│   └── advanced-template.html
├── brand/
│   ├── logo.png
│   └── fonts/
└── boilerplate/
    └── project-structure/
```

**Content types:**
- Templates for document generation
- Brand assets (logos, fonts, colors)
- Boilerplate code and project structures
- Sample files for copy/modify operations

**Usage pattern:**
- Referenced by path in SKILL.md
- Copied or modified for output
- Never loaded into context window
- Can be binary files

---

## Progressive Disclosure Design

Skills use three-level loading to manage context efficiently:

### Level 1: Metadata (Always Loaded)

**What loads:** YAML frontmatter only (~100 words)

**When:** At Claude Code startup, every session

**Purpose:** Help Claude decide which skill to trigger

**Optimization:** Keep descriptions specific but concise

**Cost:** Minimal (loaded for all skills)

### Level 2: SKILL.md Body (Loaded on Trigger)

**What loads:** Full SKILL.md content (<5k words)

**When:** When skill description matches user intent

**Purpose:** Provide navigation map and core instructions

**Optimization:**
- Router pattern for workflow skills
- Direct execution for simple skills
- Reference maps for complex skills
- Keep under 200 lines for routers

**Cost:** Moderate (only triggered skills)

### Level 3: Bundled Resources (Loaded as Needed)

**What loads:** Individual workflow/reference/script files

**When:** When Claude determines specific resource needed

**Purpose:** Provide detailed instructions for specific operations

**Optimization:**
- Load only what's needed for current step
- Keep each file 200-300 lines
- Clear file names for selective loading
- Scripts can execute without loading

**Cost:** Variable (truly on-demand)

### Progressive Disclosure Benefits

**Context efficiency:**
- All skills: ~100 words metadata
- Triggered skill: +5k words for SKILL.md
- Active workflow: +1-2k words per workflow/reference
- Total: ~7k words vs loading everything upfront

**Performance:**
- Faster trigger evaluation (metadata only)
- Smaller context window footprint
- More room for actual codebase context
- Scripts execute without context cost

**Maintainability:**
- Easier to update specific workflows
- Clear separation of concerns
- Focused files easier to review
- Scalable to complex skills

---

## Best Practices

### Writing Style

**Voice:** Imperative/infinitive (verb-first instructions)

**Good:**
```markdown
To rotate a PDF, run the rotation script with target angle.

Check file exists before processing.

If error occurs, report and halt.
```

**Bad:**
```markdown
You should rotate the PDF by running...

Make sure you check that the file exists...

If there's an error you need to report it...
```

**Consistency:** Maintain objective, instructional language throughout.

### Information Architecture

**Principle:** Right information at right time

**SKILL.md should answer:**
- What does this skill do?
- When should it be used?
- How do I navigate to specific capabilities?

**SKILL.md should NOT contain:**
- Lengthy examples (→ references/)
- Complete API docs (→ references/)
- Detailed procedures (→ workflows/)
- Large code blocks (→ scripts/)

**References should contain:**
- Deep dives on specific topics
- Comprehensive examples
- Technical specifications
- Domain knowledge

### File Size Management

**Why size matters:**
- Context scanning efficiency drops beyond 400 lines
- Decision-making slows with large files
- Navigation becomes harder
- Token budget suffers

**Size targets:**
- SKILL.md router: <200 lines
- SKILL.md direct: <250 lines
- Workflows: 200-300 lines (400 max)
- References: 200-300 lines each
- No hard limit on scripts/assets

**When to split:**
- Workflow >400 lines → Extract phases to sub-workflows
- Reference >400 lines → Split by topic
- Multiple distinct capabilities → Separate workflow files
- Repeated patterns → Extract to reference

**Splitting example:**

**Before:** 500-line mega-workflow
```
workflows/
└── do-everything.md (500 lines)
```

**After:** Focused workflow + sub-workflows
```
workflows/
├── main.md (150 lines - routing)
├── phase-1-setup.md (200 lines)
├── phase-2-execution.md (250 lines)
└── phase-3-cleanup.md (150 lines)
```

### Resource Organization

**Directory structure communicates purpose:**

**Workflow-heavy skill:**
```
skill-name/
├── SKILL.md (router)
├── workflows/ (primary)
│   ├── workflow-a.md
│   └── workflow-b.md
└── references/ (supporting)
    └── patterns.md
```

**Tool-heavy skill:**
```
skill-name/
├── SKILL.md (script guide)
├── scripts/ (primary)
│   ├── tool.py
│   └── helper.py
└── references/ (API docs)
    └── api-spec.md
```

**Reference-heavy skill:**
```
skill-name/
├── SKILL.md (doc map)
└── references/ (primary)
    ├── schemas.md
    ├── policies.md
    └── examples.md
```

Structure reflects primary purpose at a glance.

### Maintenance Patterns

**Version naming:** Include in SKILL.md if versioning matters
```markdown
## Version

Current: 2.1.0
Last updated: 2025-01-15
```

**Changelog:** If skill frequently updated, maintain in SKILL.md or separate
```markdown
## Changelog

### 2.1.0 (2025-01-15)
- Added execution language to workflows
- Split mega-workflow into phases
- Updated momentum integration patterns
```

**Testing references:** Document how to test skill
```markdown
## Testing

Test new workflow:
1. Trigger with: "create a new command for X"
2. Verify skill loads workflows/new.md
3. Check STOP points honored
4. Confirm output matches template
```

**Deprecation:** Mark deprecated resources clearly
```markdown
## Deprecated

~~workflows/old-style.md~~ - Use workflows/new-style.md instead
Removed in: Version 3.0.0
```

---

## Common Patterns

### Router Pattern (Workflow Skills)

```markdown
## Workflow

- [ ] Step 1: Determine scenario
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow

## Execute ALL steps in sequence

### Step 1: Determine Scenario

ASK user about intent
RECORD response
DECIDE which workflow needed

### Step 2: Load Workflow

READ workflows/[scenario].md

### Step 3: Execute

FOLLOW workflow exactly as written
```

**Benefits:** Clean navigation, focused workflows, easy to extend

### Script Catalog Pattern (Tool Skills)

```markdown
## Available Operations

### Rotate PDF
```bash
python scripts/rotate_pdf.py input.pdf output.pdf --angle 90
```

### Merge PDFs
```bash
python scripts/merge_pdfs.py output.pdf input1.pdf input2.pdf
```

### Split PDF
```bash
python scripts/split_pdf.py input.pdf --pages 1-5 output.pdf
```

## Usage

Determine operation needed
Run appropriate script with parameters
Handle errors if script fails
```

**Benefits:** Clear operation inventory, direct usage, low overhead

### Reference Map Pattern (Domain Skills)

```markdown
## Available Documentation

- `references/schemas.md` - Database tables and relationships
- `references/api.md` - REST endpoints and parameters
- `references/examples.md` - Common query patterns

## Usage

Determine what information needed
READ appropriate reference file
Apply knowledge to user's task

## Search Hints

Find table schema: grep "table_name" references/schemas.md
Find endpoint: grep "POST" references/api.md
```

**Benefits:** Quick reference lookup, efficient loading, clear navigation

---

## Integration with WORKFLOW-EXECUTION-SPEC

Workflow skills must follow WORKFLOW-EXECUTION-SPEC patterns:

**Required elements:**
- Execution Requirements framing
- REQUIRED ACTIONS in numbered steps
- CAPS tool names (READ, WRITE, RUN, etc.)
- STOP points before major decisions
- VERIFICATION sections with success criteria
- IF/THEN/ELSE with explicit branches

**See:** ../WORKFLOW-EXECUTION-SPEC.md for complete patterns

Non-workflow skills use imperative commands but don't need full execution language.

---

## Summary Checklist

Before finalizing skill:

**Structure:**
- [ ] SKILL.md with valid YAML frontmatter
- [ ] Description specific and trigger-appropriate
- [ ] Bundled resources organized by type
- [ ] File sizes within targets
- [ ] Clear navigation in SKILL.md

**Content:**
- [ ] Imperative/infinitive writing style
- [ ] No duplication between SKILL.md and references
- [ ] Examples and details in appropriate files
- [ ] Search hints for large references
- [ ] Execution language if workflow skill

**Usability:**
- [ ] Clear what skill does and when to use
- [ ] Easy to find specific capabilities
- [ ] Resources load on-demand efficiently
- [ ] Test cases documented
- [ ] Maintenance patterns established

Well-structured skills are discoverable, efficient, and maintainable.
