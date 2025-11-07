# Momentum Integration Reference

When and how to integrate skills with the momentum workflow system.

## What is Momentum

Momentum is an iteration-first development workflow system using Claude Code with mode-based routing:
- **Project mode** - Active development on specific project
- **Assistant mode** - Navigation and project switching

Skills themselves are generic and work in any mode. However, some skill content may need mode awareness to function correctly (e.g., checking if in project mode before accessing project files).

Momentum skills integrate through path injection, optional mode awareness, and standardized structure.

## When Momentum Integration Needed

**Integrate with momentum when skill:**
- Operates on project artifacts (TASKS.md, ITERATION.md, PROJECT_SUMMARY.md)
- Needs mode awareness to function correctly
- Uses injected paths (ARTIFACTS_DIR, PROJECT_ROOT, EXPLORATIONS_DIR)
- Will be distributed via momentum installer

**Don't integrate when skill:**
- Works with any Claude Code setup
- Has no mode-specific behavior
- Doesn't need project context or paths
- Purely general-purpose capability

## Momentum Integration Choice

Ask user if they want momentum integration:

**Questions to ask:**
1. "Will this skill integrate with the momentum workflow system?"
2. If yes: "Where is your momentum project located?"

**User provides momentum path:**
- Create skill in `{momentum-path}/skills/{skill-name}/`
- Apply momentum-specific patterns (allowed-tools, paths, mode checks)
- Skill distributed via momentum installer

**User chooses general-purpose:**
- Create skill in user-specified location
- Skip momentum-specific elements
- User installs manually to `~/.claude/skills/`

## Required Elements

### 1. Frontmatter: allowed-tools

Declare which tools the skill uses:

```yaml
---
name: skill-name
description: What it does and when to use it
allowed-tools: Read, Write, Bash
---
```

**Common combinations:**
- `Read, Grep, Write` - Reading code, searching, documenting
- `Read, Glob, Write` - Finding files by pattern, creating files
- `Read, Write, Bash` - Reading, writing, running commands
- `Read, Write, Task` - Reading, writing, launching subagents

### 2. Available Paths Section

Document which injected paths the skill uses.

Momentum hook injects these as HTML comments:
```html
<!-- MODE: {mode} -->
<!-- PROJECT: {project-name} -->
<!-- PROJECT_ROOT: {path} -->
<!-- WORKFLOW_DIR: {path} -->
<!-- ARTIFACTS_DIR: {path} -->
<!-- PROJECT_OBSIDIAN_DIR: {path} -->
<!-- EXPLORATIONS_DIR: {path} -->
<!-- WORKFLOW_PROJECTS: {path} -->
<!-- WORKFLOW_DEV: {path} -->
```

**Include in SKILL.md after Overview:**

```markdown
## Available Paths

Momentum injects these paths for use:

- `PROJECT` - Current project name
- `PROJECT_ROOT` - Project directory
- `ARTIFACTS_DIR` - Workflow artifacts (TASKS.md, etc.)
- `EXPLORATIONS_DIR` - Project explorations directory
- `WORKFLOW_PROJECTS` - Global Obsidian projects directory

(Include only paths skill actually uses)
```

### 3. Mode Requirements (if mode-specific)

Determine which mode(s) skill requires:

**Project mode only:**
- Skill operates on current project's code/files
- Writes to project-specific directories
- Needs codebase context

**Any mode:**
- Operates on global resources
- Doesn't need project context
- Creates new projects (ideation)
- Works regardless of current mode

**If mode-specific, add Mode Requirement section:**

```markdown
## Mode Requirement

**This skill requires project mode.**

CHECK `<!-- MODE: {mode} -->` comment before proceeding.

**IF MODE is "project":**
- Proceed with skill execution

**IF MODE is "assistant":**
- INFORM user: "This skill requires project mode. Switch to a project first: 'work on [project]'"
- STOP execution
```

## Implementation Steps

### Step 1: Add Frontmatter

```yaml
---
name: your-skill
description: Your description
allowed-tools: Read, Write, Bash
---
```

### Step 2: Document Paths

After Overview section:

```markdown
## Available Paths

Momentum injects these paths:

- `ARTIFACTS_DIR` - Workflow artifacts directory
- `PROJECT_ROOT` - Project root directory

(Only include paths you'll use)
```

### Step 3: Add Mode Check (if needed)

If mode-specific, add requirement section with check logic.

### Step 4: Reference Paths Correctly

**In skill instructions, use path variable format:**

**Good:**
```markdown
READ `{ARTIFACTS_DIR}/TASKS.md`
WRITE to `{EXPLORATIONS_DIR}/analysis.md`
RUN `cd {PROJECT_ROOT} && pytest`
```

**Bad:**
```markdown
Read TASKS.md from artifacts directory
Write to explorations folder
Run tests in project directory
```

Use the exact variable names in curly braces.

## Common Patterns

### Reading Project Artifacts

```markdown
1. READ `{ARTIFACTS_DIR}/TASKS.md`
2. PARSE current task status
3. EXTRACT task details
```

### Writing Explorations

```markdown
1. GENERATE exploration content
2. CREATE filename: `{timestamp}-{topic}.md`
3. WRITE to `{EXPLORATIONS_DIR}/{filename}`
```

### Creating New Projects (Ideation)

```markdown
1. GENERATE IDEA.md from conversation
2. CREATE directory: `{WORKFLOW_PROJECTS}/{project-name}/`
3. WRITE IDEA.md to new directory
```

### Mode-Specific Operations

```markdown
1. CHECK `<!-- MODE: {mode} -->` comment
2. IF MODE is "project":
   - READ `{PROJECT_ROOT}` files
   - ANALYZE codebase
3. IF MODE is not "project":
   - INFORM user of requirement
   - STOP execution
```

## Example: Project-Only Skill

```markdown
---
name: code-metrics
description: Analyzes code metrics for current project
allowed-tools: Read, Grep, Write, Bash
---

# Code Metrics

## Overview

Generates code quality metrics and reports for the current project.

## Available Paths

- `PROJECT` - Current project name
- `PROJECT_ROOT` - Project directory
- `ARTIFACTS_DIR` - Workflow artifacts

## Mode Requirement

**This skill requires project mode.**

CHECK `<!-- MODE: {mode} -->` comment.

IF MODE is not "project":
  INFORM user: "Code metrics require project mode. Switch to project: 'work on [project]'"
  STOP execution

## Execution

1. CHECK mode requirement
2. SCAN `{PROJECT_ROOT}` for source files
3. ANALYZE patterns and complexity
4. GENERATE metrics report
5. WRITE to `{ARTIFACTS_DIR}/code-metrics.md`
```

## Example: Any-Mode Skill

```markdown
---
name: quick-capture
description: Captures notes and ideas to global capture file
allowed-tools: Read, Write
---

# Quick Capture

## Overview

Captures quick notes to global inbox for later processing.

## Available Paths

- `WORKFLOW_PROJECTS` - Global Obsidian projects directory

## Capture Process

1. ASK user for note content
2. GENERATE timestamp
3. APPEND to `{WORKFLOW_PROJECTS}/inbox.md`
4. CONFIRM saved
```

## Mode-Specific Behavior

### Project Mode

**Characteristics:**
- Current project context available
- PROJECT_ROOT, ARTIFACTS_DIR, EXPLORATIONS_DIR accessible
- Operates on specific codebase
- Most development skills use this mode

**Common operations:**
- Code analysis
- Task management
- Exploration generation
- Project-specific documentation

### Assistant Mode

**Characteristics:**
- No current project context
- Used for navigation and routing
- Global resources accessible
- Project switching happens here

**Common operations:**
- Project creation (ideation)
- Cross-project queries
- Global note capture
- Mode switching

## Testing Momentum Integration

**Before finalizing skill, verify:**

**Frontmatter:**
- [ ] `allowed-tools` declared correctly
- [ ] Tools listed match actual usage

**Paths:**
- [ ] Available Paths section included
- [ ] Only used paths documented
- [ ] Path references use `{VARIABLE}` format
- [ ] No hardcoded paths or "current directory" references

**Mode:**
- [ ] Mode requirement determined (project/any)
- [ ] Mode check implemented if required
- [ ] Error message clear and actionable
- [ ] Skill tested in correct mode(s)
- [ ] Skill tested in wrong mode (if mode-specific)

**Integration:**
- [ ] Skill works with momentum path injection
- [ ] No conflicts with momentum workflows
- [ ] Distribution plan clear (momentum installer vs standalone)

## Skill Creation Locations

**Momentum skills:**
- Created in: `{momentum-project-root}/skills/{skill-name}/`
- Distributed via: momentum installer
- Installed to: `~/.config/momentum/skills/{skill-name}/` (or equivalent momentum config location)
- Picked up by: momentum's skill loading system

**General skills:**
- Created in: User-specified location (typically `./skills/` or `~/.claude/skills/`)
- Distributed via: Manual copy or skill package
- Installed to: `~/.claude/skills/{skill-name}/`
- Picked up by: Claude Code's standard skill loading

## Distribution Flow

**For momentum skills:**
1. Create in momentum project: `{momentum-project-root}/skills/{skill-name}/`
2. Test during development in momentum environment
3. Momentum installer handles distribution to user's momentum config
4. Users get skill automatically with momentum

**For general skills:**
1. Create in desired location
2. Test locally
3. Package as zip (optional)
4. Users install by copying to `~/.claude/skills/`

## Summary

**For momentum integration:**
1. Add `allowed-tools` to frontmatter
2. Document Available Paths (only what you use)
3. Add Mode Requirement if mode-specific
4. Reference paths using `{VARIABLE}` format
5. Test in correct mode(s)

**For general skills:**
- Skip momentum-specific elements
- Install to `~/.claude/skills/`
- Work in any Claude Code setup
