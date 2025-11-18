---
name: artifact-builder
description: Build and improve Claude Code slash commands, skills, and agents. Use when creating, building, making, improving, updating, migrating, fixing, or optimizing slash commands, skills, or agents. Handles new creation, structural migration, and optimization workflows for all artifact types.
---

# Artifact Builder

## Overview

Build and improve Claude Code artifacts through focused, conversational workflows.

## Workflow

Copy to track progress:
```
Artifact Builder Workflow:
- [ ] Step 1: Determine artifact type and action
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow steps
```

## Execute ALL steps in sequence

### Step 1: Determine Artifact Type and Action

**ANALYZE user's initial message for:**

**Artifact type indicators:**
- **Command**: "slash", "command", "/something", "momentum command", "generic command"
- **Skill**: "skill", "SKILL.md", "workflow skill", "tool integration", "domain knowledge"
- **Agent**: "agent", "subagent" (future)

**Action indicators:**
- **New**: "create", "build", "make", "new", "from scratch"
- **Improve**: "improve", "optimize", "reduce tokens", "make clearer", "refactor", "tighten"
- **Migrate**: "migrate", "fix structure", "update format", "convert", "validation issues", "old format"

**IF artifact type AND action clear from message:**
→ Proceed directly to Step 2 with determined workflow

**IF artifact type unclear:**
ASK: "What are you building? A slash command or a skill?"
RECORD response

**IF action unclear (after knowing type):**
ASK based on artifact type:
- For commands: "Are you creating a new command, fixing an existing command's structure, or improving an already-working command?"
- For skills: "Are you creating a new skill or improving an existing one?"
RECORD response

### Step 2: Load Appropriate Workflow

Based on Step 1 determination:

**Commands:**
- Create new command → READ `workflows/command-new.md`
- Fix structure/migrate → READ `workflows/command-migrate.md`
- Improve existing → READ `workflows/command-improve.md`

**Skills:**
- Create new skill → READ `workflows/skill-new.md`
- Fix structure/migrate → READ `workflows/skill-migrate.md`
- Improve existing → READ `workflows/skill-improve.md`

**Agents:** (future)
- Create new agent → READ `workflows/agent-new.md`

### Step 3: Execute Workflow Steps

Follow the loaded workflow file exactly as written.

Each workflow contains complete step-by-step instructions for its specific scenario.

## Key Principles

**Be conversational:**
- Discuss, don't interrogate
- Show examples
- Iterate based on feedback
- Build collaboratively

**Preserve functionality:**
- Never silently delete content
- Offer options on conflicts
- Explain all changes
- Get confirmation before major edits

**Focus on quality:**
- Token efficiency matters
- Clarity over cleverness
- Follow established patterns
- Validate structure

## Workflow Guidelines

**Separation of concerns:**
- Each workflow handles one scenario completely
- If artifact needs migration AND improvement, run migration first, then improve

**Quality gates:**
- Always run validation after structural changes
- Show work incrementally
- Get user feedback before major changes

**Collaboration:**
- Be conversational, not interrogative
- Show examples and options
- Iterate based on feedback
