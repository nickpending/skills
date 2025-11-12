# Writing Fundamentals

Core patterns for writing effective Claude Code artifacts (commands and skills).

## Language Patterns

### Imperative Directives

**Strong commands:**
- **MUST** / **REQUIRED** / **CRITICAL** - Non-negotiable
- **ALWAYS** / **NEVER** - Absolute rules
- **READ** / **WRITE** / **EDIT** - File operations
- **VERIFY** / **VALIDATE** / **ENSURE** - Quality gates

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

### Structure Patterns

**Checkpoint gates:**
```markdown
CHECKPOINT 1: Load Context
- READ file X
- EXTRACT data Y
- VERIFY data is valid

PROCEED only if all checks pass
```

**Verification gates:**
```markdown
VERIFICATION GATE:
- [ ] Requirement 1 met
- [ ] Requirement 2 met
- [ ] Ready to proceed

FAILURE MODE: If validation fails, [specific action]
```

**Sequential steps:**
```markdown
PHASE 1: Preparation
1. First action
2. Second action
VERIFICATION: State what was accomplished

PHASE 2: Execution
1. Next action
2. Final action
VERIFICATION: Confirm completion
```

## Workflow Execution Patterns

For workflow skills and complex commands that must execute as procedures.

### Execution Requirements Framing

Start workflows with explicit execution framing:

```markdown
# Workflow Name

[One sentence: what this accomplishes]

## Execution Requirements

**YOU MUST execute these steps sequentially.**

Each step builds on previous steps. Do not skip ahead or summarize.
```

### Step Structure

Complete step format enforces procedural execution:

```markdown
## Step N: [Action Verb] [Object]

[Brief context if needed]

**REQUIRED ACTIONS:**
1. ACTION: Specific thing to do
2. ACTION: Next specific thing
3. IF condition:
   - ACTION: Response
   - ELSE: Alternative

**VERIFICATION:**
Check that [specific outcome occurred]

**STOP before Step N+1.**
```

### Action Verbs

**Tools (use CAPS):**
- READ `file.md`
- WRITE `file.md` with [content]
- RUN `command`
- SHOW [output to user]
- ASK user: "question"

**Control flow:**
- STOP - halt and wait for input
- WAIT for [condition/approval]
- REQUIRED: [must-do item]
- NEVER: [forbidden action]

### STOP Points

Force checkpoints between steps:

```markdown
**STOP before Step 3.**

User must review [output] before proceeding.
```

Prevents skipping to final result without executing intermediate steps.

## Variable Notation

**Four types of variables:**

**CAPS** - Injected by momentum hooks
```markdown
ARTIFACTS_DIR - Workflow artifacts
PROJECT_ROOT - Project root directory
STATE_DIR - Saved state files
```

**$VARS** - Environment variables
```markdown
$HOME - User home directory
$PWD - Current working directory
$USER - Current username
```

**`{runtime}`** - Calculated at execution
```markdown
{timestamp} - Generated as YYYYMMDD-HHMM
{parsed_data} - Extracted from file/API
{computed_value} - Calculated from inputs
```

**`[placeholders]`** - User input or template values
```markdown
[user_input] - From AskUserQuestion
[file_path] - From command arguments
[selected_option] - From selection process
```

**Standard header:**
```markdown
**Variables**: Variables in CAPS are injected by hooks (see HTML comments above), `{vars}` are runtime values (find/calculate them), `[vars]` are template placeholders (substitute them).
```

## Claude Code Capabilities

### @ Shortcuts

Reference files efficiently:

```markdown
# With injected variables
Read @ARTIFACTS_DIR/TASKS.md
Write @STATE_DIR/checkpoint.json

# Relative to current directory
Read @README.md
Edit @src/main.ts

# Absolute paths
Read @/Users/user/.config/app/settings.toml
```

**Usage:**
- Use @ shortcuts directly in workflow steps
- Combine with injected path variables for portability
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
- Artifact needs configuration choices
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

## Token Efficiency

Keep artifacts concise while maintaining clarity.

### Remove Redundancy

**Verbose:**
```markdown
In order to accomplish this task, please make sure to carefully read the file
```

**Concise:**
```markdown
READ the file
```

**Common eliminations:**
- ❌ "In order to" → ✅ "To"
- ❌ "Please ensure that" → ✅ "Ensure"
- ❌ "You should" → ✅ [Direct imperative]
- ❌ "It is important to note that" → ✅ [Just state the fact]
- ❌ "At this point in time" → ✅ "Now"
- ❌ "Due to the fact that" → ✅ "Because"

### Efficient Lists

**Verbose:**
```markdown
First, you should read the file
Second, you should extract the data
Third, you should validate the results
```

**Concise:**
```markdown
1. Read file
2. Extract data
3. Validate results
```

### Reference Don't Repeat

**Don't repeat information:**
```markdown
## Constraints
- MUST validate input
- MUST check file exists
- MUST handle errors

## Step 2
Follow all constraints from above ← Don't repeat
```

**Reference instead:**
```markdown
## Constraints
[List constraints once]

## Step 2
Apply constraints from above
```

### Variable Documentation

**Verbose:**
```markdown
The TASK_NUMBER variable is a variable that contains the number of the task that was passed as an argument to the command
```

**Concise:**
```markdown
TASK_NUMBER - Task number from command argument
```

## When NOT to Optimize

Clarity > brevity for:

- **Complex logic** - Better explicit than ambiguous
- **Critical constraints** - Worth repeating if truly important
- **Edge cases** - Include if they significantly affect behavior
- **First drafts** - Optimize after testing

## Power Words

**Commands:**
- Execute, Implement, Construct, Formulate, Devise

**Analysis:**
- Evaluate, Assess, Examine, Investigate, Scrutinize

**Constraints:**
- Must, Shall, Required, Mandatory, Essential

**Prohibitions:**
- Never, Avoid, Exclude, Omit, Reject

## Emphasis Techniques

- **CAPITALS** for critical requirements
- **Bold** for key concepts
- `Code format` for technical terms
- > Blockquotes for important notes

## Quick Reference

**Be Direct and Specific:**
- Use clear imperatives
- Avoid vague language
- State exact requirements upfront

**Structure Over Chaos:**
- Use markdown headers and formatting
- Separate sections clearly
- Order: Context → Task → Constraints → Output

**Show, Don't Just Tell:**
- Include examples for complex tasks
- Demonstrate edge cases
- Provide counter-examples when helpful
