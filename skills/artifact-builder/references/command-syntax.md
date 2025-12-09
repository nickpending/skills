# Slash Command Syntax Reference

Claude Code slash commands support special syntax for context injection, arguments, and configuration.

## Frontmatter Options

```yaml
---
description: What the command does (required for discovery)
allowed-tools: Tool restrictions (e.g., Bash(git:*), Read, Write)
model: Force specific model (haiku, sonnet, opus, inherit)
argument-hint: Help text shown for arguments (e.g., [feature description])
---
```

## Inline Syntax

### Command Arguments
Access arguments passed to the command:
- `$ARGUMENTS` - All arguments as single string
- `$1`, `$2`, etc. - Positional arguments

```markdown
## Variables
USER_REQUEST: $ARGUMENTS
FILE_PATH: $1
```

### Command Injection (Preprocessed)
Execute commands and inject output before model sees the prompt:

```markdown
## Context
- Git status: !`git status`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`
```

The `!` backtick syntax runs during preprocessing - output is already present when the model processes the command.

### File Include
Include file contents directly:

```markdown
## Context
- SSH config: @~/.ssh/config
- Project config: @./config.toml
```

## Patterns by Command Type

### Minimal Procedural (18-25 lines)
Single-purpose commands with immediate execution:
```markdown
---
allowed-tools: Bash(git:*)
description: Create a git commit
---

## Context
- Git status: !`git status`
- Git diff: !`git diff HEAD`

## Task
Based on the above, create a commit with appropriate message.
```

### Priming Command (40-60 lines)
Load state, report readiness, wait for direction:
```markdown
---
description: Prime network context
---

## Instructions
- Load device inventory and topology
- Index by hostname, IP, services
- After priming, wait for commands

## Workflow
1. Read inventory: !`cat ~/.local/share/app/inventory.json`
2. Extract mappings with jq
3. Report readiness

## Report
Confirm indexed: hosts, services, network segments
```

### Workflow Command (30-50 lines)
Conditional logic with variables and reporting:
```markdown
---
description: Process documentation files
allowed-tools: Task, WebFetch, Write
---

## Variables
CACHE_HOURS: 24
OUTPUT_DIR: docs/

## Workflow
1. Check if files exist and are recent
2. If stale, fetch and update
3. Report results

## Report Format
- ✅ Success: [url] - [file]
- ❌ Failed: [url] - [reason]
```

### Multi-Phase Orchestration (80-150 lines)
Complex workflows with user checkpoints:
```markdown
---
description: Guided feature development
argument-hint: [feature description]
---

## Core Principles
- Ask clarifying questions before implementing
- Use TodoWrite to track progress

## Phase 1: Discovery
**Goal**: Understand requirements
Initial request: $ARGUMENTS
...

## Phase 2: Exploration
**Goal**: Understand codebase
Launch explorer agents...
...

## Phase N: Summary
**Goal**: Document results
```

## Tool Restrictions

Limit available tools for safety:
```yaml
# Specific commands only
allowed-tools: Bash(git add:*), Bash(git commit:*), Bash(git push:*)

# Read-only
allowed-tools: Read, Glob, Grep

# Multiple tool types
allowed-tools: Read, Write, Edit, Bash(npm:*), Task
```

## Best Practices

1. **Use `!` backticks for dynamic context** - Git status, file contents, command output
2. **Define variables at top** - Makes configuration clear and editable
3. **Include report format** - Standardizes output across runs
4. **Restrict tools appropriately** - Limit scope to what's needed
5. **Add argument hints** - Help users understand expected input
