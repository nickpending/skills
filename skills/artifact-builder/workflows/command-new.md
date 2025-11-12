# Build New Slash Command

Collaborative command building through conversation, examples, and iteration.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow builds commands conversationally through discovery and iteration. Each step builds context for the next. Do not skip ahead or produce the final command without completing all discovery steps.

**This is a conversation, not a form.** Build together through questions, examples, and feedback.

## Step 1: Understand the Need

**REQUIRED ACTIONS:**

1. ASK user: "What are you trying to accomplish with this command?"

2. LISTEN for and RECORD:
   - The actual problem they're solving
   - When they'd use this command
   - What success looks like
   - Any existing workflows this fits into

3. SUMMARIZE understanding:
   ```
   You need a command that [purpose]
   Used when [trigger/context]
   Success means [outcome]
   ```

4. CONFIRM with user: "Did I understand correctly?"

**STOP before Step 2.**

## Step 2: Find Relevant Examples

**REQUIRED ACTIONS:**

1. CHECK command type from Step 1:

2. **IF momentum workflow command:**
   - SEARCH `~/development/projects/momentum/commands/` for similar patterns
   - SELECT 1-2 relevant examples
   - SHOW user: "Here's how `/complete-task` handles approval gates..."
   - READ example command file to show actual pattern

3. **IF generic command:**
   - READ `references/templates/commands/generic.md`
   - EXTRACT applicable patterns
   - SHOW user relevant sections

4. ASK: "This command does something similar. Would this approach work for you?"

5. WAIT for feedback and adjust if needed

**VERIFICATION:**
User has seen relevant examples and confirmed approach direction.

**STOP before Step 3.**

## Step 3: Sketch Core Structure and Tools

**REQUIRED ACTIONS:**

1. READ `references/tool-selection.md` for tool selection patterns

2. ANALYZE command operations from Steps 1-2:
   - What files does it read?
   - Does it create or modify files?
   - Does it run shell commands?
   - Does it need file finding (Glob) or content search (Grep)?
   - Does it need code review (Task)?
   - Does it need user choices (AskUserQuestion)?

3. DETERMINE tools using selection logic:
   - Core operations → Read/Write/Edit/Bash
   - File finding → Glob
   - Content search → Grep
   - Quality review → Task
   - User interaction → AskUserQuestion

4. PROPOSE structure with reasoning:
   ```
   I'm thinking:
   - Framework: [momentum/generic] because [reason]
   - Structure: [simple/complex] because [your workflow is linear/needs validation gates]
   - Tools needed: [Read, Write, Bash] because:
     * Read - [loads TASKS.md]
     * Write - [generates report]
     * Bash - [runs git commit]

   Does this match what you're envisioning?
   ```

5. SHOW reasoning for each tool choice

6. ASK for confirmation or adjustments

7. **IF user disagrees:**
   - ASK what needs to change
   - ADJUST framework/structure/tools
   - REPEAT proposal
   - WAIT for approval

8. **IF user approves:**
   - RECORD structure and tool decisions
   - Proceed to Step 4

**VERIFICATION:**
Tool selection matches actual command operations.

**STOP before Step 4.**

## Step 4: Build Variables Section

**REQUIRED ACTIONS:**

1. READ `references/command-structure.md` for:
   - Variable notation guide (CAPS, $VARS, `{runtime}`, `[placeholders]`)
   - Complete momentum injected variable reference
   - Selection guidance based on command purpose

2. IDENTIFY what data the command needs based on Steps 1-3

3. EXPLAIN selections to user:
   - "You'll need ARTIFACTS_DIR for TASKS.md"
   - "This generates timestamps - use `{timestamp}` notation"
   - "Takes filename as argument - document as `[filename]`"

4. SHOW drafted Variables section:
   ```markdown
   **Key Paths**:
   - ARTIFACTS_DIR - Workflow artifacts
   - PROJECT_ROOT - Project root
   - `{timestamp}` - Generated as YYYYMMDD-HHMM
   - `[filename]` - From user argument
   ```

5. ASK: "Missing anything you'll need?"

6. WAIT for feedback and update if needed

**VERIFICATION:**
All variables needed for workflow are documented with correct notation.

**STOP before Step 5.**

## Step 5: Outline Workflow Steps

**REQUIRED ACTIONS:**

1. DRAFT main workflow phases conversationally:
   ```
   Let's outline the workflow:
   1. First, we'll load TASKS.md and find the active task
   2. Then we'll show a git diff for your review
   3. After approval, mark it complete with notes
   4. Finally, commit and report progress

   How does that flow sound? Any steps missing?
   ```

2. SHOW proposed sequence

3. ASK for feedback on flow

4. **IF user suggests changes:**
   - ADJUST workflow steps
   - RE-SHOW updated flow
   - CONTINUE iteration until approved

5. **IF user approves:**
   - RECORD workflow outline
   - Proceed to Step 6

**VERIFICATION:**
Workflow outline covers all requirements from Step 1 and makes logical sense.

**STOP before Step 6.**

## Step 6: Draft Critical Sections

**REQUIRED ACTIONS:**

1. ASK: "What's absolutely required for this command to work correctly?"

2. LISTEN for and RECORD requirements:
   - "Must show changes before committing"
   - "Never skip implementation notes"
   - "Always return to project root"

3. DRAFT Critical section:
   ```markdown
   ## ⚠️ CRITICAL: [CORE PRINCIPLE]

   **REQUIRED:**
   - [Must-do behaviors]
   - [Quality gates]

   **NEVER:**
   - [Anti-patterns]
   - [Things to avoid]
   ```

4. SHOW drafted section to user

5. ASK: "Anything else critical I'm missing?"

6. WAIT for feedback and update if needed

**VERIFICATION:**
Critical section captures all must-do and must-not-do behaviors.

**STOP before Step 7.**

## Step 7: Write Success Criteria

**REQUIRED ACTIONS:**

1. EXTRACT success criteria from Steps 1-6

2. CONVERT to checkboxes:
   ```
   So the command succeeds when:
   - [ ] TASKS.md updated correctly
   - [ ] Changes approved and committed
   - [ ] Progress reported
   - [ ] Back in project root

   Right?
   ```

3. SHOW drafted criteria to user

4. ASK for confirmation

5. WAIT for approval and adjust if needed

**VERIFICATION:**
Success criteria are complete, measurable, and match requirements.

**STOP before Step 8.**

## Step 8: Choose Template and Generate

**REQUIRED ACTIONS:**

1. DETERMINE template based on Steps 1-7:
   - Simple workflow → `references/templates/commands/momentum-simple.md`
   - Complex with checkpoints → `references/templates/commands/momentum-complex.md`
   - Generic command → `references/templates/commands/generic.md`

2. EXPLAIN choice to user:
   ```
   This command fits [template] because [reasoning].
   ```

3. READ the selected template file

4. CUSTOMIZE template with all elements from Steps 1-7:
   - Variables from Step 4
   - Workflow from Step 5
   - Critical section from Step 6
   - Success criteria from Step 7

**VERIFICATION:**
Template loaded and all discussed elements ready to integrate.

**STOP before Step 9.**

## Step 9: Present Draft

**REQUIRED ACTIONS:**

1. SHOW complete command file to user:
   ```
   Here's the full command based on our discussion. The structure follows [template] with:
   - Variables section listing everything we identified
   - Core workflow with the 4 phases we outlined
   - Critical section enforcing approval gates
   - Success criteria we defined

   [Show actual command content]

   What needs adjustment?
   ```

2. WAIT for user feedback

3. RECORD any requested changes

**VERIFICATION:**
User has seen complete draft and provided feedback.

**STOP before Step 10.**

## Step 10: Iterate and Finalize

**REQUIRED ACTIONS:**

1. **IF user requests changes:**
   - ADJUST sections as requested
   - CLARIFY instructions where needed
   - ADD missing pieces
   - TIGHTEN language - READ `references/writing-fundamentals.md` for efficiency patterns if needed
   - RE-SHOW updated sections
   - CONTINUE iteration until approved

2. **IF user approves:**
   - ASK for filename: "What should we name this? Something like `your-command-name.md`?"
   - WAIT for filename
   - WRITE the file to their desired location
   - CONFIRM file written

**STOP before Step 11.**

## Step 11: Validation

**REQUIRED ACTIONS:**

1. RUN validation:
   ```bash
   python3 scripts/validate_command.py [filename]
   ```

2. SHOW results to user

3. **IF validation fails:**
   - ADDRESS structural issues
   - RE-RUN validation
   - Do not proceed until passing

4. **IF validation passes:**
   - SHOW next steps:
     ```
     Command created and validated.

     Next steps:
     - Test command: `/your-command`
     - Iterate based on testing
     - Move to `.claude/commands/` when ready
     ```

**Command creation workflow complete.**

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
