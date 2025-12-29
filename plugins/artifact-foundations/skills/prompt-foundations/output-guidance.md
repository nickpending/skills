# Output Format Specification

How to specify output formats. Based on empirical analysis of 50+ agents/skills.

## Location and Timing

- PLACE output format section LAST in prompt (after instructions, examples, constraints)
- SPECIFY upfront in system prompt, not dynamically per-request
- USE dedicated `## Output Format:` section header

## Format Selection

### Markdown Prose + Sections

- IF task is analysis, review, report, or documentation
- THEN use markdown sections

```markdown
## Output Format:

- ## Summary (2-3 sentences)
- ## Findings (categorized)
- ## Recommendations (actionable)
```

### Severity-Grouped Lists

- IF task produces multiple findings (code review, security analysis)
- THEN group by severity with file:line references

```markdown
## Output Format:

## Critical Issues (confidence 90-100)
- `file:line` - [Issue] - [Impact] - [Fix]

## Major Issues (80-89)
- [Same structure]

## Minor/Recommendations
- [Suggestions]
```

### JSON

- IF output needs machine parsing (inter-agent, API responses)
- THEN specify JSON structure

```markdown
## Output Format:

{
  "status": "success|error",
  "findings": [{"file": "path", "line": N, "issue": "description"}],
  "summary": "string"
}
```

### Code Blocks

- IF task is code generation, test generation, scaffolding
- THEN specify target language and context style

```markdown
## Output Format:

Generate in [language]:
- Include context comments
- Show file path header
- Follow project conventions
```

### Tables

- IF task is comparison, decision matrix, specification
- THEN use table format

```markdown
## Output Format:

| Field | Current | Proposed | Impact |
|-------|---------|----------|--------|
```

## When to Specify vs Imply

**ALWAYS specify when:**
- Task produces structured findings
- Output needs machine parsing
- Multiple items/issues reported
- Generated code is deliverable
- Consumer is async/unknown

**IMPLIED (no spec needed) when:**
- Response is conversational
- Output is brief (< 3 sentences)
- Natural formatting sufficient

**Default:** Specify for anything non-trivial.

## Prefill Pattern

- IF must force specific format (JSON, arrays)
- THEN start assistant message with format opener

```
# Prefill with:
{
```

Forces JSON without preamble. USE sparingly (~10% of cases).

## Best Practices

### Analysis/Review

```markdown
## Output Format:

State what you're reviewing.

For each issue (confidence >= 80):
- `file:line` - [Description]
- [Why it matters]
- [Specific fix]

Group: Critical (90-100) → Major (80-89)

If no issues: Brief confirmation code meets standards.
```

### Generation

```markdown
## Output Format:

## [Type] Created

### Location
`path/to/file.ext`

### Contents
[Code block]

### Verification
[How to test]
```

### Inter-Agent

```markdown
## Output Format:

{
  "agent": "name",
  "status": "pending|completed|failed",
  "payload": { ... }
}
```

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| "Tell me what you find" | Specify exact sections and structure |
| "Clear format" | Show explicit structure |
| "Be brief but detailed" | Pick one, be specific |
| No output section | Always include for non-trivial tasks |

## Impact Data

- Format spec alone: +25% compliance
- Spec + 1-3 examples: ~95% correct first try
