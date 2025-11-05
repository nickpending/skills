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
- USER_INPUT: $ARGUMENTS (what user passed to command)

### Injected (from hooks - see HTML comments)
- PROJECT_ROOT: Project root directory
- ARTIFACTS_DIR: .workflow/artifacts/ (TASKS.md, ITERATION.md, etc.)
- STATE_DIR: .workflow/state/ (saved state files)
- [Only list variables actually used in this command]

### Runtime (calculated during execution)
- timestamp: Generated as YYYYMMDD-HHMM (e.g., 20251029-1745)
- [any other vars computed by command]

## Core Instructions

### Step 1: Load Context

Read @ARTIFACTS_DIR/TASKS.md and validate structure.

Extract required information and verify completeness.

### Step 2: Process Data

Transform data according to requirements.

Apply business logic and handle edge cases.

### Step 3: Execute Action

Perform main command operation.

Update @STATE_DIR/checkpoint.json if needed.

### Step 4: Generate Output

Write results to @ARTIFACTS_DIR/output.md.

Format according to Output Format section below.

### Step 5: Confirmation

Report completion with key details and next steps.

## Output Format

Structured, concise output:

```
✅ [Action] Complete

[Key Information]
File: path/to/output.md
Status: Success
Items: 5 processed

Next: [What user should do next]
```

## Success Criteria

Command succeeds when:

- [ ] Required files read successfully
- [ ] Data validated and processed
- [ ] Output files written correctly
- [ ] User notified with confirmation
- [ ] Ready for next workflow step

## Error Handling

**If file not found:**
- Check alternate locations
- Report specific missing file
- Provide recovery guidance

**If validation fails:**
- Report specific validation errors
- Don't proceed to next step
- Suggest corrections

## Notes

- Use @ shortcuts with injected variables (@ARTIFACTS_DIR/file.md)
- Prefer Edit over Write for existing files
- Keep output concise and structured
- Remove sections not needed for this command
- See `references/command-writing-guide.md` for patterns and best practices
