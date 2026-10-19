#!/usr/bin/env python3
"""Create a project documentation seed without overwriting existing work."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE_TITLES = {
    "generic": "Generic Project",
    "agent-evaluation": "Agent Evaluation & Simulation",
    "agent-application": "Agent Application",
    "rag-system": "RAG / Knowledge-Augmented Generation",
}


def render(content: str, *, name: str, description: str, profile: str) -> str:
    replacements = {
        "{{PROJECT_NAME}}": name,
        "{{PROJECT_DESCRIPTION}}": description,
        "{{PROFILE_NAME}}": PROFILE_TITLES[profile],
    }
    for key, value in replacements.items():
        content = content.replace(key, value)
    return content


def build_file_map(*, name: str, description: str, profile: str) -> dict[str, str]:
    """Return generated relative paths and rendered UTF-8 content."""
    mapping = {
        "AGENTS.md": ROOT / "templates/AGENTS.md",
        "README.md": ROOT / "templates/README.md",
        ".gitignore": ROOT / ".gitignore",
        "docs/PROJECT_BRIEF.md": ROOT / "templates/docs/PROJECT_BRIEF.md",
        "docs/PRODUCT.md": ROOT / "templates/docs/PRODUCT.md",
        "docs/ARCHITECTURE.md": ROOT / "templates/docs/ARCHITECTURE.md",
        "docs/CONTRACTS.md": ROOT / "templates/docs/CONTRACTS.md",
        "docs/QUALITY_GATES.md": ROOT / "templates/docs/QUALITY_GATES.md",
        "docs/PROJECT_STATUS.md": ROOT / "templates/docs/PROJECT_STATUS.md",
        "docs/ROADMAP.md": ROOT / "templates/docs/ROADMAP.md",
        "docs/decisions/ADR-TEMPLATE.md": ROOT / "templates/docs/decisions/ADR-TEMPLATE.md",
        "docs/changes/templates/FEATURE.md": ROOT / "templates/changes/FEATURE.md",
        "docs/changes/templates/ARCHITECTURE_CHANGE.md": ROOT / "templates/changes/ARCHITECTURE_CHANGE.md",
        "docs/changes/templates/SPIKE.md": ROOT / "templates/changes/SPIKE.md",
        "docs/reviews/templates/ARCHITECTURE_REVIEW.md": ROOT / "templates/reviews/ARCHITECTURE_REVIEW.md",
        "docs/reviews/templates/RELEASE_CHECKLIST.md": ROOT / "templates/reviews/RELEASE_CHECKLIST.md",
        "docs/PROJECT_PROFILE.md": ROOT / f"profiles/{profile}.md",
    }
    return {
        relative: render(source.read_text(encoding="utf-8"), name=name, description=description, profile=profile)
        for relative, source in mapping.items()
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a lightweight AI project seed.")
    parser.add_argument("--target", required=True, help="Target directory; must not contain files")
    parser.add_argument("--name", required=True, help="Human-readable project name")
    parser.add_argument("--description", default="TBD — add a one-line project description", help="One-line project description")
    parser.add_argument("--profile", choices=sorted(PROFILE_TITLES), default="generic", help="Project-specific guidance profile")
    parser.add_argument("--dry-run", action="store_true", help="List files without writing them")
    args = parser.parse_args(argv)

    target = Path(args.target).expanduser().resolve()
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        print(f"ERROR: target must be a new or empty directory: {target}", file=sys.stderr)
        return 2

    files = build_file_map(name=args.name.strip(), description=args.description.strip(), profile=args.profile)
    if args.dry_run:
        print(f"Would create {len(files)} files under {target}:")
        for relative in sorted(files):
            print(f"  {relative}")
        return 0

    target.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Recheck each path to avoid clobbering a file if the target changed after validation.
        if destination.exists():
            print(f"ERROR: refusing to overwrite existing file: {destination}", file=sys.stderr)
            return 2
        destination.write_text(content, encoding="utf-8")

    print(f"Created {len(files)} starter files in {target}")
    print("Next: complete docs/PROJECT_BRIEF.md, then ask your Coding Agent for a read-only discovery and planning pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
