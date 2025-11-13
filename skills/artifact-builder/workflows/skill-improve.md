# Improve Existing Skill

Enhance skills for clarity, token efficiency, and effectiveness through type-aware analysis.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow improves existing skills through analysis, proposal, approval, and incremental application. Do not skip approval gates or apply changes without user confirmation.

## Step 1: Read and Understand

**REQUIRED ACTIONS:**

1. ASK: "Which skill should I improve? Please provide the path to the skill directory."

2. WAIT for path

3. READ skill structure:
   ```bash
   find [skill-path] -type f -name "*.md" | head -20
   ```

4. READ `[skill-path]/SKILL.md` completely

5. READ bundled resources (workflows, references, scripts, assets)

6. ANALYZE and RECORD:
   - Current purpose and capabilities
   - Skill type (workflow/tool/domain/template/reference)
   - Structure (router vs direct, bundled resources)
   - Token usage (verbose vs concise)
   - Clarity issues (vague instructions, missing steps)
   - Strong points (what works well)

7. CREATE initial assessment:
   ```
   Skill: [name]
   Type: [inferred type]
   Structure: [description]

   Current state:
   - SKILL.md: [X] lines
   - [resource files and sizes]

   Observations:
   - Verbosity: [terse/moderate/verbose]
   - Clarity: [clear/some issues/confusing]
   - Structure: [well-organized/could improve]
   - Execution language: [present/missing/partial] (if workflow skill)

   Strong points:
   - [what works well]
   ```

8. SHOW assessment to user

**VERIFICATION:**
Complete understanding of current skill state and structure.

**STOP before Step 2.**

## Step 2: Identify Improvements

**REQUIRED ACTIONS:**

1. **CHECK skill type and analyze type-specific improvements:**

   **IF workflow skill:**
   - CHECK for execution language patterns
   - SCAN for missing REQUIRED ACTIONS sections
   - SCAN for missing STOP points
   - SCAN for passive voice or suggestion language
   - CHECK CAPS tool names (READ, WRITE, RUN, etc.)
   - CHECK VERIFICATION sections
   - REFERENCE `references/writing-fundamentals.md` for execution patterns

   **IF tool skill:**
   - CHECK script documentation clarity
   - SCAN for imperative commands
   - CHECK error handling guidance
   - CHECK usage examples completeness

   **IF domain/reference skill:**
   - CHECK reference organization
   - SCAN for navigation aids
   - CHECK grep patterns if files large
   - CHECK information architecture

   **IF template skill:**
   - CHECK asset catalog completeness
   - SCAN for customization guidance
   - CHECK usage examples

2. **SCAN all skills for token efficiency opportunities:**

   **Check for redundant phrasing:**
   - "In order to" → direct statement
   - "Please make sure to" → imperative
   - "You should" → directive form

   **Check for verbose instructions:**
   - Long explanations → bullet points
   - Repeated context → reference earlier sections
   - Over-documented obvious steps

   **Check for weak directives:**
   - Hedging language ("maybe", "perhaps")
   - Passive voice
   - Unclear requirements

3. **CHECK momentum integration (if applicable):**
   - `allowed-tools` in frontmatter
   - Available Paths section
   - Mode Requirement section (if mode-specific)
   - Path references using `{VARIABLE}` format

4. **CHECK file sizes:**
   - SKILL.md within 200 lines (router) or 250 (direct)
   - Workflows within 200-300 lines (400 max)
   - References within 200-300 lines

5. CREATE improvement inventory:
   ```
   Improvements identified:

   Type-specific:
   - [type-specific issue 1]
   - [type-specific issue 2]

   Token efficiency:
   - [verbosity issue 1]: [line numbers]
   - [verbosity issue 2]: [line numbers]

   Clarity:
   - [clarity issue 1]
   - [clarity issue 2]

   Structure:
   - [file size issues]
   - [organization issues]

   Integration:
   - [momentum issues if applicable]
   ```

6. SHOW inventory to user

**VERIFICATION:**
Complete analysis with specific improvement opportunities identified.

**STOP before Step 3.**

## Step 3: Propose Improvements

**REQUIRED ACTIONS:**

1. FOR each improvement from Step 2, CREATE structured proposal:

   **Format:**
   ```
   Issue: [description]
   Location: [file:line or section]

   Current:
   [show existing text]

   Proposed:
   [show improved version]

   Rationale: [why this is better]
   Impact: [token savings/clarity gain/better execution]
   ```

2. **PRIORITIZE proposals:**
   - Critical: Missing execution language (workflow skills)
   - High: Major clarity issues, missing required sections
   - Medium: Token efficiency, minor improvements
   - Low: Optional optimizations

3. SHOW all proposals grouped by priority

4. ASK: "Which improvements would you like to apply? (all/critical+high/specific ones)"

5. WAIT for decision

6. RECORD approved improvements

**VERIFICATION:**
All improvements proposed with clear before/after examples and user decisions recorded.

**STOP before Step 4.**

## Step 4: Discuss Trade-offs

**REQUIRED ACTIONS:**

1. **IF proposals have trade-offs, EXPLAIN options:**

   **Conciseness vs Clarity:**
   ```
   This section could be:
   - Terse: [example] (saves [N] tokens, may lose beginners)
   - Detailed: [example] (clearer, costs [N] tokens)
   - Balanced: [example] (middle ground)

   Which level fits your audience?
   ```

   **Structure vs Flexibility:**
   ```
   We could:
   - Split this 500-line file into focused files (better navigation, more files)
   - Keep it together (single reference, but large)

   What works better for this skill's usage?
   ```

2. FOR each trade-off, ASK user preference

3. WAIT for decisions

4. RECORD preferences

**VERIFICATION:**
All trade-offs discussed and preferences recorded.

**STOP before Step 5.**

## Step 5: Build Improvement Plan

**REQUIRED ACTIONS:**

1. COMPILE all approved improvements from Steps 3-4

2. **IF workflow skill needs execution language:**
   - CALCULATE impact (lines added for REQUIRED ACTIONS, STOP points, etc.)
   - ESTIMATE token change

3. **IF file splitting needed:**
   - PROPOSE new structure
   - SHOW what goes where

4. CALCULATE overall impact:
   - Token savings/additions
   - Clarity improvements
   - Structural changes

5. CREATE improvement plan:
   ```
   Improvement plan for [skill-name]:

   Changes by file:
   - SKILL.md:
     - [change 1]: [impact]
     - [change 2]: [impact]
   - [other files...]

   Overall impact:
   - Token efficiency: [+/- N tokens] ([X]% change)
   - Execution language: [added/improved/none]
   - Clarity: [specific improvements]
   - Structure: [changes]

   These changes [preserve/enhance] all functionality while making the skill [improvements summary].

   Proceed with improvements?
   ```

6. SHOW plan to user

7. ASK for final approval

8. WAIT for confirmation

**STOP if user does not approve.**

**IF approved, proceed to Step 6.**

## Step 6: Apply Improvements

**REQUIRED ACTIONS:**

1. FOR each approved improvement, execute incrementally:

   **Process per change:**
   - SHOW section being changed
   - SHOW before state
   - SHOW after state
   - CONFIRM logic/meaning preserved
   - APPLY change using Edit tool
   - VERIFY change applied correctly

2. **IF adding execution language to workflow:**
   - ADD "Execution Requirements" framing
   - CONVERT steps to "REQUIRED ACTIONS" format
   - ADD CAPS tool names
   - ADD STOP points between steps
   - ADD VERIFICATION sections
   - SHOW each section as converted
   - WAIT for confirmation on each

3. **IF splitting files:**
   - CREATE new files with content
   - UPDATE SKILL.md references
   - VERIFY all content preserved
   - CONFIRM navigation still clear

4. WAIT for confirmation on each major section before proceeding

5. **NEVER:**
   - Apply multiple changes without showing each
   - Skip before/after comparisons
   - Change logic without explicit approval
   - Proceed if user raises concerns

**VERIFICATION:**
All approved improvements applied and confirmed incrementally.

**STOP before Step 7.**

## Step 7: Validate and Review

**REQUIRED ACTIONS:**

1. RUN validation:
   ```bash
   python3 skills/artifact-builder/scripts/validate_skill.py [skill-path]
   ```

2. **IF validation fails:**
   - SHOW errors
   - FIX issues
   - RETRY validation

3. **IF validation succeeds:**
   - CONFIRM structure valid

4. LIST all modified files:
   ```bash
   git diff --name-only [skill-path]
   ```
   (or list files if not in git)

5. CHECK file sizes:
   ```bash
   wc -l [skill-path]/**/*.md
   ```

6. **IF workflow skill:**
   - VERIFY execution language complete
   - CHECK STOP points present
   - CHECK VERIFICATION sections exist

7. **IF momentum skill:**
   - VERIFY allowed-tools correct
   - CHECK paths documented
   - CHECK mode requirements if applicable

8. CREATE final summary:
   ```
   Improvements applied to [skill-name]:

   Files modified:
   - [file 1]: [changes summary] ([X] → [Y] lines)
   - [file 2]: [changes summary] ([X] → [Y] lines)

   Results:
   - Token efficiency: [impact]
   - Execution language: [status]
   - Clarity: [improvements]
   - Structure: [changes]

   The skill now [summarize improvements].

   Next steps:
   - Test skill with actual use cases
   - Iterate based on performance
   - Monitor effectiveness improvements
   ```

6. SHOW summary to user

7. ASK: "Would you like to test the improved skill or make additional adjustments?"

**Improvement workflow complete.**

## Key Principles

**Type-aware improvements:**
- Workflow skills need execution language
- Tool skills need clear script guidance
- Domain skills need good navigation
- Template skills need usage clarity
- Reference skills need organization
- Apply appropriate patterns for type

**Incremental application:**
- Show each change before applying
- Confirm logic preserved
- Wait for approval on major changes
- Build confidence through visibility

**Preserve functionality:**
- NEVER change working logic
- NEVER skip showing changes
- NEVER batch edits without review
- Keep author's intent clear

**Balance goals:**
- Token efficiency vs clarity
- Conciseness vs completeness
- Structure vs simplicity
- Optimization vs readability
