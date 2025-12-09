# Improve Artifact

Enhance an existing skill or command that already works.

## Prerequisites

- Artifact exists and functions correctly
- User wants enhancement, not structural fixes (use migrate.md for that)

## Step 1: Load Current State

1. **READ the artifact** - full content
2. **Identify type:** Skill (SKILL.md + directory) or Command (single .md)
3. **Note current size** - lines, token estimate

## Step 2: Understand Goals

**ASK user what they want to improve:**

| Goal | Approach |
|------|----------|
| Reduce tokens | Tighten language, remove redundancy |
| Add capability | Extend without bloating |
| Improve clarity | Restructure, better examples |
| Better triggers | Refine description keywords |
| Fix edge cases | Add handling without over-engineering |

**Get specific.** "Make it better" isn't actionable.

## Step 3: Analyze Current State

**Review for:**
- Redundant instructions (same thing said multiple ways)
- Overly verbose sections
- Missing trigger keywords in description
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
- Offer to keep removed content as reference

## Step 6: Validate

### For Skills
- Description still has trigger keywords
- Frontmatter intact
- Referenced files still exist
- No broken internal links

### For Commands
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
