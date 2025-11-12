---
name: skill-name
description: Brief description of templates provided. Use when [natural scenarios for template generation or boilerplate creation]. Include specific triggers.
allowed-tools: Read, Write, Edit, AskUserQuestion
---

# Skill Name

## Overview

[2-3 sentence description of what templates this skill provides, when they're used, and what they generate]

<!--
DIRECTORY STRUCTURE:
skill-name/
├── SKILL.md (this file - asset catalog + customization)
├── assets/
│   ├── template-a/
│   │   ├── file1.ext
│   │   └── file2.ext
│   ├── template-b/
│   │   ├── structure/
│   │   └── files.ext
│   └── boilerplate-c.ext
└── references/ (optional)
    └── customization-guide.md (detailed customization patterns)

Replace [placeholders], remove unused sections, keep under 250 lines.
Assets copy directly - keep catalog clear and usage guide focused.
See references/skill-structure.md for structure patterns.
See references/writing-fundamentals.md for writing patterns.
-->

## Available Templates

### Template A: [Template Name]

**Purpose:** [What this template generates]

**Location:** `assets/template-a/`

**Structure:**
```
template-a/
├── file1.ext ([description])
├── file2.ext ([description])
└── config.ext ([description])
```

**Use when:**
- [Scenario 1]
- [Scenario 2]

**Customization points:**
- `[PROJECT_NAME]` - Project or application name
- `[AUTHOR]` - Author or organization
- `[DESCRIPTION]` - Project description
- `[OPTION]` - Configuration option

### Template B: [Template Name]

**Purpose:** [What this template generates]

**Location:** `assets/template-b/`

**Structure:**
```
template-b/
├── structure/
│   ├── core/
│   └── optional/
└── config.ext
```

**Use when:**
- [Scenario 1]
- [Scenario 2]

**Customization points:**
- `[VAR_1]` - Description
- `[VAR_2]` - Description
- `[VAR_3]` - Description

### Boilerplate C: [Template Name]

**Purpose:** [What this boilerplate provides]

**Location:** `assets/boilerplate-c.ext`

**Use when:**
- [Scenario 1]
- [Scenario 2]

**Customization points:**
- `[PLACEHOLDER_1]` - Description
- `[PLACEHOLDER_2]` - Description

## How to Use

### Step 1: Determine Template

ASK user about requirements to select appropriate template:
- "What are you building?"
- "What structure do you need?"
- "Any specific requirements or constraints?"

MATCH requirements against available templates above.

### Step 2: Gather Customization Values

ASK user for customization values using AskUserQuestion:
- Question: "What should I name [PROJECT/COMPONENT]?"
- Question: "What [OPTION] do you prefer?"
- Question: "[Other customization point]?"

COLLECT all values before proceeding.

### Step 3: Copy and Customize

READ template files from `assets/[template]/`

REPLACE all `[PLACEHOLDER]` markers with collected values:
- `[PROJECT_NAME]` → {user_provided_name}
- `[AUTHOR]` → {user_provided_author}
- etc.

WRITE customized files to user's target location.

### Step 4: Verify and Report

VERIFY all files created successfully.

LIST generated files with paths.

PROVIDE next steps or usage instructions.

## Customization Patterns

### Simple Substitution

Replace placeholders directly:
```
[PROJECT_NAME] → UserProject
[AUTHOR] → John Doe
```

### Conditional Sections

Some templates have optional sections marked:
```
<!-- OPTIONAL: Feature X
[Feature X code]
-->
```

ASK user if optional features wanted, remove markers if included, delete section if not.

### Configuration Options

Templates may have multiple variants:
```
[DATABASE: postgres|mysql|sqlite]
```

ASK user to select from options, include appropriate variant.

## Common Use Cases

### Use Case 1: [Scenario Name]

**Template:** Template A

**Steps:**
1. Select Template A
2. Gather: [required values]
3. Customize and generate
4. Result: [what gets created]

### Use Case 2: [Scenario Name]

**Template:** Template B

**Steps:**
1. Select Template B
2. Gather: [required values]
3. Customize structure if needed
4. Result: [what gets created]

### Use Case 3: [Scenario Name]

**Template:** Boilerplate C

**Steps:**
1. Select Boilerplate C
2. Gather: [required values]
3. Insert into existing project
4. Result: [what gets added]

## When to Use

**Use this skill when:**
- [Template generation trigger 1]
- [Boilerplate need trigger 2]
- [Project setup trigger 3]

**Choose Template A when:**
- [Condition 1]
- [Condition 2]

**Choose Template B when:**
- [Different condition 1]
- [Different condition 2]

**Choose Boilerplate C when:**
- [Specific need 1]
- [Specific need 2]

## Examples

**Example 1: [Common scenario]**
```
User: "I need to [create/generate X]"
Assistant: [Selects Template A]
Asks: [Customization questions]
Generates: [Output structure]
Result: [Files created at target location]
```

**Example 2: [Another scenario]**
```
User: "[Natural request for template]"
Assistant: [Selects Template B]
Asks: [Configuration questions]
Generates: [Output structure]
Result: [Files created with customization]
```

## Template Maintenance

**Adding templates:**
1. Create template in assets/
2. Use `[PLACEHOLDER]` for customization points
3. Add to Available Templates section
4. Document structure and use cases
5. Test customization flow

**Template variables:**
- Use `[CAPS_SNAKE_CASE]` for placeholders
- Document all placeholders in template section
- Keep placeholders semantic and clear
- Avoid ambiguous names

**Optional sections:**
- Mark with HTML comments
- Explain what feature they provide
- Make removal clean (no broken references)

## Notes

- Assets copy without context loading - efficient
- Keep SKILL.md under 250 lines for quick scanning
- Put detailed customization guides in references/
- Use AskUserQuestion for structured input
- Validate user input before substitution
- Test generated output works immediately
- Provide clear next steps after generation
