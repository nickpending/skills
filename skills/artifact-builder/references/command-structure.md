# Command Structure

Command-specific structure and patterns. See `writing-fundamentals.md` for writing patterns.

## Anatomy

Single markdown file:
```
command-name.md
├── YAML frontmatter (required)
└── Markdown content (required)
```

## YAML Requirements

```yaml
---
allowed-tools: Read, Write, Edit, Bash
description: Brief command purpose
argument-hint: [optional-arg]  # Optional
---
```

**allowed-tools:**
- Analysis: `Read, Glob, Grep`
- File manipulation: `Read, Write, Edit`
- Complex workflows: `Read, Write, Bash, Task`

**description:** One sentence, what command does

**argument-hint:** Show expected argument format

## Content Requirements

**Required sections:**
- H1 command name + brief overview
- Variables (if used)
- Core instructions
- Workflow steps
- Success criteria

**Optional sections:**
- Output format
- Error handling
- Notes

## Key Paths Format

Document ALL variables. Single source of truth.

```markdown
**Variables**: Variables in CAPS are injected by hooks (see HTML comments above), `{vars}` are runtime values (find/calculate them), `[vars]` are template placeholders (substitute them).

**Key Paths**:
- ARTIFACTS_DIR - Workflow artifacts
- STATE_DIR - Saved state
- `{timestamp}` - Generated YYYYMMDD-HHMM
- `[task_id]` - From $ARGUMENTS
```

Reference `momentum-integration.md` for momentum paths.

## Execution Patterns

### Step Pattern (Simple)

Linear sequential:

```markdown
### Step 1: Load

READ @ARTIFACTS_DIR/TASKS.md

### Step 2: Process

EXTRACT incomplete tasks

### Step 3: Output

WRITE results to @STATE_DIR/output.json
```

Use for straightforward workflows.

### CHECKPOINT Pattern (Complex)

Multi-phase with gates:

```markdown
### PHASE 1: Preparation

**CHECKPOINT 1: Load Files**

READ:
- @ARTIFACTS_DIR/TASKS.md
- @PROJECT_ROOT/README.md

VERIFY: Files exist and valid

**CHECKPOINT 1.5: Validate**

CHECK dependencies met
```

Use for:
- Operations with dependencies
- Explicit validation gates
- Partial completion risk

### Critical Bash

Force halt on failure:

```markdown
```bash
! git status
```
```

Use when command must succeed or stop.

## Success Criteria

Testable checkboxes:

```markdown
- [ ] Files read
- [ ] Data validated
- [ ] Output written
```

Each must be:
- Verifiable (true/false)
- Specific (not vague)
- Outcome-focused

## Output Format

Structured and scannable:

```markdown
✅ Complete

File: path/to/output.md
Items: 5 processed

Next: /next-command
```

Not explanatory prose.

## File Size Management

**Target lengths:**
- Simple commands: <150 lines
- Complex commands: 150-300 lines
- Maximum: 400 lines

**Why:**
Context scanning efficiency drops beyond 400 lines. Token budget suffers.

**When to split:**
- Command >400 lines → Extract phases or move patterns to references
- Repeated logic → Create reference file
- Multiple operations → Separate commands

## Templates

- `templates/commands/momentum-simple.md` - Step pattern with momentum paths
- `templates/commands/momentum-complex.md` - CHECKPOINT pattern
- `templates/commands/generic.md` - Framework-agnostic

Copy structure, remove unused sections, add logic.
