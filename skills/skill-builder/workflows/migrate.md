# Migrate Skill

Fix structural issues and bring skills into compliance with current patterns.

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
3. Content third (internal references)
4. Examples section
5. Validation last

**For each fix:**
- Make the change
- Show what changed
- Verify no breakage

## Step 5: Validate

```
Required:
- [ ] SKILL.md exists at root
- [ ] Frontmatter has `name` field (kebab-case)
- [ ] Frontmatter has `description` field
- [ ] Description includes USE WHEN with intent-based triggers
- [ ] Examples section with 2-3 patterns

Optional but recommended:
- [ ] workflows/ contains valid .md files (if used)
- [ ] tools/ directory exists (even if empty)
- [ ] No orphaned files
```

## Step 6: Test

Verify trigger scenario works - describe a situation that should invoke the skill.

## Migration Checklist

- [ ] All structural issues identified
- [ ] User approved migration plan
- [ ] Changes made incrementally
- [ ] Validation passes
- [ ] Skill triggers correctly
- [ ] No functionality lost
