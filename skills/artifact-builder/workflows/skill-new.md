# Create New Skill

Build skills conversationally, determining type, pattern, and structure based on use cases.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

Build through discovery and iteration. Each step builds context for the next. Do not skip ahead.

**This is a conversation, not a form.**

## Step 1: Understand with Examples

**REQUIRED ACTIONS:**

1. ASK: "What capability do you want? Give examples of how you'd use it."

2. RECORD:
   - Core capability
   - Concrete usage examples (2-3 minimum)
   - Trigger phrases
   - Success outcome

3. **IF vague:**
   - ASK: "When would you use this? Walk through a scenario."
   - CONTINUE until concrete examples

4. SUMMARIZE:
   ```
   Skill: [capability]

   Examples:
   - "[example 1]"
   - "[example 2]"

   Success: [outcome]
   ```

5. CONFIRM: "Did I capture this correctly?"

**VERIFICATION:**
Clear understanding with concrete examples.

**STOP before Step 2.**

## Step 2: Determine Type and Pattern

**REQUIRED ACTIONS:**

1. ANALYZE examples against skill types

2. READ `references/skill-types.md` for type indicators

3. PROPOSE type:
   ```
   Type: [workflow/tool/domain/template/reference]

   Reasoning:
   - [reason from analysis]
   - [reason from examples]

   Match your vision?
   ```

4. CONFIRM with user

5. **IF disagreement:**
   - DISCUSS differences
   - ADJUST determination
   - WAIT for agreement

6. READ `references/pattern-selection.md` for pattern guidance

7. DETERMINE pattern:
   - Single well-documented tool → Minimal
   - Multi-operation (3-10) → Middle-ground
   - Multi-phase with gates → Execution

8. PROPOSE pattern:
   ```
   Pattern: [minimal/middle-ground/execution]

   Reasoning:
   - [complexity assessment]
   - [operations count]

   This means ~[N] lines per artifact.
   ```

9. CONFIRM pattern choice

**VERIFICATION:**
Type and pattern determined and confirmed.

**STOP before Step 3.**

## Step 3: Check Integration

**REQUIRED ACTIONS:**

1. ASK: "Momentum integration or general-purpose?"

2. **IF momentum:**
   - ASK: "Mode-specific? (project/assistant)"
   - RECORD mode requirements
   - READ `references/momentum-integration.md`
   - NOTE: Will ask for momentum path in Step 5

3. **IF general:**
   - RECORD: No momentum integration

**VERIFICATION:**
Integration needs determined.

**STOP before Step 4.**

## Step 4: Plan Resources

**REQUIRED ACTIONS:**

1. READ `references/skill-structure.md`

2. ANALYZE examples to identify resources

3. PLAN based on type:
   - **Workflow**: `workflows/` directory, determine pattern per operation
   - **Tool**: `scripts/` directory, list script names
   - **Domain**: `references/` directory, organize by topic
   - **Template**: `assets/` directory, list templates
   - **Reference**: `references/` only, plan navigation

4. CREATE plan:
   ```
   Structure:
   skill-name/
   ├── SKILL.md
   └── [primary-dir]/
       ├── [resource-1]
       └── [resource-2]

   Resources:
   - [name]: [purpose]
   ```

5. SHOW plan

6. ASK: "Structure make sense? Anything missing?"

7. ADJUST based on feedback

**VERIFICATION:**
Resource plan approved.

**STOP before Step 5.**

## Step 5: Create Structure

**REQUIRED ACTIONS:**

1. DETERMINE path:
   - **Momentum**: ASK for momentum path, use `{path}/skills/skill-name/`
   - **General**: ASK for path, suggest `./skills/skill-name/` or `~/.claude/skills/skill-name/`

2. CREATE directories:
   ```bash
   mkdir -p [skill-path]
   mkdir -p [skill-path]/[resource-dirs from Step 4]
   ```

3. CONFIRM:
   ```
   Created at: [path]

   Structure:
   skill-name/
   ├── [subdirs]
   ```

**VERIFICATION:**
Structure exists and matches plan.

**STOP before Step 6.**

## Step 6: Build SKILL.md

**REQUIRED ACTIONS:**

1. READ `references/tool-selection.md`

2. ANALYZE operations:
   - Files read/written?
   - Shell commands?
   - File finding/search?
   - Subagents?
   - User questions?

3. DETERMINE tools from analysis

4. SELECT model:
   - `haiku` - Simple CLI tool wrapper (parse intent → execute command → return)
   - `sonnet` - Everything else (code generation, multi-step workflows, complex logic)

5. DRAFT frontmatter:
   ```yaml
   ---
   name: skill-name
   description: [what + when from Steps 1-2]
   allowed-tools: [tools from analysis]
   model: [haiku|sonnet]
   ---
   ```

6. EXPLAIN tool and model choices

7. SELECT template based on type AND pattern:
   - Minimal tool: `templates/skills/minimal-tool-skill.md`
   - Middle tool: `templates/skills/middle-ground-tool-skill.md`
   - Middle workflow: `templates/skills/middle-ground-workflow-skill.md`
   - Execution workflow: `templates/skills/execution-workflow-skill.md`
   - Execution tool: `templates/skills/execution-tool-skill.md`
   - Execution domain: `templates/skills/execution-domain-skill.md`
   - Execution template: `templates/skills/execution-template-skill.md`
   - Execution reference: `templates/skills/execution-reference-skill.md`

8. EXPLAIN: "Using [template] for [type] skill with [pattern] pattern."

9. READ template

10. CUSTOMIZE:
   - Replace `skill-name` with actual name
   - Update description
   - Set allowed-tools
   - Set model
   - Add momentum paths if Step 3
   - Customize sections per resource plan
   - Replace placeholders
   - Remove unused sections

11. SHOW customized SKILL.md

12. ASK: "Capture the skill correctly? Adjustments?"

13. ITERATE on feedback

**VERIFICATION:**
SKILL.md approved.

**STOP before Step 7.**

## Step 7: Create Resources

**REQUIRED ACTIONS:**

1. **FOR each resource from Step 4:**

   - EXPLAIN what it contains

   - **IF workflow:**
     - Use pattern from Step 2
     - Minimal: ~30 lines, --help emphasis
     - Middle: ~60 lines, inline examples, conditional READ
     - Execution: ~250 lines, REQUIRED ACTIONS, STOP, VERIFICATION

   - **IF script:**
     - DISCUSS inputs/outputs
     - WRITE code with docstring and error handling

   - **IF reference:**
     - ORGANIZE by topic, clear headers

   - **IF asset:**
     - CREATE or REQUEST from user

   - SHOW drafted resource
   - ITERATE on feedback
   - WRITE file

2. VERIFY all resources created

**VERIFICATION:**
All resources created.

**STOP before Step 8.**

## Step 8: Package and Validate

**REQUIRED ACTIONS:**

1. LIST files:
   ```bash
   find [skill-path] -type f | grep -v ".git"
   ```

2. RUN validation and packaging:
   ```bash
   python3 skills/artifact-builder/scripts/package_skill.py [skill-path]
   ```

3. **IF fails:**
   - SHOW errors
   - FIX issues
   - RETRY

4. **IF succeeds:**
   - CAPTURE zip location and size

5. CREATE summary:
   ```
   Skill: [name]
   Type: [type]
   Pattern: [pattern]

   Files: [count] ([total] lines)
   Package: [path] ([size] KB)

   Capabilities:
   [list from Step 1]

   Install:
   unzip [name].zip
   mv [name] ~/.claude/skills/
   ```

6. SHOW summary

7. ASK: "Test now or make adjustments?"

**Skill creation complete.**

## Key Principles

**Conversational:**
- Open questions
- Show examples
- Discuss trade-offs
- Iterate

**Type-aware:**
- Match structure to type
- Pattern to complexity

**Practical:**
- Build what's needed
- Test early
