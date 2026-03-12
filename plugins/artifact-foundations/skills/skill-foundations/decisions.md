# Feature Decisions

When to use which skill features. Each section is a decision point — read the one relevant to your situation.

## Fork or Inline?

**Fork (`context: fork`)** when:
- Skill needs isolation from conversation context
- Validation or analysis that shouldn't be influenced by prior messages
- Deterministic tasks with predictable input/output
- Parallel execution (multiple forked skills can run simultaneously)

**Inline (default)** when:
- Skill needs conversation context (what the user said, what was decided)
- Multi-step coordination with user interaction during execution
- Skill orchestrates other tools/skills and needs to see results
- Context from prior tool calls informs the skill's behavior

**Rule of thumb:** If the skill needs to know what happened before it was invoked, keep it inline. If it just needs input data and produces output, fork it.

## Restrict Tools?

**Yes** when:
- Skill should be read-only → `allowed-tools: Read, Grep, Glob`
- Skill wraps a specific CLI → `allowed-tools: Bash(npm *), Bash(npx *)`
- Preventing unintended side effects matters (analysis, validation, research)
- Skill runs in a context where broad tool access is risky

**No** when:
- Skill needs to create/edit files as part of its workflow
- Tool needs are unpredictable (general-purpose skills)
- Restriction would require listing too many tools to be practical

**Prefix matching:** `Bash(git *)` allows `git status`, `git diff`, etc. but blocks `rm`, `curl`, and everything else. Combine multiple: `Bash(git *), Bash(npm *), Read`.

## Dynamic Injection?

**Use `` !`command` ``** when:
- Skill needs live data before reasoning (git status, file listings, API responses)
- Data is cheap to fetch and small enough to inject inline
- Saving a tool call round-trip matters for responsiveness

**Don't use** when:
- Command output is large or unpredictable in size
- Command has side effects (mutations, network calls to non-idempotent endpoints)
- Data might not be available (command might fail) — failures replace the placeholder with error text

**Examples:**
```markdown
Current branch: !`git branch --show-current`
Changed files: !`git diff --name-only`
PR context: !`gh pr view --json title,body`
```

## Skill-Scoped Hooks?

**Use hooks in frontmatter** when:
- Skill needs its own lifecycle enforcement (security checks before tool use)
- Setup or teardown logic specific to this skill
- Audit logging for skill-specific operations
- Validation gates that only apply during this skill's execution

**Use `once: true`** when:
- One-time setup at skill start (check dependencies, verify config, warm up resources)
- The hook's purpose is initialization, not ongoing enforcement

**Don't use skill hooks** when:
- The enforcement should be global (put it in settings.json instead)
- The hook logic is complex enough to warrant a standalone hook file

**Syntax:**
```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
          once: true
```

## Model Selection?

**`model: haiku`** when:
- Fast, cheap, deterministic tasks
- Simple parsing, formatting, classification
- The skill doesn't need deep reasoning

**Default (omit `model`)** when:
- The skill uses the caller's model — usually what you want
- Complex analysis, code generation, multi-factor decisions

**Don't set `model`** to force a specific powerful model — let the caller decide. The skill should work across model tiers.

## Invocation Control?

**`disable-model-invocation: true`** when:
- Skill has side effects the user should explicitly trigger
- Dangerous operations (deploy, delete, force-push)
- Manual-only tools where auto-triggering would be surprising

**`user-invocable: false`** when:
- Internal skill used by orchestrators or other skills
- Shouldn't appear in user's `/` menu
- Claude invokes it programmatically based on context

**Default (both omitted)** when:
- Both user and Claude should be able to invoke — most skills

## Extended Thinking?

**Use `ultrathink`** when:
- Complex multi-factor analysis
- Decisions with many interacting constraints
- Deep code review or architectural reasoning
- Tasks where shallow reasoning produces wrong answers

**Don't use** when:
- Task is mechanical or deterministic
- Speed matters more than depth
- The skill is already forked with a fast model (`model: haiku`)

Place `ultrathink` anywhere in the skill content — even in a comment or heading. Its presence anywhere enables extended thinking for the entire invocation.
