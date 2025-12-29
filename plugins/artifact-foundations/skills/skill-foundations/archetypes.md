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

```markdown
# skill-name

## Overview
[1-2 sentences]

## Instructions
[IMPORTANT warnings, tool quirks]

## Workflow
1. Determine operation
2. RUN command with appropriate flags
3. Parse and present output

## Common Operations
[Code blocks with actual commands]
```

**Characteristics:**
- ~40-80 lines
- Frontmatter with USE WHEN triggers
- IMPORTANT warnings at top
- Numbered workflow steps
- Code blocks with actual commands

**Multi-tool variant:** For skills that orchestrate multiple CLI tools in a pipeline (e.g., nmap → httpx → nuclei), use the same structure but chain commands in the workflow. Add error handling for partial failures.

**Exemplar:** `exemplar-cli-wrapper.md`

---

## Workflow Router

Routes to different procedures based on state or intent.

```markdown
# skill-name

## Overview
[What this does, what it outputs]

## Workflow

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

**Exemplar:** `exemplar-workflow-router.md`

---

## Knowledge Injection

Injects domain expertise - HOW to approach a task.

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
- No workflows - pure expertise
- Design Thinking section (questions)
- Guidelines by aspect
- CRITICAL/NEVER inline warnings

**Exemplar:** `exemplar-knowledge-injection.md`

---

## Foundations

Provides reference content - WHAT to use.

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

**Exemplar:** `exemplar-foundations.md` (see also: `visual-foundations`)
