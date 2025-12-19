# Improve Command

Enhance an existing command that already works.

## Prerequisites

- Command exists and functions correctly
- User wants enhancement, not structural fixes (use migrate.md for that)

## Step 1: Load Current State

1. **READ the command** - full content
2. **Note current size** - lines, token estimate

## Step 2: Understand Goals

**ASK user what they want to improve:**

| Goal | Approach |
|------|----------|
| Reduce tokens | Tighten language, remove redundancy |
| Add capability | Extend without bloating |
| Improve clarity | Restructure, better flow |
| Better context | Add preprocessing (`!`, `@`) |
| Fix edge cases | Add handling without over-engineering |

**Get specific.** "Make it better" isn't actionable.

## Step 3: Analyze Current State

**Review for:**
- Redundant instructions (same thing said multiple ways)
- Overly verbose sections
- Missing context injection opportunities
- Unused or vestigial content
- Opportunities to use preprocessing (`!`, `@`, `$ARGUMENTS`)

**Present findings** before making changes.

## Step 4: Propose Changes

**Show user:**
1. What you'll change and why
2. Expected token reduction (if applicable)
3. Any trade-offs

**Get confirmation** before editing.

## Step 5: Implement

**Make changes incrementally:**
1. Edit one section at a time
2. Show diff or summary after each change
3. Verify nothing broke

**Preserve functionality:**
- Never silently delete working content
- If removing something, explain why

## Step 6: Validate

- Frontmatter valid
- Preprocessing syntax correct
- Tool restrictions still appropriate

## Step 7: Compare

**Show before/after:**
- Line count change
- Key improvements
- Anything removed and why

## Quality Checklist

- [ ] Core functionality preserved
- [ ] No silent deletions
- [ ] Token count reduced (if that was the goal)
- [ ] Clarity improved
- [ ] User approved changes
