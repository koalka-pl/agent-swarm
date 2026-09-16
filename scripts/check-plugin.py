#!/usr/bin/env python3
"""Static consistency check for an AgentSwarm plugin.

Usage: python3 scripts/check-plugin.py plugins/<plugin-name>

Checks that every registry path exists, every library file is registered, every
always_load file exists, every router route resolves to exactly one registered skill
whose H1 matches the display name, and reports skill "Routes to" names that do not
resolve. Exits non-zero on errors; unresolved "Routes to" names are warnings.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def load_yaml(plugin: Path, rel: str):
    sys.path.insert(0, str(plugin / "engine"))
    import validate

    return validate.load(plugin / rel)


def walk(node, out: list[str]):
    if isinstance(node, dict):
        for v in node.values():
            walk(v, out)
    elif isinstance(node, list):
        for v in node:
            walk(v, out)
    elif isinstance(node, str) and re.search(r"\.(md|json|yaml)$", node):
        out.append(node)


def h1(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip())
        return 2
    plugin = Path(argv[1]).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for manifest in (plugin / ".claude-plugin" / "plugin.json", plugin / "hooks" / "hooks.json"):
        if manifest.is_file():
            try:
                json.loads(manifest.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid JSON {manifest.relative_to(plugin)}: {exc}")

    config = load_yaml(plugin, "engine/config.yaml")["as"]
    registry = load_yaml(plugin, "engine/registry.yaml")

    package_paths: list[str] = []
    for key, value in registry.items():
        if key not in ("project", "path_bases"):
            walk(value, package_paths)
    for rel in package_paths:
        if not (plugin / rel).is_file():
            errors.append(f"registry path missing: {rel}")
    for rel in config["always_load"]:
        if not (plugin / rel).is_file():
            errors.append(f"always_load path missing: {rel}")

    registered = set(package_paths)
    for f in sorted((plugin / "library").rglob("*.md")):
        rel = f.relative_to(plugin).as_posix()
        if rel not in registered:
            errors.append(f"library file not in registry: {rel}")

    skills: dict[str, list[str]] = {}
    for domain in registry["skills"].values():
        for rel in domain:
            if (plugin / rel).is_file():
                skills.setdefault(h1(plugin / rel), []).append(rel)
                if Path(rel).stem != re.sub(r"[^a-z0-9]+", "-", h1(plugin / rel).lower()).strip("-"):
                    warnings.append(f"file name differs from H1 slug: {rel} ({h1(plugin / rel)})")

    routes = 0
    for rel in registry["routers"].values():
        path = plugin / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        block = re.search(r"(?ms)^## Routing\n(.*?)(?=^## |\Z)", text)
        if not block:
            errors.append(f"router without Routing section: {rel}")
            continue
        for line in block.group(1).splitlines():
            if "→" not in line:
                continue
            routes += 1
            name = line.split("→", 1)[1].strip()
            found = skills.get(name, [])
            if len(found) != 1:
                errors.append(f"{rel}: route '{name}' resolves to {len(found)} skills")

    for name, rels in skills.items():
        if len(rels) > 1:
            errors.append(f"duplicate skill H1 '{name}': {rels}")
        for rel in rels:
            text = (plugin / rel).read_text(encoding="utf-8")
            block = re.search(r"(?ms)^## Routes to\n(.*?)(?=^## |\Z)", text)
            if not block:
                continue
            for target in re.split(r",|\n", block.group(1)):
                target = re.sub(r"[.\s]+$", "", target.strip(" -*"))
                if target and target not in skills:
                    warnings.append(f"{rel}: 'Routes to' name not registered: {target}")

    print(f"plugin: {plugin.name}")
    print(f"registry paths: {len(package_paths)}, skills: {sum(len(v) for v in skills.values())}, router routes: {routes}")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print("PASSED" if not errors else f"FAILED ({len(errors)} errors)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
