# Create New Skill

Build skills through conversational discovery, determining type and structure based on actual use cases.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow builds skills conversationally through discovery and iteration. Each step builds context for the next. Do not skip ahead or produce the final skill without completing all discovery steps.

**This is a conversation, not a form.** Build together through questions, examples, and feedback.

## Step 1: Understand with Examples

**REQUIRED ACTIONS:**

1. ASK user: "What capability do you want the skill to provide? Can you give examples of how you'd use it?"

2. LISTEN for and RECORD:
   - Core capability being added
   - Concrete usage examples
   - Trigger phrases or contexts
   - What success looks like

3. **IF examples are vague:**
   - ASK clarifying questions:
     - "When would you ask for this?"
     - "What would be different after using it?"
     - "Can you walk through a specific scenario?"
   - CONTINUE until clear concrete examples

4. SUMMARIZE understanding:
   ```
   You need a skill that [capability]

   Usage examples:
   - "[example 1]"
   - "[example 2]"
   - "[example 3]"

   Success means [outcome]
   ```

5. CONFIRM with user: "Did I capture this correctly?"

**VERIFICATION:**
Clear understanding of capability with 2-3 concrete usage examples.

**STOP before Step 2.**

## Step 2: Determine Skill Type

**REQUIRED ACTIONS:**

1. ANALYZE examples from Step 1 against skill types

2. **CHECK each type:**

   **Workflow skill indicators:**
   - Multi-step procedures with decisions
   - User interaction and approval gates
   - Sequential phases with checkpoints
   - Example: "Guide me through setting up X"

   **Tool integration indicators:**
   - Specific file format handling
   - Repeated deterministic operations
   - API or external system interaction
   - Example: "Rotate this PDF" or "Query this API"

   **Domain knowledge indicators:**
   - Schema or system documentation
   - Business rules and policies
   - Reference material needed during work
   - Example: "What's the schema for X table?"

   **Template indicators:**
   - Standard output generation
   - Boilerplate or project structures
   - Consistent formatting needs
   - Example: "Generate a React app" or "Create proposal doc"

   **Reference indicators:**
   - Pure documentation
   - Static information lookup
   - No procedures, just knowledge
   - Example: "What's our NDA policy?"

3. PROPOSE type with reasoning:
   ```
   Based on examples, this appears to be a [type] skill because:
   - [reason 1 from analysis]
   - [reason 2 from analysis]

   This means the skill will be [characteristic]-heavy with [structure].

   Does this match your vision?
   ```

4. ASK for confirmation

5. **IF user disagrees:**
   - ASK what they see differently
   - ADJUST type determination
   - RE-EXPLAIN reasoning
   - WAIT for agreement

6. **IF user agrees:**
   - RECORD skill type
   - READ `references/skill-types.md` for type-specific guidance
   - Proceed to Step 3

**VERIFICATION:**
Skill type determined and confirmed with user.

**STOP before Step 3.**

## Step 3: Check Momentum Integration

**REQUIRED ACTIONS:**

1. ASK: "Will this skill integrate with the momentum workflow system, or is it general-purpose?"

2. WAIT for answer

3. **IF momentum integration chosen:**
   - ASK: "Does this skill need to check which mode it's running in? (project vs assistant)"
   - IF yes: ASK "Which mode(s) should it require?"
   - RECORD mode requirements (if any)
   - READ `references/momentum-integration.md` for patterns
   - NOTE: Will need allowed-tools, paths, and mode checks (if mode-specific)
   - NOTE: Will ask for momentum project location in Step 5

4. **IF general-purpose chosen:**
   - RECORD: No momentum integration
   - SKIP momentum-specific elements

**VERIFICATION:**
Integration needs determined and relevant guidance loaded.

**STOP before Step 4.**

## Step 4: Plan Bundled Resources

**REQUIRED ACTIONS:**

1. ANALYZE examples from Step 1 to identify reusable resources

2. **FOR workflow skills:**
   - IDENTIFY distinct workflows needed
   - DETERMINE if execution language required (YES for workflows)
   - PLAN `workflows/` directory structure
   - CONSIDER `references/` for supporting patterns

3. **FOR tool integration skills:**
   - IDENTIFY repeated operations needing scripts
   - DETERMINE script inputs/outputs
   - PLAN `scripts/` directory with script names
   - CONSIDER `references/` for API docs or specs

4. **FOR domain knowledge skills:**
   - IDENTIFY documentation needed
   - DETERMINE how to organize (by topic, by system)
   - PLAN `references/` directory structure
   - CONSIDER grep patterns for large files

5. **FOR template skills:**
   - IDENTIFY templates and boilerplate needed
   - DETERMINE asset organization
   - PLAN `assets/` directory structure
   - CONSIDER `references/` for usage guides

6. **FOR reference skills:**
   - IDENTIFY documentation to include
   - DETERMINE organization structure
   - PLAN `references/` directory only
   - CONSIDER navigation aids

7. CREATE resource plan:
   ```
   Skill: [name]
   Type: [type]

   Directory structure:
   skill-name/
   ├── SKILL.md ([router/direct] pattern)
   └── [primary-resource-dir]/
       ├── [file-1]
       └── [file-2]

   Key resources needed:
   - [resource 1]: [purpose]
   - [resource 2]: [purpose]
   ```

8. SHOW plan to user

9. ASK: "Does this resource structure make sense? Anything missing?"

10. WAIT for feedback and adjust if needed

**VERIFICATION:**
Resource plan complete and approved by user.

**STOP before Step 5.**

## Step 5: Create Directory Structure

**REQUIRED ACTIONS:**

1. DETERMINE creation path based on Step 3:

   **IF momentum integration:**
   - ASK: "Where is your momentum project located? (Path to momentum directory)"
   - WAIT for momentum project path
   - SET path: `{momentum-path}/skills/skill-name/`
   - INFORM user: "Creating momentum skill at: {momentum-path}/skills/skill-name/"
   - NOTE: "Skill will be distributed via momentum installer from this location"

   **IF general-purpose:**
   - ASK: "Where should I create the skill?"
   - SUGGEST: `./skills/skill-name/` or `~/.claude/skills/skill-name/`
   - WAIT for path confirmation
   - SET path from user input

2. CREATE skill directory:
   ```bash
   mkdir -p [path]
   ```

3. CREATE subdirectories based on Step 4 plan:
   ```bash
   mkdir -p [path]/workflows  # if workflow skill
   mkdir -p [path]/scripts    # if tool skill
   mkdir -p [path]/references # if has references
   mkdir -p [path]/assets     # if template skill
   ```

4. CONFIRM structure created:
   ```
   Skill directory created at: [path]

   Structure:
   skill-name/
   ├── (subdirectories based on type)
   ```

**VERIFICATION:**
Directory structure exists at correct location and matches plan.

**STOP before Step 6.**

## Step 6: Build SKILL.md

**REQUIRED ACTIONS:**

1. DRAFT frontmatter:
   ```yaml
   ---
   name: skill-name
   description: [Concise what + when, from Steps 1-2]
   allowed-tools: [if momentum: Read, Write, Bash, etc.]
   ---
   ```

2. DRAFT Overview section:
   ```markdown
   # Skill Name

   ## Overview

   [Brief purpose - 2-3 sentences from Step 1]

   [If momentum: ## Available Paths section]
   [If momentum + mode-specific: ## Mode Requirement section]
   ```

3. **IF workflow skill (router pattern):**
   - DRAFT workflow checklist
   - DRAFT router steps with explicit READ commands
   - KEEP under 200 lines
   - REFERENCE execution patterns from WORKFLOW-EXECUTION-SPEC

4. **IF tool skill:**
   - DRAFT script catalog with usage examples
   - DRAFT operation guide
   - KEEP direct and imperative
   - NO execution language needed

5. **IF domain skill:**
   - DRAFT reference map (what's in which file)
   - DRAFT when to load which reference
   - ADD grep patterns if files will be large
   - KEEP navigation clear

6. **IF template skill:**
   - DRAFT asset catalog
   - DRAFT customization guide
   - EXPLAIN template usage
   - KEEP practical

7. **IF reference skill:**
   - DRAFT documentation organization
   - DRAFT navigation hints
   - EXPLAIN content structure
   - KEEP simple

8. SHOW drafted SKILL.md to user

9. ASK: "Does this capture the skill correctly? What needs adjustment?"

10. WAIT for feedback and iterate

**VERIFICATION:**
SKILL.md drafted, reviewed, and approved.

**STOP before Step 7.**

## Step 7: Create Bundled Resources

**REQUIRED ACTIONS:**

1. **FOR each resource identified in Step 4:**

   **Process per resource:**
   - EXPLAIN what resource will contain
   - **IF workflow file:**
     - APPLY execution language patterns
     - ADD Execution Requirements framing
     - USE CAPS tool names
     - ADD STOP points
     - ADD VERIFICATION sections
     - TARGET 200-300 lines
   - **IF script:**
     - DISCUSS inputs/outputs
     - WRITE functional code
     - ADD docstring with usage
     - INCLUDE error handling
   - **IF reference:**
     - ORGANIZE by topic
     - ADD clear section headers
     - TARGET 200-300 lines per file
   - **IF asset:**
     - CREATE or REQUEST from user
     - ORGANIZE by purpose

   - SHOW drafted resource
   - ASK for feedback
   - ITERATE until approved
   - WRITE resource file

2. VERIFY all planned resources created

**VERIFICATION:**
All bundled resources created and working.

**STOP before Step 8.**

## Step 8: Final Review

**REQUIRED ACTIONS:**

1. LIST all created files:
   ```bash
   find skill-name -type f | grep -v ".git"
   ```

2. SHOW structure to user

3. CREATE summary:
   ```
   Skill created: [name]
   Type: [type]
   Integration: [momentum/general]

   Files created:
   - SKILL.md ([X] lines)
   - [list other files with line counts]

   The skill is ready to:
   [list key capabilities from Step 1]

   Next steps:
   - Test the skill with actual use cases
   - Iterate based on performance
   [If momentum skill:]
   - Skill is in momentum/skills/ and will be distributed via momentum installer
   [If general skill:]
   - Install skill: Copy to ~/.claude/skills/ or use from current location
   ```

4. SHOW summary

5. ASK: "Would you like to test it now or make any adjustments?"

**Skill creation complete.**

## Key Principles

**Be conversational:**
- Ask open questions about actual usage
- Show examples to clarify
- Discuss trade-offs
- Build together through iteration

**Be type-aware:**
- Different types need different structures
- Workflow skills need execution language
- Tool skills need scripts
- Domain skills need references
- Template skills need assets
- Match structure to purpose

**Be iterative:**
- Draft, show, get feedback, adjust
- Don't create everything at once
- Confirm direction before building
- Iterate until it feels right

**Be practical:**
- Focus on real use cases from Step 1
- Build what's needed, no more
- Test early and often
- Keep files focused and appropriately sized
