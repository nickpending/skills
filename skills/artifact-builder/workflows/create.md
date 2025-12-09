# Create Artifact

Build a new skill or slash command from scratch.

## Step 1: Determine Type

**From user's request, identify artifact type:**

| Type | Indicators | Structure |
|------|------------|-----------|
| **Skill** | "skill", "SKILL.md", auto-triggered | Directory with SKILL.md |
| **Command** | "command", "slash", "/something" | Single .md file |

**If unclear, ASK:** "Are you building a skill (auto-triggers on keywords) or a slash command (manually invoked with /)?"

## Step 2: Understand Requirements

**Discuss with user:**
1. What should it do? (core purpose)
2. What triggers it? (for skills: keywords; for commands: when to invoke)
3. What tools/capabilities needed?
4. Any existing patterns to follow?

**Don't interrogate** - have a conversation. Offer examples from exemplars.

## Step 3: Select Pattern

### For Skills

| Pattern | Lines | When to use | Exemplar |
|---------|-------|-------------|----------|
| CLI wrapper | ~50 | Single tool, direct mapping | `references/exemplar-skill-cli-wrapper.md` |
| Multi-command CLI | ~150 | Multiple commands, intent mapping | `references/exemplar-skill-multi-command.md` |
| Workflow router | ~130 | Conditional workflows based on state | `references/exemplar-skill-workflow-router.md` |
| Procedural | ~600 | Teaching how to build something | `references/exemplar-skill-procedural.md` |
| Knowledge injection | ~40 | Pure domain expertise, no workflows | `references/exemplar-skill-knowledge-injection.md` |

READ the relevant exemplar before building.

### For Commands

| Pattern | Lines | When to use | Exemplar |
|---------|-------|-------------|----------|
| Minimal procedural | ~18 | Single task, immediate execution | `references/exemplar-command-minimal.md` |
| Priming | ~50 | Load state, report, wait for direction | `references/exemplar-command-priming.md` |
| Workflow | ~25 | Variables, conditional logic, reporting | `references/exemplar-command-workflow.md` |
| Multi-phase orchestration | ~125 | Complex workflows, user checkpoints | `references/exemplar-command-orchestration.md` |

READ `references/command-syntax.md` for preprocessing syntax (!backticks, @includes, $ARGUMENTS).

**Present options** and let user choose complexity level.

## Step 4: Build the Artifact

### For Skills

1. **Create directory** under appropriate location:
   - Plugin skill: `skills/<skill-name>/`
   - User skill: `~/.claude/skills/<skill-name>/`
   - Project skill: `.claude/skills/<skill-name>/`

2. **Write SKILL.md** following the baseline structure:
   ```yaml
   ---
   name: skill-name
   description: What it does. USE WHEN user says "[trigger1]", "[trigger2]", or [semantic catch-all].
   allowed-tools: Tool1, Tool2  # Optional
   ---
   ```

   ```markdown
   # Skill Name

   ## Overview
   [1-3 sentences on what this does]

   ## Instructions
   [IMPORTANT warnings, DO NOT assumptions]

   ## Workflow
   [Numbered steps or decision tree]

   ## Common Operations / Commands
   [Code blocks with actual commands]

   ## References (if bundled)
   [Pointers to workflows/, references/, scripts/]
   ```

3. **Critical: The description determines triggering.** Be specific:
   ```yaml
   # Bad - too vague
   description: Helps with documents

   # Good - tool-namespaced triggers
   description: Query prismis content database. USE WHEN user says "use prismis", "query prismis", "search prismis", or searching saved articles.
   ```

4. **Add workflows/** if needed for conditional routing
5. **Add references/** for supporting documentation

### For Commands

1. **Create file** at appropriate location:
   - User command: `~/.claude/commands/<command-name>.md`
   - Project command: `.claude/commands/<command-name>.md`

2. **Write with frontmatter:**
   ```yaml
   ---
   description: What it does (required)
   allowed-tools: Tool restrictions  # Optional
   model: haiku|sonnet|opus  # Optional
   argument-hint: [expected args]  # Optional
   ---
   ```

3. **Follow baseline structure:**
   ```markdown
   # Command Name

   ## Context (optional)
   [Injected state via !`commands` or @file includes]

   ## Variables (if using $ARGUMENTS)
   VARIABLE_NAME: $ARGUMENTS

   ## Instructions / Workflow
   [What to do - numbered steps or direct instructions]

   ## Report (optional)
   [Output format expectations]
   ```

4. **Use preprocessing syntax:**
   - `!`\`command\` - Execute and inject output
   - `@path/to/file` - Include file contents
   - `$ARGUMENTS` or `$1` - Access arguments

## Step 5: Validate

### For Skills
- [ ] Frontmatter has `name` and `description`
- [ ] Description includes USE WHEN with trigger phrases
- [ ] Has Overview, Instructions, Workflow sections
- [ ] Any referenced workflows/references exist

### For Commands
- [ ] Frontmatter has `description`
- [ ] Tool restrictions match intended use
- [ ] Preprocessing syntax is correct
- [ ] Has clear Instructions/Workflow section

## Step 6: Test

**For skills:** Ask user to describe a scenario that should trigger it.

**For commands:** Have user invoke it with `/command-name` and verify behavior.

## Quality Checklist

- [ ] Description is specific with trigger keywords
- [ ] Minimal tokens for the job (not over-engineered)
- [ ] Follows established patterns from exemplars
- [ ] Clear structure and flow
- [ ] No placeholder content
