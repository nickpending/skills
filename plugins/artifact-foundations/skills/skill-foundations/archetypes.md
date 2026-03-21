# Skill Archetypes

## Decision Tree

```
What does the skill primarily do?
│
├─► Execute CLI commands? ──────────► CLI Wrapper
│
├─► Route to procedures?
│   ├─► Main thread? ──────────────► Workflow Router
│   └─► Isolated execution? ───────► Forked Workflow
│
├─► Validate/check? ───────────────► Forked Validator
│
└─► Provide context?
    ├─► HOW to approach ────────────► Knowledge Injection
    └─► WHAT to use ────────────────► Foundations
```

---

## CLI Wrapper

Wraps CLI tool(s) with intent mapping.

```yaml
---
name: skill-name
description: [What CLI it wraps]. USE WHEN [triggers].
argument-hint: <command> [options]
allowed-tools: Bash(tool-name *)
---
```

```markdown
# skill-name

[What this wraps, where it lives]

**CLI:** `tool-name` (system PATH)

**IMPORTANT:** When unsure about flags or syntax, RUN `tool-name <command> --help` first.

## When to Use

| Trigger | Flow |
|---------|------|
| "do X" | → Flow 1 |
| "show Y" | → Flow 2 |

## Flow 1: [Action]

[Code blocks with actual commands]

## Flow 2: [Action]

[Code blocks with actual commands]

## Key Flags

| Flag | Purpose |
|------|---------|
| `--flag` | Does thing |
```

**Characteristics:**
- ~40-160 lines
- `allowed-tools` scopes to the wrapped CLI
- `argument-hint` shows expected syntax
- IMPORTANT warnings at top
- Flow-based organization with code blocks
- Key Flags reference table

**Recommended features:**
- `allowed-tools: Bash(tool *)` — prevents the skill from running unrelated commands
- `argument-hint` — guides user on expected input format
- Skill-scoped hooks with `once: true` — one-time setup (check tool installed, verify config)

**Pipe behavior:** When the CLI pipes output through tools like `jq`, the full command (including pipes) must start with the allowed prefix. `Bash(prismis-cli *)` allows `prismis-cli ... | jq '...'` because prefix matching applies to the command string.

**Multi-tool variant:** For skills that orchestrate multiple CLI tools in a pipeline (e.g., nmap → httpx → nuclei), use the same structure but chain commands in the workflow. Use `allowed-tools: Bash(nmap *), Bash(httpx *), Bash(nuclei *)`.

**Real examples:** flux (161 lines), lore (195 lines), prismis (106 lines)

**Exemplar:** `exemplar-cli-wrapper.md`

---

## Workflow Router

Routes to different procedures based on state or intent. Runs in main thread with full conversation context.

```yaml
---
name: skill-name
description: [What this manages]. USE WHEN [triggers].
argument-hint: bootstrap|sync|report [options]
---
```

```markdown
# skill-name

[What this does, what it outputs]

## Determine Action

Parse $0 for the action keyword.

| `$0` | Flow |
|------|------|
| bootstrap | → Setup flow |
| sync | → Update flow |
| report | → Status flow |

## Flow 1: Bootstrap

### Step 1: Check Existing
[Precondition check]

### Step 2: Create
[Create artifacts]

### Step 3: Confirm
[Present results]

## Flow 2: Sync
[...]
```

**Characteristics:**
- ~100-200 lines (SKILL.md + workflows)
- Routing table maps intent → workflow
- Workflows are self-contained procedures
- May have reference/ for supporting docs
- `$ARGUMENTS` or `$0` for dispatch
- Runs in main thread — needs conversation context

**Recommended features:**
- `argument-hint` — shows valid action keywords
- `$0` for action dispatch, `$1`+ for parameters
- Dynamic injection (`` !`command` ``) — when routing depends on live state
- `${CLAUDE_SKILL_DIR}` — when referencing supporting files via tool calls

**When to split:** For simple routers (2-3 flows, <200 lines total), keep everything in SKILL.md. Split into `workflows/` only when individual flows are independently reusable or the SKILL.md exceeds ~200 lines.

**Real examples:** architecture (106 lines), build-notes (loaded from session), ideation (156 lines), exploration (106 lines)

**Exemplar:** `exemplar-workflow-router.md`

---

## Forked Workflow

Complex procedures that run in isolation. Reads all context from disk, returns structured results.

```yaml
---
name: skill-name
description: [What it processes]. Internal skill for [orchestrator/system].
context: fork
model: haiku
allowed-tools: Read, Glob, Grep, Bash(tool *), Skill
user-invocable: false
---
```

```markdown
# skill-name

[What this does, who calls it, what it returns]

## $ARGUMENTS
\```
KEY: {value}
ANOTHER_KEY: {value}
FLAGS: {"status": "...", ...}
\```

## Process

### Step 1: Read Inputs
[Read from disk — work order, config, operator logs]

### Step 2: Analyze/Transform
[Multi-step procedure with conditional branching]

### Step 3: Write Outputs
[Capture to lore, update files, produce report]

### Step 4: Return Result
[Structured markdown or confirmation]
```

**Characteristics:**
- 200-400 lines
- `context: fork` + `model: haiku` + `user-invocable: false`
- Reads ALL context from disk (no conversation history)
- Receives structured `$ARGUMENTS` from orchestrator
- Multi-step procedures with conditional logic
- May invoke other skills (`Skill` in allowed-tools)
- Returns structured results (markdown or text)

**Recommended features:**
- `allowed-tools` with specific Bash prefixes + `Skill` if it invokes other skills
- `$ARGUMENTS` with structured input blocks (labeled fields)
- `${CLAUDE_SKILL_DIR}` if it has supporting reference files

**Key difference from Workflow Router:** Workflow Routers run in main thread with conversation context and route based on user intent. Forked Workflows run in isolation, receive structured input from orchestrators, and return structured output. They're internal processing skills, not user-facing.

**Real examples:** configure-quality (387 lines), synthesize-learnings (362 lines)

---

## Forked Validator

Validates artifacts against requirements. Receives structured input, returns structured JSON.

```yaml
---
name: validate-something
description: Validate [what] — [acceptance criteria summary]
context: fork
model: haiku
allowed-tools: Read, Glob, Grep
user-invocable: false
---
```

```markdown
# Validator Name

[What is being validated, who calls this]

## $ARGUMENTS
\```
REPORT: {path to report being validated}
OPERATOR_LOG: {path to operator log}
FLAGS: {"status": "complete", "verified": true}
\```

## Validation Process

### Step 1: Read Required Files
1. **Report** — Read REPORT path
2. **Operator log** — Read OPERATOR_LOG path
3. **Source spec** — Read the spec being validated against

### Step 2: Check [Aspect 1]
[Specific checks with pass/fail criteria]

### Step 3: Check [Aspect 2]
[More checks]

### Step N: Return Structured Result

Return ONLY this JSON format:

\```json
{
  "valid": true|false,
  "issues": [
    {
      "category": "category_name",
      "item": "description",
      "severity": "high|medium|low"
    }
  ],
  "summary": "One sentence overall assessment"
}
\```

## Constraints

- Check EVERY item against EVERY validation category
- Be specific — cite exact text
- Return ONLY the JSON — no explanation or commentary
```

**Characteristics:**
- 100-250 lines
- `context: fork` + `model: haiku` + `user-invocable: false`
- Read-only tools (mostly — add `Edit` only if validator annotates files, `Bash` only if it runs verification commands)
- Always returns structured JSON
- Receives structured `$ARGUMENTS` from orchestrator
- Numbered validation steps, each checking one aspect
- Severity guidelines and "valid = true" criteria

**Recommended features:**
- `allowed-tools: Read, Glob, Grep` — add `Bash` only for running verification commands, `Edit` only for annotating files
- `agent: worker` — when validation needs general-purpose tool access beyond read-only
- Structured `$ARGUMENTS` with report paths, operator log paths, and flags
- "Return ONLY this JSON" constraint to prevent explanation text

**Key difference from Forked Workflow:** Validators are read-mostly, always return JSON, and check work against specs. Forked Workflows are read-write, return varied formats, and process/transform data.

**Real examples:** validate-build (233 lines), validate-decomposition (198 lines), validate-iteration (145 lines), validate-plan (134 lines), validate-test (208 lines)

---

## Knowledge Injection

Injects domain expertise — HOW to approach a task.

```yaml
---
name: skill-name
description: [Domain] guidance. USE WHEN [triggers].
allowed-tools: Read, Grep, Glob
user-invocable: false
---
```

```markdown
# skill-name

## Design Thinking
[Questions to ask before acting]

## Guidelines
[Domain expertise by aspect]

## Anti-patterns
[What to avoid]
```

**Characteristics:**
- ~40-60 lines
- No workflows — pure expertise
- Design Thinking section (questions)
- Guidelines by aspect
- CRITICAL/NEVER inline warnings

**Recommended features:**
- `allowed-tools: Read, Grep, Glob` — read-only when the skill should never modify anything
- `user-invocable: false` — when this is an internal skill invoked by other skills or orchestrators
- `ultrathink` — when the injected expertise drives complex analysis

**Exemplar:** `exemplar-knowledge-injection.md`

---

## Foundations

Provides reference content — WHAT to use.

```yaml
---
name: skill-name
description: [Domain] reference - [content types]. USE WHEN [triggers] OR another skill needs [domain] context.
disable-model-invocation: true
---
```

```markdown
# skill-name

[Brief description]

## Content Routing

| Intent | Load |
|--------|------|
| palette, colors | `palette.md` |
| aesthetic, style | `aesthetic.md` |

## Defaults
[Common choices]
```

**Characteristics:**
- ~20-40 lines (SKILL.md)
- Content files as siblings
- No workflows
- Content routing table
- Defaults section

**Recommended features:**
- `disable-model-invocation: true` — when foundations should only load on explicit request, not auto-trigger
- Dynamic injection (`` !`command` ``) — when reference content comes from live sources (API schemas, config files)
- `${CLAUDE_SKILL_DIR}` — portable references to sibling content files

**Real examples:** skill-foundations, visual-foundations

**Exemplar:** `exemplar-foundations.md`
