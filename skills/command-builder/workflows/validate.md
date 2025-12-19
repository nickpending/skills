# Validate Command

Check if a command follows the canonical structure.

## Step 1: Load Structure Requirements

Use command-foundations structure requirements.

## Step 2: Read Target Command

READ the command file.

## Step 3: Validate Frontmatter

CHECK:
- [ ] Has `description` field
- [ ] If `model` used: is haiku|sonnet|opus
- [ ] If `allowed-tools` used: valid tool syntax
- [ ] If `argument-hint` used: clear format

## Step 4: Validate Body

Use command-foundations archetype patterns.

IDENTIFY which archetype the command matches, then CHECK body follows that pattern.

## Step 5: Validate Preprocessing

CHECK any preprocessing syntax:
- [ ] `!`\`command\` syntax correct
- [ ] `@path` references exist
- [ ] `$ARGUMENTS` / `$1` used appropriately

## Step 6: Report

**COMPLIANT** if all checks pass.

**NON-COMPLIANT** if any check fails:
- LIST specific failures
- SUGGEST fixes
- ASK if user wants automated fixes
