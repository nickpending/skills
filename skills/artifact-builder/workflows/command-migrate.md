# Migrate Slash Command to New Format

Convert existing commands to new structural standard while preserving all logic and functionality.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow fixes structural format issues while preserving all command logic. Each step builds on the previous. Do not skip ahead or produce final output without completing all steps.

**Migration preserves:**
- All variables actually used
- Complete workflow logic and steps
- Critical warnings and requirements
- Error handling patterns
- Success criteria
- Command-specific formatting

**Migration removes:**
- Decorative emojis
- Old subsection structures (## Variables with ### subheadings)

**Migration adds:**
- YAML frontmatter
- **Key Paths**: format for variables
- Required sections (H1, Core Instructions, Success Criteria)

## Step 1: Read and Analyze

**REQUIRED ACTIONS:**

1. READ the existing command file completely
2. IDENTIFY these elements:
   - Core purpose and workflow
   - Framework type (momentum vs generic)
   - Workflow structure (linear Step N vs multi-phase CHECKPOINT pattern)
   - All variables used (CAPS, $ENV, {runtime}, [placeholders])
   - Critical sections (## ⚠️ CRITICAL)

3. CREATE analysis summary:
   ```
   Command: [name]
   Framework: [momentum/generic]
   Structure: [linear/phased]
   Variables found: [list]
   Has custom critical section: [yes/no]
   ```

4. SHOW summary to user

**STOP before Step 2.**

## Step 2: Run Validation

**REQUIRED ACTIONS:**

1. RUN validation script:
   ```bash
   python3 scripts/validate_command.py [existing-command.md]
   ```

2. SHOW output to user with explanation:
   ```
   Validation found these issues:
   - [Issue 1]
   - [Issue 2]
   - [Issue 3]

   Let's fix these while preserving all command logic.
   ```

**VERIFICATION:**
Validation output must be shown to user before proceeding.

**STOP before Step 3.**

## Step 3: Determine Pattern and Momentum Integration

**REQUIRED ACTIONS:**

1. CHECK complexity and framework from Step 1 analysis

2. READ `references/pattern-selection.md` for pattern guidance

3. SELECT pattern based on complexity:
   - Single simple operation → `references/templates/commands/minimal-command.md`
   - Multi-operation (3-10) → `references/templates/commands/middle-ground-command.md`
   - Multi-phase with gates → `references/templates/commands/execution-command.md`

4. EXPLAIN choice to user:
   ```
   This command uses [pattern] pattern because [complexity reasoning].
   ```

5. READ the selected template file

6. CHECK if momentum integration from Step 1:
   **IF uses momentum variables (ARTIFACTS_DIR, PROJECT_ROOT, etc):**
   - READ `references/momentum-integration.md`
   - EXPLAIN: "This is a momentum command, will add momentum integration elements"
   - NOTE which momentum elements to preserve/add

7. READ `references/command-structure.md` for Key Paths format

8. READ `references/writing-fundamentals.md` for language patterns

9. READ `references/tool-selection.md` for tool selection guidance
   - EXTRACT allowed-tools from existing command frontmatter (if present)
   - ANALYZE command operations to determine required tools
   - NOTE tools that should be in allowed-tools for migrated version

**VERIFICATION:**
All reference files (template + structure + patterns + tool-selection + momentum if needed) must be read before proceeding.

**STOP before Step 4.**

## Step 4: Detect Conflicts

**REQUIRED ACTIONS:**

### Check 1: Variable Format

1. SEARCH command for `## Variables` heading
2. CHECK if it has subsections (### Injected, ### Runtime, etc.)

**IF old subsection format found:**
- SHOW user the current format
- SHOW proposed Key Paths conversion
- ASK: "This preserves all your variables in new format. Look correct?"
- WAIT for confirmation
- RECORD user's approval

**IF no subsections (already Key Paths format):**
- No conflict, proceed to Check 2

### Check 2: Critical Section Format

1. SEARCH command for `## ⚠️ CRITICAL` heading
2. EXTRACT critical section content
3. CHECK for emojis (🛑, ⚠️) or non-standard formatting

**IF custom formatting found:**

**STOP - YOU MUST NOT PROCEED WITHOUT USER INPUT**

SHOW user the conflict:
```
Your command has this critical section:
[show exact current format]

Template standard format is:
## ⚠️ CRITICAL: [PRINCIPLE]

**REQUIRED:**
- [items]

**NEVER:**
- [items]
```

OFFER options:
1. Keep exact format (preserve emojis and styling)
2. Convert to standard REQUIRED/NEVER format
3. Hybrid approach

ASK: "Which option do you prefer?"

WAIT for user response.

RECORD choice before proceeding.

**IF already in standard format:**
- No conflict, proceed to Check 3

### Check 3: Workflow Pattern Compatibility

1. COMPARE command workflow structure to template structure
2. CHECK if patterns match (Step N vs PHASE/CHECKPOINT, section order, etc.)

**IF patterns differ significantly:**

**STOP - GET USER DECISION**

EXPLAIN difference:
```
Your command uses [specific pattern].
Template uses [different pattern].
```

OFFER options:
1. Keep your pattern (works but differs from template)
2. Adapt to template pattern (more consistency)
3. Hybrid approach

ASK: "Which approach works better for this command?"

WAIT for user choice.

**IF patterns compatible:**
- No conflict, proceed to Check 4

### Check 4: Unmapped Content

1. SCAN for sections not in template structure
2. LIST any unique sections found

**IF unique sections exist:**

**STOP - GET USER DECISION**

SHOW content:
```
Found these sections not in template:
- [Section name]: [brief description]
```

OFFER placement options:
1. Move to Notes section
2. Create custom section
3. Integrate into Core Instructions
4. Move to separate reference file

ASK: "Where should each section go?"

WAIT for user decisions.

**IF no unique sections:**
- No conflict, all checks complete

**VERIFICATION:**
All conflict checks must be complete and user decisions recorded.

**STOP before Step 5.**

## Step 5: Build Migration Plan

**REQUIRED ACTIONS:**

1. COMPILE all decisions from Step 4 checks
2. CREATE migration plan listing every change
3. SHOW plan to user:

```
Migration plan for [command-name]:

Structural changes:
1. Add YAML frontmatter with tools: [list from analysis]
2. Convert Variables → Key Paths format [or "already compliant"]
3. Critical section: [keep exact / convert to REQUIRED-NEVER / hybrid]
4. Workflow pattern: [keep current / adapt to template]
5. Unique sections: [placement decisions from Check 4]

Preservation confirmed:
- All [N] variables maintained
- Complete workflow logic intact
- All error handling preserved

This migration fixes structure while preserving all functionality.
Proceed with these changes?
```

4. ASK user for approval
5. WAIT for confirmation

**STOP if user does not approve.**

**IF approved, proceed to Step 6.**

## Step 6: Apply Changes

**REQUIRED ACTIONS:**

Execute migration plan from Step 5 using Edit tool.

**For each structural change:**

1. SHOW user the current section
2. SHOW the migrated version
3. VERIFY logic preservation
4. APPLY edit using Edit tool
5. CONFIRM change with user

**Example execution:**

```
Migrating Variables section:

Current format:
## Variables
### Injected
- ARTIFACTS_DIR - Workflow artifacts
...

New format:
**Key Paths**:
- ARTIFACTS_DIR - Workflow artifacts
- `{timestamp}` - Generated runtime
...

All [N] variables preserved with proper notation.
Applying change now.
```

**VERIFICATION:**
After each edit, confirm the change preserved all content.

**NEVER:**
- Delete content without showing where it moved
- Skip showing before/after
- Make multiple changes without confirmation

**STOP before Step 7.**

## Step 7: Validate Changes

**REQUIRED ACTIONS:**

1. RUN validation script on migrated file:
   ```bash
   python3 scripts/validate_command.py [migrated-command.md]
   ```

2. SHOW comparison to user:
   ```
   Validation Results:

   Before migration: [N] issues
   After migration: [result]

   Structure compliance:
   ✓ YAML frontmatter present
   ✓ Key Paths format correct
   ✓ Required sections present
   ✓ Logic preservation verified
   ```

3. **IF validation fails:**
   - SHOW specific errors
   - FIX issues
   - RE-RUN validation
   - Do not proceed until passing

4. **IF validation passes:**
   - Proceed to Step 8

**VERIFICATION:**
Validation must pass before proceeding.

**STOP before Step 8.**

## Step 8: Review and Confirm

**REQUIRED ACTIONS:**

1. **IF in git repository:**
   RUN git diff to show changes:
   ```bash
   git diff [command-file]
   ```

2. CREATE final summary:
   ```
   Migration Complete

   Changes applied:
   - [List each structural change]
   - [List what was preserved]

   Verification:
   - All [N] variables intact
   - Complete workflow logic preserved
   - Validation passing

   Command structure now compliant while maintaining all functionality.
   ```

3. SHOW summary to user

4. ASK: "Migration successful. Command ready to use."

**Migration workflow complete.**

## Conflict Resolution Principles

**When you encounter a conflict:**

1. **Stop immediately** - Don't proceed with assumptions
2. **Explain the conflict** clearly with examples
3. **Show options** (2-3 viable approaches)
4. **Ask user to decide** - never choose for them
5. **Confirm the choice** before proceeding

**Examples of good conflict handling:**

"Your command uses [pattern X] but new format expects [pattern Y].

Option 1: Keep [X] - your logic works but structure differs
Option 2: Adapt to [Y] - more consistent but requires rewrite
Option 3: Hybrid [Z] - combines both approaches

Which would work better for your use case?"

## What Never to Do

**NEVER:**
- Silently delete content
- Remove variables without confirming they're unused
- Change logic to fit template
- Assume you know best approach
- Skip conflict detection

**ALWAYS:**
- Explain every structural change
- Show before/after
- Offer options on conflicts
- Preserve functionality
- Get confirmation before major changes
