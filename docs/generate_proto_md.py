#!/usr/bin/env python3
"""
CS2 Protobuf → Mermaid Markdown Diagram Generator

Inspired by https://github.com/GoogleCloudPlatform/proto-gen-md-diagrams

Reads every .proto file under the Protobufs/ directory and generates a
companion .proto.md file containing:

  1. A Mermaid classDiagram block showing every message and enum as a class
     node, with fields listed inside, plus directed arrows for message-type
     field references (composition) and enum usage.
  2. A Markdown table for each message describing every field: ordinal,
     type, label (optional/repeated/required), and any inline comment.

Output files are written to docs/proto-diagrams/ (one .proto.md per .proto
source file).  Because the output directory is tracked in the repository,
GitHub renders the Mermaid diagrams natively when you browse the files.

Usage:
    python3 docs/generate_proto_md.py [--repo-root PATH] [--output PATH]

Dependencies: Python 3.9+ standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Parser  (proto2 / proto3 compatible)
# ---------------------------------------------------------------------------

_PRIMITIVE_TYPES = {
    "double", "float", "int32", "int64", "uint32", "uint64",
    "sint32", "sint64", "fixed32", "fixed64", "sfixed32", "sfixed64",
    "bool", "string", "bytes",
}


def _strip_leading_dot(name: str) -> str:
    return name.lstrip(".")


def parse_proto(path: Path) -> dict[str, Any]:
    """Parse a single .proto file and return a structured dict.

    Keys:
      filename  – e.g. "netmessages.proto"
      imports   – list of imported filenames
      package   – package name string or ""
      messages  – list of message dicts
      enums     – list of top-level enum dicts
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    lines = text.splitlines()

    # ---- top-level metadata ----
    imports: list[str] = []
    package = ""
    for line in lines:
        s = line.strip()
        m = re.match(r'^import\s+"([^"]+)"', s)
        if m:
            imports.append(m.group(1))
        pm = re.match(r"^package\s+([\w.]+)\s*;", s)
        if pm:
            package = pm.group(1)

    messages: list[dict] = []
    top_enums: list[dict] = []

    # ---- stateful line-by-line parser ----
    i = 0
    depth = 0
    msg_stack: list[dict] = []
    pending_comments: list[str] = []

    def _new_msg(name: str, parent_fqn: str = "") -> dict:
        fqn = f"{parent_fqn}.{name}" if parent_fqn else name
        return {
            "name": name,
            "fqn": fqn,
            "fields": [],
            "nested": [],
            "enums": [],
            "comments": [],
        }

    def _new_enum(name: str) -> dict:
        return {"name": name, "values": [], "comments": list(pending_comments)}

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        i += 1

        # accumulate inline/line comments
        if s.startswith("//"):
            pending_comments.append(s[2:].strip())
            continue

        brace_open = s.count("{")
        brace_close = s.count("}")

        if depth == 0:
            msg_m = re.match(r"^message\s+(\w+)", s)
            enum_m = re.match(r"^enum\s+(\w+)", s)
            if msg_m:
                msg = _new_msg(msg_m.group(1))
                msg["comments"] = list(pending_comments)
                messages.append(msg)
                msg_stack = [msg]
                depth += brace_open - brace_close
                pending_comments = []
                continue
            if enum_m:
                en = _new_enum(enum_m.group(1))
                top_enums.append(en)
                depth += brace_open - brace_close
                while i < len(lines) and depth > 0:
                    l2 = lines[i].strip()
                    i += 1
                    depth += l2.count("{") - l2.count("}")
                    vm = re.match(r"(\w+)\s*=\s*(-?\d+)", l2)
                    if vm:
                        en["values"].append({"name": vm.group(1), "number": vm.group(2)})
                pending_comments = []
                continue

        # inside a message
        if msg_stack:
            msg = msg_stack[-1]

            # nested message
            nm = re.match(r"^message\s+(\w+)", s)
            if nm and brace_open > brace_close:
                nested = _new_msg(nm.group(1), msg.get("fqn", msg["name"]))
                nested["comments"] = list(pending_comments)
                msg["nested"].append(nested)
                msg_stack.append(nested)
                depth += brace_open - brace_close
                pending_comments = []
                continue

            # nested enum
            ne = re.match(r"^enum\s+(\w+)", s)
            if ne and brace_open > brace_close:
                en = _new_enum(ne.group(1))
                msg["enums"].append(en)
                depth += brace_open - brace_close
                while i < len(lines) and depth > len(msg_stack):
                    l2 = lines[i].strip()
                    i += 1
                    depth += l2.count("{") - l2.count("}")
                    vm = re.match(r"(\w+)\s*=\s*(-?\d+)", l2)
                    if vm:
                        en["values"].append({"name": vm.group(1), "number": vm.group(2)})
                pending_comments = []
                continue

            # oneof block – treat as transparent (just collect fields inside)
            if re.match(r"^oneof\s+\w+", s) and brace_open > brace_close:
                # just increase depth; fields will be parsed normally
                depth += brace_open - brace_close
                pending_comments = []
                continue

            # field declaration:
            # [label] [.] type name = number [options] ;
            field_m = re.match(
                r"^(optional|repeated|required)?\s*(?:\.)?([.\w]+)\s+(\w+)\s*=\s*(\d+)",
                s,
            )
            if field_m:
                label = field_m.group(1) or "optional"
                ftype = _strip_leading_dot(field_m.group(2))
                fname = field_m.group(3)
                fnumber = field_m.group(4)
                is_map = ftype.startswith("map<")
                # extract inline default / comment after ';'
                inline_comment_m = re.search(r"//\s*(.+)$", s)
                inline_comment = inline_comment_m.group(1).strip() if inline_comment_m else ""
                default_m = re.search(r'\[default\s*=\s*([^\],]+)', s)
                default_val = default_m.group(1).strip() if default_m else ""
                comment = " ".join(pending_comments) or inline_comment
                msg["fields"].append({
                    "name": fname,
                    "type": ftype,
                    "number": int(fnumber),
                    "label": label,
                    "comment": comment,
                    "default": default_val,
                    "is_map": is_map,
                })

        depth += brace_open - brace_close
        if depth < 0:
            depth = 0
        # pop nested message scopes as we close braces
        while len(msg_stack) > 1 and depth < len(msg_stack):
            msg_stack.pop()
        if depth == 0:
            msg_stack = []
        pending_comments = []

    return {
        "filename": path.name,
        "imports": imports,
        "package": package,
        "messages": messages,
        "enums": top_enums,
    }


# ---------------------------------------------------------------------------
# Mermaid Markdown generator  (proto-gen-md-diagrams compatible output)
# ---------------------------------------------------------------------------

# Types that should NOT get relationship arrows (primitives + well-known)
_SCALAR_TYPES = _PRIMITIVE_TYPES | {
    "google.protobuf.Timestamp", "google.protobuf.Duration",
    "google.protobuf.Any", "google.protobuf.Empty",
    "google.protobuf.Struct", "google.protobuf.Value",
    "google.protobuf.ListValue", "google.protobuf.FieldMask",
    "google.protobuf.BoolValue", "google.protobuf.StringValue",
    "google.protobuf.BytesValue", "google.protobuf.Int32Value",
    "google.protobuf.Int64Value", "google.protobuf.UInt32Value",
    "google.protobuf.UInt64Value", "google.protobuf.FloatValue",
    "google.protobuf.DoubleValue",
}


def _mermaid_safe(name: str) -> str:
    """Quote a name that contains dots or other special chars for Mermaid."""
    if re.match(r"^[A-Za-z_]\w*$", name):
        return name
    return f'"{name}"'


def _all_messages_in(proto: dict) -> list[dict]:
    """Flatten nested messages into a single list (BFS)."""
    result: list[dict] = []
    queue = list(proto["messages"])
    while queue:
        msg = queue.pop(0)
        result.append(msg)
        queue.extend(msg.get("nested", []))
    return result


def _all_enums_in(proto: dict) -> list[dict]:
    """Collect all enums: top-level + nested inside messages."""
    result = list(proto.get("enums", []))
    for msg in _all_messages_in(proto):
        result.extend(msg.get("enums", []))
    return result


def _build_local_name_set(proto: dict) -> set[str]:
    """Build the set of message and enum names defined in this proto file."""
    names: set[str] = set()
    for msg in _all_messages_in(proto):
        names.add(msg["name"])
        names.add(msg.get("fqn", msg["name"]))
    for en in _all_enums_in(proto):
        names.add(en["name"])
    return names


def _render_field_type(field: dict) -> str:
    """Human-readable type string including label decoration."""
    ftype = field["type"]
    label = field.get("label", "optional")
    if label == "repeated":
        return f"List~{ftype}~"
    return ftype


def _mermaid_class_block(msg: dict, local_names: set[str]) -> str:
    """Return the Mermaid class block lines for a message."""
    lines: list[str] = []
    comment = " ".join(msg.get("comments", []))
    if comment:
        lines.append(f"  %% {comment}")
    safe_name = _mermaid_safe(msg["name"])
    lines.append(f"  class {safe_name} {{")
    for field in msg["fields"]:
        type_str = _render_field_type(field)
        lines.append(f"    +{type_str} {field['name']}")
    lines.append("  }")
    return "\n".join(lines)


def _mermaid_enum_block(en: dict) -> str:
    """Return the Mermaid class block lines for an enum."""
    lines: list[str] = []
    comment = " ".join(en.get("comments", []))
    if comment:
        lines.append(f"  %% {comment}")
    safe_name = _mermaid_safe(en["name"])
    lines.append(f"  class {safe_name}{{")
    lines.append("    <<enumeration>>")
    for val in en.get("values", []):
        lines.append(f"    {val['name']}")
    lines.append("  }")
    return "\n".join(lines)


def _collect_relationships(msg: dict, local_names: set[str]) -> list[str]:
    """Return Mermaid relationship arrow lines for a message's fields."""
    arrows: list[str] = []
    seen: set[str] = set()
    src = _mermaid_safe(msg["name"])
    for field in msg["fields"]:
        raw_type = _strip_leading_dot(field["type"])
        # Skip scalars and unknown external types
        if raw_type in _SCALAR_TYPES:
            continue
        # Only draw arrows to types defined in this file
        simple = raw_type.split(".")[-1]
        if simple not in local_names and raw_type not in local_names:
            continue
        target = _mermaid_safe(simple)
        key = f"{src}-->{target}"
        if key in seen:
            continue
        seen.add(key)
        if field.get("label") == "repeated":
            arrows.append(f"  {src} --> {target} : {field['name']}[]")
        else:
            arrows.append(f"  {src} --> {target} : {field['name']}")
    return arrows


def _field_table(msg: dict) -> str:
    """Render a Markdown table for all fields of a message."""
    if not msg["fields"]:
        return ""
    rows: list[str] = [
        "| Field | Ordinal | Type | Label | Description |",
        "|-------|---------|------|-------|-------------|",
    ]
    for field in sorted(msg["fields"], key=lambda f: f["number"]):
        label = field.get("label", "optional")
        default = field.get("default", "")
        desc = field.get("comment", "")
        if default:
            desc = f"{desc} *(default: `{default}`)*" if desc else f"*(default: `{default}`)*"
        ftype = field["type"]
        rows.append(f"| `{field['name']}` | {field['number']} | `{ftype}` | {label} | {desc} |")
    return "\n".join(rows)


def generate_proto_md(proto: dict) -> str:
    """Generate the full Markdown content for one proto file."""
    fname = proto["filename"]
    all_msgs = _all_messages_in(proto)
    all_enums = _all_enums_in(proto)
    local_names = _build_local_name_set(proto)

    lines: list[str] = []

    # Jekyll front matter
    lines.append("---")
    lines.append(f"title: {fname}")
    lines.append("parent: Proto Diagrams")
    lines.append("nav_exclude: true")
    lines.append("---")
    lines.append("")

    # Header
    lines.append(f"# `{fname}`")
    lines.append("")
    if proto.get("imports"):
        lines.append("**Imports:** " + ", ".join(f"`{imp}`" for imp in proto["imports"]))
        lines.append("")

    if not all_msgs and not all_enums:
        lines.append("*No messages or enums defined in this file.*")
        return "\n".join(lines)

    # ---- Mermaid diagram ----
    lines.append("## Diagram")
    lines.append("")
    lines.append("```mermaid")
    lines.append("classDiagram")
    lines.append("direction LR")
    lines.append("")

    # Emit class blocks for messages
    for msg in all_msgs:
        lines.append(_mermaid_class_block(msg, local_names))
        lines.append("")

    # Emit relationship arrows for messages
    for msg in all_msgs:
        arrows = _collect_relationships(msg, local_names)
        if arrows:
            lines.extend(arrows)
            lines.append("")

    # Emit enum blocks
    for en in all_enums:
        lines.append(_mermaid_enum_block(en))
        lines.append("")

    lines.append("```")
    lines.append("")

    # ---- Top-level enum tables ----
    if proto.get("enums"):
        lines.append("## Enums")
        lines.append("")
        for en in proto["enums"]:
            comment = " ".join(en.get("comments", []))
            lines.append(f"### `{en['name']}`")
            lines.append("")
            if comment:
                lines.append(comment)
                lines.append("")
            if en["values"]:
                lines.append("| Name | Value |")
                lines.append("|------|-------|")
                for val in en["values"]:
                    lines.append(f"| `{val['name']}` | {val['number']} |")
                lines.append("")

    # ---- Message descriptions ----
    if all_msgs:
        lines.append("## Messages")
        lines.append("")
        for msg in all_msgs:
            comment = " ".join(msg.get("comments", []))
            indent = "  " * (msg.get("fqn", msg["name"]).count("."))
            lines.append(f"### `{msg.get('fqn', msg['name'])}`")
            lines.append("")
            if comment:
                lines.append(comment)
                lines.append("")
            table = _field_table(msg)
            if table:
                lines.append(table)
                lines.append("")

            # nested enums
            for en in msg.get("enums", []):
                en_comment = " ".join(en.get("comments", []))
                lines.append(f"#### `{msg['name']}.{en['name']}`")
                lines.append("")
                if en_comment:
                    lines.append(en_comment)
                    lines.append("")
                if en["values"]:
                    lines.append("| Name | Value |")
                    lines.append("|------|-------|")
                    for val in en["values"]:
                        lines.append(f"| `{val['name']}` | {val['number']} |")
                    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate Mermaid Markdown diagram docs for CS2 Protobuf files. "
            "Inspired by https://github.com/GoogleCloudPlatform/proto-gen-md-diagrams"
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to the repository root (default: current directory)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output directory for .proto.md files "
            "(default: docs/proto-diagrams/ under repo-root)"
        ),
    )
    parser.add_argument(
        "--proto-dir",
        default=None,
        help="Directory containing .proto files (default: Protobufs/ under repo-root)",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    proto_dir = Path(args.proto_dir).resolve() if args.proto_dir else repo_root / "Protobufs"
    out_dir = Path(args.output).resolve() if args.output else repo_root / "docs" / "proto-diagrams"

    if not proto_dir.is_dir():
        print(f"ERROR: proto directory not found: {proto_dir}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    proto_files = sorted(proto_dir.glob("*.proto"))
    if not proto_files:
        print(f"WARNING: no .proto files found in {proto_dir}", file=sys.stderr)
        return 0

    generated = 0
    for proto_path in proto_files:
        proto = parse_proto(proto_path)
        if not proto:
            continue
        md_content = generate_proto_md(proto)
        out_path = out_dir / f"{proto_path.name}.md"
        out_path.write_text(md_content, encoding="utf-8")
        generated += 1

    # Write an index README
    index_lines: list[str] = [
        "---",
        "title: Proto Diagrams",
        "nav_order: 6",
        "---",
        "",
        "# CS2 Protobuf Diagram Index",
        "",
        "Auto-generated Mermaid class diagrams for every CS2 Protobuf file.",
        "Inspired by [proto-gen-md-diagrams](https://github.com/GoogleCloudPlatform/proto-gen-md-diagrams).",
        "",
        "GitHub renders the Mermaid diagrams natively — click any file below to view.",
        "",
        "| File | Description |",
        "|------|-------------|",
    ]
    for proto_path in proto_files:
        stem = proto_path.name
        link = f"[{stem}](./{stem}.md)"
        # short description from the file's top-level comments
        try:
            first_comment = ""
            for line in proto_path.read_text(encoding="utf-8").splitlines():
                s = line.strip()
                if s.startswith("//"):
                    first_comment = s[2:].strip()
                    if first_comment:
                        break
        except OSError:
            first_comment = ""
        index_lines.append(f"| {link} | {first_comment} |")
    index_lines.append("")

    (out_dir / "README.md").write_text("\n".join(index_lines), encoding="utf-8")

    print(f"Generated {generated} .proto.md file(s) → {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
