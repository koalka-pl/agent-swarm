#!/usr/bin/env python3
"""Validate AgentSwarm state files against the plugin's JSON Schemas.

Usage:
    python3 validate.py <schema-name> <file.yaml|file.json>
    schema-name: project-state | audit-record | approval

Standard library only. Supports the YAML subset used by AgentSwarm state files
(block mappings, block sequences, inline [] and {}, quoted scalars, folded and
literal block scalars) and the JSON Schema keywords used by the bundled schemas.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

SCHEMAS = Path(__file__).resolve().parent / "schemas"


def scalar(raw: str):
    s = raw.strip()
    if s == "" or s in ("null", "~"):
        return None
    if s in ("true", "false"):
        return s == "true"
    if s == "[]":
        return []
    if s == "{}":
        return {}
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [scalar(p) for p in split_inline(inner)] if inner else []
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        out = {}
        for part in split_inline(inner):
            k, _, v = part.partition(":")
            out[k.strip().strip("\"'")] = scalar(v)
        return out
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        body = s[1:-1]
        return body.replace("\\\"", "\"") if s[0] == "\"" else body.replace("''", "'")
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


def split_inline(text: str) -> list[str]:
    parts, depth, quote, buf = [], 0, "", ""
    for ch in text:
        if quote:
            buf += ch
            if ch == quote:
                quote = ""
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(buf)
            buf = ""
            continue
        buf += ch
    if buf.strip():
        parts.append(buf)
    return parts


def strip_comment(line: str) -> str:
    quote = ""
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            return line[:i].rstrip()
    return line.rstrip()


class Parser:
    def __init__(self, text: str):
        self.lines = [l.rstrip("\n") for l in text.splitlines()]
        self.i = 0

    def indent(self, line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def skip(self):
        while self.i < len(self.lines):
            s = strip_comment(self.lines[self.i])
            if s.strip() and not s.strip().startswith("---"):
                return
            self.i += 1

    def parse(self, level: int):
        self.skip()
        if self.i >= len(self.lines):
            return None
        line = strip_comment(self.lines[self.i])
        if self.indent(line) < level:
            return None
        if line.strip().startswith("- ") or line.strip() == "-":
            return self.sequence(self.indent(line))
        return self.mapping(self.indent(line))

    def block_scalar(self, style: str, parent: int) -> str:
        collected = []
        while self.i < len(self.lines):
            raw = self.lines[self.i]
            if raw.strip() and self.indent(raw) <= parent:
                break
            collected.append(raw)
            self.i += 1
        nonblank = [l for l in collected if l.strip()]
        cut = min((self.indent(l) for l in nonblank), default=0)
        body = [l[cut:] for l in collected]
        while body and not body[-1].strip():
            body.pop()
        if style.startswith("|"):
            return "\n".join(body)
        return " ".join(l.strip() for l in body if l.strip())

    def value(self, rest: str, parent: int):
        rest = rest.strip()
        if rest.startswith(">") or rest.startswith("|"):
            return self.block_scalar(rest, parent)
        if rest:
            return scalar(rest)
        self.skip()
        if self.i < len(self.lines):
            nxt = strip_comment(self.lines[self.i])
            if self.indent(nxt) > parent or (self.indent(nxt) == parent and nxt.strip().startswith("- ")):
                return self.parse(self.indent(nxt))
        return None

    def mapping(self, level: int) -> dict:
        out = {}
        while True:
            self.skip()
            if self.i >= len(self.lines):
                return out
            line = strip_comment(self.lines[self.i])
            if self.indent(line) != level or line.strip().startswith("- "):
                return out
            m = re.match(r"\s*(\"[^\"]*\"|'[^']*'|[^:]+?):(?:\s+(.*)|\s*$)", line)
            if not m:
                raise ValueError(f"line {self.i + 1}: cannot parse: {line.strip()}")
            key = m.group(1).strip("\"'")
            self.i += 1
            out[key] = self.value(m.group(2) or "", level)

    def sequence(self, level: int) -> list:
        out = []
        while True:
            self.skip()
            if self.i >= len(self.lines):
                return out
            line = strip_comment(self.lines[self.i])
            if self.indent(line) != level or not (line.strip().startswith("- ") or line.strip() == "-"):
                return out
            rest = line.strip()[1:].strip()
            if re.match(r"(\"[^\"]*\"|'[^']*'|[^:\[{\"']+?):(\s|$)", rest):
                child = level + 2
                self.lines[self.i] = " " * child + rest
                out.append(self.mapping(child))
            else:
                self.i += 1
                out.append(self.value(rest, level))


def load(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    return Parser(text).parse(0)


def is_type(value, name: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "null": value is None,
        "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
    }[name]


def check(value, schema: dict, where: str, errors: list[str]):
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(is_type(value, t) for t in types):
            errors.append(f"{where}: expected {types}, got {type(value).__name__}")
            return
    if "const" in schema and value != schema["const"]:
        errors.append(f"{where}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{where}: must be one of {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{where}: shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{where}: does not match {schema['pattern']}")
        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"{where}: not an ISO-8601 date-time")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{where}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{where}: more than {schema['maxItems']} items")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(f"{where}: items are not unique")
        for n, item in enumerate(value):
            if "items" in schema:
                check(item, schema["items"], f"{where}[{n}]", errors)
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{where}: missing required '{key}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{where}: unexpected property '{key}'")
        for key, sub in props.items():
            if key in value:
                check(value[key], sub, f"{where}.{key}", errors)
    for rule in schema.get("allOf", []):
        cond = rule.get("if")
        if cond is not None:
            probe: list[str] = []
            check(value, cond, where, probe)
            if not probe and "then" in rule:
                check(value, rule["then"], where, errors)
        else:
            check(value, rule, where, errors)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__.strip())
        return 2
    schema_path = SCHEMAS / f"{argv[1]}.schema.json"
    if not schema_path.is_file():
        print(f"Unknown schema: {argv[1]}")
        return 2
    try:
        data = load(Path(argv[2]))
    except Exception as exc:
        print(f"FAILED {argv[2]}: parse error: {exc}")
        return 1
    errors: list[str] = []
    check(data, json.loads(schema_path.read_text(encoding="utf-8")), "$", errors)
    if errors:
        print(f"FAILED {argv[2]} against {argv[1]}:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"PASSED {argv[2]} against {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
