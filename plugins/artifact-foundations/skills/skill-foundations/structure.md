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
          command: "./tools/check.sh"
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
| `agent` | string | — | Subagent type when `context: fork`. Values: `Explore`, `Plan`, `general-purpose`, `worker`. |
| `hooks` | object | — | Skill-scoped hooks. Same syntax as settings.json hooks. Only active during skill execution. |

### Argument Hints

Use angle brackets for required, square brackets for optional:

```yaml
argument-hint: <command> [options]              # CLI wrapper
argument-hint: bootstrap|sync|report [project]  # Workflow router with actions
argument-hint: <search|capture> [query]          # Action + freeform
argument-hint: [idea description]                # Pure freeform
```

Good hints show the **shape** of expected input. Bad hints restate the description.

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

**Pipe behavior:** Prefix matching applies to the full command string. `Bash(prismis-cli *)` matches `prismis-cli list --json | jq '...'` because the command starts with `prismis-cli`. Verify pipe behavior with your specific tool if critical — this is expected behavior but not explicitly guaranteed.

**Common restriction patterns:**

| Pattern | Use Case |
|---------|----------|
| `Bash(flux *)` | CLI wrapper for flux |
| `Read, Glob, Grep` | Read-only validator |
| `Read, Glob, Grep, Bash` | Validator that runs verification commands |
| `Read, Glob, Grep, Edit` | Validator that annotates files |
| `Read, Glob, Grep, Bash(lore *), Skill` | Processor that captures to lore and invokes skills |

### Model Selection

| Scenario | Model | Why |
|----------|-------|-----|
| Forked validator/checker | `haiku` | Procedural, structured I/O, speed matters |
| Forked processor | `haiku` | Multi-step but deterministic logic |
| Complex analysis | default (omit) | Needs reasoning depth |
| Creative/exploratory | default (omit) | Benefits from nuance |
| User-facing skill | default (omit) | Quality of output matters |

Don't set `model` to force a specific powerful model — let the caller decide. The skill should work across model tiers.

**Note:** `ultrathink` on haiku is wasted — extended thinking only benefits models with enough capacity to use the extra reasoning budget.

### Agent Type Selection

When using `context: fork`, the `agent` field controls subagent behavior:

| Agent | When | Characteristics |
|-------|------|-----------------|
| (omitted) | Most forked skills | Default subagent, general tool access |
| `worker` | Needs broad tool access + structured output | General-purpose execution |
| `Explore` | Codebase search and analysis | Optimized for Read/Grep/Glob patterns |
| `Plan` | Planning and decomposition | Structured planning output |

Most forked skills omit `agent` — the default is sufficient. Use `worker` when the skill needs general-purpose execution. Use `Explore` or `Plan` only when the skill's primary purpose aligns with that agent's specialization.

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

**Freeform arguments** — user types natural language, skill parses intent:
```markdown
## Workflow
1. Parse $ARGUMENTS for intent
2. Match against known operations
3. Execute appropriate flow
```

**Structured arguments** — orchestrator injects formatted blocks with labeled fields:
```markdown
## $ARGUMENTS
\```
TASK_NUMBER: {task number}
REPORT_PATH: {path to report}
BUILD_FLAGS: {"status": "complete", "verified": true}
\```
```

**Positional dispatch** — first argument is an action keyword:
```markdown
## Determine Action
Parse `$0` for the action keyword:
| `$0` | Flow |
|------|------|
| bootstrap | → Setup flow |
| sync | → Update flow |
| report | → Status flow |
```

### Environment Variables

| Variable | Description | Use Case |
|----------|-------------|----------|
| `${CLAUDE_SESSION_ID}` | Current session identifier | Correlation IDs for logging, agent tracking |
| `${CLAUDE_SKILL_DIR}` | Absolute path to the skill's directory | Portable references to supporting files |

**`${CLAUDE_SKILL_DIR}` — when to use:**

Use when the skill body contains tool calls (Read, Bash) that reference files inside the skill directory:
```markdown
# Good — tool call needs the path
READ ${CLAUDE_SKILL_DIR}/references/idea_template.md
RUN ${CLAUDE_SKILL_DIR}/tools/generate_id.py
```

Skip when supporting files are only mentioned descriptively:
```markdown
# Unnecessary — descriptive reference, model can resolve it
See the examples in references/ for inspiration.
```

**Rule of thumb:** If a tool call needs to find a file in the skill directory, use `${CLAUDE_SKILL_DIR}`. If you're just telling the model about the file, you don't need it.

## Dynamic Command Injection

Run shell commands and inject output into skill content before the model sees it.

**Syntax:** `` !`command` ``

```markdown
## Current State

- Branch: !`git branch --show-current`
- Recent changes: !`git log --oneline -5`
- PR context: !`gh pr view --json title,body`
```

The commands execute immediately when the skill loads. Output replaces the `` !`command` `` placeholder. If a command fails, the placeholder is replaced with the error.

**When to use:** When the skill needs live data (git state, API responses, file listings) as context before reasoning. Saves a tool call round-trip.

**When NOT to use:**
- Command output is large or unpredictable in size
- Command has side effects (mutations, network calls to non-idempotent endpoints)
- Data might not be available (command might fail)

**Trade-off:** Adds shell execution latency to skill load time. A skill that always runs `flux list` on load pays that cost even when the task count doesn't matter.

## Extended Thinking

Include the word `ultrathink` anywhere in skill content to enable Claude's extended thinking mode for that skill invocation.

```markdown
## Analysis

ultrathink

Analyze the following code for potential issues...
```

Useful for complex analysis, multi-factor decisions, or deep reasoning tasks. Don't use with `model: haiku` — extended thinking needs model capacity to be effective.

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
          command: "./tools/security-check.sh"
          once: true
  PostToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./tools/audit-log.sh"
---
```

### Supported Hook Types

| Type | Syntax | Description |
|------|--------|-------------|
| `command` | `command: "./script.sh"` | Run a shell command |
| `http` | `url: "https://..."` | Make an HTTP request |
| `prompt` | `prompt: "Evaluate: {{tool_input}}"` | Use Claude to evaluate (LLM-based) |
| `agent` | `prompt: "Review..." agent: code-reviewer` | Spawn an agent to evaluate |

**Command hook** (most common):
```yaml
- type: command
  command: "./tools/validate.sh"
```

**Prompt hook** (LLM evaluates):
```yaml
- type: prompt
  prompt: "Is this Bash command safe to run? Evaluate: {{tool_input.command}}"
```

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

### Forked Complexity Spectrum

Forked skills range from simple to complex:

- **Simple** (50-150 lines): Validators, checkers — structured input, JSON output, `model: haiku`
- **Complex** (200-400 lines): Processors, configurators — multi-step procedures, disk reads, conditional branching, `model: haiku` for procedural work

Both are valid. Forked skills don't compete for context budget (they load in isolation), so body length guidelines for main-thread skills don't apply. A 400-line forked skill is fine if the content is necessary.

## Return Formats

| Pattern | When | Example |
|---------|------|---------|
| Structured JSON | Forked validators, status checks | `{"valid": true, "issues": [...]}` |
| Markdown | Reports, summaries, findings | Formatted sections with headers |
| CLI output | CLI wrappers | Pass through tool output directly |
| Plain text | Simple responses | One-line confirmations |

Forked skills called by orchestrators should return structured output (JSON or markdown with predictable sections) so the caller can parse results programmatically.

Main-thread skills return naturally — the output is part of the conversation.

## Error Handling

When a forked skill fails:
- Shell command errors in dynamic injection replace the placeholder with error text
- Tool call failures surface to the skill as error responses
- Skill timeout terminates the subagent; the caller sees a timeout error

Design for graceful degradation:
- Check preconditions early (file exists, tool installed, required args present)
- Return structured error responses the caller can parse
- Use `once: true` hooks for setup validation rather than failing mid-execution
- For CLI wrappers: run `command --help` when unsure about syntax rather than guessing

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

**Note:** This budget applies to main-thread skill descriptions. Forked skill bodies load in isolation and don't count against the context budget.

### Nested Directory Discovery

When editing files in a subdirectory that contains `.claude/skills/`, those skills are automatically discovered. Skills in directories added via `--add-dir` get live change detection.

### Preloading Into Subagents

Skills can be preloaded into subagent context via the `skills` field on agent spawn. The subagent starts with those skills already available. Use this when an agent needs access to specific skills without the user explicitly invoking them.

## Length Guidelines

| Metric | Max | Best Practice |
|--------|-----|---------------|
| Description | 1,024 chars | 200-500 chars |
| Body (SKILL.md) | ~5,000 words | 1,500-2,000 words |
| References | As needed | 2,000-5,000 words |

**Forked skills exception:** Body length guidelines apply to main-thread skills competing for context budget. Forked skills load in isolation and can be longer (300-400 lines) without penalty.

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
├── tools/             # Optional — executable scripts and utilities
└── workflows/         # Optional — workflow procedures
```

### Workflow Files

Workflow files contain step-by-step procedures the SKILL.md dispatches to.

**Naming:** Match the action keyword or scenario that routes to the file. If `$0` dispatches `create`, the file is `workflows/create.md`. If routing is scenario-based, name matches the scenario: `workflows/discover.md`, `workflows/update.md`.

The dispatch table in SKILL.md and the workflow filenames must correspond:

```markdown
## Determine Action

| `$0` | Workflow |
|------|----------|
| create | `workflows/create.md` |
| improve | `workflows/improve.md` |
| sync | `workflows/sync.md` |
```

**Rules:**
- One file per dispatchable action — don't split an action across multiple files
- Use phases/headings within a workflow file for multi-step procedures
- Shared content referenced by multiple workflows → `references/` directory
- Workflow files are not independently invocable — they're loaded by SKILL.md

### Supporting Directories

| Directory | Contents | When to use |
|-----------|----------|-------------|
| `workflows/` | Step-by-step procedures dispatched by SKILL.md | Skill has multiple distinct actions or scenarios |
| `references/` | Supporting knowledge shared across workflows | Multiple workflows need the same context |
| `templates/` | File templates the skill creates from | Skill generates files with consistent structure |
| `tools/` | Executable scripts and utilities (Python, Bash) | Deterministic operations better handled by code than LLM |

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
