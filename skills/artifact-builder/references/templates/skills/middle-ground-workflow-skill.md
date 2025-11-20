---
name: [skill-name]
description: [What it does]. USE WHEN user says "[trigger1]", "[trigger2]", "[trigger3]", or [semantic category].
allowed-tools: Read, Bash, AskUserQuestion
---

# [Skill Name]

Route to workflow based on user intent.

## Available Operations

**[Operation 1]** - [description]
**[Operation 2]** - [description]
**[Operation 3]** - [description]

## Intent Detection

Analyze for:
- Keywords: [keyword1], [keyword2]
- Context: [context clues]
- Outcome: [what user wants]

Load `workflows/[operation].md` for matched operation.

## Workflow

1. Determine operation needed
2. READ `workflows/[operation].md`
3. Execute workflow
4. Return results
