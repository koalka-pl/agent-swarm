#!/usr/bin/env python3
"""PreToolUse hook: enforce source-access consent for the as-marketing source-reader agent.

Plugin hooks fire for the whole session, so this hook acts only on calls made by the
agent "as-marketing:source-reader" and lets every other call through untouched. For that
agent it allows Read/Grep/Glob only inside read_paths from <project>/.as/access.yaml when
granted is true, and always denies secret-looking files.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

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
    project = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()
    access = project / ".as" / "access.yaml"
    if not access.is_file():
        return deny("Brak .as/access.yaml. Uruchom /as-marketing:start i udziel zgody na dostęp do źródeł.")

    granted, read_paths = load_access(access)
    if not granted or not read_paths:
        return deny("Dostęp do źródeł projektu nie został udzielony w .as/access.yaml.")

    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") or tool_input.get("path") or "."
    target = (Path(raw) if os.path.isabs(raw) else project / raw).resolve()
    try:
        rel = target.relative_to(project).as_posix()
    except ValueError:
        return deny(f"Ścieżka {raw} leży poza projektem.")
    if rel == ".":
        rel = ""

    if rel and SECRET.search(rel):
        return deny(f"Plik {rel} wygląda na sekret i nie jest udostępniany.")

    for allowed in read_paths:
        base = allowed.strip().strip("/")
        if base in ("", "."):
            return 0
        if rel == base or rel.startswith(base + "/"):
            return 0
    return deny(f"Ścieżka {rel or '.'} jest poza zakresem zgody: {', '.join(read_paths)}.")


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
