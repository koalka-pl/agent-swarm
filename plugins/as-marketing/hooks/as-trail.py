#!/usr/bin/env python3
"""PostToolUse hook: record which as-marketing routers, skills and workflows were loaded.

Writes to <data>/state/.as-trail.json, where <data> is the project's AgentSwarm data
directory (see as_data.py). Does nothing in projects without one, so the plugin stays
silent in repositories where it was never started.
Only paths inside this plugin's own root are recorded, so several AgentSwarm plugins
can share one trail file without mixing entries. Reads of project files outside <data>/
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from as_data import data_dir, project_dir, relative

PLUGIN = "as-marketing"
MAX_ENTRIES = 80

PATTERNS = [
    ("router", re.compile(r"library/routers/[a-z0-9-]+\.md")),
    ("skill", re.compile(r"library/skills/(?:core|full/[a-z0-9-]+)/[a-z0-9-]+\.md")),
    ("workflow", re.compile(r"library/workflows/[a-z0-9-]+\.md")),
    ("profile", re.compile(r"library/business-model-profiles\.md")),
]


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def targets(payload: dict) -> list[str]:
    tool_input = payload.get("tool_input") or {}
    return [str(tool_input.get(k)) for k in ("file_path", "command", "pattern", "path") if tool_input.get(k)]


def classify(texts: list[str], plugin_root: str, data_rel: str) -> list[tuple[str, str]]:
    context = re.compile(re.escape(f"{data_rel}/project-context.md"))
    found: list[tuple[str, str]] = []
    for text in texts:
        if plugin_root and plugin_root in text:
            for kind, pattern in PATTERNS:
                found.extend((kind, m.group(0)) for m in pattern.finditer(text))
        found.extend(("context", m.group(0)) for m in context.finditer(text))
    return found


def source_reads(payload: dict, project: Path, data_rel: str) -> list[str]:
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
    rel_posix = rel.as_posix()
    if rel_posix == data_rel or rel_posix.startswith(data_rel + "/"):
        return []
    return [rel_posix]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    project = project_dir(payload)
    data = data_dir(project)
    if data is None or not data.is_dir():
        return 0
    data_rel = relative(data, project)

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    trail_path = data / "state" / ".as-trail.json"
    session_id = str(payload.get("session_id") or "unknown")

    try:
        trail = json.loads(trail_path.read_text(encoding="utf-8"))
    except Exception:
        trail = {}
    if trail.get("session_id") != session_id:
        trail = {"session_id": session_id, "entries": []}
    entries = trail.get("entries") or []

    hits = classify(targets(payload), plugin_root, data_rel)
    active = any(e.get("plugin") == PLUGIN and e.get("kind") in ("router", "skill") for e in entries) or any(
        k in ("router", "skill") for k, _ in hits
    )
    if active:
        hits.extend(("source", p) for p in source_reads(payload, project, data_rel))
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
