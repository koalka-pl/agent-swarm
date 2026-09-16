#!/usr/bin/env python3
"""PostToolUse hook: record which as-marketing routers, skills and workflows were loaded.

Writes to <project>/.as/state/.as-trail.json. Does nothing in projects without a .as/
directory, so the plugin stays silent in repositories where it was never started.
Only paths inside this plugin's own root are recorded, so several AgentSwarm plugins
can share one trail file without mixing entries. Reads of project files outside .as/
are recorded as kind "source" only once this session has loaded a router or skill.

Never fails loudly: any error exits 0 so tool calls are never blocked.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PLUGIN = "as-marketing"
MAX_ENTRIES = 80

PATTERNS = [
    ("router", re.compile(r"library/routers/[a-z0-9-]+\.md")),
    ("skill", re.compile(r"library/skills/(?:core|full/[a-z0-9-]+)/[a-z0-9-]+\.md")),
    ("workflow", re.compile(r"library/workflows/[a-z0-9-]+\.md")),
    ("profile", re.compile(r"library/business-model-profiles\.md")),
]
CONTEXT = re.compile(r"\.as/project-context\.md")


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def targets(payload: dict) -> list[str]:
    tool_input = payload.get("tool_input") or {}
    return [str(tool_input.get(k)) for k in ("file_path", "command", "pattern", "path") if tool_input.get(k)]


def classify(texts: list[str], plugin_root: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for text in texts:
        if plugin_root and plugin_root in text:
            for kind, pattern in PATTERNS:
                found.extend((kind, m.group(0)) for m in pattern.finditer(text))
        found.extend(("context", m.group(0)) for m in CONTEXT.finditer(text))
    return found


def source_reads(payload: dict, project: Path) -> list[str]:
    if payload.get("tool_name") not in ("Read", "Grep", "Glob"):
        return []
    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") or tool_input.get("path")
    if not raw:
        return []
    try:
        resolved = (project / raw).resolve() if not os.path.isabs(raw) else Path(raw).resolve()
        rel = resolved.relative_to(project)
    except Exception:
        return []
    if rel.parts and rel.parts[0] == ".as":
        return []
    return [str(rel)]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    project = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()
    if not (project / ".as").is_dir():
        return 0

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    trail_path = project / ".as" / "state" / ".as-trail.json"
    session_id = str(payload.get("session_id") or "unknown")

    try:
        trail = json.loads(trail_path.read_text(encoding="utf-8"))
    except Exception:
        trail = {}
    if trail.get("session_id") != session_id:
        trail = {"session_id": session_id, "entries": []}
    entries = trail.get("entries") or []

    hits = classify(targets(payload), plugin_root)
    active = any(e.get("plugin") == PLUGIN and e.get("kind") in ("router", "skill") for e in entries) or any(
        k in ("router", "skill") for k, _ in hits
    )
    if active:
        hits.extend(("source", p) for p in source_reads(payload, project))
    if not hits:
        return 0

    seen = {(e.get("plugin"), e.get("kind"), e.get("path")) for e in entries}
    now = stamp()
    agent = payload.get("agent_type") or "main"
    for kind, path in hits:
        key = (PLUGIN, kind, path)
        if key in seen:
            continue
        seen.add(key)
        entries.append({"plugin": PLUGIN, "kind": kind, "path": path, "name": Path(path).stem, "agent": agent, "at": now})

    trail["entries"] = entries[-MAX_ENTRIES:]
    trail["updated_at"] = now
    try:
        trail_path.parent.mkdir(parents=True, exist_ok=True)
        trail_path.write_text(json.dumps(trail, indent=2) + "\n", encoding="utf-8")
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception:
        raise SystemExit(0)
