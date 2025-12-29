# Skill Structure

## Frontmatter

```yaml
---
name: skill-name
description: [What it does]. USE WHEN [triggers]. [Additional context].
---
```

| Field | Required | Limit |
|-------|----------|-------|
| `name` | Yes | 64 chars, lowercase-hyphens |
| `description` | Yes | 1,024 chars max |
| `version` | No | Common in plugins |

## Length Guidelines

| Metric | Max | Best Practice |
|--------|-----|---------------|
| Description | 1,024 chars | 200-500 chars |
| Body (SKILL.md) | ~5,000 words | 1,500-2,000 words |
| References | As needed | 2,000-5,000 words |

## Hard Limits

Enforced by Claude Code:
- **Skill name**: 64 chars — YAML parse failure if exceeded
- **Description**: 1,024 chars — truncated silently

## Description Patterns

The description determines when the skill triggers. Two valid patterns:

### Pattern 1: USE WHEN (Direct)

```
[What it does]. USE WHEN [quoted trigger phrases]. [Additional context].
```

**Example:**
```yaml
description: Build and improve Claude Code skills. USE WHEN user says "create skill", "build skill", "new skill", "improve skill", or any request to create/modify skills.
```

**Key elements:**
- Quote specific trigger phrases users would say
- Use "OR" to chain multiple triggers
- Include verb variations ("create", "build", "make", "new")

### Pattern 2: Third-Person (Anthropic Style)

```
This skill should be used when the user asks to "[action]", "[action]", or needs guidance on [topic].
```

**Example:**
```yaml
description: This skill should be used when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", or needs guidance on hook development.
```

**Key elements:**
- Third-person framing ("This skill should be used when...")
- Quoted action phrases
- Ends with broader topic coverage

### Both patterns work. Pick one and be consistent.

## Directory

```
skill-name/
├── SKILL.md           # Required
├── workflows/         # Optional (for workflow routers)
├── tools/             # Optional
```

## Required Sections

### Examples (Recommended)

2-3 concrete usage patterns showing typical invocations. Helps model understand triggering scenarios.

```markdown
## Examples

**Example 1: [Use case name]**
```
User: "[Exact request phrasing]"
→ [Action skill takes]
→ [Outcome/result]
```

**Example 2: [Different use case]**
```
User: "[Different request phrasing]"
→ [Action skill takes]
→ [Outcome/result]
```
```

**Good examples:**
- Show different phrasings that trigger the skill
- Cover primary use cases (create, validate, improve)
- Keep each example 3-4 lines max

**Note:** Examples in SKILL.md are for triggering clarity. Detailed reference implementations go in exemplars (foundations) or reference/ directories.

### Workflow Routing (if skill has workflows)

```markdown
## Determine Action

| Intent | Keywords | Workflow |
|--------|----------|----------|
| Create | "create", "new" | `workflows/create.md` |

## Execute

1. Determine action from user's request
2. READ the appropriate workflow file
3. Follow workflow instructions exactly
```

## Foundations Loading Pattern

When a skill uses foundations (skill-foundations, prompt-foundations, visual-foundations, etc.):

**SKILL.md: INVOKE foundations**
```markdown
**INVOKE** `skill-foundations` for:
- Structure requirements
- Archetypes
- Exemplars
```

**Workflows: Reference directly (no INVOKE)**
```markdown
Use the archetype body pattern from skill-foundations.
Apply token efficiency patterns from prompt-foundations.
```

The SKILL.md INVOKE loads foundations into context. Workflows reference the already-loaded content without re-invoking.

## Body

Varies by archetype. See `archetypes.md`.
