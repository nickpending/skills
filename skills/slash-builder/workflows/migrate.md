# Migrate Slash Command to New Format

Convert existing commands to new structural standard while preserving all logic and functionality.

## Approach

This workflow:
- Fixes structural issues (old format → new format)
- Preserves ALL logic, variables, workflow steps, critical warnings
- Detects conflicts and offers options
- **NEVER silently deletes anything**

## What Gets Preserved

**Keep intact:**
- All variables actually used in workflow
- Complete workflow logic and steps
- Critical warnings and requirements
- Error handling patterns
- Success criteria
- Command-specific styling (bold, formatting)

**Can be removed:**
- Emojis (unless part of critical warnings)
- Old subsection structures that don't fit new format

## What Changes

**Structural updates:**
- Add YAML frontmatter if missing
- Convert `## Variables` subsections → `**Key Paths:**` format
- Ensure required sections present (H1, Core Instructions, Success Criteria)
- Add optional sections if beneficial (Workflow summary, Error Handling)

## Step 1: Read and Analyze

READ the existing command file.

Understand what it does:
- Core purpose and workflow
- Framework (momentum vs generic)
- Complexity (simple linear vs multi-phase)
- All variables used

## Step 2: Run Validation

RUN validation script:
```bash
python3 scripts/validate_command.py [existing-command.md]
```

Show results to user:
"Validation found these issues:
- Missing YAML frontmatter
- Using old ## Variables format instead of **Key Paths:**
- Missing Workflow summary section

Let's fix these while preserving all your command logic."

## Step 3: Determine Template

Based on analysis:

**IF momentum command** (uses PROJECT_ROOT, ARTIFACTS_DIR, etc.):
- Simple linear workflow → `references/momentum-simple.md`
- Multi-phase with checkpoints → `references/momentum-complex.md`

**IF generic command:**
- Use `references/generic.md`

Explain choice:
"This command uses momentum variables and has checkpoint structure, so we'll align with `momentum-complex.md` template."

**REQUIRED:** READ the selected template file.

**REQUIRED:** READ `references/command-writing-guide.md` for Key Paths format and variable notation.

## Step 4: Detect Conflicts

Check for patterns that don't fit new structure:

### Variable Conflicts

**IF command has variables in old subsection format:**
```markdown
## Variables

### Injected
- ARTIFACTS_DIR - ...

### Runtime
- {timestamp} - ...
```

**Explain:** "Old format uses subsections. New format uses single Key Paths list."

**Show conversion:**
```markdown
**Key Paths**:
- ARTIFACTS_DIR - Workflow artifacts
- `{timestamp}` - Generated as YYYYMMDD-HHMM
```

**Ask:** "This preserves all your variables in new format. Look correct?"

### Critical Section Conflicts

**If command has custom critical section:**
```markdown
## ⚠️ CRITICAL: MARK TASK COMPLETE AND DOCUMENT ⚠️

**🛑 NO REDUNDANT DEMOS**
**🛑 CAPTURE WHAT HAPPENED**
```

**Template has placeholder:**
```markdown
## ⚠️ CRITICAL: [KEY COMMAND PRINCIPLE]

**REQUIRED:**
- ...
```

**Explain conflict:** "Your command has specific critical warnings. Template has placeholder structure."

**Offer options:**
1. Keep your exact critical section (including emojis, text)
2. Adapt your warnings to template's REQUIRED/NEVER format
3. Hybrid: Use template structure but keep your specific warnings

**Ask:** "Which approach do you prefer?"

**Never silently choose - always ask.**

### Workflow Structure Conflicts

**If command has unique workflow pattern not in template:**

**Explain:** "Your command uses pattern X, but template uses pattern Y."

**Show both patterns.**

**Offer options:**
1. Keep your pattern (may not match template perfectly but works)
2. Adapt to template pattern (more consistent with other commands)
3. Custom solution that fits both needs

**Ask:** "What would work better for your use case?"

### Content That Doesn't Fit

**If command has sections/content with no clear home in new structure:**

**Stop and explain:** "This command has [specific content] that doesn't fit standard sections."

**Show the content.**

**Offer options:**
1. Move to Notes section
2. Create custom section
3. Integrate into Core Instructions
4. Move to separate reference doc

**Ask:** "Where should this live?"

## Step 5: Build Migration Plan

**Summarize all changes:**

```
Migration plan for [command-name]:

1. Add YAML frontmatter with tools: [list]
2. Convert Variables subsections → Key Paths format
3. [If conflict] Preserve critical section exactly as-is
4. Add Workflow summary section
5. Keep all existing workflow steps
6. Preserve all variables: [list]

This keeps all your logic while fixing structure.
Proceed with these changes?
```

**Wait for confirmation.**

## Step 6: Apply Changes

**Make structural updates using Edit tool:**

**For each change:**
1. Show old structure
2. Show new structure
3. Confirm preservation of logic

**Never delete content without explaining where it moved.**

### Example: Variable Section Migration

**Old:**
```markdown
## Variables

### Injected
- ARTIFACTS_DIR - Workflow artifacts
- PROJECT_ROOT - Project root

### Runtime
- Current date for timestamp
```

**New:**
```markdown
**Key Paths**:
- ARTIFACTS_DIR - Workflow artifacts
- PROJECT_ROOT - Project root
- `{current_date}` - Generated as YYYY-MM-DD for timestamp
```

**Confirm:** "All variables preserved, notation clarified. Correct?"

## Step 7: Validate Changes

RUN validation again:
```bash
python3 scripts/validate_command.py [migrated-command.md]
```

Show comparison:
```
Before: 4 issues
After: All checks pass ✓

Structure now compliant:
✓ YAML frontmatter
✓ Key Paths format
✓ All required sections
✓ All logic preserved
```

## Step 8: Review and Confirm

**IF in git repository:** Show diff:
```bash
git diff [command-file]
```

Summarize changes:
"Changes made:
- Added frontmatter
- Converted variable format
- Preserved all [X] variables
- Kept complete workflow logic
- Maintained critical warnings

Command now passes validation while keeping all functionality.

Ready to save these changes?"

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
