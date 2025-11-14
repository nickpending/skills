# Tool Selection Reference

Sharp patterns for selecting tools based on command purpose and operations.

## Available Tools

### File Operations
- **Read** - View file contents, parse data structures
- **Write** - Create new files, overwrite existing
- **Edit** - Modify existing files with exact string replacement
- **MultiEdit** - Batch edits across multiple files in single operation
- **NotebookEdit** - Edit Jupyter notebook cells (code/markdown)
- **Glob** - Find files by pattern (*.ts, **/*.md)
- **Grep** - Search file contents by regex

### Execution
- **Bash** - Run shell commands, git operations, build tools
- **BashOutput** - Read output from background shell processes
- **KillShell** - Terminate background shell processes
- **Task** - Launch specialized subagents (code-reviewer, architecture-analyst)

### Research
- **WebFetch** - Fetch and analyze web content with AI processing
- **WebSearch** - Search the web for current information

### Composition
- **Skill** - Invoke other skills programmatically
- **SlashCommand** - Invoke slash commands programmatically

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

**Batch modify multiple files:**
```yaml
allowed-tools: Read, MultiEdit
```
Examples: "Update version across package.json files", "Apply pattern to all configs"
Safer than sequential edits when consistency matters

**Edit Jupyter notebooks:**
```yaml
allowed-tools: Read, NotebookEdit
```
Examples: "Update notebook cells", "Modify data analysis workflow"
For data science and analysis notebooks

### Research and Web Operations

**Fetch and analyze web content:**
```yaml
allowed-tools: WebFetch
```
Examples: "Read documentation from URL", "Analyze blog post"
Fetches HTML, converts to markdown, processes with AI

**Search for current information:**
```yaml
allowed-tools: WebSearch
```
Examples: "Find latest framework version", "Search recent discussions"
For information beyond knowledge cutoff

**Research then document:**
```yaml
allowed-tools: WebFetch, WebSearch, Write
```
Examples: "Research topic and create summary", "Compile documentation from web"
Combine web research with file generation

### Background Process Management

**Long-running commands:**
```yaml
allowed-tools: Bash, BashOutput
```
Examples: "Run server and monitor logs", "Start build and check progress"
Launch in background, read output later

**Process lifecycle:**
```yaml
allowed-tools: Bash, BashOutput, KillShell
```
Examples: "Start service, monitor, stop when done", "Manage background processes"
Full control over background execution

### Skill and Command Composition

**Invoke other skills:**
```yaml
allowed-tools: Skill
```
Examples: "Use PDF skill for extraction", "Delegate to specialized skill"
Programmatic skill invocation

**Chain slash commands:**
```yaml
allowed-tools: SlashCommand
```
Examples: "Run multiple workflow commands", "Orchestrate command sequence"
Sequential command execution

**Complex orchestration:**
```yaml
allowed-tools: Read, Write, Skill, SlashCommand
```
Examples: "Coordinate multi-skill workflow", "Build complex automation"
Combine skills and commands with file operations

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
- Multiple files → `Read, Edit, Glob` or `Read, MultiEdit`
- With testing → `Read, Edit, Bash`
- With review → `Read, Edit, Task`

**Web research:**
- Fetch docs → `WebFetch`
- Search info → `WebSearch`
- Research and write → `WebFetch, WebSearch, Write`

**Data science:**
- Analyze notebook → `Read, NotebookEdit`
- Update analysis → `Read, NotebookEdit, Bash`

**Process management:**
- Background task → `Bash, BashOutput`
- Managed processes → `Bash, BashOutput, KillShell`

**Orchestration:**
- Use other skills → `Skill`
- Chain commands → `SlashCommand`
- Complex workflows → `Read, Write, Skill, SlashCommand`

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

**Keywords requiring MultiEdit:**
- batch update, update all, apply to multiple, consistent changes across files

**Keywords requiring NotebookEdit:**
- notebook, jupyter, ipynb, data analysis cells, update analysis

**Keywords requiring WebFetch:**
- fetch from URL, read documentation at, analyze web page, get content from

**Keywords requiring WebSearch:**
- search for, find online, latest information, current status, recent news

**Keywords requiring BashOutput:**
- monitor output, check progress, read logs from, background process output

**Keywords requiring KillShell:**
- stop process, terminate, kill background, end running

**Keywords requiring Skill:**
- use skill, delegate to, invoke capability, specialized function

**Keywords requiring SlashCommand:**
- run command, execute workflow, chain commands, sequential operations

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

Does command modify multiple files with same pattern?
├─ Yes → Consider MultiEdit instead of Edit
└─ No → Use Edit for single file changes

Does command work with Jupyter notebooks?
├─ Yes → Include NotebookEdit
└─ No → Skip NotebookEdit

Does command need web content or search?
├─ Yes → Include WebFetch and/or WebSearch
└─ No → Skip web tools

Does command run background processes?
├─ Yes → Include BashOutput (and KillShell if managing lifecycle)
└─ No → Skip process management tools

Does command delegate to other skills or commands?
├─ Yes → Include Skill and/or SlashCommand
└─ No → Skip composition tools
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
6. **"Update all", "batch modify", "apply to multiple"** → Add `Read, MultiEdit`
7. **"Notebook", "jupyter", "ipynb"** → Add `NotebookEdit`
8. **"Run", "execute", "test", "build", "commit"** → Add `Bash`
9. **"Monitor", "check progress", "background"** → Add `Bash, BashOutput`
10. **"Stop", "kill", "terminate process"** → Add `KillShell`
11. **"Fetch from", "read URL", "web content"** → Add `WebFetch`
12. **"Search online", "latest", "current info"** → Add `WebSearch`
13. **"Use skill", "delegate to"** → Add `Skill`
14. **"Run command", "chain workflow"** → Add `SlashCommand`
15. **"Review", "analyze architecture", "check quality"** → Add `Task`
16. **"Ask", "choose", "select option", "configure"** → Add `AskUserQuestion`

**Combine tools based on workflow phases:**
- Phase 1: Analysis → `Read, Grep/Glob` or `WebFetch/WebSearch`
- Phase 2: Modification → `Write/Edit/MultiEdit/NotebookEdit`
- Phase 3: Execution → `Bash` (with `BashOutput/KillShell` if background)
- Phase 4: Review → `Task`
- Phase 5: Orchestration → `Skill/SlashCommand`

**Start minimal, add incrementally:**
1. What's the core operation? (Read/Write/Edit/Bash)
2. Does it modify multiple files? (MultiEdit)
3. Does it work with notebooks? (NotebookEdit)
4. Does it need file finding? (Glob)
5. Does it need content search? (Grep)
6. Does it need web research? (WebFetch/WebSearch)
7. Does it run in background? (BashOutput/KillShell)
8. Does it delegate work? (Skill/SlashCommand)
9. Does it need review? (Task)
10. Does it need user input? (AskUserQuestion)

This produces sharp, accurate tool selections every time.
