# Improve Command

Enhance an existing command that already works.

## Prerequisites

- Command exists and functions correctly
- User wants enhancement, not structural fixes (use migrate.md for that)

## Step 1: Load Current State

1. **READ the command** - full content
2. **Note current size** - lines, token estimate
3. **Identify archetype** - minimal, priming, workflow, or orchestration

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

## Step 3: Analyze Against Foundations

Use foundations to ground analysis, not generic intuition.

**From command-foundations:**

1. Check against structure.md:
   - Length within guidelines?
   - Frontmatter fields appropriate?
   - Preprocessing opportunities (`!`, `@`, `$ARGUMENTS`)?

2. Check against archetypes.md:
   - Matches expected characteristics for identified archetype?
   - Body follows archetype pattern?

**From prompt-foundations:**

3. Apply token efficiency patterns from writing-patterns.md

4. Check for anti-patterns from principles.md

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

Follow `workflows/validate.md` to check the improved command.

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
