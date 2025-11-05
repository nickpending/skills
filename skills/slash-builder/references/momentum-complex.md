---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: One-line description of what this command does
argument-hint: [optional-argument]
---

# Command Name

Brief 2-3 sentence overview of command purpose, when to use it, and expected outcomes.

**Variables**: CAPS are injected by hooks (see HTML comments above), `{vars}` are runtime values (find/calculate them), `[vars]` are template placeholders (substitute them).

## ⚠️ CRITICAL: [KEY COMMAND PRINCIPLE]

**REQUIRED:**
- Primary must-do behavior
- Critical constraint that cannot be violated
- Quality gate that must pass

**NEVER:**
- Action that should never happen
- Pattern to avoid
- Anti-pattern to watch for

## Variables

### From Arguments
- TASK_NUMBER: $ARGUMENTS (task number to process)

### Injected (from hooks - see HTML comments)
- PROJECT_ROOT: Project root directory
- ARTIFACTS_DIR: .workflow/artifacts/ (TASKS.md, ITERATION.md, etc.)
- STATE_DIR: .workflow/state/ (saved state files)
- WORKFLOW_PROJECTS: Obsidian projects directory
- PROJECT_OBSIDIAN_DIR: Current project's obsidian directory
- [Only list variables actually used in this command]

### Runtime (calculated during execution)
- timestamp: Generated as YYYYMMDD-HHMM (e.g., 20251029-1745)
- current_task: Task object extracted from TASKS.md
- [any other vars computed by command]

## Workflow

Tight summary of execution phases:

1. **Preparation** - Load context, validate prerequisites
2. **Analysis** - Process requirements, identify patterns
3. **Execution** - Perform main operations with validation
4. **Output** - Generate results and reports
5. **Confirmation** - Verify completion and report status

## Core Instructions

### PHASE 1: Context Loading

**CHECKPOINT 1: Load Required Files**

```
READ:
- @ARTIFACTS_DIR/TASKS.md
- @PROJECT_OBSIDIAN_DIR/context.md

VERIFY: Files exist and structure is valid
```

**CHECKPOINT 1.5: Validate Prerequisites**

Extract required information and confirm completeness.

Verify all dependencies are met before proceeding.

### PHASE 2: Data Processing

**CHECKPOINT 2: Transform Data**

```
REQUIRED:
- Apply business logic to extracted data
- Handle edge cases explicitly
- Validate intermediate results

VERIFY: Data ready for execution phase
```

### PHASE 3: Execution

**CHECKPOINT 3: Perform Main Operation**

Execute primary command logic.

Track state changes in @STATE_DIR/checkpoint.json if needed.

**CHECKPOINT 3.5: Validation Gate**

```
VERIFY:
- [ ] Operation completed successfully
- [ ] No errors encountered
- [ ] Output meets requirements

IF validation fails: Report issues and halt
```

### PHASE 4: Output Generation

**CHECKPOINT 4: Generate Results**

Write results to @ARTIFACTS_DIR/output.md.

Format according to Output Format section below.

### PHASE 5: Confirmation

**CHECKPOINT 5: Report Completion**

Display completion status with key details and next steps.

## Output Format

Structured, concise output:

```
=====================================
[OPERATION] COMPLETE ✅
=====================================

[Key Information]
File: path/to/output.md
Status: Success
Items: 5 processed
Duration: 2.3s

Key Points:
- Point 1
- Point 2
- Point 3

Next: [What user should do next]
```

## Success Criteria

Command succeeds when:

- [ ] All checkpoints passed successfully
- [ ] Required files read and validated
- [ ] Data processed according to requirements
- [ ] Output files written correctly
- [ ] Quality gates passed
- [ ] User notified with clear confirmation
- [ ] System in valid state for next operation

## Error Handling

**If file not found:**
- Check alternate locations
- Report specific missing file
- Provide recovery guidance
- Don't proceed to next checkpoint

**If validation fails:**
- Report specific validation errors
- Show which checkpoint failed
- Suggest corrections
- Halt execution immediately

**If checkpoint failure:**
- Report which CHECKPOINT failed
- Show specific error details
- Don't proceed to next PHASE
- Provide recovery steps

## Notes

- Use @ shortcuts with injected variables (@ARTIFACTS_DIR/file.md)
- Prefer Edit over Write for existing files
- Each CHECKPOINT must pass before proceeding
- Keep output concise and structured
- Remove sections not needed for this command
- See `references/command-writing-guide.md` for patterns and best practices
