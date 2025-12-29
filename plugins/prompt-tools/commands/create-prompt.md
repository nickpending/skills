---
description: Create a well-structured prompt from scratch
argument-hint: [purpose]
---

# Create Prompt

Build a prompt using prompt-foundations patterns.

## Input

**Purpose:** $ARGUMENTS

IF no purpose provided, ASK: What should this prompt accomplish?

## Workflow

### 1. Gather Requirements

DETERMINE:
- Task type (generation, analysis, extraction, transformation)
- Target model (Claude, GPT, local)
- Input format (text, code, data)
- Output format (prose, JSON, markdown, code)
- Complexity (simple vs multi-step)

### 2. Load Patterns

**INVOKE** `prompt-foundations` — read `principles.md` for core patterns.

### 3. Select Structure

**Simple (single task):**
```
[Role - 1 sentence]
[Clear instruction]
[Input/context]
[Output format]
```

**Complex (multi-step):**
```
[Role]

## Context
[Background]

## Task
[Steps]

## Constraints
[MUST/NEVER]

## Output
[Format spec]
```

### 4. Apply Principles

From prompt-foundations:
- [ ] Clear and direct (no hedging)
- [ ] Examples if task is ambiguous
- [ ] XML tags if complex/multi-part
- [ ] Output format explicit and LAST
- [ ] Role if domain expertise needed

### 5. Deliver

OUTPUT the complete prompt in a code block.

State what patterns were applied.
