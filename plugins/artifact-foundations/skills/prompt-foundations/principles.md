# Prompt Engineering Principles

Apply these when writing prompts for skills, commands, agents, or system prompts.

## Core Principles

### 1. Be Clear and Direct

- IF instruction could confuse someone with no context, THEN rewrite it
- ALWAYS provide: what output is for, who audience is, what success looks like
- USE numbered steps for multi-step tasks
- EXPLAIN why behaviors matter, not just what to do
- SAY what to do, not what NOT to do

### 2. Use Examples (Few-Shot)

- IF task has specific output format, THEN provide 3-5 examples
- WRAP examples in `<example>` tags
- INCLUDE edge cases in examples
- MAKE examples diverse (different scenarios, not variations of same)

### 3. Assign Roles

- IF task requires domain expertise, THEN assign specific role
- BE specific: "senior security engineer at Fortune 500" not "security expert"
- PLACE role in system prompt or prompt opener

### 4. Use XML Tags

**WHEN to use XML tags:**
- IF prompt has multiple data sources (instructions + context + data), THEN use tags to separate
- IF you need Claude to output structured sections, THEN use tags Claude can mirror
- IF prompt exceeds ~500 words, THEN use tags for organization
- IF you'll post-process Claude's response, THEN request output in matching tags

**WHEN NOT to use XML tags:**
- Simple, short prompts
- Single-purpose instructions
- When natural language separation is clear enough

**Common tags:**
```
<instructions>What to do</instructions>
<context>Background information</context>
<data>Content to process</data>
<example>Sample input/output</example>
<thinking>Reasoning (for CoT)</thinking>
<answer>Final response</answer>
```

### 5. Enable Reasoning (Chain of Thought)

- IF task requires multi-step logic, math, or complex analysis, THEN request step-by-step thinking
- IF you need to see reasoning, THEN use `<thinking>` tags
- IF you only need final answer, THEN request thinking then answer separately

**Levels:**
- Simple: "Think step-by-step before answering"
- Structured: "Put your reasoning in `<thinking>` tags, then your answer in `<answer>` tags"

**Critical:** Thinking only happens when Claude OUTPUTS it.

## Directive Patterns

### Prefill Responses

- IF you need specific format, THEN start assistant message with format opener
- Prefill `{` for JSON, `[` for arrays, format headers for structured output

### Action vs Suggestion

- IF you want changes made, SAY "Make these changes" not "Suggest changes"
- IF you want recommendations only, SAY "Provide recommendations, do not modify"

### Emphasis

- AVOID aggressive language ("CRITICAL: You MUST...")
- USE direct statements: "Use this tool when..." not "You MUST use this tool"
- BOLD for emphasis, not caps-lock shouting

## Anti-Patterns

| Instead of | Do this |
|------------|---------|
| "Don't use markdown" | "Use flowing prose" |
| "You MUST always..." | "Always..." |
| Vague: "analyze this" | Specific: "identify security vulnerabilities in authentication flow" |
| "Maybe consider..." | "Do X" |
| Dozens of edge cases | 3-5 canonical examples |

## Application Checklist

BEFORE finalizing a prompt, verify:

- [ ] Instructions for model, not documentation for humans
- [ ] Instructions are specific and actionable
- [ ] Context explains purpose and audience
- [ ] Examples provided (if format matters)
- [ ] XML tags used (if complex/multi-part)
- [ ] Role assigned (if domain expertise needed)
- [ ] Chain of thought requested (if complex reasoning)
- [ ] Output format specified explicitly
- [ ] Action vs suggestion is clear
