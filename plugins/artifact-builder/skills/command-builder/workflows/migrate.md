# Migrate Command

Fix structural issues and bring commands into compliance with current patterns.

## When to Use

- Missing frontmatter
- Invalid preprocessing syntax
- Wrong location
- Broken commands that won't execute

## Step 1: Load and Assess

1. **READ the command** - full content
2. **Identify issues:**

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing frontmatter | No `---` block | Add description |
| Invalid model | Full version string | Use haiku/sonnet/opus |
| Broken preprocessing | `!` or `@` not working | Fix syntax |
| Wrong location | Not in commands/ | Move to correct path |
| No description | Command not listed in /help | Add frontmatter |

## Step 2: Report Issues

**Present findings clearly:**
```
Migration Assessment:
- [x] Missing description in frontmatter
- [ ] Preprocessing syntax correct
- [x] Core logic is sound
```

## Step 3: Plan Migration

**Propose changes:**
1. List each fix needed
2. Explain what will change
3. Get user confirmation

## Step 4: Execute Migration

**Fix in order:**
1. Location first (move to correct path)
2. Frontmatter second (required fields)
3. Content third (preprocessing syntax)
4. Validation last

**For each fix:**
- Make the change
- Show what changed
- Verify no breakage

## Step 5: Validate

Follow `workflows/validate.md` to check the migrated command.

## Step 6: Test

Invoke the command and verify execution.

## Migration Checklist

- [ ] All structural issues identified
- [ ] User approved migration plan
- [ ] Changes made incrementally
- [ ] Validation passes
- [ ] Command executes correctly
- [ ] No functionality lost
