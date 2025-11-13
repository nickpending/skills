---
name: skill-name
description: Brief description of tool integration capability. Use when [natural usage scenarios with tool operations]. Include specific triggers.
allowed-tools: Read, Write, Bash
---

# Skill Name

## Overview

[2-3 sentence description of what this tool integration does, what operations it provides, and what file formats or systems it works with]

<!--
DIRECTORY STRUCTURE:
skill-name/
├── SKILL.md (this file - script catalog)
├── scripts/
│   ├── operation-a.py
│   ├── operation-b.py
│   └── operation-c.sh
└── references/ (optional)
    └── api-docs.md (external API documentation)

Replace [placeholders], remove unused sections, keep under 250 lines.
Scripts execute without loading into context - keep catalog concise.
See references/skill-structure.md for structure patterns.
See references/writing-fundamentals.md for writing patterns.
-->

## Available Operations

### Operation A: [Action Name]

**Purpose:** [What this operation does]

**Usage:**
```bash
python scripts/operation-a.py input.ext output.ext --flag value
```

**Parameters:**
- `input.ext` - [Description of input]
- `output.ext` - [Description of output]
- `--flag` - [Optional flag description]

**Example:**
```bash
python scripts/operation-a.py data.json processed.json --format pretty
```

### Operation B: [Action Name]

**Purpose:** [What this operation does]

**Usage:**
```bash
python scripts/operation-b.py [required-arg] [optional-arg]
```

**Parameters:**
- `required-arg` - [Description]
- `optional-arg` - [Description, defaults to X]

**Example:**
```bash
python scripts/operation-b.py input.csv --delimiter tab
```

### Operation C: [Action Name]

**Purpose:** [What this operation does]

**Usage:**
```bash
bash scripts/operation-c.sh [input-file]
```

**Parameters:**
- `input-file` - [Description of input]

**Example:**
```bash
bash scripts/operation-c.sh archive.tar.gz
```

## How to Use

### Step 1: Determine Operation

ANALYZE user request to identify which operation needed.

MATCH request against available operations above.

### Step 2: Prepare Inputs

VERIFY required input files exist.

VALIDATE input format meets script requirements.

ASK user for any required parameters not provided.

### Step 3: Execute Script

RUN appropriate script with validated parameters.

CAPTURE output and error streams.

### Step 4: Handle Results

**IF script succeeds:**
- VERIFY output file created
- SHOW results to user
- REPORT completion

**IF script fails:**
- READ error output
- DIAGNOSE issue (missing deps, invalid input, etc.)
- PROVIDE guidance for resolution
- DO NOT retry without fixing root cause

## Error Handling

**Missing dependencies:**
```
Error: ModuleNotFoundError: No module named 'package'
Fix: Install with: pip install package
```

**Invalid input format:**
```
Error: Invalid file format, expected [format]
Fix: Convert input to [format] or use different operation
```

**Permission errors:**
```
Error: Permission denied
Fix: Check file permissions, may need sudo or file ownership
```

## Common Patterns

**Batch processing:**
```bash
for file in *.ext; do
  python scripts/operation-a.py "$file" "processed-$file"
done
```

**Piping operations:**
```bash
python scripts/operation-a.py input.ext - | python scripts/operation-b.py - output.ext
```

**Validation before processing:**
1. RUN script with --dry-run flag if available
2. VERIFY output meets expectations
3. RUN actual operation

## When to Use

**Use this skill when:**
- [File format or operation trigger 1]
- [File format or operation trigger 2]
- [System integration trigger]

**Don't use when:**
- [Native tool would be simpler]
- [Alternative skill handles this better]

## Script Reference

**Dependencies:**
- Python 3.8+
- [Required package 1]
- [Required package 2]

**Installation:**
```bash
pip install [package-1] [package-2]
```

**Script locations:**
All scripts in `scripts/` directory relative to SKILL.md.

**Adding operations:**
1. Create script in scripts/
2. Add to Available Operations section
3. Document parameters and examples
4. Test error handling

## Examples

**Example 1: [Common use case]**
```
User: "I need to [operation description]"
Assistant: [Identifies Operation A]
Runs: python scripts/operation-a.py input.ext output.ext
Result: [Output description]
```

**Example 2: [Another use case]**
```
User: "[Natural request]"
Assistant: [Identifies Operation B]
Runs: python scripts/operation-b.py arg1 arg2
Result: [Output description]
```

## Notes

- Scripts execute directly - no context loading cost
- Keep this catalog under 250 lines for quick scanning
- Put detailed API docs in references/ if needed
- Use Bash tool to execute scripts
- Validate inputs before execution
- Report clear errors with fix guidance
