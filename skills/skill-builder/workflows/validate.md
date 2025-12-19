# Validate Skill

Check if a skill follows the canonical structure.

## Step 1: Load Structure Requirements

Use skill-foundations structure requirements.

## Step 2: Read Target Skill

READ the skill's SKILL.md file.

## Step 3: Validate Frontmatter

CHECK:
- [ ] Has `name` field (kebab-case)
- [ ] Has `description` field (single line)
- [ ] Description includes `USE WHEN` clause
- [ ] Description under 1024 characters

## Step 4: Validate Body

Use skill-foundations archetype patterns.

IDENTIFY which archetype the skill matches, then CHECK body follows that pattern.

## Step 5: Validate Structure

CHECK:
- [ ] SKILL.md exists
- [ ] Examples section with 2-3 usage patterns
- [ ] Any referenced workflows/ files exist
- [ ] Any referenced tools/ files exist

## Step 6: Report

**COMPLIANT** if all checks pass.

**NON-COMPLIANT** if any check fails:
- LIST specific failures
- SUGGEST fixes
- ASK if user wants automated fixes
