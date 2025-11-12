# Migrate Skill to New Format

Convert existing skills to structural standard while preserving all functionality.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

**Migration preserves:**
- All skill logic and workflows
- Reference files and scripts
- Examples and templates
- Error handling patterns

**Migration removes:**
- Decorative emojis
- Outdated patterns

**Migration adds:**
- Valid YAML frontmatter (if missing)
- Execution language (if workflow skill)
- Progressive disclosure (if needed)
- Tool restrictions (if appropriate)

## Step 1: Read and Analyze

**REQUIRED ACTIONS:**

1. READ the existing SKILL.md file completely

2. IDENTIFY these elements:
   - Skill type (workflow/tool/domain/template/reference)
   - Current frontmatter (present/missing/invalid)
   - Execution language usage (CAPS commands like READ, WRITE)
   - File structure (single file vs bundled resources)
   - Tool restrictions (allowed-tools present/missing)

3. CREATE analysis summary:
   ```
   Skill: [name]
   Type: [workflow/tool/domain/template/reference]
   Frontmatter: [valid/missing/invalid]
   Execution language: [present/missing]
   Structure: [flat/bundled]
   Tool restrictions: [present/missing]
   ```

4. SHOW summary to user

**STOP before Step 2.**

## Step 2: Fix Frontmatter

**REQUIRED ACTIONS:**

1. CHECK existing frontmatter

2. **IF missing or invalid:**
   - CREATE valid YAML frontmatter:
     ```yaml
     ---
     name: [Gerund form, based on skill purpose]
     description: [What it does]. Use when [triggers and keywords].
     ---
     ```
   - ENSURE description includes:
     - What the skill does (third person)
     - When to use it (trigger contexts)
     - Key terms for discovery

3. **IF adding tool restrictions:**
   - DETERMINE if skill should be read-only or limited
   - ADD `allowed-tools: Read, Grep, Glob` if appropriate

4. SHOW proposed frontmatter to user for approval

**STOP before Step 3.**

## Step 3: Apply Execution Language (Workflow Skills Only)

**REQUIRED ACTIONS:**

1. **IF skill type is workflow:**

   a. READ `references/tool-selection.md` for execution patterns

   b. READ `references/writing-fundamentals.md` for language patterns

   c. IDENTIFY workflow steps that need execution language

   d. APPLY CAPS commands:
      - READ for file loading
      - WRITE for file creation
      - ASK for user questions
      - RUN for script execution
      - STOP for checkpoint gates

   e. ADD STOP checkpoints between major phases

2. **IF skill type is NOT workflow:**
   - SKIP execution language changes
   - Preserve existing instructional style

3. EXPLAIN changes made (or skipped)

**STOP before Step 4.**

## Step 4: Progressive Disclosure Check

**REQUIRED ACTIONS:**

1. CHECK if SKILL.md is >500 lines

2. **IF too large:**
   - IDENTIFY sections that could move to reference files
   - SUGGEST structure:
     ```
     skill-name/
     ├── SKILL.md (workflow and navigation)
     ├── references/
     │   ├── domain1.md
     │   └── domain2.md
     ```
   - GET user approval for split

3. **IF appropriate size:**
   - SKIP restructuring

4. EXPLAIN decision

**STOP before Step 5.**

## Step 5: Produce Migrated Skill

**REQUIRED ACTIONS:**

1. CREATE complete migrated SKILL.md with:
   - Valid YAML frontmatter
   - Execution language (if workflow skill)
   - Proper structure
   - All preserved functionality

2. **IF progressive disclosure needed:**
   - CREATE reference files
   - UPDATE SKILL.md navigation

3. SHOW complete output to user

4. EXPLAIN all changes made

**VERIFICATION:**
User reviews and approves before writing files.

## Step 6: Write Files

**REQUIRED ACTIONS:**

1. WAIT for user approval

2. **IF approved:**
   - WRITE migrated SKILL.md
   - WRITE any new reference files
   - PRESERVE existing scripts/assets

3. CONFIRM completion

**VERIFICATION:**
Files written only after explicit approval.
