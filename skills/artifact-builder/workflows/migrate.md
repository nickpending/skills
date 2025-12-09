# Migrate Artifact

Fix structural issues and bring artifacts into compliance with current patterns.

## When to Use

- Validation errors (missing frontmatter, wrong structure)
- Old format that needs updating
- Non-compliant patterns that should be standardized
- Broken artifacts that won't trigger or execute

## Step 1: Load and Assess

1. **READ the artifact** - full content
2. **Identify issues:**

### Skill Issues
| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing frontmatter | No `---` block | Add name + description |
| Bad description | Doesn't trigger | Add USE WHEN keywords |
| Wrong structure | Files in wrong places | Reorganize to standard layout |
| Broken references | Links to missing files | Fix or remove references |

### Command Issues
| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing frontmatter | No description | Add `---` block with description |
| Invalid model | Full version string | Use haiku/sonnet/opus/inherit |
| Broken preprocessing | `!` or `@` not working | Fix syntax |
| Wrong location | Not in commands/ | Move to correct path |

## Step 2: Report Issues

**Present findings clearly:**
```
Migration Assessment:
- ❌ Missing description in frontmatter
- ❌ No trigger keywords
- ⚠️ Overly complex structure for functionality
- ✅ Core logic is sound
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
3. Content third (internal references, syntax)
4. Validation last

**For each fix:**
- Make the change
- Show what changed
- Verify no breakage

## Step 5: Validate

### Skill Validation
```
Required:
- [ ] SKILL.md exists at root
- [ ] Frontmatter has `name` field
- [ ] Frontmatter has `description` field
- [ ] Description includes trigger keywords

Optional but recommended:
- [ ] workflows/ contains valid .md files (if used)
- [ ] references/ contains valid .md files (if used)
- [ ] No orphaned files
```

### Command Validation
```
Required:
- [ ] Frontmatter has `description` field
- [ ] File is in correct commands/ location

If using optional fields:
- [ ] `model` is haiku|sonnet|opus|inherit
- [ ] `allowed-tools` uses valid tool syntax
- [ ] `argument-hint` format is clear
```

## Step 6: Test

**For skills:** Verify trigger scenario works.

**For commands:** Invoke and verify execution.

## Migration Checklist

- [ ] All structural issues identified
- [ ] User approved migration plan
- [ ] Changes made incrementally
- [ ] Validation passes
- [ ] Artifact triggers/executes correctly
- [ ] No functionality lost
