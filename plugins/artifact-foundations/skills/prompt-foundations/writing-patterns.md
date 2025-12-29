# Writing Patterns

Language patterns for effective Claude Code artifacts.

## Directive Language

**Strong commands:**
- **MUST** / **REQUIRED** / **CRITICAL** — Non-negotiable
- **ALWAYS** / **NEVER** — Absolute rules
- **VERIFY** / **VALIDATE** / **ENSURE** — Quality gates

**Example:**
```markdown
REQUIRED: Read TASKS.md and extract incomplete tasks

VERIFY all tasks have:
- [ ] Status field
- [ ] Description
```

## Variable Notation

| Pattern | Meaning | Examples |
|---------|---------|----------|
| `{CAPS}` | Given to you | `{PROJECT_ROOT}`, `{TASK_NUMBER}` |
| `{lowercase}` | You generate it | `{id}`, `{slug}`, `{timestamp}` |
| `${VAR}` | Bash only | `${PROJECT_ROOT}` in shell commands |

CAPS = provided. lowercase = generated.

## Token Efficiency

### Remove Filler

| Verbose | Concise |
|---------|---------|
| "In order to" | "To" |
| "Please ensure that" | "Ensure" |
| "You should" | [Direct imperative] |
| "It is important to note that" | [Just state it] |
| "At this point in time" | "Now" |
| "Due to the fact that" | "Because" |

### Bullets Over Prose

**Verbose:**
```markdown
First, you should read the file. Second, you should extract
the data. Third, you should validate the results.
```

**Concise:**
```markdown
1. Read file
2. Extract data
3. Validate results
```

### Reference Don't Repeat

**Don't repeat information:**
```markdown
## Constraints
- MUST validate input
- MUST check file exists

## Step 2
Apply constraints from above  ← reference, don't repeat
```

## Structure Patterns

### Checkpoint Gates

```markdown
CHECKPOINT 1: Load Context
- READ file X
- EXTRACT data Y
- VERIFY data is valid

PROCEED only if all checks pass
```

### Verification Gates

```markdown
VERIFICATION GATE:
- [ ] Requirement 1 met
- [ ] Requirement 2 met

FAILURE MODE: If validation fails, [specific action]
```

### Sequential Phases

```markdown
PHASE 1: Preparation
1. First action
2. Second action
VERIFICATION: State what was accomplished

PHASE 2: Execution
1. Next action
2. Final action
```

## Emphasis

- **Bold** for key concepts
- `Code format` for technical terms
- CAPS for tool names and critical requirements
- > Blockquotes for important notes

Avoid aggressive language ("CRITICAL: You MUST..."). Use direct statements.

## When NOT to Optimize

Clarity > brevity for:
- Complex logic — explicit beats ambiguous
- Critical constraints — worth repeating
- Edge cases — include if they affect behavior
- First drafts — optimize after testing
