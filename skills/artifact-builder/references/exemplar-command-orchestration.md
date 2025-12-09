# Exemplar: Multi-Phase Orchestration Command

**Pattern:** Multi-Phase Orchestration
**Source:** Claude Code plugins/feature-dev/commands/feature-dev.md
**Lines:** 126
**Use when:** Complex workflows with user checkpoints, agent delegation, multiple phases

---

## Structure Analysis

- Frontmatter with description and argument-hint
- Core Principles section (behavioral guidance)
- 7 numbered phases with clear goals
- User checkpoints between phases
- Agent delegation patterns
- DO NOT SKIP / DO NOT START warnings

---

## Full Exemplar

```yaml
---
description: Guided feature development with codebase understanding and architecture focus
argument-hint: Optional feature description
---
```

```markdown
# Feature Development

You are helping a developer implement a new feature. Follow a systematic approach: understand the codebase deeply, identify and ask about all underspecified details, design elegant architectures, then implement.

## Core Principles

- **Ask clarifying questions**: Identify all ambiguities, edge cases, and underspecified behaviors. Ask specific, concrete questions rather than making assumptions. Wait for user answers before proceeding with implementation.
- **Understand before acting**: Read and comprehend existing code patterns first
- **Read files identified by agents**: When launching agents, ask them to return lists of the most important files to read.
- **Simple and elegant**: Prioritize readable, maintainable, architecturally sound code
- **Use TodoWrite**: Track all progress throughout

---

## Phase 1: Discovery

**Goal**: Understand what needs to be built

Initial request: $ARGUMENTS

**Actions**:
1. Create todo list with all phases
2. If feature unclear, ask user for:
   - What problem are they solving?
   - What should the feature do?
   - Any constraints or requirements?
3. Summarize understanding and confirm with user

---

## Phase 2: Codebase Exploration

**Goal**: Understand relevant existing code and patterns at both high and low levels

**Actions**:
1. Launch 2-3 code-explorer agents in parallel. Each agent should:
   - Trace through the code comprehensively
   - Target a different aspect of the codebase
   - Include a list of 5-10 key files to read

   **Example agent prompts**:
   - "Find features similar to [feature] and trace through their implementation"
   - "Map the architecture and abstractions for [feature area]"
   - "Analyze the current implementation of [existing feature/area]"

2. Once agents return, read all files identified
3. Present comprehensive summary of findings and patterns

---

## Phase 3: Clarifying Questions

**Goal**: Fill in gaps and resolve all ambiguities before designing

**CRITICAL**: This is one of the most important phases. DO NOT SKIP.

**Actions**:
1. Review codebase findings and original feature request
2. Identify underspecified aspects: edge cases, error handling, integration points, scope boundaries
3. **Present all questions to the user in a clear, organized list**
4. **Wait for answers before proceeding to architecture design**

If the user says "whatever you think is best", provide your recommendation and get explicit confirmation.

---

## Phase 4: Architecture Design

**Goal**: Design multiple implementation approaches with different trade-offs

**Actions**:
1. Launch 2-3 code-architect agents in parallel with different focuses: minimal changes, clean architecture, pragmatic balance
2. Review all approaches and form your opinion on which fits best
3. Present to user: brief summary of each approach, trade-offs comparison, **your recommendation with reasoning**
4. **Ask user which approach they prefer**

---

## Phase 5: Implementation

**Goal**: Build the feature

**DO NOT START WITHOUT USER APPROVAL**

**Actions**:
1. Wait for explicit user approval
2. Read all relevant files identified in previous phases
3. Implement following chosen architecture
4. Follow codebase conventions strictly
5. Write clean, well-documented code
6. Update todos as you progress

---

## Phase 6: Quality Review

**Goal**: Ensure code is simple, DRY, elegant, and functionally correct

**Actions**:
1. Launch 3 code-reviewer agents in parallel: simplicity/DRY, bugs/correctness, conventions/abstractions
2. Consolidate findings and identify highest severity issues
3. **Present findings to user and ask what they want to do** (fix now, fix later, proceed as-is)
4. Address issues based on user decision

---

## Phase 7: Summary

**Goal**: Document what was accomplished

**Actions**:
1. Mark all todos complete
2. Summarize:
   - What was built
   - Key decisions made
   - Files modified
   - Suggested next steps
```

---

## Key Patterns

1. **Core Principles:** Behavioral guidance before phases
2. **Numbered phases:** Clear progression with goals
3. **Goal statements:** Each phase starts with "Goal: X"
4. **Actions lists:** Numbered steps within phases
5. **Agent delegation:** "Launch 2-3 agents in parallel"
6. **User checkpoints:** Bold "Ask user", "Wait for", "Present to user"
7. **DO NOT warnings:** "DO NOT SKIP", "DO NOT START WITHOUT"
8. **Explicit approval:** "Wait for explicit user approval"
9. **TodoWrite integration:** Track progress throughout
10. **Summary phase:** Document what was accomplished
