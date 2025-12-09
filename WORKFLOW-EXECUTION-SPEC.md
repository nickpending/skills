# Workflow Execution Specification

How to write skills and workflows that execute as procedures rather than being read as descriptive context.

## Contents
- [The Problem](#the-problem)
- [Token Efficiency and File Size](#token-efficiency-and-file-size)
- [Router Pattern for SKILL.md](#router-pattern-for-skillmd)
- [Workflow Execution Language](#workflow-execution-language)
- [Tool References](#tool-references)
- [Checkpoint Pattern](#checkpoint-pattern)
- [Anti-Patterns](#anti-patterns)
- [Examples](#examples)
- [Validation Checklist](#validation-checklist)

## The Problem

Language models can interpret workflow instructions in two ways:

**As context** (wrong): "Here's what a good migration looks like"
- Model understands the concept
- Produces output matching the description
- Skips the actual procedural steps

**As procedure** (correct): "Do these steps now in this order"
- Model executes each step
- Shows work incrementally
- Follows exact sequence

The difference is in how workflows are written.

## Token Efficiency and File Size

Execution language (CAPS tools, explicit steps, STOP points) ensures workflows execute as procedures. But verbose execution language must be balanced against token efficiency.

### File Size Targets

Based on empirical testing with progressive disclosure patterns:

**SKILL.md (Tier 2 - Entry point):**
- Target: <200 lines
- Maximum: 250 lines
- Purpose: Quick navigation map to workflows
- If larger: Split into multiple skills by capability

**Workflow files (Tier 3 - Loaded on-demand):**
- Target: 200-300 lines
- Maximum: 400 lines
- Purpose: Complete execution instructions for one capability
- If larger: Consider splitting into sub-workflows

**Reference files (Tier 3 - Loaded selectively):**
- Target: 200-300 lines each
- Purpose: Deep documentation for specific topics
- Organization: One topic per file

### Why These Limits Matter

**Context scanning efficiency:**
- LLMs scan ~200 lines efficiently to decide next action
- Beyond 400 lines, decision-making slows
- Navigation becomes harder

**Token budget:**
- Loading 3-4 files (SKILL.md + 2-3 workflows/references) = 600-1200 lines
- Leaves room for actual codebase context
- Prevents context overflow

**Cognitive load:**
- Humans reviewing workflows benefit from focused files
- Easier to maintain and update
- Clear separation of concerns

### When to Split Workflows

Split a workflow file when:

**Length exceeds 400 lines:**
- Extract repeated patterns into separate reference
- Split into phase-specific sub-workflows
- Move examples to separate examples file

**Multiple distinct capabilities:**
- Each capability = separate workflow file
- Example: migrate.md handles structure fixes, not content improvement

**Conditional branches dominate:**
- If workflow is mostly "IF framework A do X, IF framework B do Y"
- Split into framework-specific workflows
- Router handles the IF/THEN at skill level

### Balancing Execution Language vs Brevity

Execution language requires some verbosity for clarity:

**Keep verbose (for execution):**
- Explicit numbered steps
- STOP/WAIT checkpoints
- Tool names in CAPS
- IF/THEN conditions with THEN actions spelled out

**Keep concise (for tokens):**
- Remove filler words ("in order to", "please make sure")
- Use bullets over prose
- Reference don't repeat (point to earlier steps)
- Combine related actions into single step

**Example of balanced language:**

```markdown
## Step 3: Validate Template

**REQUIRED ACTIONS:**

1. CHECK framework type from Step 1 analysis
2. SELECT template based on framework
3. READ selected template file
4. VERIFY template loaded

**STOP before Step 4.**
```

This is explicit enough to force execution while being concise enough for token efficiency.

### Splitting Example

**Before:** 450-line migrate.md workflow

**After (if needed):**
```
workflows/
├── migrate.md (200 lines - main flow with routing)
├── migrate-variables.md (150 lines - variable migration details)
├── migrate-critical.md (100 lines - critical section conflict resolution)
└── migrate-structure.md (150 lines - structural pattern migration)
```

Main workflow points to sub-workflows when needed: "For variable migration details, READ workflows/migrate-variables.md"

### Current Architecture Check

The artifact-builder structure demonstrates this pattern:
- SKILL.md: 57 lines ✓ (lean router)
- create.md: 167 lines ✓ (unified create workflow)
- improve.md: 89 lines ✓ (focused)
- migrate.md: 107 lines ✓ (focused)
- 9 exemplar files: 63-191 lines each ✓ (loaded on-demand)

This follows progressive disclosure: router → workflow → exemplars as needed.

## Router Pattern for SKILL.md

Router-based skills delegate to focused workflow files while maintaining skill-creation-spec compliance.

### Structure

```markdown
---
name: skill-name
description: [What + when, includes triggers]
---

# Skill Name

Brief overview of capability.

## Workflow

Copy to track progress:
```
- [ ] Step 1: Determine intent/scenario
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow steps
```

## Execute ALL steps in sequence

### Step 1: Determine Intent

[Clear decision tree with specific triggers]

**Scenario A** (triggers: X, Y, Z) → workflows/scenario-a.md
**Scenario B** (triggers: A, B, C) → workflows/scenario-b.md

### Step 2: Load Workflow

READ the workflow file for the matching scenario.

### Step 3: Execute Workflow

Follow workflow instructions exactly as written.
Each workflow contains complete step-by-step instructions.

## [Optional supporting sections]
```

### Key Elements

1. **Workflow checklist** - Per skill-creation-spec pattern
2. **"Execute ALL steps in sequence"** - Standard section header
3. **Explicit READ** - Don't say "use" or "reference", say READ
4. **Router as procedure** - Present routing as steps to execute, not concepts to understand

## Workflow Execution Language

Workflows must use language patterns that signal immediate execution.

### Framing

Start workflows with execution framing:

```markdown
# Workflow Name

[One sentence: what this accomplishes]

## Execution Requirements

**YOU MUST execute these steps sequentially.**

Each step builds on previous steps. Do not skip ahead or summarize.
```

### Step Format

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

**BEFORE PROCEEDING:**
[What must be true to continue]
```

### Action Verbs

Use strong imperatives:

**Tools:**
- READ `file.md`
- WRITE `file.md` with [content]
- RUN `command`
- SHOW [output to user]
- ASK user: "question"
- VERIFY [condition]

**Control flow:**
- STOP - halt and wait for input
- WAIT for [condition/approval]
- IF/THEN/ELSE - conditional logic
- REQUIRED: [must-do item]
- NEVER: [forbidden action]

## Tool References

### Explicit Tool Calls

Models need explicit cues to use tools:

**Ineffective:**
```markdown
Reference the template for structure
Use the validation script
Check existing patterns
```

**Effective:**
```markdown
READ `references/template.md`
RUN `python scripts/validate.py [file]`
GREP pattern in existing files
```

### Tool Name Format

Use CAPS for tool names to signal tool invocation:

- READ (not "read", "view", "check")
- WRITE (not "create", "save")
- EDIT (not "modify", "update")
- RUN/Bash (not "execute", "run command")
- ASK (not "ask user", "confirm with")

## Checkpoint Pattern

For workflows with validation gates:

```markdown
### CHECKPOINT N: [Verification Name]

**What you just did:**
- [Summary of previous step]

**Verify now:**
```bash
command to check state
```

**Expected result:**
[What success looks like]

**IF verification fails:**
1. [Specific fix action]
2. Re-run verification
3. Do not proceed until passing

**IF verification passes:**
Proceed to [next step/checkpoint]
```

### Stop Points

Use STOP to force checkpoint validation:

```markdown
**STOP HERE**

Before proceeding, user must:
- Review [output]
- Confirm [decision]
- Approve [action]

ASK: "Are you ready to proceed?"
- If NO: Exit workflow
- If YES: Continue to Step N
```

## Anti-Patterns

Patterns that cause workflows to be treated as context:

### ❌ Passive Voice

```markdown
The file should be read
The validation can be run
Results would be shown to user
```

**Fix:** Use imperative active voice

```markdown
READ the file
RUN validation
SHOW results to user
```

### ❌ Suggestion Language

```markdown
You might want to check...
Consider running validation...
It would be good to verify...
```

**Fix:** Use directives

```markdown
CHECK [specific thing]
RUN validation now
VERIFY [condition]
```

### ❌ Implementation Details

```markdown
The workflow will determine the template type by analyzing...
```

**Fix:** Direct action

```markdown
READ the command file
CHECK for momentum variables (ARTIFACTS_DIR, PROJECT_ROOT)
IF found: momentum template
IF not found: generic template
```

### ❌ Vague References

```markdown
Use the appropriate template
Reference the guide as needed
Follow standard patterns
```

**Fix:** Explicit paths

```markdown
READ `references/momentum-simple.md`
READ `references/command-writing-guide.md` section "Variable Notation"
```

### ❌ Conceptual Description

```markdown
This step involves understanding the command structure...
The goal is to identify conflicts...
```

**Fix:** Concrete actions

```markdown
READ command file lines 1-50
IDENTIFY critical section (look for ## ⚠️ CRITICAL)
COMPARE to template critical section
```

## Examples

### Bad: Descriptive Context

```markdown
## Step 4: Detect Conflicts

When migrating, the workflow should check for patterns that don't
fit the new structure. Critical sections might have custom formatting
that differs from the template. The model should detect this and
offer options to the user.
```

**Problem:** Describes what should happen, doesn't instruct to do it.

### Good: Executable Procedure

```markdown
## Step 4: Detect Conflicts

**CHECK critical section:**

READ command file
FIND section matching `## ⚠️ CRITICAL`
EXTRACT section content

READ `references/template.md`
FIND template critical section
EXTRACT template content

**COMPARE sections:**

IF command section format differs from template:
  STOP and explain conflict to user
  SHOW both formats
  ASK: "Which format should we use?"
  - Option 1: Keep original format
  - Option 2: Adopt template format
  - Option 3: Hybrid approach

  WAIT for user choice

IF sections match:
  Continue to Step 5
```

### Bad: Workflow as Guide

```markdown
## Migration Approach

This workflow preserves all logic while fixing structural issues.
It removes emojis and converts to standard format. When conflicts
arise, options are offered to the user.
```

**Problem:** Explains philosophy, no actions to execute.

### Good: Workflow as Script

```markdown
## Step 1: Analyze Current Command

**REQUIRED ACTIONS:**

1. READ the command file completely
2. IDENTIFY these elements:
   - Variables used (CAPS, $ENV, {runtime})
   - Critical sections (## ⚠️ CRITICAL)
   - Workflow structure (linear vs phased)
   - Section headers

3. CREATE analysis summary:
   ```
   Command: [name]
   Type: [linear/phased]
   Variables: [list]
   Has custom critical: [yes/no]
   ```

4. SHOW summary to user

**VERIFICATION:**
Summary must list all variables actually used in workflow steps.

**STOP before Step 2.**
User reviews analysis for accuracy.
```

## Validation Checklist

Before finalizing a workflow, verify:

### Language Check
- [ ] Every step uses imperative verbs
- [ ] Tool names in CAPS (READ, RUN, SHOW, etc)
- [ ] No passive voice or suggestion language
- [ ] No "should", "would", "might", "could"
- [ ] Present tense imperatives only

### Structure Check
- [ ] Steps numbered explicitly
- [ ] Each step has concrete actions
- [ ] Checkpoints have verification commands
- [ ] STOP/WAIT points before major decisions
- [ ] IF/THEN/ELSE for all conditionals

### Execution Check
- [ ] File references use explicit READ
- [ ] Scripts referenced with RUN command
- [ ] Questions use ASK with exact wording
- [ ] No vague references ("appropriate", "relevant")
- [ ] Every "reference" converted to READ

### Flow Check
- [ ] Dependencies clear (Step N requires Step N-1)
- [ ] No circular references
- [ ] User confirmation points identified
- [ ] Error handling for each failure mode
- [ ] Clear exit conditions

### Test
- [ ] Read workflow aloud - does it sound like instructions?
- [ ] Could someone execute this without interpretation?
- [ ] Are all tools explicitly named?
- [ ] Would model know when to stop and ask?

## Integration with artifact-builder

The artifact-builder skill uses this spec when creating skills and commands:

**Creating new:**
- SKILL.md follows router pattern (this spec)
- Workflows use execution language (this spec)
- Points to real exemplars, not abstract templates

**Migrating existing:**
- Check workflow language against anti-patterns
- Convert descriptive to imperative
- Add explicit tool calls

**Improving existing:**
- Tighten language using execution patterns
- Remove hedging/suggestion language
- Add STOP points for validation

---

**Related:**
- `skills/artifact-builder/` - Skill and command creation
- `skills/artifact-builder/references/writing-fundamentals.md` - Token efficiency, imperative language
