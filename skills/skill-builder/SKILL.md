---
name: skill-builder
description: Build and improve skills through conversational discovery. Use when creating new skills or enhancing existing ones. Handles workflow skills, tool integrations, domain knowledge, templates, and reference skills with type-specific guidance.
---

# Skill Builder

Build effective skills through conversational discovery and type-aware workflows.

## Overview

Skills extend capabilities through specialized knowledge, workflows, and tool integrations. This skill guides creation and improvement through discovery conversations that determine skill type and structure.

**Skill types supported:**
- **Workflow skills** - Multi-step procedures requiring execution patterns
- **Tool integration skills** - Format/API handlers with scripts
- **Domain knowledge skills** - Schemas and business logic with references
- **Template skills** - Standard output with assets/boilerplate
- **Reference skills** - Passive documentation and policies

## Workflow

Copy to track progress:
```
- [ ] Step 1: Determine intent (new or improve)
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow steps
```

## Execute ALL steps in sequence

### Step 1: Determine Intent

**REQUIRED ACTIONS:**

1. ASK user: "Are you creating a new skill or improving an existing one?"

2. RECORD response:
   - **New skill** → Proceed to Step 2a
   - **Improve existing** → Proceed to Step 2b

**STOP before Step 2.**

### Step 2a: Route to New Skill Workflow

**IF creating new skill:**

1. READ `workflows/new.md`

2. FOLLOW workflow exactly as written

The new skill workflow will:
- Discover skill purpose through examples
- Determine skill type (workflow/tool/domain/template/reference)
- Check momentum integration needs
- Build type-appropriate structure
- Create SKILL.md and bundled resources

**Workflow handles complete skill creation.**

### Step 2b: Route to Improve Workflow

**IF improving existing skill:**

1. READ `workflows/improve.md`

2. FOLLOW workflow exactly as written

The improve workflow will:
- Analyze current skill structure
- Identify improvement opportunities
- Apply execution language if workflow skill
- Optimize for token efficiency
- Enhance clarity and effectiveness

**Workflow handles complete skill improvement.**

## Supporting References

Available references loaded on-demand during workflows:

- `references/skill-types.md` - Characteristics of each skill type
- `references/skill-structure.md` - Anatomy, progressive disclosure, best practices
- `references/momentum-integration.md` - When/how to add momentum patterns

Workflows will READ these as needed for specific guidance.

## When to Use This Skill

Use skill-builder when user wants to:
- Create a new skill for specific capability
- Improve or optimize existing skill
- Add momentum integration to skill
- Understand skill structure and patterns
- Refactor skill for better organization

**Trigger phrases:**
- "create a skill for..."
- "build a skill that..."
- "improve this skill"
- "make this skill better"
- "add momentum support to skill"
