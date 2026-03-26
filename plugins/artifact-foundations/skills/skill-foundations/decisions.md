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

### Fork Complexity

Simple fork (50-150 lines):
- Validators, checkers, classifiers
- Structured input → structured output
- `model: haiku` is appropriate

Complex fork (200-400 lines):
- Processors, configurators, synthesizers
- Multi-step procedures with disk reads and conditional branching
- `model: haiku` works for procedural tasks; use default for tasks requiring deep reasoning

**Key consideration:** Forked skills read ALL context from disk. If the skill needs 5+ files to do its job, that's fine — but each Read call adds latency. Design structured `$ARGUMENTS` to tell the skill exactly which files to read rather than making it discover them.

## Restrict Tools?

**Yes** when:
- Skill should be read-only → `allowed-tools: Read, Grep, Glob`
- Skill wraps a specific CLI → `allowed-tools: Bash(flux *)`
- Preventing unintended side effects matters (analysis, validation, research)
- Skill runs in a context where broad tool access is risky

**No** when:
- Skill needs to create/edit files as part of its workflow
- Tool needs are unpredictable (general-purpose skills)
- Restriction would require listing too many tools to be practical

**Prefix matching:** `Bash(git *)` allows `git status`, `git diff`, etc. but blocks `rm`, `curl`, and everything else. Combine multiple: `Bash(git *), Bash(npm *), Read`.

**Pipe behavior:** Prefix matching applies to the full command string. `Bash(prismis-cli *)` matches `prismis-cli list --json | jq '...'` because the command starts with `prismis-cli`. This is expected behavior but not explicitly guaranteed — verify if critical.

**Common restriction patterns from real skills:**

| Pattern | Use Case | Example Skill |
|---------|----------|---------------|
| `Bash(flux *)` | CLI wrapper | flux |
| `Bash(lore *)` | CLI wrapper | lore |
| `Read, Glob, Grep` | Read-only validator | validate-plan, validate-decomposition |
| `Read, Glob, Grep, Bash` | Validator with execution | validate-iteration, validate-test |
| `Read, Glob, Grep, Edit` | Validator with annotation | validate-build |
| `Read, Glob, Grep, Bash(lore *), Skill` | Processor with lore + skills | synthesize-learnings |

## Dynamic Injection?

**Use `` !`command` ``** when:
- Skill needs live data before reasoning (git status, file listings, API responses)
- Data is cheap to fetch and small enough to inject inline
- Saving a tool call round-trip matters for responsiveness

**Don't use** when:
- Command output is large or unpredictable in size
- Command has side effects (mutations, network calls to non-idempotent endpoints)
- Data might not be available (command might fail) — failures replace the placeholder with error text

**Trade-off:** Every injected command adds latency to skill load time. A skill that always runs `flux list` on load pays that cost even when the task count doesn't matter for the current invocation.

**Good candidates:**
```markdown
Branch: !`git branch --show-current`            # Near-instant, always relevant
Dir exists: !`test -d /path && echo yes || echo no`  # Near-instant, gates all flows
Changed files: !`git diff --name-only`           # Small output, useful context
```

**Bad candidates:**
```markdown
Full diff: !`git diff`                           # Unbounded output size
API call: !`curl https://api.example.com/data`   # Network latency, might fail
Task list: !`flux list`                          # Only useful for some invocations
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

**CLI tool verification pattern:**
```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "command -v flux >/dev/null || echo 'BLOCK: flux CLI not installed'"
          once: true
```

## Model Selection?

**`model: haiku`** when:
- Forked validators and checkers — procedural, structured I/O
- Forked processors — multi-step but deterministic logic
- Simple parsing, formatting, classification
- Speed and cost matter more than depth

**Default (omit `model`)** when:
- Complex analysis or reasoning required
- Creative or exploratory tasks
- User-facing skills where output quality matters
- The skill uses the caller's model — usually what you want

**Don't set `model`** to force a specific powerful model — let the caller decide.

**Note:** `ultrathink` on haiku is wasted. Extended thinking only benefits models with enough capacity to use the extra reasoning budget. If a skill needs both `model: haiku` and deep reasoning, that's a signal to drop haiku.

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
- The skill is already forked with `model: haiku` — extended thinking is wasted on haiku

Place `ultrathink` anywhere in the skill content — even in a comment or heading. Its presence anywhere enables extended thinking for the entire invocation.

## Agent Type Selection?

When using `context: fork`, the `agent` field controls subagent behavior:

| Agent | When | Characteristics |
|-------|------|-----------------|
| (omitted) | Most forked skills | Default subagent, general tool access |
| `worker` | Needs broad tool access + structured output | General-purpose execution |
| `Explore` | Codebase search and analysis | Optimized for Read/Grep/Glob patterns |
| `Plan` | Planning and decomposition | Structured planning output |

**Most forked skills omit `agent`** — the default is sufficient. Use `worker` when the skill needs general-purpose execution with no specialization. Use `Explore` or `Plan` only when the skill's primary purpose aligns with that agent's specialization.

## When to Split Into Supporting Files?

**Keep inline** when:
- Skill is under ~200 lines (main-thread) or ~400 lines (forked)
- All content is needed every invocation
- Splitting would just be cosmetic (no independently reusable sections)

**Split into supporting files** when:
- Individual workflows/templates are reusable by other skills
- Content is conditionally loaded (not needed every invocation)
- Skill exceeds guidelines and has naturally separable sections

**Split candidates** (see `structure.md` Directory section for naming conventions):
- Workflow procedures → `workflows/create.md`, `workflows/sync.md` (name matches dispatch keyword)
- Templates → `templates/default.md`
- Reference data → `references/patterns.md`
- Executable utilities → `tools/validate.py`, `tools/generate.sh`

**Reference with `${CLAUDE_SKILL_DIR}`:**
```markdown
READ ${CLAUDE_SKILL_DIR}/workflows/setup.md
```

**Note:** Forked skills pay latency for each Read call to supporting files. If a forked skill needs all its content every time, keeping it in one file is faster than splitting and re-reading.

## Structured vs Freeform Arguments?

**Freeform (`$ARGUMENTS` as natural language)** when:
- User invokes directly with varying intent
- Skill parses intent from natural language
- Examples: CLI wrappers, ideation, exploration

**Structured (`$ARGUMENTS` as formatted blocks)** when:
- Orchestrator invokes programmatically with specific data
- Skill needs multiple distinct inputs (paths, flags, config)
- Examples: validators, processors, synthesizers

**Structured pattern:**
```markdown
## $ARGUMENTS
\```
TASK_NUMBER: {task number}
REPORT_PATH: {path to report}
BUILD_FLAGS: {"status": "complete", "verified": true}
\```
```

**Positional (`$0`, `$1`) dispatch** when:
- First argument is an action keyword
- Remaining arguments are parameters
- Examples: workflow routers (`bootstrap|sync|report`)

## Feature Combinations

Tested combinations from real skills:

| Recipe | Features | Example Skills |
|--------|----------|----------------|
| CLI Wrapper | `allowed-tools: Bash(tool *)` + `argument-hint` | flux, lore, prismis |
| Lifecycle Manager | `argument-hint` (action keywords) + inline + user-invocable | architecture, build-notes |
| Read-Only Validator | `fork` + `haiku` + `allowed-tools: Read,Glob,Grep` + `user-invocable: false` | validate-plan, validate-decomposition |
| Validator with Execution | Above + `Bash` + `agent: worker` | validate-build, validate-test |
| Forked Processor | `fork` + `haiku` + specific `allowed-tools` + `Skill` + `user-invocable: false` | synthesize-learnings |
| Forked Configurator | `fork` + `haiku` + `allowed-tools` + `user-invocable: false` | configure-quality |
| Reference Library | `disable-model-invocation: true` + content routing table | skill-foundations, visual-foundations |

These are proven patterns. When building a new skill that fits one of these profiles, start with the recipe and adjust.

## Task Tracking for Multi-Step Flows?

**Use TaskCreate to gate major steps** when:
- Skill has 3+ sequential steps that must all complete
- Steps have dependencies (Step 2 needs Step 1's output)
- Skipping a step would produce incorrect or incomplete results
- The skill is a Workflow Router, Forked Workflow, or multi-step CLI Wrapper

**Don't use** when:
- Skill is stateless knowledge injection (no steps to track)
- Skill is a Foundations reference (no execution flow)
- Skill has only 1-2 trivial steps where tracking adds overhead without value

**Why:** TaskCreate is behavioral enforcement, not progress tracking. Models follow through on multi-step flows more reliably when each gate requires explicit task completion. Without it, steps get skipped silently or the model claims completion without hitting every gate.

**Pattern — embed in skill body:**
```markdown
## Process

Create a task for each major step before starting work:

1. TaskCreate: "Step 1 — Read inputs"
2. TaskCreate: "Step 2 — Analyze/transform"
3. TaskCreate: "Step 3 — Write outputs"
4. TaskCreate: "Step 4 — Return result"

Mark each task complete as you finish it. Do not proceed to the next step until the current task is marked complete.
```

**Which archetypes need it:**

| Archetype | Task Tracking | Why |
|-----------|--------------|-----|
| CLI Wrapper | When multi-step | Simple wrappers don't need it; pipelines do |
| Workflow Router | Yes | Multiple flows with sequential steps |
| Forked Workflow | Yes | Multi-step procedures are the whole point |
| Forked Validator | When 4+ checks | Simple validators are fine without; complex ones benefit |
| Knowledge Injection | No | No execution flow |
| Foundations | No | No execution flow |
