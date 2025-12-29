# Conditional Execution Pattern

General-purpose pattern for branching logic in prompts. Works in skills, commands, agents, and system prompts.

## IF-THEN-EXAMPLES Syntax

```markdown
### [Branch Name]

- IF: [condition to check] AND [optional second condition]
- THEN: [action to take]
- EXAMPLES:
  - "[trigger phrase 1]"
  - "[trigger phrase 2]"
  - "[trigger phrase 3]"
```

## Complete Example

```markdown
## Cookbook

### Claude Code

- IF: The user requests a claude code agent AND `ENABLE_CLAUDE_CODE` is true.
- THEN: READ and execute: `cookbook/claude-code.md`
- EXAMPLES:
  - "fork terminal use claude code to <xyz>"
  - "spin up a new terminal using claude code"
  - "create a new terminal with claude code"

### Raw CLI

- IF: The user requests a non-agentic tool AND `ENABLE_RAW_CLI` is true.
- THEN: READ and execute: `cookbook/cli-command.md`
- EXAMPLES:
  - "Create a new terminal with ffmpeg"
  - "fork terminal using curl"
```

## Key Elements

**IF clause:**
- State the condition clearly
- Use AND for compound conditions
- Reference variables with backticks: `ENABLE_X`

**THEN clause:**
- Use action verbs: READ, EXECUTE, RUN, LOAD
- Specify exact file paths
- Be explicit about what happens

**EXAMPLES clause:**
- 2-4 concrete trigger phrases
- Show variations users might say
- Helps model pattern-match

## Feature Flag Pattern

Combine with variables for toggleable features:

```markdown
## Variables

ENABLE_HTTPX: true
ENABLE_NAABU: true
ENABLE_KATANA: false  # Not installed

## Tool Configuration

### HTTP Probing

- IF: task requires HTTP analysis AND `ENABLE_HTTPX` is true
- THEN: READ `config/httpx.md`
- EXAMPLES:
  - "probe the target"
  - "check what's running on port 80"

### Port Scanning

- IF: task requires port discovery AND `ENABLE_NAABU` is true
- THEN: READ `config/naabu.md`
- EXAMPLES:
  - "scan for open ports"
  - "find services"
```

## When to Use

- **Routing:** Different workflows based on user intent
- **Feature toggles:** Enable/disable capabilities
- **Tool selection:** Choose between multiple tools
- **Mode switching:** Different behavior based on context

## Anti-Patterns

**Vague conditions:**
```markdown
# Bad
- IF: user wants something done
- THEN: do it
```

**Missing examples:**
```markdown
# Bad - no EXAMPLES clause
- IF: user requests claude code
- THEN: use claude code
```

**Nested conditionals:** Split into separate branches instead of nesting IF statements.
