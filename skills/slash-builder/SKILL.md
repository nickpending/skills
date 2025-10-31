---
name: slash-builder
description: Interactive builder for creating and updating Claude Code slash commands. Use when user wants to create a new slash command, update an existing command structure, or improve command organization - guides through discovery, planning, generation, and validation phases.
---

# Slash Builder

Build and update well-structured Claude Code slash commands through phased discovery, planning, generation, and validation.

## When to Use This Skill

Use this skill when:
- User wants to create a new slash command
- User wants to update an existing slash command structure
- User wants to improve or refactor a command
- User needs guidance on command structure and best practices
- User mentions "create a command", "build a slash command", "update this command", "improve command structure"

## Overview

This skill guides you through building and updating slash commands using structured, interactive workflows:

**For Creating New Commands:**
1. **Discovery** - Understand what the user wants to build
2. **Planning** - Determine framework, structure, and sections needed
3. **Generation** - Create the command file using appropriate template
4. **Validation** - Check structure and offer validation

**For Updating Existing Commands:**
1. **Analyze** - Read existing command and identify gaps
2. **Compare** - Load appropriate template and compare structure
3. **Plan** - Identify improvements using validation script
4. **Apply** - Update command structure while preserving logic
5. **Validate** - Verify improved structure

## Phase 1: Discovery

**Goal:** Understand what command the user wants to create.

**REQUIRED: Use AskUserQuestion to gather:**

1. **Command purpose** (header: "Purpose")
   - What should this command do?
   - When would someone use it?
   - What's the expected outcome?

2. **Command type** (header: "Type")
   - Options:
     - Workflow command (step-by-step process)
     - Analysis command (reads and reports)
     - Generation command (creates files/output)
     - Management command (updates state/config)

3. **Framework context** (header: "Framework")
   - Options:
     - Momentum workflow system
     - Generic Claude Code project
     - Other framework

**After discovery, confirm understanding:**
```
Command: [name]
Purpose: [1-2 sentences]
Type: [workflow/analysis/generation/management]
Framework: [momentum/generic/other]
```

## Phase 2: Planning

**Goal:** Determine command structure and required sections.

**Plan command structure:**

### Template Selection
- **Momentum:** Use `references/momentum-template.md`
- **Generic:** Use `references/generic-template.md`

### Core Sections (Always Include)
- YAML frontmatter (allowed-tools, description, argument-hint)
- Command Name + overview
- Variables (Arguments/Injected/Runtime)
- Core Instructions
- Workflow steps
- Success Criteria

### Optional Sections (Based on Need)
- Claude Code Patterns (if command uses @shortcuts, AskUserQuestion, or Task tool)
- Output Format (if structured output needed)
- Error Handling (if complex error scenarios)
- Notes (if special considerations exist)

**Use AskUserQuestion to clarify:**

1. **Tools needed** (header: "Tools", multiSelect: true)
   - Options:
     - Read/Write/Edit files
     - Glob/Grep search
     - Bash commands
     - Task (subagents)
     - AskUserQuestion

2. **Arguments** (header: "Arguments")
   - Does command take arguments?
   - Required or optional?

3. **Output type** (header: "Output")
   - Options:
     - File output (creates/updates files)
     - Report output (displays information)
     - State change (modifies system state)
     - Mixed output

**Document plan:**
```
Template: [momentum/generic]
Tools: [list]
Arguments: [yes/no - description]
Output: [type]
Special sections: [list if any]
```

## Phase 3: Generation

**Goal:** Create the command file.

### Step 1: Load Template

Read the appropriate template:
- Momentum: `references/momentum-template.md`
- Generic: `references/generic-template.md`

### Step 2: Customize Sections

**YAML Frontmatter:**
```yaml
---
allowed-tools: [list from planning]
description: [one-line from discovery]
argument-hint: [if args needed]
---
```

**Variables Section:**
- List only variables ACTUALLY USED in the command
- Include argument variable if command takes arguments
- Include injected variables if momentum framework
- Document any runtime-calculated variables

**Core Instructions:**
- Convert discovery "what it does" into bullet points
- Focus on requirements, constraints, behavior

**Workflow:**
- Break command execution into clear phases
- Use numbered list with phase names
- Keep steps high-level (not pseudocode)

**Success Criteria:**
- Convert requirements into checkboxes
- Each criterion should be verifiable
- Focus on deliverables and outcomes

**Optional Sections:**
- Only include if needed based on planning
- Remove sections that don't apply
- Keep Claude Code Patterns if using @shortcuts, AskUserQuestion, or Task tool

**CRITICAL: Apply prompt patterns from `references/prompt-patterns.md` when writing command text.**

### Step 3: Write Command File

**Use AskUserQuestion to get filename:**
- Question: "What should the command file be named?"
- Header: "Filename"
- Provide suggestion based on command name
- Reminder: filename should be lowercase-with-dashes.md

**Write the complete command file to user's desired location.**

## Phase 4: Validation

**Goal:** Verify command structure and offer validation.

### Structure Check

Verify command file has:
- [ ] Valid YAML frontmatter
- [ ] Command name as H1
- [ ] Brief overview (2-3 sentences)
- [ ] Variables section (if needed)
- [ ] Core Instructions
- [ ] Workflow or execution steps
- [ ] Success Criteria
- [ ] Appropriate optional sections

### Offer Validation Script

```bash
# Validate command structure
python3 scripts/validate_command.py [command-file.md]
```

**Report results:**
```
✅ Slash Command Created

File: [path]
Framework: [momentum/generic]
Type: [workflow/analysis/generation/management]
Tools: [list]

Structure:
✓ YAML frontmatter valid
✓ All required sections present
✓ Variables properly documented
✓ Success criteria defined

Next Steps:
1. Test command: /[command-name]
2. Iterate based on testing
3. Add to project .claude/commands/ when ready
```

## Updating Existing Commands

**Goal:** Improve existing command structure using templates as reference.

### Step 1: Read and Analyze Existing Command

**Read the existing command file and assess:**
- Does it have valid YAML frontmatter?
- Which sections are present vs missing?
- Is the Variables section properly structured?
- Are Success Criteria defined with checkboxes?

### Step 2: Identify Framework and Load Template

**Determine framework:**
- Check for momentum-specific injected variables (PROJECT_ROOT, WORKFLOW_DIR, etc.)
- If present: momentum framework → use `references/momentum-template.md`
- If absent: generic framework → use `references/generic-template.md`

**Load the appropriate template for reference.**

### Step 3: Compare and Plan Updates

**Use validation script to identify issues:**
```bash
python3 scripts/validate_command.py [existing-command.md]
```

**Compare existing command to template:**
- Missing required sections?
- Variables section needs restructuring?
- Success Criteria need checkboxes?
- Optional sections would improve clarity?

**Use AskUserQuestion to confirm changes:**
- Question: "What improvements should be made?"
- Options based on gaps found:
  - Add missing sections
  - Restructure Variables section
  - Add Success Criteria checkboxes
  - Improve YAML frontmatter
  - Add optional sections (Claude Code Patterns, Error Handling, Notes)

### Step 4: Apply Updates

**Update the command file using Edit tool:**
- Add missing sections from template
- Restructure existing sections to match template format
- Preserve existing command logic and content
- Only change structure and organization

**Maintain:**
- Existing command name and purpose
- Core workflow steps (adapt format if needed)
- Existing business logic

### Step 5: Validate Updates

**Run validation script again:**
```bash
python3 scripts/validate_command.py [updated-command.md]
```

**Report results:**
```
✅ Slash Command Updated

File: [path]
Framework: [momentum/generic]
Changes Applied:
• [list changes made]

Validation:
✓ All required sections present
✓ YAML frontmatter valid
✓ Variables properly structured
✓ Success criteria defined

Next: Test updated command
```

## Command Structure Reference

### YAML Frontmatter
```yaml
---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: One-line description of what this command does
argument-hint: [optional-argument]
---
```

### Variable Taxonomy

**From Arguments:**
- `$ARGUMENTS` - What user passed to command

**Injected (Momentum only):**
- Provided by hooks as HTML comments
- PROJECT_ROOT, WORKFLOW_DIR, ARTIFACTS_DIR, STATE_DIR, etc.
- Only list variables actually used

**Runtime:**
- Calculated during command execution
- timestamps, computed paths, extracted values

### Claude Code Patterns

**@ Shortcuts:**
- `@ARTIFACTS_DIR/file.md` - Uses injected path variable
- `@README.md` - Relative to cwd
- `@/abs/path/file.md` - Absolute path

**AskUserQuestion:**
- Structured user input with multiple choice
- 1-4 questions per call
- Headers, options with descriptions

**Task Tool:**
- Launch specialized subagents
- code-reviewer, architecture-analyst, etc.

## Templates

This skill includes two command templates:

### momentum-template.md
For Momentum workflow system commands. Includes:
- Full set of Momentum injected variables
- Momentum-specific patterns
- Workflow integration guidance

### generic-template.md
For framework-agnostic commands. Includes:
- Basic injected variable structure
- Generic Claude Code patterns
- Simplified variable section

## Validation Script

The `scripts/validate_command.py` script checks:
- YAML frontmatter syntax
- Required section presence
- Variable documentation
- Success criteria format

Run validation:
```bash
python3 scripts/validate_command.py path/to/command.md
```

## Tips for Good Commands

**Be directive, not descriptive:**
- ✓ "Read TASKS.md and extract incomplete tasks"
- ✗ "This command reads TASKS.md to extract incomplete tasks"

**Use bullets for instructions:**
- Clear, scannable requirements
- One requirement per bullet
- Action-oriented language

**Success criteria are testable:**
- Each checkbox is verifiable
- Focus on deliverables
- Include what "done" looks like

**Only include relevant sections:**
- Remove sections that don't apply
- Don't include examples unless helpful
- Keep output concise

**Variable documentation matters:**
- List only variables actually used
- Explain where each comes from
- Show example values if helpful

## Resources

### references/
- `prompt-patterns.md` - Language patterns and token efficiency techniques
- `momentum-template.md` - Complete template with momentum-specific variables
- `generic-template.md` - Framework-agnostic template

### scripts/
- `validate_command.py` - Structure validation script
