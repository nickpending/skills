---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: One-line description of what this command does
argument-hint: [optional-argument]
---

# Command Name

Brief 2-3 sentence overview of command purpose, when to use it, and expected outcomes.

## Variables

### From Arguments
- USER_INPUT: $ARGUMENTS (what user passed to command)

### Injected (from hooks - see HTML comments)
- PROJECT_ROOT: Project root directory
- WORKFLOW_DIR: .workflow/ directory
- ARTIFACTS_DIR: .workflow/artifacts/ (TASKS.md, ITERATION.md, etc.)
- STATE_DIR: .workflow/state/ (saved state files)
- CONTEXTS_PATH: .workflow/contexts/ (context files)
- WORKFLOW_PROJECTS: Obsidian projects directory
- PROJECT_OBSIDIAN_DIR: Current project's obsidian directory
- EXPLORATIONS_DIR: Project explorations directory
- [Only list vars actually used in this command]

### Runtime (calculated during execution)
- timestamp: Generated as YYYYMMDD-HHMM (e.g., 20251029-1745)
- [any other vars computed by command]

## Core Instructions

Brief, concise requirements using bullets:

- Primary behavior or requirement
- Critical rule or constraint
- Expected outcome or deliverable
- Error handling approach

## Workflow

1. **Preparation** - Read context files, validate inputs
2. **Analysis** - Extract/process information
3. **Execution** - Perform main command action
4. **Output** - Write files, generate reports
5. **Confirmation** - Notify user of completion

## Claude Code Patterns

### @ Shortcuts

@ symbols resolve relative to current working directory unless using injected path variables:

```markdown
# Injected path variables (recommended)
@ARTIFACTS_DIR/TASKS.md          # Uses injected ARTIFACTS_DIR path
@STATE_DIR/state-latest.md       # Uses injected STATE_DIR path

# Relative paths (resolve from cwd)
@README.md                       # Current directory
@src/main.ts                     # Relative to cwd
@../other-project/file.md        # Parent directory navigation

# Absolute paths
@/Users/user/project/file.md     # Absolute path
```

### AskUserQuestion

Structured user input with multiple choice options.

### Task Tool

Launch subagents for specialized analysis.

## Output Format

Provide structured, concise output to reduce token usage:

```
✅ [Action] Complete

[Key Information]
File: path/to/output.md
Status: Success
Items Processed: 5

Key Points:
- Point 1
- Point 2
- Point 3

Next: [What user should do next]
```

## Success Criteria

Command succeeds when:

- [ ] Required files read successfully
- [ ] Analysis/processing completed
- [ ] Output files written (if applicable)
- [ ] User notified with clear confirmation
- [ ] Ready for next workflow step

## Error Handling

**If [common error]:**
- Action to take
- Fallback behavior

**If [another error]:**
- Recovery steps
- User notification

## Notes

- Prefer Edit over Write for existing files
- Don't create documentation unless explicitly requested
- Use @ shortcuts for common file reads
- Keep output concise and structured
- Only include sections relevant to this command
