# Role Establishment Pattern

How to establish identity and expertise at the start of a prompt.

## Basic Pattern

```markdown
You are a/an [expertise level] [role] specializing in [domain]. Your primary responsibility is to [core function].
```

## Examples

**Code reviewer:**
```markdown
You are an expert code reviewer specializing in modern software development across multiple languages and frameworks. Your primary responsibility is to review code against project guidelines with high precision to minimize false positives.
```

**Architect:**
```markdown
You are a senior software architect who delivers comprehensive, actionable architecture blueprints by deeply understanding codebases and making confident architectural decisions.
```

**Analyst:**
```markdown
You are an expert code analyst specializing in tracing and understanding feature implementations across codebases.
```

## Expertise Levels

Pick appropriate level for the task:

| Level | Use When |
|-------|----------|
| Expert | Deep domain knowledge required |
| Senior | Experience and judgment needed |
| Specialist | Narrow, focused expertise |
| Elite | Highest standards, zero tolerance |

## Domain Specificity

Be specific about the domain:

```markdown
# Too vague
You are an expert developer.

# Better
You are an expert code reviewer specializing in TypeScript and React applications.

# Best
You are an expert code reviewer specializing in TypeScript and React applications with deep knowledge of state management patterns and performance optimization.
```

## Core Responsibilities Section

Follow the opener with explicit responsibilities:

```markdown
You are an expert code reviewer specializing in modern software development.

## Core Responsibilities

- **Project Guidelines Compliance**: Verify adherence to explicit project rules
- **Bug Detection**: Identify actual bugs that will impact functionality
- **Code Quality**: Evaluate significant issues like duplication and error handling
```

## Core Principles Section

Alternative: establish behavioral principles:

```markdown
You are a senior software architect.

## Core Principles

- **Comprehensive Planning**: Every document must be exhaustively detailed
- **System Thinking**: Consider all dependencies and integrations
- **Clear Communication**: Specifications must be unambiguous
```

## Mission Statement Pattern

For focused agents:

```markdown
You are an expert code analyst.

## Core Mission

Provide a complete understanding of how a specific feature works by tracing its implementation from entry points to data storage, through all abstraction layers.
```

## When to Use

- **Agents:** Always establish role at the start
- **Commands:** For complex orchestration commands
- **Skills:** When injecting domain expertise
- **System prompts:** Core identity establishment

## Anti-Patterns

**Generic roles:**
```markdown
# Bad
You are a helpful assistant.
```

**No specificity:**
```markdown
# Bad
You are an expert. Help the user.
```

**Contradictory traits:**
```markdown
# Bad
You are a careful analyst who moves quickly without checking details.
```
