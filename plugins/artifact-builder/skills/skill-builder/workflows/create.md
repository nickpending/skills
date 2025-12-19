# Create Skill

Build a new skill from scratch.

## Step 1: Understand Requirements

**Discuss with user:**
1. What should it do? (core purpose)
2. What triggers it? (keywords, intents)
3. What tools/capabilities needed?
4. Any existing patterns to follow?

**Don't interrogate** - have a conversation. Offer examples from exemplars.

## Step 2: Select Archetype

Use skill-foundations to get:
- Decision tree for picking pattern
- Relevant exemplar for chosen archetype

Let the user pick from: CLI wrapper, Workflow router, Knowledge injection, Foundations.

## Step 3: Check Foundation Skills

**Before creating reference content, check if a `*-foundations` skill already provides it.**

**IF a foundation provides what you need:**

1. **INVOKE** it in SKILL.md
2. **Use intent-based references** in workflows ("Use X guidance from Y-foundations")
3. **Do NOT** hardcode paths or duplicate foundation content

## Step 4: Build the Skill

1. **Create directory** under appropriate location:
   - Plugin skill: `skills/<skill-name>/`
   - User skill: `~/.claude/skills/<skill-name>/`
   - Project skill: `.claude/skills/<skill-name>/`

2. Use skill-foundations for structure and body pattern based on chosen archetype

3. **Write SKILL.md** following structure from skill-foundations:
   - Frontmatter: `name`, `description` with `USE WHEN`
   - Body: per archetype pattern

4. **Add workflows/, tools/** as needed for the archetype

5. **Add Examples section** - 2-3 concrete usage patterns (improves tool selection accuracy)

## Step 5: Validate

Use skill-foundations structure requirements to validate:
- [ ] Frontmatter has `name` (kebab-case) and `description`
- [ ] Description includes `USE WHEN` clause with intent-based triggers
- [ ] Body matches chosen archetype pattern
- [ ] Examples section exists with 2-3 patterns
- [ ] Any referenced files exist

## Step 6: Test

Ask user to describe a scenario that should trigger it. Verify the skill activates correctly.

## Quality Checklist

- [ ] Description is specific with intent-based triggers
- [ ] Minimal tokens for the job (not over-engineered)
- [ ] Follows established patterns from exemplars
- [ ] Clear structure and flow
- [ ] No placeholder content
