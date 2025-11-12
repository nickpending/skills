#!/usr/bin/env python3
"""
Skill Packager

Packages validated skill directories as distributable zip files.
OUTPUT FORMAT: Structured for model consumption and user display.
"""

import sys
import shutil
from pathlib import Path
from validate_skill import validate_skill


def package_skill(skill_dir: Path, output_dir: Path = None) -> tuple[bool, str]:
    """Package skill as zip after validation.

    Returns: (success: bool, message: str)
    """

    skill_path = Path(skill_dir)

    # Validate structure first
    results = validate_skill(skill_path)

    if not results["valid"]:
        issues_str = "\n".join(
            f"  - {issue}" for issue in results.get("issues", results.get("errors", []))
        )
        return False, f"Validation failed:\n{issues_str}"

    # Determine output location
    if output_dir:
        output_path = Path(output_dir)
        if not output_path.exists():
            return False, f"Output directory not found: {output_path}"
    else:
        output_path = Path("/tmp")

    # Create zip
    skill_name = skill_path.name
    zip_basename = f"{skill_name}"
    zip_path = output_path / zip_basename

    try:
        archive_path = shutil.make_archive(
            str(zip_path), "zip", root_dir=skill_path.parent, base_dir=skill_path.name
        )

        archive_size = Path(archive_path).stat().st_size
        size_kb = archive_size / 1024

        return True, f"{archive_path}|{size_kb:.1f}"

    except Exception as e:
        return False, f"Packaging failed: {str(e)}"


def main() -> None:
    """Main entry point. Outputs structured packaging results."""

    if len(sys.argv) < 2:
        print("Usage: python3 package_skill.py <skill-directory> [output-directory]")
        print()
        print("Validates and packages skill as distributable zip.")
        print()
        print("Arguments:")
        print("  skill-directory    Path to skill directory")
        print("  output-directory   Optional output location (default: /tmp)")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    # Run validation and packaging
    success, result = package_skill(skill_dir, output_dir)

    if success:
        # Parse result
        archive_path, size = result.split("|")
        print(f"Skill: {skill_dir.name}")
        print()
        print("✅ PACKAGED")
        print()
        print(f"Location: {archive_path}")
        print(f"Size: {size} KB")
        print()
        print("Installation:")
        print(f"  unzip {Path(archive_path).name}")
        print(f"  mv {skill_dir.name} ~/.claude/skills/")
        sys.exit(0)
    else:
        print(f"Skill: {skill_dir.name}")
        print()
        print("❌ FAILED")
        print()
        print(result)
        sys.exit(1)


if __name__ == "__main__":
    main()
