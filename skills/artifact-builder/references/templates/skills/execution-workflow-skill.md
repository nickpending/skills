---
name: skill-name
description: Brief description of skill capability. USE WHEN user says "[trigger1]", "[trigger2]", "[trigger3]", or [semantic usage category].
allowed-tools: Read, Write, Edit, AskUserQuestion
---

# Skill Name

## Overview

[2-3 sentence description of what this skill does, when to use it, and what success looks like]

<!--
DIRECTORY STRUCTURE:
skill-name/
├── SKILL.md (this file - router)
├── workflows/
│   ├── scenario-a.md (200-300 lines)
│   ├── scenario-b.md (200-300 lines)
│   └── scenario-c.md (200-300 lines)
└── references/ (optional)
    └── patterns.md (supporting documentation)

Replace [placeholders], remove unused sections, keep under 200 lines.
See references/skill-structure.md for structure patterns.
See references/writing-fundamentals.md for writing patterns.
-->

## Available Workflows

**Scenario A:**
- Use when [specific condition or use case]
- Workflow: `workflows/scenario-a.md`
- Outcome: [what gets accomplished]

**Scenario B:**
- Use when [different condition or use case]
- Workflow: `workflows/scenario-b.md`
- Outcome: [what gets accomplished]

**Scenario C:**
- Use when [another condition or use case]
- Workflow: `workflows/scenario-c.md`
- Outcome: [what gets accomplished]

## Workflow Checklist

- [ ] Determine which scenario applies
- [ ] Load appropriate workflow
- [ ] Execute workflow steps sequentially
- [ ] Verify completion

## Execute ALL steps in sequence

### Step 1: Determine Scenario

ASK user clarifying questions to identify which workflow needed:
- "What are you trying to accomplish?"
- "[Specific question relevant to skill]"
- "[Another discriminating question]"

ANALYZE responses against workflow scenarios above.

DECIDE which workflow matches user's intent.

### Step 2: Load Workflow

READ `workflows/[selected-scenario].md`

VERIFY file loaded successfully.

### Step 3: Execute Workflow

FOLLOW loaded workflow exactly as written.

DO NOT skip steps or summarize.

DO NOT proceed to next steps until current workflow completes.

**Each workflow contains:**
- Execution requirements framing
- Step-by-step REQUIRED ACTIONS
- VERIFICATION checkpoints
- STOP points between steps

### Step 4: Verify Completion

CONFIRM workflow completed successfully:
- All steps executed
- Output generated
- Success criteria met

REPORT results to user with next steps if applicable.

## Usage Notes

**Workflow files use execution language:**
- REQUIRED ACTIONS in each step
- CAPS for tool names (READ, WRITE, ASK)
- STOP points between steps
- VERIFICATION sections
- See `references/writing-fundamentals.md` for execution patterns

**Router responsibilities:**
- Scenario determination
- Workflow loading
- Execution delegation
- Completion verification

**Keep workflows focused:**
- 200-300 lines per workflow (400 max)
- One capability per workflow
- Split large workflows into phases
- Extract common patterns to references/

## When to Use

**Use this skill when:**
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]

**Don't use when:**
- [Anti-pattern or wrong use case]
- [Alternative skill or approach would be better]

## Examples

**Example 1:**
```
User: "[Natural request that triggers scenario A]"
Result: [What happens - scenario A workflow executes]
```

**Example 2:**
```
User: "[Natural request that triggers scenario B]"
Result: [What happens - scenario B workflow executes]
```

**Example 3:**
```
User: "[Natural request that triggers scenario C]"
Result: [What happens - scenario C workflow executes]
```

## Maintenance

**Adding workflows:**
1. Create workflow file in workflows/
2. Add to Available Workflows section
3. Update Step 1 discriminating questions
4. Test scenario determination logic

**Splitting workflows:**
- If workflow >400 lines, split into phases
- Create phase-1-name.md, phase-2-name.md
- Router loads first phase, phases chain to next

**Common patterns:**
- Extract repeated logic to references/
- Keep workflows DRY by referencing shared patterns
- Document domain knowledge in references/
