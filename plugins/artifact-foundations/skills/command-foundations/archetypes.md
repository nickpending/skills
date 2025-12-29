# Command Archetypes

## Decision Tree

```
What does the command do?
│
├─► Single immediate action? ────────► Minimal
│
├─► Load state, wait for direction? ─► Priming
│
├─► Variables + conditional logic? ──► Workflow
│
└─► Multi-phase with checkpoints? ───► Orchestration
```

---

## Minimal

Single task, immediate execution, no interaction.

```markdown
---
allowed-tools: Bash(git:*)
description: Create a git commit
---

## Context

Current status: !`git status`
Changes: !`git diff HEAD`

## Task

Based on the above changes, create a single git commit.
```

**Characteristics:**
- ~15-25 lines
- Tool restrictions in frontmatter
- Context injection with `!`backticks
- Single clear instruction
- No Report section needed

**Exemplar:** `exemplar-minimal.md`

---

## Priming

Load dynamic state, confirm what's indexed, wait for direction.

```markdown
---
description: Prime network context
---

## Instructions

- Focus on X, not Y
- Do NOT read source code

## Workflow

1. Read inventory: `!`\`cat ~/.local/share/data.json\`
2. Extract mappings with jq
3. Read config: @~/.ssh/config

## Report

Ready for operations. Confirm you indexed:
- Total items
- Key categories
```

**Characteristics:**
- ~40-60 lines
- Focus instructions (what to load, what NOT to)
- Numbered workflow with actual commands
- Report confirms what was loaded
- Implies waiting, not acting

**Exemplar:** `exemplar-priming.md`

---

## Workflow

Variables, conditional logic, structured execution with report.

```markdown
---
description: Build from plan
argument-hint: [path-to-plan]
allowed-tools: Read, Write, Bash
model: claude-sonnet-4-5-20250929
---

## Variables

PATH_TO_PLAN: $ARGUMENTS

## Workflow

- If no PATH_TO_PLAN, STOP and ask user
- Read plan, implement into codebase

## Report

- Summarize work in bullet points
- Show files changed with `git diff --stat`
```

**Characteristics:**
- ~20-30 lines
- Variables section maps $ARGUMENTS
- Conditional logic ("If X, STOP")
- Model override when needed
- Specific report format

**Exemplar:** `exemplar-workflow.md`

---

## Orchestration

Complex multi-phase workflows with user checkpoints and agent delegation.

```markdown
---
description: Guided feature development
argument-hint: Optional feature description
---

## Core Principles

- Ask clarifying questions
- Understand before acting
- Use TodoWrite throughout

## Phase 1: Discovery

**Goal:** Understand what to build

1. Create todo list
2. If unclear, ask user
3. Confirm understanding

## Phase 2: Exploration

**Goal:** Understand existing code

**Actions:**
1. Launch 2-3 explorer agents in parallel
2. Read files they identify
3. Present summary

## Phase 3: Implementation

**DO NOT START WITHOUT USER APPROVAL**

...
```

**Characteristics:**
- ~100-200 lines
- Core Principles section
- Numbered phases with Goal statements
- User checkpoints (bold "Ask user", "Wait for")
- Agent delegation patterns
- DO NOT SKIP / DO NOT START warnings
- TodoWrite integration

**Exemplar:** `exemplar-orchestration.md`
