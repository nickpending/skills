# Claude Code Primitives

When to use each primitive for building Claude Code artifacts.

## The Primitives

| Primitive | Loads | Context | Invocation |
|-----------|-------|---------|------------|
| CLAUDE.md | Always | Main | Automatic |
| Skill | On description match | Main | Automatic |
| Command | On `/invoke` | Main | Manual |
| Subagent | On delegation | Isolated | Auto/Manual |
| Hook | On event | External | Automatic |

## Decision Tree

```
Is this needed for EVERY conversation?
├─ Yes → CLAUDE.md
└─ No → Continue

Is this triggered automatically by task type?
├─ Yes → Skill
└─ No → Continue

Do I need explicit control over when it runs?
├─ Yes → Slash command
└─ No → Continue

Does this need isolated context or parallel execution?
├─ Yes → Subagent
└─ No → Continue

Is this event-driven automation?
├─ Yes → Hook
└─ No → Probably CLAUDE.md or skill
```

## CLAUDE.md

**What:** Files loaded at conversation start, always present.

**Use for:**
- Project identity and structure
- Coding conventions that apply everywhere
- Critical rules that must never be forgotten

**Avoid:**
- Large reference docs (wastes tokens when irrelevant)
- Task-specific instructions (use skills instead)

## Skills

**What:** Portable expertise, auto-loaded when description matches user request.

**Use for:**
- Domain knowledge (brand guidelines, API patterns)
- Repeatable procedures (PR formatting, data analysis)
- Template-driven output (reports, newsletters)

**Key insight:** Description determines when skill triggers. Be specific with USE WHEN triggers.

## Slash Commands

**What:** User-invoked prompts for specific tasks.

**Use for:**
- Standardized procedures (commit, PR, deploy)
- Priming/context loading
- Operations you want explicit control over

**Key insight:** Commands = explicit invocation. Skills = automatic detection.

## Subagents

**What:** Isolated executors with their own context.

**Use for:**
- Complex multi-step work (security audits, TDD)
- Tasks needing deep focus without main context pollution
- Parallel processing (multiple reviewers)
- Restricted operations (read-only code review)

**Characteristics:**
- Fresh context for each invocation
- Custom model selection (can use cheaper models)
- Tool restrictions possible
- Can run in parallel
- Context discarded after completion

## Hooks

**What:** Event-driven automation running on specific events.

**Events:** session-start, user-prompt-submit, pre-tool-use, post-tool-use, stop, subagent-stop

**Use for:**
- Context injection (paths, metadata)
- Observability (logging, metrics)
- Output processing (extract markers from responses)
- Enforcing rules (blocking operations)

**Not for:**
- Complex synchronous logic (slows every message)
- Replacing skills (hooks don't have full context)

## Skill vs Subagent?

| Factor | Skill | Subagent |
|--------|-------|----------|
| Context | Main window | Isolated |
| Follow-up | Easy | New invocation |
| Parallel | No | Yes |
| Tool restriction | No | Yes |
| Best for | Knowledge | Execution |

**Rule of thumb:**
- Teaching expertise any agent can apply → Skill
- Independent task with specific permissions → Subagent

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Context bloat | Loading everything "just in case" | Progressive disclosure, specific descriptions |
| Monolithic skills | One skill with 10k tokens | Split into focused skills |
| Skill/Command confusion | Skills for user-initiated tasks | Skills = auto-detected, Commands = explicit |
| Subagent overuse | Spawning subagent for simple tasks | Simple tasks stay in main context |
| Hook complexity | Complex logic slowing every message | Hooks should be fast; offload to skills |
