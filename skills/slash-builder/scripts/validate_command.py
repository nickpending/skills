#!/usr/bin/env python3
"""
Slash Command Structure Validator

Validates Claude Code slash command markdown files for:
- YAML frontmatter syntax and required fields
- Required section presence
- Variable documentation structure
- Success criteria format
"""

import sys
import re
from pathlib import Path


def validate_yaml_frontmatter(content: str) -> tuple[bool, list[str]]:
    """Validate YAML frontmatter exists and has required fields."""
    issues = []

    # Check frontmatter exists
    if not content.startswith("---"):
        issues.append("Missing YAML frontmatter (should start with '---')")
        return False, issues

    # Extract frontmatter
    try:
        end_marker = content.index("---", 3)
        frontmatter = content[3:end_marker].strip()
    except ValueError:
        issues.append("YAML frontmatter not properly closed (missing closing '---')")
        return False, issues

    # Check required fields
    required_fields = ["allowed-tools", "description"]
    for field in required_fields:
        if f"{field}:" not in frontmatter:
            issues.append(f"Missing required frontmatter field: {field}")

    # Check allowed-tools format
    if "allowed-tools:" in frontmatter:
        tools_line = [
            line for line in frontmatter.split("\n") if "allowed-tools:" in line
        ]
        if tools_line and tools_line[0].strip() == "allowed-tools:":
            issues.append("allowed-tools field is empty (should list tools)")

    return len(issues) == 0, issues


def check_required_sections(content: str) -> tuple[list[str], list[str]]:
    """Check for required markdown sections."""
    required_sections = [
        (r"^# .+", "Command name (H1 header)"),
        (r"^## Variables", "Variables section"),
        (r"^## Core Instructions", "Core Instructions section"),
        (r"^## Workflow", "Workflow section"),
        (r"^## Success Criteria", "Success Criteria section"),
    ]

    found = []
    missing = []

    for pattern, name in required_sections:
        if re.search(pattern, content, re.MULTILINE):
            found.append(name)
        else:
            missing.append(name)

    return found, missing


def check_optional_sections(content: str) -> list[str]:
    """Check for optional sections that are present."""
    optional_sections = [
        (r"^## Claude Code Patterns", "Claude Code Patterns"),
        (r"^## Output Format", "Output Format"),
        (r"^## Error Handling", "Error Handling"),
        (r"^## Notes", "Notes"),
    ]

    found = []
    for pattern, name in optional_sections:
        if re.search(pattern, content, re.MULTILINE):
            found.append(name)

    return found


def validate_variables_section(content: str) -> list[str]:
    """Check Variables section structure."""
    issues = []

    # Find Variables section
    var_section_match = re.search(
        r"^## Variables\s*\n(.+?)(?=^## |\Z)", content, re.MULTILINE | re.DOTALL
    )

    if not var_section_match:
        return issues

    var_content = var_section_match.group(1)

    # Check for subsections
    expected_subsections = ["From Arguments", "Injected", "Runtime"]

    found_subsections = []
    for subsection in expected_subsections:
        if f"### {subsection}" in var_content:
            found_subsections.append(subsection)

    if not found_subsections:
        issues.append(
            "Variables section should have subsections (From Arguments/Injected/Runtime)"
        )

    return issues


def validate_success_criteria(content: str) -> list[str]:
    """Check Success Criteria section has checkboxes."""
    issues = []

    # Find Success Criteria section
    criteria_match = re.search(
        r"^## Success Criteria\s*\n(.+?)(?=^## |\Z)", content, re.MULTILINE | re.DOTALL
    )

    if not criteria_match:
        return issues

    criteria_content = criteria_match.group(1)

    # Check for checkbox items
    checkboxes = re.findall(r"- \[ \]", criteria_content)

    if not checkboxes:
        issues.append("Success Criteria should contain checkbox items (- [ ])")

    return issues


def validate_command_file(filepath: Path) -> dict:
    """Validate a slash command file."""

    if not filepath.exists():
        return {"valid": False, "errors": [f"File not found: {filepath}"]}

    content = filepath.read_text()

    # Run all validations
    frontmatter_valid, frontmatter_issues = validate_yaml_frontmatter(content)
    required_found, required_missing = check_required_sections(content)
    optional_found = check_optional_sections(content)
    var_issues = validate_variables_section(content)
    criteria_issues = validate_success_criteria(content)

    # Compile results
    all_issues = frontmatter_issues + required_missing + var_issues + criteria_issues

    return {
        "valid": len(all_issues) == 0,
        "frontmatter_valid": frontmatter_valid,
        "required_sections": required_found,
        "missing_sections": required_missing,
        "optional_sections": optional_found,
        "issues": all_issues,
    }


def print_results(filepath: Path, results: dict) -> None:
    """Print validation results."""
    print(f"\n{'=' * 60}")
    print(f"Slash Command Validation: {filepath.name}")
    print(f"{'=' * 60}\n")

    if results["valid"]:
        print("✅ VALID - All required structure present\n")
    else:
        print("❌ INVALID - Issues found\n")

    # Frontmatter
    if results["frontmatter_valid"]:
        print("✓ YAML frontmatter valid")
    else:
        print("✗ YAML frontmatter issues")

    # Required sections
    print(f"\n📋 Required Sections ({len(results['required_sections'])}/5):")
    for section in results["required_sections"]:
        print(f"  ✓ {section}")

    if results["missing_sections"]:
        print("\n❌ Missing Required Sections:")
        for section in results["missing_sections"]:
            print(f"  ✗ {section}")

    # Optional sections
    if results["optional_sections"]:
        print(f"\n📝 Optional Sections Present ({len(results['optional_sections'])}):")
        for section in results["optional_sections"]:
            print(f"  • {section}")

    # Issues
    if results["issues"]:
        print(f"\n⚠️  Issues Found ({len(results['issues'])}):")
        for issue in results["issues"]:
            print(f"  • {issue}")

    print(f"\n{'=' * 60}\n")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python3 validate_command.py <command-file.md>")
        print("\nValidates slash command structure including:")
        print("  - YAML frontmatter syntax and fields")
        print("  - Required sections presence")
        print("  - Variables section structure")
        print("  - Success criteria format")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    results = validate_command_file(filepath)

    print_results(filepath, results)

    # Exit code
    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
