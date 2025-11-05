---
name: slash-builder
description: Build, migrate, and optimize Claude Code slash commands. Use when user needs to create new commands from scratch, convert old command formats to current standards, fix structural validation issues, or improve existing commands for clarity and token efficiency. Handles momentum workflow commands and generic slash commands.
---

# Slash Builder

Build and improve Claude Code slash commands through conversational workflows.

## Intent Router

This skill provides three specialized workflows. Determine user intent and load the appropriate workflow.

### When User Wants to Create New Command

**Trigger phrases:**
- "Create a new command"
- "Build a slash command for..."
- "I need a command that..."
- "Help me create..."

**Action:** Load `workflows/new.md` and follow its conversational building process.

**Approach:** Collaborative command building through discussion, examples, and iteration.

### When User Wants to Migrate/Fix Structure

**Trigger phrases:**
- "Update this command to new format"
- "Fix the structure of..."
- "Migrate command to..."
- "This command doesn't pass validation"
- "Convert old format to new"

**Action:** Load `workflows/migrate.md` and follow its structural migration process.

**Approach:** Fix format issues while preserving all logic. Detect conflicts, offer options, never silently delete.

### When User Wants to Improve Existing Command

**Trigger phrases:**
- "Improve this command"
- "Make this clearer"
- "Reduce tokens in..."
- "Tighten up this command"
- "Refactor for clarity"

**Action:** Load `workflows/improve.md` and follow its optimization process.

**Approach:** Enhance clarity and token efficiency using prompt engineering patterns.

## Routing Logic

**Step 1: Determine Intent**

Ask clarifying question if ambiguous:
- "Are you looking to create a new command, fix an existing command's structure, or improve an already-working command?"

**Step 2: Load Appropriate Workflow**

Based on intent:
- **New** → Read and execute `workflows/new.md`
- **Migrate** → Read and execute `workflows/migrate.md`
- **Improve** → Read and execute `workflows/improve.md`

**Step 3: Follow Workflow Instructions**

Each workflow file contains complete, detailed instructions for that specific scenario. Follow the workflow exactly as written.

## Resources Available

**Templates** (`references/`):
- `momentum-simple.md` - Linear step-by-step commands
- `momentum-complex.md` - Multi-phase commands with checkpoints
- `generic.md` - Framework-agnostic commands
- `command-writing-guide.md` - Comprehensive patterns and best practices
- `prompt-patterns.md` - Token efficiency techniques

**Scripts** (`scripts/`):
- `validate_command.py` - Structure validation

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

## Important Notes

- Each workflow handles its scenario completely - don't mix approaches
- If command needs migration AND improvement, do migration first
- Always validate after changes
- Show work incrementally, get feedback often
- Reference guides but don't duplicate them in commands
