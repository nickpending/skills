# Improve Existing Slash Command

Enhance command clarity and token efficiency using prompt engineering patterns.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow improves structurally-compliant commands for clarity and token efficiency. Each step analyzes, proposes improvements, gets approval, and applies changes incrementally. Do not skip approval gates or apply changes without user confirmation.

**Prerequisites - Command must already:**
- Pass validation (use `/migrate` first if needed)
- Have correct structure (**Key Paths**, required sections)
- Work functionally

## Step 1: Read and Understand

**REQUIRED ACTIONS:**

1. READ the existing command file completely

2. ANALYZE and RECORD:
   - What it accomplishes (core purpose)
   - Current workflow structure (linear vs phased)
   - Pain points or unclear areas
   - Token usage (verbose vs concise sections)

3. CREATE initial assessment:
   ```
   Command: [name]
   Purpose: [what it does]
   Structure: [linear/phased]
   Initial observations:
   - Verbosity level: [terse/moderate/verbose]
   - Clarity issues: [list if any]
   - Strong points: [what works well]
   ```

4. SHOW assessment to user

**VERIFICATION:**
Complete understanding of command purpose and current state.

**STOP before Step 2.**

## Step 2: Analyze for Improvements

**REQUIRED ACTIONS:**

1. READ `references/writing-fundamentals.md` to load efficiency patterns

2. SCAN command for token efficiency opportunities:

   **Check for redundant phrasing:**
   - "In order to" → just explain the action
   - "Please make sure to" → imperative instead
   - "You should" → directive form

   **Check for verbose instructions:**
   - Long explanations → bullet points
   - Repeated context → reference earlier sections
   - Over-documented obvious steps

   **Example of issue:**
   ```markdown
   In order to complete the task, you should first make sure to
   read the TASKS.md file and then locate the task that is currently
   marked as in progress.
   ```

   **Improved version:**
   ```markdown
   Read TASKS.md and find task marked 🔄 In Progress.
   ```

3. SCAN command for clarity opportunities:

   **Check for ambiguous instructions:**
   - Unclear success criteria
   - Vague conditional logic
   - Missing error handling

   **Check for poor organization:**
   - Steps in wrong order
   - Related instructions scattered
   - Missing phase summaries

   **Check for weak directives:**
   - Hedging language ("maybe", "perhaps")
   - Passive voice
   - Unclear requirements

4. IDENTIFY pattern application opportunities:

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

5. CREATE improvement inventory (list all opportunities found)

**VERIFICATION:**
Complete analysis with specific examples from command.

**STOP before Step 3.**

## Step 3: Propose Improvements

**REQUIRED ACTIONS:**

1. For EACH improvement from Step 2 inventory, CREATE structured proposal:

   **Format:**
   - **Current state:** Show existing text
   - **Issue:** Why it could be better
   - **Proposed improvement:** Show new version
   - **Rationale:** Why this is clearer/more efficient

   **Example:**
   ```
   Current workflow section (45 tokens):
   First you should read the TASKS.md file to understand what task
   needs to be completed. After reading, verify that the task is
   currently in progress before proceeding with completion.

   Issue: Verbose, hedging language, buried requirement

   Proposed (18 tokens):
   READ TASKS.md and locate the task.

   VERIFY: Task is currently 🔄 In Progress

   Rationale: Cuts 27 tokens, clearer directive, explicit verification

   Would this work better?
   ```

2. SHOW all proposals to user

3. WAIT for feedback on each proposal

4. RECORD user decisions (approve/reject/modify)

**VERIFICATION:**
All improvements proposed with clear before/after examples.

**STOP before Step 4.**

## Step 4: Discuss Trade-offs

**REQUIRED ACTIONS:**

1. IDENTIFY any trade-offs in proposed improvements

2. **FOR each trade-off, EXPLAIN options:**

   **Conciseness vs. Clarity:**
   ```
   This instruction could be:
   - Terse: 'Mark complete with notes'
   - Detailed: 'Update task status from In Progress to Complete and document...'
   - Balanced: 'Mark task ✅ Complete with implementation notes'

   Which level works for your users?
   ```

   **Structure vs. Flexibility:**
   - Rigid structure ensures consistency
   - Flexible structure adapts to edge cases
   - Consider command's variability

3. ASK user about preferences for each trade-off

4. WAIT for decisions

5. RECORD user preferences

**VERIFICATION:**
All trade-offs discussed and user preferences recorded.

**STOP before Step 5.**

## Step 5: Build Improvement Plan

**REQUIRED ACTIONS:**

1. COMPILE all approved improvements from Steps 3-4

2. CALCULATE token impact and clarity gains

3. CREATE improvement plan summary:
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

4. SHOW plan to user

5. ASK for final approval

6. WAIT for confirmation

**STOP if user does not approve.**

**IF approved, proceed to Step 6.**

## Step 6: Apply Improvements

**REQUIRED ACTIONS:**

1. FOR each approved improvement, execute incrementally:

   **Process per section:**
   - SHOW original
   - SHOW improved version
   - CONFIRM it maintains meaning
   - APPLY edit using Edit tool
   - VERIFY change applied correctly

   **Example execution:**
   ```
   Updating Critical section:

   Before:
   Make sure you don't skip the implementation notes as they
   are important for future reference.

   After:
   **NEVER:**
   - Skip implementation notes

   Same requirement, 70% fewer tokens. Correct?
   ```

2. WAIT for confirmation on each section before proceeding to next

3. **NEVER:**
   - Apply multiple changes without showing each
   - Skip showing before/after
   - Change logic without explicit approval

**VERIFICATION:**
All approved improvements applied and confirmed section by section.

**STOP before Step 7.**

## Step 7: Validate and Review

**REQUIRED ACTIONS:**

1. RUN validation to verify structural compliance:
   ```bash
   python3 scripts/validate_command.py [command-file]
   ```

2. SHOW validation results

3. **IF validation fails:**
   - FIX issues
   - RE-RUN validation
   - Do not proceed until passing

4. **IF validation passes:**
   - CREATE final summary:
     ```
     Improvements applied:
     - Token reduction: 55 tokens (12%)
     - Clarity: Stronger directives, explicit checkpoints
     - Structure: Maintained all required sections
     - Logic: All workflow steps preserved

     Command is tighter and clearer while keeping functionality.

     Test the command to confirm it works as expected.
     ```

5. SHOW summary to user

**Improvement workflow complete.**

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
