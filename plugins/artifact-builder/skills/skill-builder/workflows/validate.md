# Validate Skill

Check if a skill follows canonical structure and uses recommended features.

## Step 1: Read Target Skill

READ the skill's SKILL.md and directory contents.

## Step 2: Check Structure

Validate against skill-foundations structure.md:
- Required frontmatter fields present (`name`, `description`)
- `description` includes USE WHEN or trigger phrases
- Length within archetype guidelines (main-thread vs forked)
- Directory structure matches archetype pattern

## Step 3: Check Body Pattern

Validate against skill-foundations archetypes.md:
- Matches expected characteristics for identified archetype
- Body follows archetype template
- Examples section present with 2-3 concrete usage patterns
- Code blocks use actual commands, not pseudocode

## Step 4: Check Feature Conformance

Validate against skill-foundations decisions.md feature recipes:
- Frontmatter matches archetype recipe (Feature Combinations table)
- `allowed-tools` set for CLI wrappers and forked skills
- `argument-hint` set for user-invocable skills with expected input format
- Forked skills have `context: fork`, appropriate `model`, `user-invocable: false`
- Supporting file references use `${CLAUDE_SKILL_DIR}`
- `$0` dispatch used for workflow routers with action keywords
- `ultrathink` considered for analysis/exploration skills

## Step 5: Check Prompt Quality

Validate against prompt-foundations principles checklist with skill-specific context:
- Roles are rarely needed — skills inject procedures/knowledge, not identity
- Skills load into existing context with established identity

## Step 6: Report

**COMPLIANT** if all checks pass.

**NON-COMPLIANT** if any check fails:
- LIST specific failures with location and category (structure / body / feature / prompt)
- SUGGEST fixes with specific frontmatter or content changes
- ASK if user wants automated fixes
