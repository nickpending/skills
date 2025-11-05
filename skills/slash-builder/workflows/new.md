# Build New Slash Command

Collaborative command building through conversation, examples, and iteration.

## Approach

This is a conversation, not a form. We'll build the command together by:
- Understanding what you're trying to accomplish
- Finding relevant patterns from existing commands
- Sketching structure collaboratively
- Iterating based on your feedback
- Building incrementally so you see progress

## Step 1: Understand the Need

Ask the user: "What are you trying to accomplish with this command?"

Listen for:
- The actual problem they're solving
- When they'd use this command
- What success looks like
- Any existing workflows this fits into

## Step 2: Find Relevant Examples

Based on their description, search for similar commands.

**IF momentum workflow command:**
- Check `~/development/projects/momentum/commands/` for patterns
- Show 1-2 relevant examples: "Here's how `/complete-task` handles approval gates..."

**IF generic command:**
- READ `references/generic.md`
- Show applicable patterns

Discuss the pattern: "This command does something similar. Would this approach work for you?"

## Step 3: Sketch Core Structure

Propose the high-level structure based on conversation:

```
I'm thinking:
- Framework: [momentum/generic] because [reason]
- Structure: [simple/complex] because [your workflow is linear/needs validation gates]
- Tools needed: [Read, Write, Bash] for [specific operations]

Does this match what you're envisioning?
```

**Iterate based on feedback.** Adjust framework/structure if needed.

## Step 4: Build Variables Section

**REQUIRED:** READ `references/command-writing-guide.md` for:
- Variable notation guide (CAPS, $VARS, `{runtime}`, `[placeholders]`)
- Complete momentum injected variable reference
- Selection guidance based on command purpose

Discuss what data the command needs:
- "You'll need ARTIFACTS_DIR for TASKS.md"
- "This generates timestamps - use `{timestamp}` notation"
- "Takes filename as argument - document as `[filename]`"

Show the Variables section:
```markdown
**Key Paths**:
- ARTIFACTS_DIR - Workflow artifacts
- PROJECT_ROOT - Project root
- `{timestamp}` - Generated as YYYYMMDD-HHMM
- `[filename]` - From user argument
```

Ask: "Missing anything you'll need?"

## Step 5: Outline Workflow Steps

**Sketch the main phases conversationally:**

"Let's outline the workflow:
1. First, we'll load TASKS.md and find the active task
2. Then we'll show a git diff for your review
3. After approval, mark it complete with notes
4. Finally, commit and report progress

How does that flow sound? Any steps missing?"

**Iterate on the workflow** until it makes sense for their use case.

## Step 6: Draft Critical Sections

**Identify critical behaviors:**

"What's absolutely required for this command to work correctly?"
- "Must show changes before committing"
- "Never skip implementation notes"
- "Always return to project root"

**Draft the Critical section:**
```markdown
## ⚠️ CRITICAL: [CORE PRINCIPLE]

**REQUIRED:**
- [Must-do behaviors]
- [Quality gates]

**NEVER:**
- [Anti-patterns]
- [Things to avoid]
```

**Ask:** "Anything else critical I'm missing?"

## Step 7: Write Success Criteria

**Convert requirements to checkboxes:**

"So the command succeeds when:
- [ ] TASKS.md updated correctly
- [ ] Changes approved and committed
- [ ] Progress reported
- [ ] Back in project root

Right?"

## Step 8: Choose Template and Generate

Based on the conversation, determine template:
- Simple workflow → `references/momentum-simple.md`
- Complex with checkpoints → `references/momentum-complex.md`
- Generic command → `references/generic.md`

Show which template and why.

**REQUIRED:** READ the selected template file.

Customize based on all discussed elements.

## Step 9: Present Draft

**Show the complete command file:**

"Here's the full command based on our discussion. The structure follows [template] with:
- Variables section listing everything we identified
- Core workflow with the 4 phases we outlined
- Critical section enforcing approval gates
- Success criteria we defined

[Show actual command content]

What needs adjustment?"

## Step 10: Iterate and Finalize

Based on feedback:
- Adjust sections
- Clarify instructions
- Add missing pieces
- Tighten language - READ `references/prompt-patterns.md` for efficiency patterns

When ready, ask for filename:
"What should we name this? Something like `your-command-name.md`?"

WRITE the file to their desired location.

## Step 11: Validation

RUN validation:
```bash
python3 scripts/validate_command.py [filename]
```

Show results and address any structural issues.

Guide next steps:
- Test command: `/your-command`
- Iterate based on testing
- Move to `.claude/commands/` when ready

## Key Principles

**Be conversational:**
- Ask open questions
- Show examples
- Discuss trade-offs
- Build together

**Be adaptive:**
- If they have strong opinions, follow them
- If they're unsure, guide with examples
- Iterate based on feedback

**Be transparent:**
- Show what you're building as you go
- Explain choices
- Present drafts for review

**Be helpful:**
- Reference existing patterns
- Point to relevant documentation
- Suggest improvements
- But let them decide
