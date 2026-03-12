# Skill Structure

## Frontmatter

All fields optional except `name` and `description` (recommended).

```yaml
---
name: skill-name
description: [What it does]. USE WHEN [triggers]. [Additional context].
argument-hint: <feature> [project]
disable-model-invocation: false
user-invocable: true
allowed-tools: Read, Grep, Glob
model: haiku
context: fork
agent: Explore
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
---
```

### Field Reference

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | — | Skill identifier. 64 chars max, lowercase-hyphens. |
| `description` | string | — | Always in context. Drives auto-triggering. 1,024 chars max. |
| `argument-hint` | string | — | Shows in autocomplete after `/skill-name`. Describes expected arguments. |
| `disable-model-invocation` | boolean | `false` | When `true`, only user can invoke via `/skill-name`. Claude cannot auto-trigger. |
| `user-invocable` | boolean | `true` | When `false`, only Claude can invoke. Hidden from user's `/` menu. |
| `allowed-tools` | string | all | Comma-separated tool list. Restricts which tools the skill can use. Supports prefix matching: `Bash(npm *)`. |
| `model` | string | caller's model | Run skill with a specific model. e.g., `haiku` for fast/cheap tasks. |
| `context` | string | — | Set to `fork` for isolated subagent execution. Omit for main thread. |
| `agent` | string | — | Subagent type when `context: fork`. Values: `Explore`, `Plan`, `general-purpose`. |
| `hooks` | object | — | Skill-scoped hooks. Same syntax as settings.json hooks. Only active during skill execution. |

### Invocation Control

| Combination | Who can invoke | Use case |
|-------------|---------------|----------|
| defaults (both omitted) | User + Claude | Most skills |
| `disable-model-invocation: true` | User only | Manual-only tools, dangerous operations |
| `user-invocable: false` | Claude only | Internal skills used by other skills/orchestrators |
| both set | Invalid — don't do this | — |

### Tool Restrictions

```yaml
allowed-tools: Read, Grep, Glob          # Exact tool names
allowed-tools: Bash(npm *), Bash(bun *)  # Prefix matching
allowed-tools: Read, Bash(git *)         # Mixed
```

When `allowed-tools` is set, the skill can only use listed tools. All others are denied. Useful for read-only skills, CLI wrappers targeting specific commands, or sandboxed execution.

## Content Substitutions

Variables available in skill body text, replaced before the model sees content.

### Argument Variables

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | Full argument string passed to the skill |
| `$0` | First positional argument |
| `$1` | Second positional argument |
| `$N` | Nth positional argument (0-indexed) |

Arguments are split by whitespace. Quoted strings are preserved as single arguments.

### Environment Variables

| Variable | Description |
|----------|-------------|
| `${CLAUDE_SESSION_ID}` | Current session identifier |
| `${CLAUDE_SKILL_DIR}` | Absolute path to the skill's directory |

Use `${CLAUDE_SKILL_DIR}` to reference supporting files portably:
```markdown
Read the template at ${CLAUDE_SKILL_DIR}/templates/default.md
```

## Dynamic Command Injection

Run shell commands and inject output into skill content before the model sees it.

**Syntax:** `` !`command` ``

```markdown
## Current State

- Branch: !`git branch --show-current`
- Recent changes: !`git log --oneline -5`
- PR diff: !`gh pr diff`
```

The commands execute immediately when the skill loads. Output replaces the `` !`command` `` placeholder. If a command fails, the placeholder is replaced with the error.

**When to use:** When the skill needs live data (git state, API responses, file listings) as context before reasoning. Saves a tool call round-trip.

**Trade-off:** Adds shell execution latency to skill load time.

## Extended Thinking

Include the word `ultrathink` anywhere in skill content to enable Claude's extended thinking mode for that skill invocation.

```markdown
## Analysis

ultrathink

Analyze the following code for potential issues...
```

Useful for complex analysis, multi-factor decisions, or deep reasoning tasks.

## Skill-Scoped Hooks

Define hooks that only run while the skill is active. Same syntax as settings.json hooks, nested under the `hooks` frontmatter field.

```yaml
---
name: secure-deploy
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
          once: true
  PostToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/audit-log.sh"
---
```

### Supported Hook Types

| Type | Description |
|------|-------------|
| `command` | Run a shell command |
| `http` | Make an HTTP request |
| `prompt` | Use Claude to evaluate (LLM-based) |
| `agent` | Spawn an agent to evaluate |

### The `once` Flag (Skills Only)

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./setup.sh"
          once: true
```

When `once: true`, the hook runs once per session then auto-removes. Not available on agents — skills only.

**Use case:** One-time setup, environment validation, dependency checks at skill start.

## Execution Modes

### Non-Forked (Default)

Skill runs in the main conversation thread.

- Full conversation context available
- Can reference prior messages, decisions, tool results
- Shares the caller's tool permissions
- Good for: coordination, multi-step user interaction, context-dependent work

### Forked (`context: fork`)

Skill runs in an isolated subagent context.

```yaml
---
context: fork
agent: Explore
---
```

- No conversation history
- Isolated tool permissions
- Focused execution without context pollution
- Good for: validation, analysis, deterministic tasks, parallel execution

The `agent` field controls the subagent type:
- `Explore` — codebase search and analysis
- `Plan` — planning and decomposition
- `general-purpose` — default, no specialization

## Discovery & Loading

### Resolution Order (Same-Name Priority)

```
Enterprise settings (if configured)
  ↓
Personal ~/.claude/skills/
  ↓
Project ./.claude/skills/
  ↓
Plugin skills (namespace: plugin-name:skill-name)
```

Higher priority wins on name collision.

### What Gets Loaded When

| Content | When | Budget |
|---------|------|--------|
| Descriptions (frontmatter) | Always in context | 2% of context window, min 16K chars |
| Full skill content (SKILL.md body) | On invocation only | — |
| Supporting files | On-demand when referenced | — |

If skills exceed the context budget, Claude warns "Excluded skills from context."

### Nested Directory Discovery

When editing files in a subdirectory that contains `.claude/skills/`, those skills are automatically discovered. Skills in directories added via `--add-dir` get live change detection.

### Preloading Into Subagents

Skills can be preloaded into subagent context via the `skills` field on agent spawn. The subagent starts with those skills already available.

## Length Guidelines

| Metric | Max | Best Practice |
|--------|-----|---------------|
| Description | 1,024 chars | 200-500 chars |
| Body (SKILL.md) | ~5,000 words | 1,500-2,000 words |
| References | As needed | 2,000-5,000 words |

## Description Patterns

The description determines when the skill triggers. Two valid patterns:

### Pattern 1: USE WHEN (Direct)

```
[What it does]. USE WHEN [quoted trigger phrases]. [Additional context].
```

```yaml
description: Build and improve Claude Code skills. USE WHEN user says "create skill", "build skill", "new skill", "improve skill", or any request to create/modify skills.
```

- Quote specific trigger phrases users would say
- Use "or" to chain multiple triggers
- Include verb variations ("create", "build", "make", "new")

### Pattern 2: Third-Person (Anthropic Style)

```
This skill should be used when the user asks to "[action]", "[action]", or needs guidance on [topic].
```

Both patterns work. Pick one and be consistent.

## Directory

```
skill-name/
├── SKILL.md           # Required — main instructions
├── reference.md       # Optional — supporting content
├── templates/         # Optional — file templates
├── scripts/           # Optional — helper scripts
└── workflows/         # Optional — workflow procedures
```

## Foundations Loading Pattern

When a skill uses foundations (skill-foundations, prompt-foundations, etc.):

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
```

The SKILL.md INVOKE loads foundations into context. Workflows reference already-loaded content without re-invoking.

## Body

Varies by archetype. See `archetypes.md` for templates per pattern.
See `decisions.md` for guidance on which features to use when.
