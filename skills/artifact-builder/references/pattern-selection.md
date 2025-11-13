# Pattern Selection Guide

Choose artifact pattern based on complexity. Default to leaner patterns.

## Three Patterns

### Minimal Pattern (Disler Style)

**Target:** 15-30 lines total

**Structure:**
```markdown
# Tool Name

## Variables
PATH: path/to/resource

## Instructions
- Use `tool --help` for options
- DO NOT read code files
- Default to --json output

## Workflow
1. Read README
2. Report understanding
3. Execute operation

## Report
Report understanding of [capability]
```

**Use when:**
- Single well-documented tool
- Clear --help output
- One primary operation
- External CLI integration

**Examples:** PDF tool, API client, file converter

### Middle-Ground Pattern

**Target:** 50-70 lines per workflow

**Structure:**
```markdown
# Operation Name

Brief description of operation.

## Instructions

**IMPORTANT:** Use `command --help`. DO NOT assume syntax.

- Imperative instructions
- CAPS for tool names
- Reference comprehensive docs when needed

## Workflow

1. Understand requirement
2. IF complex domain: READ `references/patterns.md`
3. Execute with tool
4. Present results

## Common Patterns

[Inline 80/20 examples here]

For comprehensive reference: READ `references/file.md`
```

**Use when:**
- Multi-operation system (3-10 operations)
- Moderate domain knowledge needed
- Some complexity but not multi-phase
- Benefits from organization

**Examples:** Lore (5 operations), CLI suite, data tools

### Execution Language Pattern

**Target:** 150-250 lines per workflow

**Structure:**
```markdown
# Workflow Name

## Execution Requirements
Execute steps sequentially.

## Step N: Action

**REQUIRED ACTIONS:**
1. ACTION verb: specific instruction
2. IF condition: handle case

**VERIFICATION:**
Expected outcome achieved.

**STOP before Step N+1.**
```

**Use when:**
- Multi-phase with dependencies
- User approval gates required
- File generation through conversation
- High error risk without guidance
- State management needed

**Examples:** Artifact-builder workflows, complex migrations

## Decision Logic

**ASK:**
1. How many distinct operations? (1 = minimal, 3-10 = middle, phases = execution)
2. Is tool well-documented? (yes = minimal, moderate = middle, complex = execution)
3. User interaction needed? (none = minimal, some = middle, gates = execution)
4. Domain knowledge required? (little = minimal, moderate = middle, extensive = execution)

**DEFAULT to leaner pattern when in doubt.**

## Pattern Characteristics

| Pattern | Lines | Tool Use | Domain | Interaction |
|---------|-------|----------|--------|-------------|
| Minimal | 15-30 | --help | Minimal | None |
| Middle | 50-70 | Some examples | Moderate | Optional |
| Execution | 150-250 | Detailed | Extensive | Required |

## Key Principles

**Minimal Pattern:**
- Trust model intelligence
- Emphasize `--help` usage
- "DO NOT read code, use --help"
- Keep extremely brief

**Middle-Ground Pattern:**
- Balance structure and trust
- Inline 80/20 patterns
- Conditional reference loading
- CAPS for tools, imperative style

**Execution Language Pattern:**
- Spell out steps explicitly
- REQUIRED ACTIONS framing
- STOP checkpoints between phases
- VERIFICATION gates
- Handle edge cases

## Examples

### Minimal: PDF Rotation
```markdown
# Rotate PDF

## Instructions
- Use `pdf-tool --help` for options
- DO NOT parse PDF internals

## Workflow
1. Get input file and rotation
2. RUN: pdf-tool rotate --angle {N} {file}
3. Report output location
```

28 lines. Complete.

### Middle: Graph Query
```markdown
# Graph Queries

Query knowledge graph with Cypher.

## Instructions

**IMPORTANT:** Use `lore-graph --help`. DO NOT assume Cypher.

- Schema: `lore-graph schema`
- Common patterns below
- Complex: READ `references/graph-patterns.md`

## Workflow

1. Understand relationship to explore
2. Check patterns below or reference
3. Construct Cypher query
4. RUN: lore-graph query "{cypher}"
5. Present results

## Common Patterns

List technologies:
MATCH (t:Tech) RETURN t.name ORDER BY t.name

Projects using tech:
MATCH (p:Project)-[:USES]->(t:Tech {name: 'X'}) RETURN p.name
```

55 lines. Organized, examples inline.

### Execution: Skill Creation
```markdown
# Create New Skill

Guide skill creation through conversation.

## Step 1: Understand Purpose

**REQUIRED ACTIONS:**
1. ASK: "What capability? Give examples."
2. RECORD: Core capability, usage examples
3. IF vague: ASK clarifying questions
4. SUMMARIZE understanding
5. CONFIRM with user

**VERIFICATION:**
Clear understanding with concrete examples.

**STOP before Step 2.**

## Step 2: Determine Pattern
[...]
```

150+ lines. Conversational procedure.

## Template Selection

**Based on pattern determination:**

- Minimal → `templates/minimal-command.md`
- Middle → `templates/middle-ground/tool-skill.md` or `workflow-skill.md`
- Execution → `templates/execution-style/workflow-skill.md`

## Writing Guidelines

**All patterns use:**
- Imperative directives (DO, USE, READ, RUN)
- CAPS for tool names
- Clear structure
- No hedging language

**Minimal adds:**
- --help emphasis
- DO NOT read code
- Extreme brevity

**Middle adds:**
- Inline 80/20 examples
- Conditional reference loading
- Organized sections

**Execution adds:**
- REQUIRED ACTIONS
- STOP checkpoints
- VERIFICATION gates
- Explicit edge cases

## Anti-Patterns

**Don't:**
- Use execution language for simple tools
- Skip --help emphasis in minimal
- Over-specify obvious steps
- Create references when inline examples sufficient
- Default to execution pattern

**Do:**
- Choose leanest pattern that works
- Trust model intelligence
- Emphasize tool documentation
- Inline common patterns
- Conditional loading for comprehensive docs
