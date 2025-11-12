# Skill Types Reference

Understanding skill types helps determine structure, bundled resources, and whether to apply execution language patterns.

## Type Categories

### Workflow Skills

**Purpose:** Multi-step procedures that guide through complex processes

**Characteristics:**
- Sequential procedures with checkpoints
- User interaction and approval gates
- Decision trees and branching logic
- State management across steps

**SKILL.md structure:**
- Router pattern delegating to workflow files
- Execution requirements framing
- CAPS tool names (READ, WRITE, RUN, SHOW, ASK, WAIT)
- STOP points before major decisions

**Bundled resources:**
- `workflows/` - Step-by-step procedures with execution language
- `references/` - Supporting documentation and patterns
- Minimal assets (templates if needed)

**Execution language:** **REQUIRED** - Must follow execution patterns in `writing-fundamentals.md`

**Examples:**
- slash-builder (command creation workflows)
- skill-builder (this skill)
- Migration wizards
- Setup/configuration workflows

**Token efficiency target:**
- SKILL.md: <200 lines (router)
- Each workflow: 200-300 lines (400 max)

---

### Tool Integration Skills

**Purpose:** Handle specific file formats, APIs, or external tools

**Characteristics:**
- Script-heavy execution
- Deterministic operations
- Format conversion or manipulation
- API interaction patterns

**SKILL.md structure:**
- Clear instructions for when to use each script
- Input/output specifications
- Error handling guidance
- Imperative commands (not execution language)

**Bundled resources:**
- `scripts/` - **PRIMARY** - Python/Bash for deterministic operations
- `references/` - API docs, format specifications
- `assets/` - Sample files for testing

**Execution language:** Not required (imperative commands sufficient)

**Examples:**
- pdf-editor (rotate_pdf.py script)
- image-editor (image manipulation scripts)
- API client skills (REST/GraphQL wrappers)
- Format converters (JSON ↔ CSV ↔ XML)

**Key principle:** If same code is rewritten repeatedly, script it.

---

### Domain Knowledge Skills

**Purpose:** Provide specialized knowledge about schemas, systems, or business logic

**Characteristics:**
- Reference-heavy documentation
- Database schemas and relationships
- Business rules and policies
- Domain-specific terminology

**SKILL.md structure:**
- Overview of domain
- When to load which reference
- Search patterns for large references (grep hints)
- Context on relationships between docs

**Bundled resources:**
- `references/` - **PRIMARY** - Detailed domain docs
- Minimal scripts (maybe query helpers)
- No assets typically

**Execution language:** Not required (documentation-focused)

**Examples:**
- bigquery (table schemas and relationships)
- company-policies (HR/legal documentation)
- finance-schemas (accounting system documentation)
- API documentation skills

**Key principle:** Keep SKILL.md lean, load references on-demand.

---

### Template Skills

**Purpose:** Generate standard output using boilerplate and templates

**Characteristics:**
- Asset-heavy structure
- Copy/modify existing templates
- Standard project structures
- Brand/style consistency

**SKILL.md structure:**
- What templates are available
- When to use each template
- How to customize for user needs
- File structure explanations

**Bundled resources:**
- `assets/` - **PRIMARY** - Templates, boilerplate, sample files
- `references/` - Usage guides for complex templates
- Minimal scripts (maybe initialization helpers)

**Execution language:** Not required (template application)

**Examples:**
- frontend-webapp-builder (React/HTML boilerplate)
- brand-guidelines (logos, fonts, templates)
- document-templates (contracts, proposals)
- project-scaffolding (directory structures)

**Key principle:** Assets not loaded into context, used in output.

---

### Reference Skills

**Purpose:** Pure documentation and passive knowledge

**Characteristics:**
- No procedures or workflows
- Static information retrieval
- Policies, guidelines, standards
- Historical documentation

**SKILL.md structure:**
- What information is available
- How information is organized
- When to reference which sections
- Navigation hints for large docs

**Bundled resources:**
- `references/` - **ONLY** - Pure documentation
- No scripts
- No assets

**Execution language:** Not required (passive reference)

**Examples:**
- company-policies (HR/legal docs)
- style-guides (writing standards)
- mnda-templates (legal boilerplate)
- historical-docs (legacy system documentation)

**Key principle:** Load only what's needed, optimize for search.

---

## Type Selection Guide

**Ask these questions to determine type:**

1. **Does it guide through multi-step procedures with decisions?**
   → Workflow skill (needs execution language)

2. **Does it repeatedly execute same operations deterministically?**
   → Tool integration skill (script-heavy)

3. **Does it primarily provide schemas, rules, or domain knowledge?**
   → Domain knowledge skill (reference-heavy)

4. **Does it generate standard output from templates?**
   → Template skill (asset-heavy)

5. **Is it purely documentation without procedures?**
   → Reference skill (passive docs)

## Hybrid Skills

Some skills combine types:

**Workflow + Tool:**
- Workflow orchestrates script execution
- Scripts in `scripts/`, workflows in `workflows/`
- Example: data-pipeline-builder

**Workflow + Domain:**
- Workflow applies domain knowledge procedurally
- Domain docs in `references/`, workflows in `workflows/`
- Example: database-migration-planner

**Template + Domain:**
- Templates use domain-specific patterns
- Templates in `assets/`, schemas in `references/`
- Example: api-client-generator

**Principle:** Primary type determines structure, secondary adds resources.

---

## Momentum Integration

Any skill type can integrate with momentum workflow system.

**When momentum integration needed:**
- Skill operates on project artifacts (TASKS.md, ITERATION.md)
- Skill needs mode awareness (project/portfolio/assistant)
- Skill uses injected paths (ARTIFACTS_DIR, PROJECT_ROOT)
- Skill distributed via momentum installer

See `references/momentum-integration.md` for patterns.

---

## Summary Table

| Type | Primary Resources | Execution Language | SKILL.md Focus | Example |
|------|------------------|-------------------|----------------|---------|
| Workflow | workflows/ | **REQUIRED** | Router to workflows | slash-builder |
| Tool | scripts/ | No | Script usage | pdf-editor |
| Domain | references/ | No | When to load refs | bigquery |
| Template | assets/ | No | Template guide | frontend-webapp |
| Reference | references/ | No | Doc navigation | company-policies |

Choose type based on primary purpose, add secondary resources as needed.
