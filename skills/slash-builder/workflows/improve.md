# Improve Existing Slash Command

Enhance command clarity and token efficiency using prompt engineering patterns.

## Approach

This workflow:
- Assumes command is structurally compliant
- Focuses on clarity and token efficiency
- Uses patterns from `references/prompt-patterns.md`
- Proposes specific improvements
- Gets feedback before applying

## Prerequisites

**Command must already:**
- Pass validation (use `/migrate` first if needed)
- Have correct structure (**Key Paths**, required sections)
- Work functionally

## Step 1: Read and Understand

READ the existing command thoroughly.

Understand:
- What it accomplishes
- Current workflow structure
- Pain points or unclear areas
- Token usage (verbose vs concise)

## Step 2: Analyze for Improvements

**REQUIRED:** READ `references/prompt-patterns.md` to load efficiency patterns.

### Token Efficiency Opportunities

Check for:

**Redundant phrasing:**
- "In order to" → just explain the action
- "Please make sure to" → imperative instead
- "You should" → directive form

**Verbose instructions:**
- Long explanations → bullet points
- Repeated context → reference earlier sections
- Over-documented obvious steps

**Example issue:**
```markdown
In order to complete the task, you should first make sure to
read the TASKS.md file and then locate the task that is currently
marked as in progress.
```

**Improved:**
```markdown
Read TASKS.md and find task marked 🔄 In Progress.
```

### Clarity Improvements

**Check for:**

**Ambiguous instructions:**
- Unclear success criteria
- Vague conditional logic
- Missing error handling

**Poor organization:**
- Steps in wrong order
- Related instructions scattered
- Missing phase summaries

**Weak directives:**
- Hedging language ("maybe", "perhaps")
- Passive voice
- Unclear requirements

### Pattern Application

**Look for opportunities to apply:**

**Imperative directives:**
- REQUIRED / MUST / ALWAYS / NEVER
- Strong action verbs
- Clear constraints

**Conditional logic:**
- IF/THEN structure
- Clear branching
- Explicit error handling

**Phased execution:**
- Named phases
- Checkpoint validation
- Clear progression

## Step 3: Propose Improvements

**For each improvement opportunity, explain:**

1. **Current state:** Show the existing text
2. **Issue:** Why it could be better
3. **Proposed improvement:** Show new version
4. **Rationale:** Why this is clearer/more efficient

**Example proposal:**

"**Current workflow section (45 tokens):**
```
First you should read the TASKS.md file to understand what task
needs to be completed. After reading, verify that the task is
currently in progress before proceeding with completion.
```

**Issue:** Verbose, hedging language, buried requirement

**Proposed (18 tokens):**
```
READ TASKS.md and locate the task.

VERIFY: Task is currently 🔄 In Progress
```

**Rationale:** Cuts 27 tokens, clearer directive, explicit verification

Would this work better?"

## Step 4: Discuss Trade-offs

**Some improvements have trade-offs:**

**Conciseness vs. Clarity:**
- Very terse may lose beginners
- Very verbose wastes tokens
- Find balance for audience

**Example:**
"This instruction could be:
- Terse: 'Mark complete with notes'
- Detailed: 'Update task status from In Progress to Complete and document...'
- Balanced: 'Mark task ✅ Complete with implementation notes'

Which level works for your users?"

**Structure vs. Flexibility:**
- Rigid structure ensures consistency
- Flexible structure adapts to edge cases
- Consider command's variability

**Ask about preferences.**

## Step 5: Build Improvement Plan

**Summarize all proposed changes:**

```
Improvement plan for [command-name]:

Token savings:
- Variables section: -15 tokens (removed repetition)
- Workflow steps: -32 tokens (bullet points, imperatives)
- Error handling: -8 tokens (clearer conditionals)
Total: -55 tokens (~12% reduction)

Clarity improvements:
- Added explicit VERIFY checkpoints
- Clearer IF/THEN logic for errors
- Stronger directives (REQUIRED/NEVER)
- Better phase naming

These changes keep all functionality while making command
clearer and more efficient.

Proceed with improvements?
```

**Wait for confirmation.**

## Step 6: Apply Improvements

**Make changes incrementally:**

**For each section:**
1. Show original
2. Show improved version
3. Confirm it maintains meaning

**Example:**

"**Updating Critical section:**

Before:
```markdown
Make sure you don't skip the implementation notes as they
are important for future reference.
```

After:
```markdown
**NEVER:**
- Skip implementation notes
```

Same requirement, 70% fewer tokens. Correct?"

## Step 7: Validate and Review

VERIFY validation still passes:
```bash
python3 scripts/validate_command.py [command-file]
```

Review overall changes:

"Improvements applied:
- Token reduction: 55 tokens (12%)
- Clarity: Stronger directives, explicit checkpoints
- Structure: Maintained all required sections
- Logic: All workflow steps preserved

Command is tighter and clearer while keeping functionality.

Test the command to confirm it works as expected."

## Application Examples

These show how to apply patterns from `prompt-patterns.md` to command improvement.

### Remove Filler

**Before:** "In order to complete the task properly, you will need to..."
**After:** "To complete the task:..."

**Before:** "Please make sure that you..."
**After:** "REQUIRED:..."

### Use Bullet Points

**Before:**
```
You should first check if the file exists, then read the contents,
and after that validate the structure before proceeding.
```

**After:**
```
CHECK: File exists
READ: File contents
VALIDATE: Structure correct
```

### Strong Directives

**Before:** "You might want to consider checking..."
**After:** "VERIFY:..."

**Before:** "It would be good if you..."
**After:** "REQUIRED:..."

### Reference Earlier Content

**Before:**
```
## Step 1
Remember to validate input...

## Step 2
Don't forget to validate input...
```

**After:**
```
## Constraints
- Validate all inputs

## Step 1
Apply constraints above...

## Step 2
Continue with validated input...
```

### Structured Conditionals

**Before:**
```
If there's an error you should report it but if there isn't
then you can continue with the next step unless...
```

**After:**
```
IF error:
  Report and halt

IF validation passes:
  Continue to next step

IF edge case:
  Handle specifically
```

## Key Principles

**Token efficiency:**
- Remove redundancy
- Use imperatives (READ, VERIFY, NEVER)
- Bullets over prose
- Reference over repeat

**Clarity:**
- Explicit requirements (REQUIRED, MUST)
- Clear conditionals (IF/THEN)
- Named phases (PHASE 1, CHECKPOINT 1)
- Unambiguous success criteria

**Balance:**
- Not cryptic
- Not wasteful
- Right level for audience
- Test with users

**Respect existing:**
- NEVER change working logic
- Preserve command intent
- Keep author's style where it works
- Only improve, don't redesign
