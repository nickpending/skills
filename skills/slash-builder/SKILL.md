---
name: slash-builder
description: Build, migrate, and optimize Claude Code slash commands. Use when user wants to create new command, build slash command, migrate command to new format, convert old command format, update command to new format, fix command structure, fix validation issues, improve command clarity, reduce tokens, tighten command, refactor command for clarity, or optimize slash commands. Handles momentum workflow commands and generic slash commands.
---

# Slash Builder

Build and improve Claude Code slash commands through focused, conversational workflows.

## Workflow

Copy and track progress:
```
Slash Builder Workflow:
- [ ] Step 1: Determine user intent
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow steps
```

## Execute ALL steps in sequence

### Step 1: Determine User Intent

Identify which scenario matches user request:

**Creating new command** - User wants to build from scratch
- Trigger phrases: "Create a new command", "Build a slash command for...", "I need a command that...", "Help me create..."
- Workflow: `workflows/new.md` (conversational collaborative building)

**Fixing structure** - User has validation issues or old format
- Trigger phrases: "Update to new format", "Fix the structure", "Migrate command", "Doesn't pass validation", "Convert old format"
- Workflow: `workflows/migrate.md` (structural migration with conflict detection)

**Improving existing** - User wants clarity/efficiency improvements
- Trigger phrases: "Improve this command", "Make this clearer", "Reduce tokens", "Tighten up", "Refactor for clarity"
- Workflow: `workflows/improve.md` (token optimization using prompt patterns)

**IF user intent unclear:**
ASK: "Are you looking to create a new command, fix an existing command's structure, or improve an already-working command?"

### Step 2: Load Appropriate Workflow

Based on intent determined in Step 1:

**IF creating new command:**
READ `workflows/new.md`

**IF fixing structure:**
READ `workflows/migrate.md`

**IF improving existing:**
READ `workflows/improve.md`

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
- If command needs migration AND improvement, run migration first, then improve

**Quality gates:**
- Always run validation after structural changes
- Show work incrementally
- Get user feedback before major changes

**Collaboration:**
- Be conversational, not interrogative
- Show examples and options
- Iterate based on feedback
