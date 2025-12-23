# Validate Command

Check if a command follows the canonical structure.

## Step 1: Read Target Command

READ the command file.

## Step 2: Check Structure

Validate against command-foundations structure requirements.

## Step 3: Check Body Pattern

Validate against command-foundations archetype patterns.

## Step 4: Check Prompt Quality

Validate against prompt-foundations principles checklist with command-specific context:
- Roles only for complex orchestration commands
- Simple commands don't establish identity

## Step 5: Report

**COMPLIANT** if all checks pass.

**NON-COMPLIANT** if any check fails:
- LIST specific failures with location
- SUGGEST fixes
- ASK if user wants automated fixes
