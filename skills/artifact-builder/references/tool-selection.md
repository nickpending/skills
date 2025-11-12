# Tool Selection Reference

Sharp patterns for selecting tools based on command purpose and operations.

## Available Tools

### File Operations
- **Read** - View file contents, parse data structures
- **Write** - Create new files, overwrite existing
- **Edit** - Modify existing files with exact string replacement
- **Glob** - Find files by pattern (*.ts, **/*.md)
- **Grep** - Search file contents by regex

### Execution
- **Bash** - Run shell commands, git operations, build tools
- **Task** - Launch specialized subagents (code-reviewer, architecture-analyst)

### Interaction
- **AskUserQuestion** - Structured multiple-choice questions (1-4 at a time)

## Selection Logic by Operation

### Reading and Analysis

**Read single known file:**
```yaml
allowed-tools: Read
```
Examples: "Show me the config", "What's in README"

**Find then read:**
```yaml
allowed-tools: Read, Glob
```
Examples: "Find and analyze test files", "Read all TypeScript components"

**Search content then read:**
```yaml
allowed-tools: Read, Grep
```
Examples: "Find all TODOs", "Search for API calls"

**Find and search:**
```yaml
allowed-tools: Read, Glob, Grep
```
Examples: "Find database queries in services", "Search error handling patterns"

### Writing and Modifying

**Create new files:**
```yaml
allowed-tools: Read, Write
```
Examples: "Generate report", "Create new config file"
Includes Read because usually need to gather data first

**Modify existing files:**
```yaml
allowed-tools: Read, Edit
```
Examples: "Update version number", "Fix typo in config"
Always need Read before Edit

**Create and modify:**
```yaml
allowed-tools: Read, Write, Edit
```
Examples: "Refactor code structure", "Update documentation"
When workflow creates some files, modifies others

### Complex Workflows

**File operations + shell commands:**
```yaml
allowed-tools: Read, Write, Edit, Bash
```
Examples: "Run tests and document failures", "Build and commit"
Combines file work with command execution

**Analysis with code review:**
```yaml
allowed-tools: Read, Grep, Task
```
Examples: "Review security patterns", "Check architecture"
Task launches code-reviewer or architecture-analyst

**Interactive configuration:**
```yaml
allowed-tools: Read, Write, AskUserQuestion
```
Examples: "Set up project config", "Initialize settings"
Needs user choices for configuration values

**Full workflow:**
```yaml
allowed-tools: Read, Write, Edit, Bash, Task, AskUserQuestion
```
Examples: "Complete task workflow", "Complex migration"
Multi-phase operations with all capabilities

## Recognition Patterns

### Command Purpose → Tools

**Analysis commands:**
- Understand codebase → `Read, Grep`
- Find patterns → `Read, Glob, Grep`
- Review quality → `Read, Grep, Task`
- Check structure → `Read, Glob`

**Documentation commands:**
- Generate docs → `Read, Write, Grep`
- Update docs → `Read, Edit`
- Document findings → `Read, Write, Bash` (if running analysis)

**Task management commands:**
- Load tasks → `Read`
- Update tasks → `Read, Edit`
- Complete workflow → `Read, Write, Edit, Bash`

**Git operations:**
- Commit changes → `Bash`
- Review and commit → `Read, Bash`
- Generate commit from analysis → `Read, Grep, Bash`

**Build and test:**
- Run tests → `Bash`
- Test and report → `Read, Bash, Write`
- Fix and retest → `Read, Edit, Bash`

**Configuration:**
- Simple setup → `Write`
- Interactive setup → `Write, AskUserQuestion`
- Load and modify → `Read, Edit`
- Complex setup → `Read, Write, Edit, AskUserQuestion`

**Refactoring:**
- Single file → `Read, Edit`
- Multiple files → `Read, Edit, Glob`
- With testing → `Read, Edit, Bash`
- With review → `Read, Edit, Task`

### Operation Keywords → Tools

**Keywords requiring Read:**
- analyze, check, review, show, display, inspect, examine, find

**Keywords requiring Write:**
- create, generate, new, initialize, setup (new files)

**Keywords requiring Edit:**
- update, modify, change, fix, refactor (existing files)

**Keywords requiring Glob:**
- all files, find files, every, across codebase, pattern matching

**Keywords requiring Grep:**
- search, find (content), locate (text), pattern (in code), contains

**Keywords requiring Bash:**
- run, execute, test, build, commit, push, install, deploy

**Keywords requiring Task:**
- review (quality), analyze (architecture), check (implementation), audit

**Keywords requiring AskUserQuestion:**
- choose, select, configure, setup (with choices), initialize (with options)

## Common Combinations

### Minimal Sets

**Read-only:**
```yaml
allowed-tools: Read
```
Pure information retrieval, no modification

**Write-only:**
```yaml
allowed-tools: Write
```
Generate from scratch, no existing file reading

**Bash-only:**
```yaml
allowed-tools: Bash
```
Pure command execution, no file operations

### Standard Combinations

**Read-Write:**
```yaml
allowed-tools: Read, Write
```
Most common: gather info, generate output

**Read-Edit:**
```yaml
allowed-tools: Read, Edit
```
Modification workflow: read, change, save

**Read-Bash:**
```yaml
allowed-tools: Read, Bash
```
Analysis then action: check then execute

**Read-Write-Bash:**
```yaml
allowed-tools: Read, Write, Bash
```
Full automation: read, generate, execute

### Advanced Combinations

**Search and modify:**
```yaml
allowed-tools: Read, Grep, Edit
```
Find patterns across files and fix them

**Find and generate:**
```yaml
allowed-tools: Read, Glob, Write
```
Locate files by pattern and create reports

**Interactive workflow:**
```yaml
allowed-tools: Read, Write, Edit, AskUserQuestion
```
User-guided file operations

**Quality gate:**
```yaml
allowed-tools: Read, Grep, Task, Bash
```
Search, review, fix, test cycle

## Anti-Patterns

**Over-specification:**
❌ Including tools "just in case"
✅ Include only what workflow actually uses

**Under-specification:**
❌ Missing Bash when running git commands
✅ Add Bash for any shell command execution

**Wrong tool:**
❌ Using Write when Edit is appropriate (modifying existing file)
✅ Use Edit for modifications, Write for new files

**Missing Read:**
❌ Edit without Read
✅ Always include Read when using Edit

**Redundant Glob/Grep:**
❌ Both when only searching content (not finding files)
✅ Grep alone for content search, Glob+Grep for file finding then searching

## Decision Tree

```
Does command run shell commands?
├─ Yes → Include Bash
└─ No → Skip Bash

Does command read existing files?
├─ Yes → Include Read
│   ├─ Find files by name pattern?
│   │   └─ Yes → Add Glob
│   ├─ Search file contents?
│   │   └─ Yes → Add Grep
│   └─ Continue...
└─ No → Skip Read

Does command create new files?
├─ Yes → Include Write
└─ No → Skip Write

Does command modify existing files?
├─ Yes → Include Read, Edit
└─ No → Skip Edit

Does command need code review or architecture analysis?
├─ Yes → Include Task
└─ No → Skip Task

Does command need user choices during execution?
├─ Yes → Include AskUserQuestion
└─ No → Skip AskUserQuestion
```

## Validation Checklist

Before finalizing allowed-tools:

- [ ] Every tool listed is actually used in workflow
- [ ] No tools missing for described operations
- [ ] Read included if Edit used
- [ ] Bash included if any shell commands mentioned
- [ ] Task included if subagents referenced
- [ ] AskUserQuestion included if user choices needed
- [ ] Glob included if "find files" pattern mentioned
- [ ] Grep included if "search content" mentioned

## Examples by Command Type

### Simple Status Command
```yaml
allowed-tools: Read
```
Just shows information from files

### Generate Report
```yaml
allowed-tools: Read, Grep, Write
```
Search patterns, compile findings, write output

### Refactor Code
```yaml
allowed-tools: Read, Edit, Bash
```
Read files, modify them, run tests

### Complete Task
```yaml
allowed-tools: Read, Write, Edit, Bash
```
Read tasks, update files, generate notes, commit changes

### Review Code Quality
```yaml
allowed-tools: Read, Grep, Task
```
Read codebase, search patterns, launch code-reviewer

### Interactive Setup
```yaml
allowed-tools: Read, Write, AskUserQuestion
```
Ask choices, read templates, generate configured files

### Migration Workflow
```yaml
allowed-tools: Read, Glob, Write, Edit, Bash, Task
```
Complex multi-phase operation needing all capabilities

## Sharp Recognition Rules

**When you see command that will:**

1. **"Show", "display", "check", "view"** → Start with `Read`
2. **"Find files", "all \*.tsx", "every test"** → Add `Glob`
3. **"Search for", "find text", "locate usage"** → Add `Grep`
4. **"Create", "generate", "new file"** → Add `Write`
5. **"Update", "modify", "fix", "change"** → Add `Read, Edit`
6. **"Run", "execute", "test", "build", "commit"** → Add `Bash`
7. **"Review", "analyze architecture", "check quality"** → Add `Task`
8. **"Ask", "choose", "select option", "configure"** → Add `AskUserQuestion`

**Combine tools based on workflow phases:**
- Phase 1: Analysis → `Read, Grep/Glob`
- Phase 2: Modification → `Write/Edit`
- Phase 3: Execution → `Bash`
- Phase 4: Review → `Task`

**Start minimal, add incrementally:**
1. What's the core operation? (Read/Write/Edit/Bash)
2. Does it need file finding? (Glob)
3. Does it need content search? (Grep)
4. Does it need review? (Task)
5. Does it need user input? (AskUserQuestion)

This produces sharp, accurate tool selections every time.
