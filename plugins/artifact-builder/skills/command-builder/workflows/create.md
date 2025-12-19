# Create Command

Build a new slash command from scratch.

## Step 1: Understand Requirements

**Discuss with user:**
1. What should it do? (core purpose)
2. When would they invoke it?
3. What tools/capabilities needed?
4. Any existing patterns to follow?

**Don't interrogate** - have a conversation. Offer examples from exemplars.

## Step 2: Select Archetype

Use command-foundations to get:
- Decision tree for picking pattern
- Relevant exemplar for chosen archetype

Let the user pick from: Minimal, Priming, Workflow, Orchestration.

## Step 3: Build the Command

1. **Create file** at appropriate location:
   - User command: `~/.claude/commands/<command-name>.md`
   - Project command: `.claude/commands/<command-name>.md`

2. Use command-foundations for structure and body pattern based on chosen archetype

3. **Write command** following structure from command-foundations:
   - Frontmatter: `description` (required), optional `allowed-tools`, `model`, `argument-hint`
   - Body: per archetype pattern

4. **Use preprocessing syntax as needed:**
   - `!`\`command\` - Execute bash, inject output
   - `@path/to/file` - Include file contents
   - `$ARGUMENTS` or `$1`, `$2` - Access arguments

## Step 4: Validate

Use command-foundations structure requirements to validate:
- [ ] Frontmatter has `description`
- [ ] Preprocessing syntax is correct
- [ ] Has clear task/workflow section
- [ ] Tool restrictions appropriate (if using `allowed-tools`)

## Step 5: Test

Have user invoke it with `/command-name` and verify behavior.

## Quality Checklist

- [ ] Description is clear and concise
- [ ] Minimal tokens for the job (not over-engineered)
- [ ] Follows established patterns from exemplars
- [ ] Clear structure and flow
- [ ] No placeholder content
