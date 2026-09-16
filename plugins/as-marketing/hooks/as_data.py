"""Resolve the AgentSwarm data directory of a project.

The directory is chosen by the user in /as-marketing:start and recorded in
<project>/.as.yaml as `data_dir: <relative path>`. Without that file, a legacy
<project>/.as/ directory is used if it exists. The data directory must be a
relative path strictly inside the project; anything else resolves to None.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

POINTER = ".as.yaml"
DEFAULT = ".as"


def project_dir(payload: dict) -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()


def data_dir(project: Path) -> Path | None:
    pointer = project / POINTER
    if pointer.is_file():
        match = re.search(r"(?m)^data_dir:[ \t]*[\"']?([^\"'#\n]*?)[\"']?[ \t]*(?:#.*)?$", pointer.read_text(encoding="utf-8"))
        raw = match.group(1).strip() if match else ""
        if not raw or os.path.isabs(raw):
            return None
        candidate = (project / raw).resolve()
        try:
            candidate.relative_to(project)
        except ValueError:
            return None
        return None if candidate == project else candidate
    legacy = project / DEFAULT
    return legacy if legacy.is_dir() else None


def relative(path: Path, project: Path) -> str:
    return path.relative_to(project).as_posix()
