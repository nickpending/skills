# Execution Patterns

How to write instructions that execute as procedures rather than being read as descriptive context.

## The Problem

Models interpret instructions two ways:

**As context (wrong):** "Here's what a good workflow looks like"
- Model understands the concept
- Produces output matching the description
- Skips the actual procedural steps

**As procedure (correct):** "Do these steps now in this order"
- Model executes each step
- Shows work incrementally
- Follows exact sequence

## Tool Names in CAPS

Use CAPS for tool invocations to signal action:

| CAPS | Not |
|------|-----|
| READ `file.md` | "read the file", "check the file" |
| WRITE `file.md` | "create", "save" |
| EDIT `file.md` | "modify", "update" |
| RUN `command` | "execute", "run command" |
| ASK user | "ask user", "confirm with" |

## Action Verbs

**Tool operations:**
- READ — load file content
- WRITE — create new file
- EDIT — modify existing file
- RUN — execute command
- SHOW — display to user
- ASK — get user input

**Control flow:**
- STOP — halt and wait
- WAIT — pause for condition
- VERIFY — check state
- IF/THEN/ELSE — conditional

## STOP Points

Force checkpoints between steps:

```markdown
**STOP before Step 3.**

User must review output before proceeding.
```

Prevents model from skipping to final result without executing intermediate steps.

## Checkpoint Pattern

```markdown
### CHECKPOINT: [Name]

**What you did:**
- [Summary of previous step]

**Verify now:**
- [ ] Requirement 1 met
- [ ] Requirement 2 met

**IF verification fails:** [specific fix action]
**IF verification passes:** Proceed to next step
```

## Step Format

```markdown
## Step N: [Action Verb] [Object]

[Brief context if needed]

**REQUIRED ACTIONS:**
1. READ `file.md`
2. EXTRACT [specific data]
3. IF condition:
   - ACTION: Response
   - ELSE: Alternative

**VERIFICATION:**
Check that [specific outcome occurred]
```

## Anti-Patterns

| Wrong | Right |
|-------|-------|
| "The file should be read" | READ the file |
| "Consider running validation" | RUN validation |
| "You might want to check..." | CHECK [specific thing] |
| "Use the appropriate template" | READ `templates/specific.md` |
| "Follow standard patterns" | READ `reference/patterns.md` |

## Execution Framing

Start workflows with explicit framing:

```markdown
## Execution Requirements

**Execute these steps sequentially.**

Each step builds on previous steps. Do not skip ahead or summarize.
```

