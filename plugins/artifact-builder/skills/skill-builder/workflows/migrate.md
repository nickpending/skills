# Migrate Skill

Fix structural issues and bring skills into compliance with current patterns.

Create a task for each step before starting:
1. TaskCreate for each Step below
2. Mark each complete as you finish it
3. Do not skip steps

## When to Use

- Validation errors (missing frontmatter, wrong structure)
- Old format that needs updating
- Non-compliant patterns that should be standardized
- Broken skills that won't trigger

## Step 1: Load and Assess

1. **READ the skill** - SKILL.md and directory contents
2. **Identify issues:**

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing frontmatter | No `---` block | Add name + description |
| Bad description | Doesn't trigger | Add USE WHEN keywords |
| Wrong structure | Files in wrong places | Reorganize to standard layout |
| Broken references | Links to missing files | Fix or remove references |
| No Examples | Missing usage patterns | Add 2-3 concrete examples |
| Missing allowed-tools | Skill can run any command | Add archetype-appropriate restriction |
| Missing argument-hint | No autocomplete guidance | Add hint per archetype |
| Stale archetype | Follows outdated pattern | Migrate to current archetype from foundations |
| Missing feature recipe | Doesn't use recommended features | Apply recipe from decisions.md |

## Step 2: Report Issues

**Present findings clearly:**
```
Migration Assessment:
- [x] Missing description in frontmatter
- [x] No trigger keywords
- [ ] Overly complex structure for functionality
- [x] Core logic is sound
```

## Step 3: Plan Migration

**Propose changes:**
1. List each fix needed
2. Explain what will change
3. Note any content that might be lost
4. Get user confirmation

## Step 4: Execute Migration

**Fix in order:**
1. Structure first (directory layout, file locations)
2. Frontmatter second (required fields)
3. Features third (allowed-tools, argument-hint, hooks per archetype recipe)
4. Content fourth (internal references, ${CLAUDE_SKILL_DIR} paths)
5. Examples section
6. Validation last

**For each fix:**
- Make the change
- Show what changed
- Verify no breakage

## Step 5: Validate

Follow `workflows/validate.md` to check the migrated skill.

## Step 6: Test

Verify trigger scenario works - describe a situation that should invoke the skill.

## Migration Checklist

- [ ] All structural and feature issues identified
- [ ] User approved migration plan
- [ ] Changes made incrementally
- [ ] Feature recipe applied per archetype
- [ ] Validation passes
- [ ] Skill triggers correctly
- [ ] No functionality lost
