# Skill Archetypes

## Decision Tree

```
What does the skill primarily do?
│
├─► Execute CLI commands? ──────► CLI Wrapper
│   (single or multiple tools)
│
├─► Route to procedures? ───────► Workflow Router
│
└─► Provide context?
    ├─► HOW to approach ────────► Knowledge Injection
    └─► WHAT to use ────────────► Foundations
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

## Overview
[1-2 sentences]

## Instructions
[IMPORTANT warnings, tool quirks]

## Workflow
1. Determine operation from $ARGUMENTS
2. RUN command with appropriate flags
3. Parse and present output

## Common Operations
[Code blocks with actual commands]
```

**Characteristics:**
- ~40-80 lines
- `allowed-tools` scopes to the wrapped CLI
- `argument-hint` shows expected syntax
- IMPORTANT warnings at top
- Numbered workflow steps
- Code blocks with actual commands

**Recommended features:**
- `allowed-tools: Bash(tool *)` — prevents the skill from running unrelated commands
- `argument-hint` — guides user on expected input format
- Skill-scoped hooks with `once: true` — one-time setup (check tool installed, verify config)

**Multi-tool variant:** For skills that orchestrate multiple CLI tools in a pipeline (e.g., nmap → httpx → nuclei), use the same structure but chain commands in the workflow. Add error handling for partial failures. Use `allowed-tools: Bash(nmap *), Bash(httpx *), Bash(nuclei *)`.

**Exemplar:** `exemplar-cli-wrapper.md`

---

## Workflow Router

Routes to different procedures based on state or intent.

```yaml
---
name: skill-name
description: [What this manages]. USE WHEN [triggers].
argument-hint: bootstrap|sync|report [options]
---
```

```markdown
# skill-name

## Overview
[What this does, what it outputs]

## Determine Action

Parse $ARGUMENTS (or $0) for the action keyword.

| Scenario | Condition | Workflow |
|----------|-----------|----------|
| First run | config missing | `workflows/setup.md` |
| Update | config exists | `workflows/update.md` |

## Execute

1. CHECK condition
2. READ appropriate workflow
3. Follow workflow exactly
```

**Characteristics:**
- ~100-200 lines (SKILL.md + workflows)
- Routing table maps intent → workflow file
- Workflows are self-contained procedures
- May have reference/ for supporting docs
- Scripts directory common
- `$ARGUMENTS` or `$0` for dispatch

**Recommended features:**
- `argument-hint` — shows valid action keywords
- `$ARGUMENTS` / `$0` — argument-based dispatch
- `context: fork` — when workflows need isolation (validation, analysis)
- Dynamic injection (`` !`command` ``) — when routing depends on live state

**Exemplar:** `exemplar-workflow-router.md`

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

**Exemplar:** `exemplar-foundations.md` (see also: `visual-foundations`)
