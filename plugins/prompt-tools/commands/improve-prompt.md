---
description: Improve an existing prompt using prompt engineering principles
argument-hint: [prompt text or file path]
---

# Improve Prompt

Analyze and improve a prompt using prompt-foundations principles.

## Input

**Prompt to improve:** $ARGUMENTS

IF input is a file path, READ the file.
IF no input, ASK user to paste the prompt.

## Workflow

### 1. Analyze Current Prompt

IDENTIFY:
- What is it trying to accomplish?
- What patterns is it using (or missing)?
- Where is it vague, verbose, or unclear?

### 2. Load Principles

**INVOKE** `prompt-foundations` — read `principles.md`.

### 3. Apply Improvements

CHECK against each principle:

| Principle | Check | Fix |
|-----------|-------|-----|
| Clear/direct | Hedging words? ("maybe", "might", "could") | Remove, be direct |
| Examples | Ambiguous task without examples? | Add 1-2 examples |
| Role | Needs domain expertise? | Add "You are a..." |
| XML tags | Complex multi-part input? | Add `<section>` tags |
| Output format | Format unspecified or buried? | Add explicit format section LAST |
| Reasoning | Hard problem, one-shot? | Add "Think step by step" |

### 4. Restructure if Needed

IF prompt is >200 words and unstructured:
- Add section headers
- Use bullets over prose
- Move output format to end

### 5. Deliver

OUTPUT the improved prompt in a code block.

LIST changes made:
```
- [Change 1]: [Reason]
- [Change 2]: [Reason]
```
