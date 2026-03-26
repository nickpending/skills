#!/usr/bin/env python3
"""
Skill Structure Validator

Validates Claude Code skill directories for structure, frontmatter, and organization.
OUTPUT FORMAT: Structured for model consumption and user display.
"""

import sys
import re
from pathlib import Path


def validate_yaml_frontmatter(content: str) -> tuple[bool, list[str]]:
    """Validate YAML frontmatter exists and has required fields."""
    issues = []

    if not content.startswith("---"):
        issues.append("Missing YAML frontmatter (must start with '---')")
        return False, issues

    try:
        end_marker = content.index("---", 3)
        frontmatter = content[3:end_marker].strip()
    except ValueError:
        issues.append("YAML frontmatter not closed (missing closing '---')")
        return False, issues

    # Required fields
    required_fields = ["name", "description"]
    for field in required_fields:
        if f"{field}:" not in frontmatter:
            issues.append(f"Missing required field: {field}")

    # Check name format (no spaces)
    if "name:" in frontmatter:
        name_line = [line for line in frontmatter.split("\n") if "name:" in line]
        if name_line:
            name_value = name_line[0].split(":", 1)[1].strip()
            if not name_value:
                issues.append("name field is empty")
            elif " " in name_value:
                issues.append(f"name must be hyphenated (found: '{name_value}')")

    # Check description exists
    if "description:" in frontmatter:
        desc_line = [line for line in frontmatter.split("\n") if "description:" in line]
        if desc_line and desc_line[0].strip() == "description:":
            issues.append("description field is empty")

    return len(issues) == 0, issues


def detect_skill_type(skill_dir: Path) -> str:
    """Detect skill type based on directory structure."""
    has_workflows = (skill_dir / "workflows").exists()
    has_scripts = (skill_dir / "scripts").exists()
    has_references = (skill_dir / "references").exists()
    has_assets = (skill_dir / "assets").exists()

    if has_workflows:
        return "workflow"
    elif has_scripts and not has_workflows:
        return "tool"
    elif has_assets and not (has_workflows or has_scripts):
        return "template"
    elif has_references and not (has_workflows or has_scripts or has_assets):
        return "reference"
    else:
        return "mixed"


def check_skill_structure(skill_dir: Path) -> tuple[list[str], list[str]]:
    """Check skill directory structure and bundled resources."""
    found = []
    issues = []

    # Required: SKILL.md
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        issues.append("Missing SKILL.md (required)")
        return found, issues

    found.append("SKILL.md")

    # Check resource directories
    resource_dirs = {
        "workflows": "*.md",
        "scripts": ["*.py", "*.sh"],
        "references": "*.md",
        "assets": "*",
    }

    for dir_name, patterns in resource_dirs.items():
        dir_path = skill_dir / dir_name
        if dir_path.exists() and dir_path.is_dir():
            if isinstance(patterns, list):
                files = []
                for pattern in patterns:
                    files.extend(list(dir_path.glob(f"**/{pattern}")))
            else:
                files = list(dir_path.glob(f"**/{patterns}"))

            files = [f for f in files if f.is_file()]

            if files:
                found.append(f"{dir_name}/ ({len(files)} files)")
            else:
                issues.append(f"{dir_name}/ exists but is empty")

    return found, issues


def validate_description(content: str) -> list[str]:
    """Validate description quality and voice."""
    issues = []

    try:
        end_marker = content.index("---", 3)
        frontmatter = content[3:end_marker].strip()
    except ValueError:
        return issues

    desc_match = re.search(r"description:\s*(.+?)(?=\n\w+:|$)", frontmatter, re.DOTALL)
    if not desc_match:
        return issues

    description = desc_match.group(1).strip()

    # Length check
    if len(description) < 20:
        issues.append("description too short (explain what and when)")

    # Voice check (should be third-person)
    first_person_phrases = ["Use this", "This helps you", "You can use"]
    for phrase in first_person_phrases:
        if phrase in description:
            issues.append(f"description should be third-person (found '{phrase}')")
            break

    return issues


def check_skill_content(skill_dir: Path, content: str) -> list[str]:
    """Check SKILL.md content structure."""
    issues = []

    # H1 header required
    if not re.search(r"^# .+", content, re.MULTILINE):
        issues.append("Missing H1 header (skill name)")

    # Overview section recommended
    if not re.search(r"^## (Overview|About|Description)", content, re.MULTILINE):
        issues.append("Missing Overview section (recommended)")

    # Type-specific checks
    skill_type = detect_skill_type(skill_dir)

    if skill_type == "workflow":
        has_checklist = bool(re.search(r"- \[ \].*Step", content))
        has_execute = bool(re.search(r"^## Execute ALL steps", content, re.MULTILINE))

        if not (has_checklist and has_execute):
            issues.append(
                "Workflow skill needs checklist and 'Execute ALL steps' section"
            )

    return issues


def validate_skill(skill_dir: Path) -> dict:
    """Validate skill directory. Returns structured results for model."""

    skill_path = Path(skill_dir)

    if not skill_path.exists():
        return {
            "valid": False,
            "errors": [f"Directory not found: {skill_dir}"],
            "skill_type": "unknown",
        }

    if not skill_path.is_dir():
        return {
            "valid": False,
            "errors": [f"Not a directory: {skill_dir}"],
            "skill_type": "unknown",
        }

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return {
            "valid": False,
            "errors": ["Missing SKILL.md (required)"],
            "skill_type": "unknown",
        }

    content = skill_md.read_text()

    # Run validations
    frontmatter_valid, frontmatter_issues = validate_yaml_frontmatter(content)
    structure_found, structure_issues = check_skill_structure(skill_path)
    description_issues = validate_description(content)
    content_issues = check_skill_content(skill_path, content)

    skill_type = detect_skill_type(skill_path)

    all_issues = (
        frontmatter_issues + structure_issues + description_issues + content_issues
    )

    return {
        "valid": len(all_issues) == 0,
        "skill_type": skill_type,
        "structure_found": structure_found,
        "issues": all_issues,
    }


def main() -> None:
    """Main entry point. Outputs structured validation results."""

    if len(sys.argv) != 2:
        print("Usage: python3 validate_skill.py <skill-directory>")
        print()
        print("Validates skill structure:")
        print("  - SKILL.md presence and format")
        print("  - YAML frontmatter (name, description)")
        print("  - Directory structure")
        print("  - Type-appropriate organization")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    results = validate_skill(skill_dir)

    # Output for model consumption
    print(f"Skill: {skill_dir.name}")
    print(f"Type: {results['skill_type']}")
    print()

    if results["valid"]:
        print("✅ VALID")
        print()
        print("Structure found:")
        for item in results["structure_found"]:
            print(f"  - {item}")
    else:
        print("❌ INVALID")
        print()
        if "errors" in results:
            print("Errors:")
            for error in results["errors"]:
                print(f"  - {error}")
        else:
            print("Issues found:")
            for issue in results["issues"]:
                print(f"  - {issue}")
            print()
            if results["structure_found"]:
                print("Structure found:")
                for item in results["structure_found"]:
                    print(f"  - {item}")

    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
