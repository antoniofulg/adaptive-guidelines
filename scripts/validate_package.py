#!/usr/bin/env python3
"""Validate the cross-agent package without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = "adaptive-guidelines"
REPOSITORY = "https://github.com/antoniofulg/adaptive-guidelines"
SEMVER = re.compile(r"\d+\.\d+\.\d+")


def load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    skill_path = ROOT / "skills" / NAME / "SKILL.md"
    require(skill_path.is_file(), f"missing {skill_path.relative_to(ROOT)}")

    skill = skill_path.read_text(encoding="utf-8")
    require(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    require(f"name: {NAME}\n" in skill, "SKILL.md name does not match its folder")
    require("license: MIT\n" in skill, "SKILL.md must declare the MIT license")

    for reference in re.findall(r"\]\((references/[^)]+)\)", skill):
        require((skill_path.parent / reference).is_file(), f"missing reference: {reference}")

    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")
    claude_marketplace = load_json(".claude-plugin/marketplace.json")
    codex_marketplace = load_json(".agents/plugins/marketplace.json")

    require(codex.get("name") == NAME, "Codex plugin name mismatch")
    require(claude.get("name") == NAME, "Claude plugin name mismatch")
    require(codex.get("version") == claude.get("version"), "plugin versions differ")
    require(bool(SEMVER.fullmatch(str(codex.get("version", "")))), "invalid plugin version")
    require(codex.get("skills") == "./skills/", "Codex skill path must be ./skills/")
    require(codex.get("repository") == REPOSITORY, "Codex repository URL mismatch")
    require(claude.get("repository") == REPOSITORY, "Claude repository URL mismatch")

    claude_entry = claude_marketplace.get("plugins", [{}])[0]
    require(claude_entry.get("name") == NAME, "Claude marketplace name mismatch")
    require(claude_entry.get("source") == "./", "Claude marketplace must use repo root")
    require(
        claude_entry.get("version") == claude.get("version"),
        "Claude marketplace version mismatch",
    )

    codex_entry = codex_marketplace.get("plugins", [{}])[0]
    require(codex_entry.get("name") == NAME, "Codex marketplace name mismatch")
    source = codex_entry.get("source", {})
    require(source.get("source") == "url", "Codex marketplace must use a Git URL")
    require(source.get("url") == f"{REPOSITORY}.git", "Codex marketplace URL mismatch")
    require(source.get("ref") == "main", "Codex marketplace must track main")

    for relative_path in ("README.md", "LICENSE"):
        require((ROOT / relative_path).is_file(), f"missing {relative_path}")

    print(f"{NAME} package is valid ({codex['version']})")


if __name__ == "__main__":
    main()
