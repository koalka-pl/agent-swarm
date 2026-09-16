#!/usr/bin/env python3
"""PreToolUse hook: enforce source-access consent for the as-marketing source-reader agent.

Plugin hooks fire for the whole session, so this hook acts only on calls made by the
agent "as-marketing:source-reader" and lets every other call through untouched. For that
agent it allows Read/Grep/Glob only inside read_paths from <data>/access.yaml when granted
is true, and always denies secret-looking files and the <data>/private/ directory. <data> is
the project's AgentSwarm data directory (see as_data.py).
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from as_data import data_dir, project_dir, relative

AGENT = "as-marketing:source-reader"
SECRET = re.compile(r"(^|/)(\.env(\..*)?|.*\.(pem|key|p12|pfx)|id_(rsa|ed25519)(\.pub)?)$")


def deny(reason: str) -> int:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    return 0


def load_access(path: Path) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    granted = re.search(r"(?m)^granted:\s*true\s*$", text) is not None
    paths: list[str] = []
    inline = re.search(r"(?m)^read_paths:\s*\[(.*)\]\s*$", text)
    if inline:
        paths = [p.strip().strip("\"'") for p in inline.group(1).split(",") if p.strip()]
    else:
        block = re.search(r"(?m)^read_paths:\s*$\n((?:[ \t]+-.*\n?)*)", text)
        if block:
            paths = [l.strip()[1:].strip().strip("\"'") for l in block.group(1).splitlines() if l.strip().startswith("-")]
    return granted, paths


def check(payload: dict) -> int:
    project = project_dir(payload)
    data = data_dir(project)
    if data is None:
        return deny("No AgentSwarm data directory in this project. Run /as-marketing:start.")
    data_rel = relative(data, project)
    access = data / "access.yaml"
    if not access.is_file():
        return deny(f"Missing {data_rel}/access.yaml. Run /as-marketing:start and grant source access.")

    granted, read_paths = load_access(access)
    if not granted or not read_paths:
        return deny(f"Source access has not been granted in {data_rel}/access.yaml.")

    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") or tool_input.get("path") or "."
    target = (Path(raw) if os.path.isabs(raw) else project / raw).resolve()
    try:
        rel = target.relative_to(project).as_posix()
    except ValueError:
        return deny(f"Path {raw} is outside the project.")
    if rel == ".":
        rel = ""

    private = f"{data_rel}/private"
    if rel == private or rel.startswith(private + "/"):
        return deny(f"{private}/ holds sensitive project data and is not shared with source-reader.")

    if rel and SECRET.search(rel):
        return deny(f"File {rel} looks like a secret and is not shared.")

    for allowed in read_paths:
        base = allowed.strip().strip("/")
        if base in ("", "."):
            return 0
        if rel == base or rel.startswith(base + "/"):
            return 0
    return deny(f"Path {rel or '.'} is outside the granted scope: {', '.join(read_paths)}.")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("agent_type") != AGENT:
        return 0
    try:
        return check(payload)
    except Exception as exc:
        return deny(f"source-guard error: {exc}")


if __name__ == "__main__":
    raise SystemExit(main())
