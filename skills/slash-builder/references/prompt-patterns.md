# Prompt Patterns for Slash Commands

Slash commands are prompts. Use these language patterns and efficiency techniques.

## Language Patterns

### Imperative Language

**Strong Directives:**
- **MUST** / **REQUIRED** / **CRITICAL** - Non-negotiable requirements
- **ALWAYS** / **NEVER** - Absolute rules
- **Ensure** / **Verify** / **Validate** - Quality gates

**Action Starters:**
- **Read** / **Write** / **Edit** - File operations
- **Analyze** / **Extract** / **Transform** - Data operations
- **Generate** / **Create** / **Build** - Content creation
- **Check** / **Validate** / **Confirm** - Verification

**Conditional Logic:**
- **IF** [condition] **THEN** [action]
- **WHEN** [event] **perform** [action]
- **Only if** [condition] **proceed with** [action]

### Examples

**Weak:**
```markdown
Maybe you should try to read the file if it exists and then possibly extract the data
```

**Strong:**
```markdown
REQUIRED: Read TASKS.md and extract all incomplete tasks

IF file doesn't exist:
- Report error and exit

VERIFY: All extracted tasks have status and description
```

### Structure Patterns

**Checkpoint Gates:**
```markdown
CHECKPOINT 1: Load Context
- READ file X
- EXTRACT data Y
- VERIFY data is valid

PROCEED only if all checks pass
```

**Validation Requirements:**
```markdown
VERIFICATION GATE:
- [ ] Requirement 1 met
- [ ] Requirement 2 met
- [ ] Ready to proceed

FAILURE MODE: If validation fails, [specific action]
```

**Sequential Steps:**
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

## Token Efficiency

Keep commands concise while maintaining clarity.

### Remove Redundancy

**Verbose:**
```markdown
In order to accomplish this task, please make sure to carefully read the file
```

**Concise:**
```markdown
READ the file
```

**Common Eliminations:**
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

### Smart Context Usage

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

### Compact Structure Pattern

Use horizontal rules and bold labels for token-efficient structure:

```markdown
**Task:** Primary objective here

---

**Context:** Background and details

---

**Constraints:**
- Limitation 1
- Limitation 2

---

**Output:** Format requirements
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
