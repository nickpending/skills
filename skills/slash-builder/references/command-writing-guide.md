# Command Writing Guide

Reference for writing effective Claude Code slash commands.

## Template Structure

Commands follow this structure:

**Required Sections:**
- YAML frontmatter (allowed-tools, description)
- Command Name (H1) + overview
- Variables (if any used)
- Core Instructions
- Workflow/execution steps
- Success Criteria

**Optional Sections:**
- Output Format (if structured output needed)
- Error Handling (if complex scenarios)
- Notes (special considerations)

Templates show structure. Customize for your command's needs.

## Claude Code Capabilities

### @ Shortcuts

@ symbols reference files efficiently:

```markdown
# With injected variables (Momentum)
Read @ARTIFACTS_DIR/TASKS.md
Write @STATE_DIR/checkpoint.json

# Relative to current directory
Read @README.md
Edit @src/main.ts

# Absolute paths
Read @/Users/user/.config/app/settings.toml
```

**Usage in commands:**
- Use @ shortcuts directly in workflow steps
- Combine with injected path variables for portable commands
- Don't explain what @ does - just use it

### AskUserQuestion Tool

Structured user input with multiple choice:

```markdown
Use AskUserQuestion to confirm:
- Question: "Which framework?"
- Header: "Framework"
- Options:
  - React (description: Fast, component-based)
  - Vue (description: Progressive, flexible)
```

**When to use:**
- Command needs configuration choices
- Multiple valid approaches
- User preference required
- 1-4 questions per call

### Task Tool (Subagents)

Launch specialized agents:

```markdown
Use Task tool with:
- subagent_type: code-reviewer
- prompt: "Review recent changes for security issues"
- description: "Security review"

Read returned report and summarize findings.
```

**Available agents:**
- code-reviewer: Implementation quality, security
- architecture-analyst: Design approaches
- implementation-analyst: Technical approaches
- architecture-reviewer: Complexity audit

## Language Patterns

### Imperative Directives

**Strong commands:**
- MUST / REQUIRED / CRITICAL
- ALWAYS / NEVER
- READ / WRITE / EDIT
- VERIFY / VALIDATE / ENSURE

**Example:**
```markdown
REQUIRED: Read TASKS.md and extract incomplete tasks

VERIFY all tasks have:
- [ ] Status field
- [ ] Description
- [ ] Valid format
```

### Conditional Logic

**Clear branching:**
```markdown
IF file exists:
- Read and process
- Extract data

IF file missing:
- Report error
- Exit with guidance
```

### Phased Execution

**Numbered workflow:**
```markdown
1. **Preparation** - Load context, validate inputs
2. **Analysis** - Process data, identify patterns
3. **Execution** - Perform main action
4. **Output** - Write results
5. **Confirmation** - Report completion
```

## Variable Documentation

**List only variables actually used:**

```markdown
## Variables

### From Arguments
- TASK_NUM: $ARGUMENTS (task number to process)

### Injected
- ARTIFACTS_DIR: Location of TASKS.md
- PROJECT_ROOT: Project directory

### Runtime
- timestamp: Generated as YYYYMMDD-HHMM
```

**Don't include:**
- Variables not referenced in command
- Exhaustive lists of all possible injected vars
- Explanations of how injection works

## Token Efficiency

**Remove filler:**
- ❌ "In order to accomplish this"
- ✅ Direct imperative

**Use lists:**
- Bullets for requirements
- Numbers for sequential steps
- Checkboxes for criteria

**Reference, don't repeat:**
```markdown
## Constraints
- Validate input
- Check prerequisites
- Handle errors

## Step 2
Apply constraints from above
```

## Output Formatting

**Structured, scannable:**
```markdown
✅ Task Complete

File: path/to/output.md
Items: 5 processed
Status: Success

Next: Run /next-command
```

**Not:**
```markdown
The task has been completed successfully! I've processed
all 5 items and written them to the output file. Everything
worked as expected and you can now proceed to the next step...
```

## Success Criteria

**Testable checkboxes:**
```markdown
- [ ] Files read successfully
- [ ] Data validated
- [ ] Output written
- [ ] User notified
```

**Each criterion should be:**
- Verifiable (can confirm true/false)
- Specific (not vague)
- Outcome-focused (what's accomplished)

## Common Patterns

### Read-Process-Write

```markdown
1. **Load** - Read @ARTIFACTS_DIR/input.md
2. **Process** - Extract and transform data
3. **Write** - Save to @ARTIFACTS_DIR/output.md
4. **Confirm** - Report completion
```

### Conditional Execution

```markdown
Check if ARTIFACTS_DIR/STATE.md exists:

**If exists:**
- Read current state
- Continue from checkpoint

**If missing:**
- Start fresh workflow
- Create initial state
```

### Error Recovery

```markdown
**If validation fails:**
- Report specific issues
- Provide correction guidance
- Don't proceed to next step

**If file not found:**
- Check alternate locations
- Create if appropriate
- Report to user
```

## YAML Frontmatter Reference

All commands require frontmatter:

```yaml
---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: One-line description of command purpose
argument-hint: [optional-argument-name]
---
```

**Fields:**
- `allowed-tools`: List of tools command uses (comma-separated)
- `description`: Brief single-line summary
- `argument-hint`: (optional) Placeholder for command arguments

**Common tool combinations:**
- Read-only analysis: `Read, Glob, Grep`
- File manipulation: `Read, Write, Edit`
- Complex workflows: `Read, Write, Edit, Bash, Task`
- Interactive: `Read, Write, AskUserQuestion`

## Execution Patterns

### Bash Execution with `!`

For critical bash operations that must succeed:

```markdown
Run git status to verify clean state:
```bash
! git status
```

**When to use:**
- Commands that MUST succeed or halt
- Critical validation steps
- Commands where failure indicates serious issue
- Operations that following steps depend on

**Effect:**
- If command fails (non-zero exit), execution halts
- Error message displayed to user
- Prevents cascading failures

### CHECKPOINT Pattern (Complex Commands)

For multi-phase commands with validation gates:

```markdown
### PHASE 1: Preparation

**CHECKPOINT 1: Load Required Files**

READ:
- @ARTIFACTS_DIR/TASKS.md
- @PROJECT_ROOT/README.md

VERIFY: Files exist and structure valid

**CHECKPOINT 1.5: Validate Prerequisites**

Check all dependencies met before proceeding.
```

**Structure:**
- PHASE N: Major execution phase
- CHECKPOINT N: Validation gate within phase
- CHECKPOINT N.5: Optional intermediate checkpoint
- Each checkpoint verifies before proceeding

**When to use:**
- Complex multi-step workflows
- Operations with dependencies between phases
- Commands requiring explicit validation gates
- Processes where partial completion is risky

### Step Pattern (Simple Commands)

For linear sequential execution:

```markdown
### Step 1: Load Context

Read @ARTIFACTS_DIR/TASKS.md and extract data.

### Step 2: Process

Transform data according to requirements.

### Step 3: Output

Write results to @STATE_DIR/output.json.
```

**When to use:**
- Simple linear workflows
- Commands without complex validation needs
- Straightforward read-process-write patterns

## Template Usage

**Momentum commands:**
- **Simple:** Use `momentum-simple.md` for linear Step N pattern
- **Complex:** Use `momentum-complex.md` for PHASE/CHECKPOINT pattern
- Includes full injected variable set
- Workflow integration patterns

**Generic commands:**
- Use `generic.md`
- Framework-agnostic
- Minimal injected variables

**Customization:**
1. Copy template structure
2. Remove unused sections
3. Add command-specific logic
4. Demonstrate patterns in context (don't explain them)
5. Keep Variables section minimal (only what's used)

## Anti-Patterns

**Don't:**
- Explain Claude Code features in commands (use them, don't document them)
- Include educational sections (Claude Code Patterns, etc.)
- List all possible variables (only what's used)
- Over-explain simple steps
- Include sections that don't apply

**Do:**
- Use patterns directly in workflow
- Show by example
- Keep structure clean
- Focus on command logic
- Remove template sections not needed
