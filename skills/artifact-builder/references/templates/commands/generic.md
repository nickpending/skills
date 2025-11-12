---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: One-line description of what this command does
argument-hint: [optional-argument]
---

# Command Name

Brief 2-3 sentence overview of command purpose, when to use it, and expected outcomes.

**Variables**: Variables in CAPS are injected by hooks (see HTML comments above), `{vars}` are runtime values (find/calculate them), `[vars]` are template placeholders (substitute them).

**Key Paths**:
- $HOME - User home directory
- $PWD - Current working directory
- `{config_path}` - Computed from args
- `[selected_option]` - From user input
[List ALL variables used - injected CAPS (if any), environment $VARS, runtime `{vars}`, placeholders `[vars]`]

## ⚠️ CRITICAL: [KEY COMMAND PRINCIPLE]

**REQUIRED:**
- Primary must-do behavior
- Critical constraint that cannot be violated
- Quality gate that must pass

**NEVER:**
- Action that should never happen
- Pattern to avoid
- Anti-pattern to watch for

## Core Instructions

### Step 1: Preparation

Read @README.md and @config/settings.toml.

Validate inputs and verify prerequisites.

### Step 2: Analysis

Extract relevant information from inputs.

Process data according to command requirements.

### Step 3: Execution

Perform main command action.

Handle edge cases and validate intermediate results.

### Step 4: Output

Write results to @output/results.md.

Format according to Output Format section below.

### Step 5: Confirmation

Report completion with key results and next steps.

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

- Use @ shortcuts for file operations (@README.md, @config/file.toml)
- Prefer Edit over Write for existing files
- Keep output concise and structured
- Remove sections not needed for this command
