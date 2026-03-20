#!/usr/bin/env python3
"""
CS2 Documentation Generator

Parses CS2 schema dumps (entity classes, enums), Protobuf definitions,
convars, and commands, then generates structured static-HTML documentation
with Mermaid UML diagrams.

Community annotations can be added by placing YAML overlay files under
docs/overlays/{module}/{EntityName}.yml  (see docs/overlays/README.md).

Usage:
    python3 docs/generate_docs.py [--repo-root PATH] [--output PATH]
                                  [--data-root PATH]

    --repo-root  Root of the repository that contains docs/, overlays/, etc.
                 (default: current directory)
    --data-root  Root of the CS2-OpenDevDocs data tree that contains
                 DumpSource2/ and Protobufs/.  Defaults to --repo-root, which
                 is the right value when running inside this repository.  Set
                 this to a submodule or sibling checkout path when running
                 from a standalone documentation repository.

Dependencies (all in the Python 3 stdlib except PyYAML):
    pip install pyyaml
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_schema_file(path: Path) -> dict[str, Any] | None:
    """Parse a single DumpSource2 C-style schema header file.

    Returns a dict with keys:
        name, kind ('class'|'enum'|'struct'), module,
        bases (list[str]), fields (list[dict]),
        metadata (list[str] – raw // M… annotation lines),
        raw (the original source text)
    Returns None if the file cannot be parsed meaningfully.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    name = path.stem
    module = path.parent.name

    # Collect top-level // M* metadata lines that appear before the main decl
    metadata: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            metadata.append(stripped[2:].strip())
        elif stripped and not stripped.startswith("//"):
            break

    # ---- Determine kind ----
    # enum (class)? NAME : underlying_type
    enum_m = re.search(r"\benum(?:\s+class)?\s+(\w+)\s*(?::\s*([\w:]+))?", text)
    # class/struct NAME : public BASE, public BASE2 ...
    class_m = re.search(
        r"\b(class|struct)\s+(\w+)(?:\s*:\s*([\w\s,<>:*&]+?))?\s*\{",
        text,
        re.DOTALL,
    )

    kind = "unknown"
    bases: list[str] = []

    if enum_m and (not class_m or (enum_m.start() < class_m.start())):
        kind = "enum"
        name = enum_m.group(1)
    elif class_m:
        kind = class_m.group(1)  # "class" or "struct"
        name = class_m.group(2)
        if class_m.group(3):
            raw_bases = class_m.group(3)
            # Extract base class names, stripping "public", "private", etc.
            bases = [
                b.strip().removeprefix("public").removeprefix("private")
                         .removeprefix("protected").strip()
                for b in raw_bases.split(",")
                if b.strip()
            ]
            bases = [b for b in bases if re.match(r"\w", b)]
    else:
        return None

    # ---- Parse body ----
    # Find the outermost { … } block
    brace_start = text.find("{")
    if brace_start == -1:
        return None
    depth = 0
    body_start = brace_start
    body_end = brace_start
    for i, ch in enumerate(text[brace_start:], brace_start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                body_end = i
                break
    body = text[body_start + 1 : body_end]

    fields: list[dict] = []

    if kind == "enum":
        for line in body.splitlines():
            line = line.strip().rstrip(",")
            if not line or line.startswith("//"):
                continue
            val_m = re.match(r"(\w+)\s*(?:=\s*(-?\d+|0x[\dA-Fa-f]+))?", line)
            if val_m:
                fields.append({"name": val_m.group(1), "value": val_m.group(2) or ""})
    else:
        # Collect field-level annotation comments and then the field declaration
        current_annots: list[str] = []
        for line in body.splitlines():
            stripped = line.strip()
            if stripped.startswith("//"):
                current_annots.append(stripped[2:].strip())
                continue
            if not stripped or stripped == "{" or stripped == "}":
                current_annots = []
                continue
            # Remove trailing semicolon/comma
            decl = stripped.rstrip(";").rstrip(",").strip()
            if not decl:
                current_annots = []
                continue
            # Try to parse: type fieldname (may include array suffix)
            # We care about the last token as the name
            field_m = re.match(
                r"(.+?)\s+(\w+)(\[[^\]]*\])?\s*$", decl
            )
            if field_m:
                field_type = field_m.group(1).strip()
                field_name = field_m.group(2).strip()
                array_suffix = field_m.group(3) or ""
                fields.append({
                    "name": field_name,
                    "type": field_type + array_suffix,
                    "annotations": list(current_annots),
                })
            current_annots = []

    return {
        "name": name,
        "kind": kind,
        "module": module,
        "bases": bases,
        "fields": fields,
        "metadata": metadata,
        "raw": text,
    }


def parse_all_schemas(schemas_root: Path) -> dict[str, dict]:
    """Walk schemas_root and parse every .h file.

    Returns a dict mapping entity name → entity dict.
    When the same name exists in multiple modules, the last one wins
    (with a 'duplicates' list tracking the others).
    """
    entities: dict[str, dict] = {}
    for h_file in sorted(schemas_root.rglob("*.h")):
        entity = parse_schema_file(h_file)
        if entity is None:
            continue
        name = entity["name"]
        if name in entities:
            entities[name].setdefault("duplicates", []).append(entity)
        else:
            entities[name] = entity
    return entities


def parse_proto_file(path: Path) -> dict[str, Any]:
    """Parse a .proto file and return a summary dict."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    # Collect file-level imports
    imports: list[str] = []
    for raw in text.splitlines():
        imp_m = re.match(r'^import\s+"([^"]+)"', raw.strip())
        if imp_m:
            imports.append(imp_m.group(1))

    messages: list[dict] = []
    enums: list[dict] = []

    def _new_msg(name: str) -> dict:
        return {"name": name, "fields": [], "enums": [], "nested": [], "comments": []}

    lines = text.splitlines()
    i = 0
    depth = 0
    # Stack of message dicts; top of stack is the "current" message we're filling.
    msg_stack: list[dict] = []
    pending_comments: list[str] = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        i += 1

        # Collect comment lines for next declaration
        if stripped.startswith("//"):
            pending_comments.append(stripped[2:].strip())
            continue

        brace_open = stripped.count("{")
        brace_close = stripped.count("}")

        # ---- Top-level message ----
        if depth == 0:
            msg_m = re.match(r"^message\s+(\w+)", stripped)
            enum_m = re.match(r"^enum\s+(\w+)", stripped)
            if msg_m:
                msg = _new_msg(msg_m.group(1))
                msg["comments"] = list(pending_comments)
                messages.append(msg)
                msg_stack = [msg]
                depth += brace_open - brace_close
                pending_comments = []
                continue
            if enum_m:
                en = {"name": enum_m.group(1), "values": [], "comments": list(pending_comments)}
                enums.append(en)
                depth += brace_open - brace_close
                # Consume enum body
                while i < len(lines) and depth > 0:
                    l2 = lines[i].strip()
                    i += 1
                    depth += l2.count("{") - l2.count("}")
                    val_m = re.match(r"(\w+)\s*=\s*(-?\d+)", l2)
                    if val_m:
                        en["values"].append({"name": val_m.group(1), "number": val_m.group(2)})
                pending_comments = []
                continue

        # ---- Inside a message ----
        if msg_stack:
            msg = msg_stack[-1]
            nested_m = re.match(r"^message\s+(\w+)", stripped)
            if nested_m and brace_open > brace_close:
                nested = _new_msg(nested_m.group(1))
                msg["nested"].append(nested)
                msg_stack.append(nested)
                depth += brace_open - brace_close
                pending_comments = []
                continue

            # Field declaration – capture label (optional/repeated/required)
            field_m = re.match(
                r"^(optional|repeated|required)?\s*(?:\.)?([.\w]+)\s+(\w+)\s*=\s*(\d+)",
                stripped,
            )
            if field_m:
                field = {
                    "type": field_m.group(2),
                    "name": field_m.group(3),
                    "number": field_m.group(4),
                    "label": field_m.group(1) or "optional",
                    "comment": " ".join(pending_comments),
                }
                default_m = re.search(r'\[default\s*=\s*([^\]]+)\]', stripped)
                if default_m:
                    field["default"] = default_m.group(1).strip()
                msg["fields"].append(field)

        depth += brace_open - brace_close
        if depth < 0:
            depth = 0
        # Pop message stack when a closing brace brings us up a level
        while len(msg_stack) > 1 and depth < len(msg_stack):
            msg_stack.pop()
        if depth == 0:
            msg_stack = []
        pending_comments = []

    return {
        "filename": path.name,
        "imports": imports,
        "messages": messages,
        "enums": enums,
    }


def parse_convars(path: Path) -> list[dict]:
    """Parse DumpSource2/convars.txt.

    Format per entry:
        name value (flag1 flag2 ...)
        \\tdescription text
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    convars: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.startswith("\t") or line.startswith(" "):
            i += 1
            continue
        # Header line: name [default_value] (flags)
        m = re.match(r"^(\S+)\s+(.*?)\s*\(([^)]*)\)\s*$", line)
        if m:
            name, default, flags_raw = m.group(1), m.group(2), m.group(3)
            description = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("\t"):
                description = lines[i + 1].strip()
                i += 1
            convars.append({
                "name": name,
                "default": default.strip(),
                "flags": [f.strip() for f in flags_raw.split() if f.strip()],
                "description": description,
            })
        i += 1
    return convars


def parse_commands(path: Path) -> list[dict]:
    """Parse DumpSource2/commands.txt.

    Format per entry:
        name (flag1 flag2 ...)
        \\tdescription text
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    commands: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.startswith("\t") or line.startswith(" "):
            i += 1
            continue
        m = re.match(r"^(\S+)\s*\(([^)]*)\)\s*$", line)
        if m:
            name, flags_raw = m.group(1), m.group(2)
            description = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("\t"):
                description = lines[i + 1].strip()
                i += 1
            commands.append({
                "name": name,
                "flags": [f.strip() for f in flags_raw.split() if f.strip()],
                "description": description,
            })
        i += 1
    return commands


# ---------------------------------------------------------------------------
# Game-events parser  (Valve KeyValues1 format)
# ---------------------------------------------------------------------------

# Known field types in .gameevents files and their JSON Schema equivalents.
_GAMEEVENTS_TYPE_MAP: dict[str, dict[str, str]] = {
    "none":                         {"type": "null",    "description": "Value is not networked"},
    "string":                       {"type": "string",  "description": "A zero-terminated string"},
    "bool":                         {"type": "boolean", "description": "Unsigned int, 1 bit"},
    "byte":                         {"type": "integer", "description": "Unsigned int, 8 bit"},
    "short":                        {"type": "integer", "description": "Signed int, 16 bit"},
    "long":                         {"type": "integer", "description": "Signed int, 32 bit"},
    "int":                          {"type": "integer", "description": "Signed integer"},
    "float":                        {"type": "number",  "description": "Float, 32 bit"},
    "uint64":                       {"type": "string",  "description": "Unsigned 64-bit integer (string-encoded)"},
    "local":                        {"type": "string",  "description": "Any data, not networked"},
    "player_controller":            {"type": "integer", "description": "Player controller entity reference"},
    "player_controller_and_pawn":   {"type": "integer", "description": "Player controller + pawn entity reference"},
    "player_pawn":                  {"type": "integer", "description": "Player pawn entity reference"},
    "ehandle":                      {"type": "integer", "description": "Entity handle"},
}

# These keys inside an event body are event-level metadata, not field defs.
_GAMEEVENTS_META_KEYS = {"local", "reliable"}


def parse_gameevents_file(path: Path) -> list[dict[str, Any]]:
    """Parse a Valve KeyValues1 ``.gameevents`` file.

    Returns a list of event dicts, each with:
        name        – event name
        comment     – trailing ``//`` comment on the event name line
        source      – basename of the originating file (e.g. ``mod.gameevents``)
        properties  – dict of event-level metadata (``local``, ``reliable``)
        fields      – list of ``{name, type, comment}`` dicts
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    source = path.name
    events: list[dict[str, Any]] = []
    lines = text.splitlines()
    i = 0
    total = len(lines)

    def _strip_comment(line: str) -> tuple[str, str]:
        """Return (code_part, comment_text) splitting on the first ``//``."""
        idx = line.find("//")
        if idx == -1:
            return line, ""
        return line[:idx], line[idx + 2:].strip()

    # Skip until the first top-level opening brace (root container).
    while i < total:
        code, _ = _strip_comment(lines[i])
        if "{" in code:
            i += 1
            break
        i += 1

    # Now we're inside the root object.  Each event is:
    #   "event_name"  // optional comment
    #   {
    #       "field" "type"  // optional comment
    #       ...
    #   }
    depth = 0
    pending_name: str | None = None
    pending_comment = ""
    # Collect comments that appear above an event name for group/section context
    section_comments: list[str] = []

    while i < total:
        raw_line = lines[i]
        code, comment = _strip_comment(raw_line)
        stripped = code.strip()
        i += 1

        # Pure comment line — accumulate for section headings
        if not stripped and comment:
            section_comments.append(comment)
            continue

        # Blank line
        if not stripped:
            # Reset section comments on blank non-comment lines only if
            # we haven't started an event yet.
            if pending_name is None:
                section_comments = []
            continue

        # Opening brace for an event body
        if stripped == "{" and depth == 0 and pending_name is not None:
            depth = 1
            event: dict[str, Any] = {
                "name": pending_name,
                "comment": pending_comment,
                "source": source,
                "properties": {},
                "fields": [],
            }
            pending_name = None
            pending_comment = ""
            section_comments = []

            # Parse event body
            while i < total:
                braw = lines[i]
                bcode, bcomment = _strip_comment(braw)
                bstripped = bcode.strip()
                i += 1

                if bstripped == "}":
                    depth = 0
                    break
                if not bstripped:
                    continue

                # Match key-value pairs: "key" "value"
                kv_match = re.match(
                    r'^\s*"([^"]+)"\s+"([^"]*)"', braw
                )
                if kv_match:
                    key = kv_match.group(1)
                    val = kv_match.group(2)
                    if key in _GAMEEVENTS_META_KEYS:
                        event["properties"][key] = val
                    else:
                        event["fields"].append({
                            "name": key,
                            "type": val,
                            "comment": bcomment,
                        })
                # Standalone quoted key with no value (shouldn't normally happen)
                # Skip it gracefully.
            events.append(event)
            continue

        # Closing brace of the root container
        if stripped == "}":
            break

        # Event name line: "event_name" // optional comment
        name_match = re.match(r'^\s*"([^"]+)"', raw_line)
        if name_match:
            pending_name = name_match.group(1)
            pending_comment = comment
            continue

    return events


def parse_all_gameevents(data_root: Path) -> list[dict[str, Any]]:
    """Find and parse all ``.gameevents`` files under the data tree.

    Searches the three known locations and any other ``.gameevents`` files.
    Returns a flat list of event dicts.
    """
    all_events: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for ge_file in sorted(data_root.rglob("*.gameevents")):
        real = str(ge_file.resolve())
        if real in seen_paths:
            continue
        seen_paths.add(real)
        all_events.extend(parse_gameevents_file(ge_file))
    return all_events


# ---------------------------------------------------------------------------
# Overlay loader
# ---------------------------------------------------------------------------

def load_overlays(overlays_root: Path) -> dict[str, dict]:
    """Walk overlays_root and load all YAML annotation files.

    Supports two formats:

    *Single-entity* (legacy): ``overlays/{module}/{EntityName}.yml``
        The file content is the overlay for exactly one entity.
        Key → ``{module}/{EntityName}``

    *Multi-entity* (module-level): ``overlays/{module}.yml``
        Top-level YAML keys are entity / message names; their values are
        individual overlay dicts.  Each entry expands to key
        ``{module}/{EntityName}``.

    Both formats can coexist.  If the same key appears in both, the
    single-entity file (processed last due to ``sorted``) wins.
    """
    if not HAS_YAML:
        return {}
    overlays: dict[str, dict] = {}
    for yml in sorted(overlays_root.rglob("*.yml")):
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        rel = yml.relative_to(overlays_root).with_suffix("")
        key = str(rel).replace("\\", "/")
        parts = key.split("/")
        if len(parts) == 1:
            # Module-level multi-entity file: each top-level key is an entity name.
            module = parts[0]
            for entity_name, entity_data in data.items():
                if isinstance(entity_data, dict):
                    overlays[f"{module}/{entity_name}"] = entity_data
        else:
            # Single-entity file (legacy format): use path as-is.
            overlays[key] = data
    return overlays


def get_overlay(overlays: dict[str, dict], module: str, name: str) -> dict:
    """Look up an overlay by module/name; fall back to just name."""
    key = f"{module}/{name}"
    if key in overlays:
        return overlays[key]
    # Also try matching by name alone across any module
    for k, v in overlays.items():
        if k.endswith(f"/{name}"):
            return v
    return {}



# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------



def _extract_type_refs(type_str: str, entities: dict[str, dict]) -> list[str]:
    """Return names of known schema entities referenced in a field type string."""
    seen: list[str] = []
    for m in re.finditer(r"\b[A-Z_]\w+\b", type_str):
        word = m.group(0)
        if word in entities and word not in seen:
            seen.append(word)
    return seen


def _mermaid_safe(name: str) -> str:
    """Make a name safe for Mermaid by quoting if needed."""
    if re.match(r"^[A-Za-z_]\w*$", name):
        return name
    return f'"{name}"'


def _entity_anchor(name: str) -> str:
    """Return the kramdown heading anchor for an entity name (lowercase)."""
    return name.lower()


# Proto primitive scalar types that do not get anchor-linked.
_PROTO_PRIMITIVES = {
    "double", "float", "int32", "int64", "uint32", "uint64",
    "sint32", "sint64", "fixed32", "fixed64", "sfixed32", "sfixed64",
    "bool", "string", "bytes",
}


def _proto_anchor(name: str) -> str:
    """Return the GitHub Markdown anchor for a proto section heading like ``### `Name` ``."""
    # GitHub lowercases and strips all chars except word chars (a-z0-9_) and hyphens.
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    return slug.strip().replace(" ", "-")


def _proto_link_type(ftype: str, local_names: set[str]) -> str:
    """Return plain type text for primitives; an anchor link for known local types."""
    raw = ftype.lstrip(".")
    simple = raw.split(".")[-1]
    if simple in _PROTO_PRIMITIVES or simple not in local_names:
        return raw
    return f"[{simple}](#{_proto_anchor(simple)})"


def _md_link_type(
    type_str: str, entities: dict[str, dict], current_module: str = ""
) -> str:
    """Wrap known entity names in a type string with Markdown links (anchor-based).

    When *current_module* is supplied and the referenced entity also exists in
    that module (as a duplicate), the link targets the current-module page so
    readers stay within the same schema page.
    """
    def replace(m: re.Match) -> str:
        word = m.group(0)
        if word in entities:
            e = entities[word]
            mod = e["module"]
            # Prefer a same-module link when the entity exists in current_module
            if current_module and current_module != mod:
                if any(d["module"] == current_module for d in e.get("duplicates", [])):
                    mod = current_module
            return f"[{word}](../schemas/{mod}.md#{_entity_anchor(word)})"
        return word

    return re.sub(r"\b[A-Z_]\w+\b", replace, type_str)


def _md_front_matter(**kwargs: str) -> str:
    """Render a YAML front matter block for Jekyll."""
    lines = ["---"]
    for key, val in kwargs.items():
        # Quote values that might confuse YAML
        if any(c in str(val) for c in (':', '#', '[', ']', '{', '}')):
            lines.append(f'{key}: "{val}"')
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_entity_md_page(
    entity: dict,
    entities: dict[str, dict],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate a Jekyll Markdown page for a single entity."""
    mod = entity["module"]
    name = entity["name"]
    kind = entity["kind"]
    overlay = get_overlay(overlays, mod, name)

    out_file = out_dir / "entity" / mod / f"{name}.md"
    out_file.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []

    # Front matter
    lines.append(_md_front_matter(
        layout="default",
        title=name,
        parent=mod,
        grand_parent="Schemas",
        nav_exclude="true",
    ))

    # Title
    lines.append(f"# `{kind}` {name}\n")

    # Description / notes / warning from overlay
    if overlay.get("description"):
        lines.append(f"{overlay['description']}\n")
    if overlay.get("notes"):
        lines.append(f"> 📝 {overlay['notes']}\n")
    if overlay.get("warning"):
        lines.append(f"> ⚠️ {overlay['warning']}\n")

    # Bases / derived
    if entity.get("bases"):
        base_links = []
        for b in entity["bases"]:
            if b in entities:
                bmod = entities[b]["module"]
                base_links.append(f"[{b}](../{bmod}/{b}.md)")
            else:
                base_links.append(b)
        lines.append(f"**Inherits from:** {', '.join(base_links)}\n")

    derived = sorted(
        [e for e in entities.values() if name in e.get("bases", [])],
        key=lambda x: x["name"],
    )
    if derived:
        links = [f"[{d['name']}](../{d['module']}/{d['name']}.md)" for d in derived]
        lines.append(f"**Derived by:** {', '.join(links)}\n")

    # Metadata tags – exclude MNetworkVarNames entries because they only
    # repeat the field name/type information already shown in the Fields table.
    if entity.get("metadata"):
        tags = [
            f"`{m}`" for m in entity["metadata"]
            if m and not m.startswith("MNetworkVarNames")
        ]
        if tags:
            lines.append(f"**Metadata:** {', '.join(tags)}\n")

    # Relationships diagram
    diagram_lines = _build_md_relationship_diagram(name, entity, entities)
    if diagram_lines:
        lines.append("## Relationships\n")
        lines.append("```mermaid")
        lines.append("classDiagram")
        lines.extend(diagram_lines)
        lines.append("```\n")

    # Fields / enum values
    if kind == "enum":
        vals = entity.get("fields", [])
        if vals:
            lines.append("## Values\n")
            lines.append("| Name | Value |")
            lines.append("|------|-------|")
            for fld in vals:
                lines.append(f"| `{fld['name']}` | {fld.get('value', '')} |")
            lines.append("")
    else:
        fields = entity.get("fields", [])
        if fields:
            overlay_fields: dict = overlay.get("fields", {}) or {}
            lines.append("## Fields\n")
            lines.append("| Name | Type | Annotations |")
            lines.append("|------|------|-------------|")
            for fld in fields:
                fname = fld.get("name", "")
                ftype = fld.get("type", "")
                annots = fld.get("annotations", [])
                fover = overlay_fields.get(fname, {}) if isinstance(overlay_fields, dict) else {}
                type_linked = _md_link_type(ftype, entities, mod)
                annot_str = " ".join(f"`{a}`" for a in annots if a)
                desc_parts = []
                if fover and isinstance(fover, dict):
                    if fover.get("description"):
                        desc_parts.append(str(fover["description"]))
                    if fover.get("notes"):
                        desc_parts.append(f"*{fover['notes']}*")
                if annot_str:
                    desc_parts.append(annot_str)
                lines.append(f"| `{fname}` | {type_linked} | {' '.join(desc_parts)} |")


def _build_md_relationship_diagram(
    name: str,
    entity: dict,
    entities: dict[str, dict],
) -> list[str]:
    """Build Mermaid classDiagram lines for an entity's relationships."""
    lines: list[str] = []
    seen_edges: set[tuple[str, str]] = set()

    # Walk up inheritance chain (up to 5 levels)
    chain: list[str] = [name]
    current = entity
    for _ in range(5):
        bases = current.get("bases", [])
        if not bases:
            break
        parent = bases[0]
        chain.append(parent)
        current = entities.get(parent, {})
        if not current:
            break

    for i in range(len(chain) - 1):
        child = chain[i]
        parent = chain[i + 1]
        edge = (parent, child)
        if edge not in seen_edges:
            lines.append(f"    {_mermaid_safe(parent)} <|-- {_mermaid_safe(child)}")
            seen_edges.add(edge)

    for e in entities.values():
        if name in e.get("bases", []) and e["name"] != name:
            edge = (name, e["name"])
            if edge not in seen_edges:
                lines.append(f"    {_mermaid_safe(name)} <|-- {_mermaid_safe(e['name'])}")
                seen_edges.add(edge)

    comp_count = 0
    for fld in entity.get("fields", []):
        if comp_count >= 10:
            break
        for ref in _extract_type_refs(fld.get("type", ""), entities):
            if ref == name or comp_count >= 10:
                continue
            edge = (name, ref)
            if edge not in seen_edges:
                ftype = fld.get("type", "")
                arrow = "-->" if ("*" in ftype or "CHandle" in ftype) else "*--"
                lines.append(f"    {_mermaid_safe(name)} {arrow} {_mermaid_safe(ref)}")
                seen_edges.add(edge)
                comp_count += 1

    return lines


def generate_schemas_index_md(
    entities: dict[str, dict],
    overlays: dict[str, dict],
    out_dir: Path,
    diagram_modules: set[str] | None = None,
) -> None:
    """Generate schemas.md (master index) and per-module Markdown pages.

    Entity details are embedded directly in the per-module pages using
    ``### EntityName`` headings (anchor: ``#entityname``) so no separate
    per-entity files are needed.
    """
    by_module: dict[str, list[dict]] = defaultdict(list)
    for entity in entities.values():
        by_module[entity["module"]].append(entity)
        # Also include duplicates (same entity name, different module e.g. client+server)
        for dup in entity.get("duplicates", []):
            by_module[dup["module"]].append(dup)

    # Master schemas.md
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Schemas", nav_order="2"))
    lines.append("# Schema Reference\n")
    lines.append("All entities and types extracted from CS2's schema dump, organised by module.\n")
    lines.append("## Modules\n")
    lines.append("| Module | Entities | UML |")
    lines.append("|--------|----------|-----|")
    for mod in sorted(by_module):
        count = len(by_module[mod])
        has_diagram = diagram_modules is None or mod in diagram_modules
        uml_cell = f"[📊 Diagram](diagrams/{mod}.md)" if has_diagram else "—"
        lines.append(
            f"| [{mod}](schemas/{mod}.md) | {count} | {uml_cell} |"
        )
    lines.append("")
    (out_dir / "schemas.md").write_text("\n".join(lines), encoding="utf-8")

    # Per-module pages – entity details embedded with heading anchors
    (out_dir / "schemas").mkdir(exist_ok=True)
    for mod, ents in by_module.items():
        sorted_ents = sorted(ents, key=lambda x: x["name"])
        m_lines: list[str] = []
        m_lines.append(_md_front_matter(
            layout="default",
            title=mod,
            parent="Schemas",
            nav_exclude="true",
        ))
        m_lines.append(f"# Module: {mod}\n")
        if diagram_modules is None or mod in diagram_modules:
            m_lines.append(f"[📊 View UML Diagram](../diagrams/{mod}.md)\n")

        # Quick-reference index table with anchor links
        m_lines.append("| Name | Kind | Bases | Fields |")
        m_lines.append("|------|------|-------|--------|")
        for e in sorted_ents:
            anchor = _entity_anchor(e["name"])
            bases_str = ", ".join(e.get("bases", []))
            field_count = len(e.get("fields", []))
            m_lines.append(
                f"| [{e['name']}](#{anchor}) | {e['kind']} | {bases_str} | {field_count} |"
            )
        m_lines.append("")

        # Full entity detail sections
        m_lines.append("---\n")
        for e in sorted_ents:
            name = e["name"]
            kind = e["kind"]
            overlay = get_overlay(overlays, mod, name)

            m_lines.append(f"### {name}\n")

            if overlay.get("description"):
                m_lines.append(f"{overlay['description']}\n")
            if overlay.get("notes"):
                m_lines.append(f"> 📝 {overlay['notes']}\n")
            if overlay.get("warning"):
                m_lines.append(f"> ⚠️ {overlay['warning']}\n")

            # Bases / derived
            if e.get("bases"):
                base_links = []
                for b in e["bases"]:
                    if b in entities:
                        bmod = entities[b]["module"]
                        # Prefer same-module link when the base also exists in this module
                        if bmod != mod and any(
                            d["module"] == mod for d in entities[b].get("duplicates", [])
                        ):
                            bmod = mod
                        base_links.append(f"[{b}]({bmod}.md#{_entity_anchor(b)})")
                    else:
                        base_links.append(b)
                m_lines.append(f"**Inherits from:** {', '.join(base_links)}\n")

            derived = sorted(
                [d for d in entities.values() if name in d.get("bases", [])],
                key=lambda x: x["name"],
            )
            if derived:
                links = [
                    f"[{d['name']}]({d['module']}.md#{_entity_anchor(d['name'])})"
                    for d in derived
                ]
                m_lines.append(f"**Derived by:** {', '.join(links)}\n")

            # Metadata tags – exclude MNetworkVarNames entries because they
            # only repeat the field name/type already in the Fields table.
            if e.get("metadata"):
                tags = [
                    f"`{m}`" for m in e["metadata"]
                    if m and not m.startswith("MNetworkVarNames")
                ]
                if tags:
                    m_lines.append(f"**Metadata:** {', '.join(tags)}\n")

            # Relationship diagram
            diagram_lines = _build_md_relationship_diagram(name, e, entities)
            if diagram_lines:
                m_lines.append("**Relationships:**\n")
                m_lines.append("```mermaid")
                m_lines.append("classDiagram")
                m_lines.extend(diagram_lines)
                m_lines.append("```\n")

            # Fields / enum values
            if kind == "enum":
                vals = e.get("fields", [])
                if vals:
                    m_lines.append("**Values:**\n")
                    m_lines.append("| Name | Value |")
                    m_lines.append("|------|-------|")
                    for fld in vals:
                        m_lines.append(f"| `{fld['name']}` | {fld.get('value', '')} |")
                    m_lines.append("")
            else:
                fields = e.get("fields", [])
                if fields:
                    overlay_fields: dict = overlay.get("fields", {}) or {}
                    m_lines.append("**Fields:**\n")
                    m_lines.append("| Name | Type | Annotations |")
                    m_lines.append("|------|------|-------------|")
                    for fld in fields:
                        fname = fld.get("name", "")
                        ftype = fld.get("type", "")
                        annots = fld.get("annotations", [])
                        fover = overlay_fields.get(fname, {}) if isinstance(overlay_fields, dict) else {}
                        type_linked = _md_link_type(ftype, entities, mod)
                        annot_str = " ".join(f"`{a}`" for a in annots if a)
                        desc_parts = []
                        if fover and isinstance(fover, dict):
                            if fover.get("description"):
                                desc_parts.append(str(fover["description"]))
                            if fover.get("notes"):
                                desc_parts.append(f"*{fover['notes']}*")
                        if annot_str:
                            desc_parts.append(annot_str)
                        m_lines.append(f"| `{fname}` | {type_linked} | {' '.join(desc_parts)} |")
                    m_lines.append("")

        (out_dir / "schemas" / f"{mod}.md").write_text(
            "\n".join(m_lines), encoding="utf-8"
        )


def generate_module_uml_md(entities: dict[str, dict], out_dir: Path) -> set[str]:
    """Generate per-module UML Markdown pages at diagrams/{mod}.md."""
    by_module: dict[str, list[dict]] = defaultdict(list)
    for e in entities.values():
        by_module[e["module"]].append(e)
        # Also include duplicates (same entity name, different module e.g. client+server)
        for dup in e.get("duplicates", []):
            by_module[dup["module"]].append(dup)

    (out_dir / "diagrams").mkdir(exist_ok=True)
    generated: set[str] = set()

    for mod, ents in sorted(by_module.items()):
        ent_names = {e["name"] for e in ents}
        diagram_lines: list[str] = []
        seen_edges: set[tuple[str, str]] = set()

        for e in ents:
            for base in e.get("bases", []):
                edge = (base, e["name"])
                if edge not in seen_edges:
                    diagram_lines.append(
                        f"    {_mermaid_safe(base)} <|-- {_mermaid_safe(e['name'])}"
                    )
                    seen_edges.add(edge)

        for e in ents:
            ename = e["name"]
            for fld in e.get("fields", []):
                for ref in _extract_type_refs(fld.get("type", ""), entities):
                    if ref == ename or ref not in ent_names:
                        continue
                    edge = (ename, ref)
                    if edge not in seen_edges:
                        ftype = fld.get("type", "")
                        arrow = "-->" if ("*" in ftype or "CHandle" in ftype) else "*--"
                        diagram_lines.append(
                            f"    {_mermaid_safe(ename)} {arrow} {_mermaid_safe(ref)}"
                        )
                        seen_edges.add(edge)
            if len(diagram_lines) >= 300:
                break

        if not diagram_lines:
            continue

        cap = 300
        capped = diagram_lines[:cap]
        extra = len(diagram_lines) - cap
        count_note = f" (showing {cap} of {len(diagram_lines)} relationships)" if extra > 0 else ""

        md_lines: list[str] = []
        md_lines.append(_md_front_matter(
            layout="default",
            title=f"UML: {mod}",
            parent="Schemas",
            nav_exclude="true",
        ))
        md_lines.append(f"# UML: {mod}\n")
        md_lines.append(
            f"Class relationships (inheritance and composition) for the `{mod}` module{count_note}.\n"
        )
        md_lines.append(
            "**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer\n"
        )
        md_lines.append("```mermaid")
        md_lines.append("classDiagram")
        md_lines.extend(capped)
        md_lines.append("```\n")

        (out_dir / "diagrams" / f"{mod}.md").write_text(
            "\n".join(md_lines), encoding="utf-8"
        )
        generated.add(mod)

    return generated


def _build_proto_mermaid(proto: dict) -> list[str]:
    """Build Mermaid classDiagram lines for a proto file.

    Returns a list of lines to be embedded inside a ``classDiagram`` block.
    Returns an empty list when there is nothing to diagram.
    """
    _SCALARS = {
        "double", "float", "int32", "int64", "uint32", "uint64",
        "sint32", "sint64", "fixed32", "fixed64", "sfixed32", "sfixed64",
        "bool", "string", "bytes",
    }

    def _flat_msgs(msgs: list) -> list:
        result: list = []
        for m in msgs:
            result.append(m)
            result.extend(_flat_msgs(m.get("nested", [])))
        return result

    all_msgs = _flat_msgs(proto.get("messages", []))
    all_enums = list(proto.get("enums", []))
    for msg in all_msgs:
        all_enums.extend(msg.get("enums", []))

    if not all_msgs and not all_enums:
        return []

    local_names: set[str] = {m["name"] for m in all_msgs} | {e["name"] for e in all_enums}

    lines: list[str] = ["direction LR", ""]

    for msg in all_msgs:
        safe = _mermaid_safe(msg["name"])
        lines.append(f"  class {safe} {{")
        for fld in msg.get("fields", []):
            ftype = fld["type"].lstrip(".")
            type_str = f"List~{ftype}~" if fld.get("label") == "repeated" else ftype
            lines.append(f"    +{type_str} {fld['name']}")
        lines.append("  }")
        lines.append("")

    # Relationship arrows (message-type fields within the same file)
    seen_arrows: set[str] = set()
    for msg in all_msgs:
        src = _mermaid_safe(msg["name"])
        for fld in msg.get("fields", []):
            raw = fld["type"].lstrip(".")
            simple = raw.split(".")[-1]
            if simple not in local_names or simple in _SCALARS:
                continue
            tgt = _mermaid_safe(simple)
            arrow_key = f"{src}-->{tgt}"
            if arrow_key in seen_arrows:
                continue
            seen_arrows.add(arrow_key)
            suffix = "[]" if fld.get("label") == "repeated" else ""
            lines.append(f"  {src} --> {tgt} : {fld['name']}{suffix}")
    if seen_arrows:
        lines.append("")

    for en in all_enums:
        safe = _mermaid_safe(en["name"])
        lines.append(f"  class {safe}{{")
        lines.append("    <<enumeration>>")
        for v in en.get("values", []):
            lines.append(f"    {v['name']}")
        lines.append("  }")
        lines.append("")

    return lines


def generate_protobufs_md_page(
    protos: list[dict],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate protobufs.md and per-file proto Markdown pages."""
    (out_dir / "proto").mkdir(exist_ok=True)

    # Master index
    idx_lines: list[str] = []
    idx_lines.append(_md_front_matter(layout="default", title="Protobufs", nav_order="3"))
    idx_lines.append("# Protobuf Reference\n")
    idx_lines.append("Network message definitions and game event structures from CS2's Protobufs directory.\n")
    idx_lines.append("| File | Messages | Enums |")
    idx_lines.append("|------|----------|-------|")
    for proto in sorted(protos, key=lambda x: x["filename"]):
        fname = proto["filename"]
        stem = fname.removesuffix(".proto")
        msg_count = len(proto.get("messages", []))
        enum_count = len(proto.get("enums", []))
        idx_lines.append(f"| [{fname}](proto/{stem}.md) | {msg_count} | {enum_count} |")
    idx_lines.append("")
    (out_dir / "protobufs.md").write_text("\n".join(idx_lines), encoding="utf-8")

    # Per-file pages
    for proto in protos:
        pfile = proto["filename"]
        stem = pfile.removesuffix(".proto")
        overlay = overlays.get(f"protobufs/{stem}", {})

        p_lines: list[str] = []
        p_lines.append(_md_front_matter(
            layout="default",
            title=pfile,
            parent="Protobufs",
            nav_exclude="true",
        ))
        p_lines.append(f"# `{pfile}`\n")

        # File-level imports
        if proto.get("imports"):
            p_lines.append(
                "**Imports:** " + ", ".join(f"`{imp}`" for imp in proto["imports"]) + "\n"
            )

        if overlay.get("description"):
            p_lines.append(f"{overlay['description']}\n")
        if overlay.get("notes"):
            p_lines.append(f"> 📝 {overlay['notes']}\n")

        # Mermaid class diagram
        diagram = _build_proto_mermaid(proto)
        if diagram:
            p_lines.append("## Diagram\n")
            p_lines.append("```mermaid")
            p_lines.append("classDiagram")
            p_lines.extend(diagram)
            p_lines.append("```\n")

        if proto.get("enums"):
            p_lines.append("## Enums\n")
            for en in proto["enums"]:
                p_lines.append(f"### `{en['name']}`\n")
                p_lines.append("| Name | Value |")
                p_lines.append("|------|-------|")
                for v in en.get("values", []):
                    p_lines.append(f"| `{v['name']}` | {v['number']} |")
                p_lines.append("")

        # Build a set of local type names (messages + enums) for anchor-linking.
        local_names: set[str] = (
            {m["name"] for m in proto.get("messages", [])}
            | {e["name"] for e in proto.get("enums", [])}
        )

        overlay_msgs: dict = overlay.get("messages", {}) or {}
        if proto.get("messages"):
            p_lines.append("## Messages\n")
            for msg in proto["messages"]:
                mname = msg["name"]
                mover = overlay_msgs.get(mname, {}) if isinstance(overlay_msgs, dict) else {}
                p_lines.append(f"### `{mname}`\n")
                if mover and isinstance(mover, dict) and mover.get("description"):
                    p_lines.append(f"{mover['description']}\n")
                if mover and isinstance(mover, dict) and mover.get("notes"):
                    p_lines.append(f"> 📝 {mover['notes']}\n")

                if msg.get("fields"):
                    overlay_flds: dict = (
                        mover.get("fields", {}) or {}
                        if mover and isinstance(mover, dict) else {}
                    )
                    p_lines.append("| Field | Ordinal | Type | Label | Description |")
                    p_lines.append("|-------|---------|------|-------|-------------|")
                    for fld in sorted(
                        msg["fields"], key=lambda f: int(f.get("number", "0"))
                    ):
                        fname_fld = fld["name"]
                        ftype = fld["type"]
                        label = fld.get("label", "optional")
                        fnum = fld.get("number", "")
                        ftype_display = _proto_link_type(ftype, local_names)
                        # Build description from overlay + proto inline comment + default
                        desc_parts: list[str] = []
                        fover = (
                            overlay_flds.get(fname_fld, {})
                            if isinstance(overlay_flds, dict) else {}
                        )
                        if fover and isinstance(fover, dict) and fover.get("description"):
                            desc_parts.append(str(fover["description"]))
                        comment = fld.get("comment", "")
                        if comment:
                            desc_parts.append(comment)
                        default = fld.get("default", "")
                        if default:
                            desc_parts.append(f"*(default: `{default}`)*")
                        desc = " ".join(desc_parts).replace("|", "\\|")
                        p_lines.append(
                            f"| `{fname_fld}` | {fnum} | {ftype_display} | {label} | {desc} |"
                        )
                    p_lines.append("")

        (out_dir / "proto" / f"{stem}.md").write_text("\n".join(p_lines), encoding="utf-8")


def generate_convars_md_page(convars: list[dict], out_dir: Path) -> None:
    """Generate convars.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="ConVars", nav_order="4"))
    lines.append("# ConVar Reference\n")
    lines.append("All console variables extracted from CS2.\n")
    lines.append("| Name | Default | Flags | Description |")
    lines.append("|------|---------|-------|-------------|")
    for cv in convars:
        flags = " ".join(f"`{f}`" for f in cv["flags"])
        desc = cv["description"] or ""
        # Escape pipe characters in markdown table cells
        desc = desc.replace("|", "\\|")
        lines.append(f"| `{cv['name']}` | `{cv['default']}` | {flags} | {desc} |")
    lines.append("")
    (out_dir / "convars.md").write_text("\n".join(lines), encoding="utf-8")


def generate_commands_md_page(commands: list[dict], out_dir: Path) -> None:
    """Generate commands.md."""
    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Commands", nav_order="5"))
    lines.append("# Console Commands\n")
    lines.append("All console commands extracted from CS2.\n")
    lines.append("| Command | Flags | Description |")
    lines.append("|---------|-------|-------------|")
    for cmd in commands:
        flags = " ".join(f"`{f}`" for f in cmd["flags"])
        desc = (cmd["description"] or "").replace("|", "\\|")
        lines.append(f"| `{cmd['name']}` | {flags} | {desc} |")
    lines.append("")
    (out_dir / "commands.md").write_text("\n".join(lines), encoding="utf-8")


def generate_gameevents_md_page(
    gameevents: list[dict[str, Any]],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate gameevents.md – the Game Events documentation page."""
    overlay = overlays.get("gameevents", {})
    overlay_events: dict = overlay.get("events", {}) or {}

    lines: list[str] = []
    lines.append(_md_front_matter(layout="default", title="Game Events", nav_order="6"))
    lines.append("# Game Events Reference\n")
    lines.append(
        "Game events extracted from CS2's `.gameevents` resource files. "
        "These events are fired by the game engine and server to signal "
        "in-game occurrences such as player actions, round state changes, "
        "and UI notifications.\n"
    )
    if overlay.get("description"):
        lines.append(f"{overlay['description']}\n")
    if overlay.get("notes"):
        lines.append(f"> 📝 {overlay['notes']}\n")

    # Data-type legend
    lines.append("## Field Types\n")
    lines.append("| Type | Description |")
    lines.append("|------|-------------|")
    for tname, tinfo in sorted(_GAMEEVENTS_TYPE_MAP.items()):
        lines.append(f"| `{tname}` | {tinfo['description']} |")
    lines.append("")

    # Group events by source file
    by_source: dict[str, list[dict]] = {}
    for ev in gameevents:
        by_source.setdefault(ev["source"], []).append(ev)

    source_labels: dict[str, str] = {
        "core.gameevents": "Core Engine Events",
        "game.gameevents": "Game Events",
        "mod.gameevents": "CS2 (Counter-Strike) Events",
    }

    # Summary table
    lines.append("## Summary\n")
    lines.append(f"**Total events:** {len(gameevents)}\n")
    lines.append("| Source | Events | Description |")
    lines.append("|--------|--------|-------------|")
    for src in sorted(by_source):
        label = source_labels.get(src, src)
        lines.append(f"| `{src}` | {len(by_source[src])} | {label} |")
    lines.append("")

    # Quick-reference index
    lines.append("## Event Index\n")
    lines.append("| Event | Source | Fields | Description |")
    lines.append("|-------|--------|--------|-------------|")
    for ev in gameevents:
        anchor = ev["name"].lower().replace(" ", "-")
        eov = overlay_events.get(ev["name"], {}) if isinstance(overlay_events, dict) else {}
        desc = ""
        if eov and isinstance(eov, dict) and eov.get("description"):
            desc = str(eov["description"])
        elif ev["comment"]:
            desc = ev["comment"]
        desc = desc.replace("|", "\\|")
        lines.append(
            f"| [{ev['name']}](#{anchor}) | `{ev['source']}` | {len(ev['fields'])} | {desc} |"
        )
    lines.append("")

    # Detailed event sections grouped by source
    lines.append("---\n")
    for src in sorted(by_source):
        label = source_labels.get(src, src)
        lines.append(f"## {label}\n")
        lines.append(f"*Source: `{src}`*\n")

        for ev in by_source[src]:
            ename = ev["name"]
            eov = overlay_events.get(ename, {}) if isinstance(overlay_events, dict) else {}

            lines.append(f"### {ename}\n")

            # Description from overlay, then from inline comment
            if eov and isinstance(eov, dict) and eov.get("description"):
                lines.append(f"{eov['description']}\n")
            elif ev["comment"]:
                lines.append(f"{ev['comment']}\n")

            if eov and isinstance(eov, dict) and eov.get("notes"):
                lines.append(f"> 📝 {eov['notes']}\n")
            if eov and isinstance(eov, dict) and eov.get("warning"):
                lines.append(f"> ⚠️ {eov['warning']}\n")

            # Event-level properties
            if ev["properties"]:
                props = ", ".join(f"`{k}={v}`" for k, v in ev["properties"].items())
                lines.append(f"**Properties:** {props}\n")

            if ev["fields"]:
                overlay_flds: dict = (
                    eov.get("fields", {}) or {}
                    if eov and isinstance(eov, dict) else {}
                )
                lines.append("| Field | Type | Description |")
                lines.append("|-------|------|-------------|")
                for fld in ev["fields"]:
                    fname = fld["name"]
                    ftype = fld["type"]
                    fov = overlay_flds.get(fname, {}) if isinstance(overlay_flds, dict) else {}
                    desc_parts: list[str] = []
                    if fov and isinstance(fov, dict) and fov.get("description"):
                        desc_parts.append(str(fov["description"]))
                    if fld["comment"]:
                        desc_parts.append(fld["comment"])
                    if fov and isinstance(fov, dict) and fov.get("notes"):
                        desc_parts.append(f"*{fov['notes']}*")
                    desc = " ".join(desc_parts).replace("|", "\\|")
                    lines.append(f"| `{fname}` | `{ftype}` | {desc} |")
                lines.append("")
            else:
                lines.append("*No fields — this event carries no additional data.*\n")

    (out_dir / "gameevents.md").write_text("\n".join(lines), encoding="utf-8")


def generate_gameevents_json_schema(
    gameevents: list[dict[str, Any]],
    overlays: dict[str, dict],
    out_dir: Path,
) -> None:
    """Generate a JSON Schema file describing all game events.

    The schema follows the JSON Schema 2020-12 specification and uses
    ``$defs`` to define each event as a reusable sub-schema.
    """
    overlay = overlays.get("gameevents", {})
    overlay_events: dict = overlay.get("events", {}) or {}

    defs: dict[str, Any] = {}
    for ev in gameevents:
        ename = ev["name"]
        eov = overlay_events.get(ename, {}) if isinstance(overlay_events, dict) else {}

        # Build description from overlay or inline comment
        desc_parts: list[str] = []
        if eov and isinstance(eov, dict) and eov.get("description"):
            desc_parts.append(str(eov["description"]))
        elif ev["comment"]:
            desc_parts.append(ev["comment"])
        if ev["properties"]:
            props = ", ".join(f"{k}={v}" for k, v in ev["properties"].items())
            desc_parts.append(f"(properties: {props})")

        event_schema: dict[str, Any] = {
            "type": "object",
            "additionalProperties": False,
        }
        if desc_parts:
            event_schema["description"] = " ".join(desc_parts)

        # Add source metadata
        event_schema["x-source"] = ev["source"]

        properties: dict[str, Any] = {}
        required: list[str] = []
        overlay_flds: dict = (
            eov.get("fields", {}) or {}
            if eov and isinstance(eov, dict) else {}
        )
        for fld in ev["fields"]:
            fname = fld["name"]
            ftype = fld["type"]
            fov = overlay_flds.get(fname, {}) if isinstance(overlay_flds, dict) else {}

            type_info = _GAMEEVENTS_TYPE_MAP.get(ftype, {"type": "string"})
            fprop: dict[str, Any] = {"type": type_info["type"]}

            # Use the original game-event type as a format hint
            fprop["x-gameevents-type"] = ftype

            # Build field description
            fdesc_parts: list[str] = []
            if fov and isinstance(fov, dict) and fov.get("description"):
                fdesc_parts.append(str(fov["description"]))
            if fld["comment"]:
                fdesc_parts.append(fld["comment"])
            if fov and isinstance(fov, dict) and fov.get("notes"):
                fdesc_parts.append(fov["notes"])
            if fdesc_parts:
                fprop["description"] = " ".join(fdesc_parts)

            properties[fname] = fprop
            required.append(fname)

        if properties:
            event_schema["properties"] = properties
        if required:
            event_schema["required"] = required

        defs[ename] = event_schema

    schema: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://sid2934.github.io/CS2-OpenDevDocs/gameevents_schema.json",
        "title": "CS2 Game Events Schema",
        "description": (
            "JSON Schema describing all game events extracted from CS2's "
            ".gameevents resource files.  Each event is defined under $defs "
            "and can be referenced individually."
        ),
        "type": "object",
        "oneOf": [
            {"$ref": f"#/$defs/{name}"} for name in defs
        ],
        "$defs": defs,
    }

    (out_dir / "gameevents_schema.json").write_text(
        json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def generate_index_md(
    entities: dict[str, dict],
    protos: list[dict],
    convars: list[dict],
    commands: list[dict],
    out_dir: Path,
    gameevents: list[dict[str, Any]] | None = None,
) -> None:
    """Generate the Jekyll home page index.md."""
    by_module: dict[str, list] = defaultdict(list)
    for e in entities.values():
        by_module[e["module"]].append(e)

    total_entities = len(entities)
    total_proto_msgs = sum(len(p.get("messages", [])) for p in protos)

    lines: list[str] = []
    lines.append(_md_front_matter(layout="home", title="CS2 Developer Reference", nav_order="1", nav_exclude="true"))
    lines.append("# CS2 Developer Reference\n")
    lines.append(
        "Auto-generated documentation from the CS2 game tracking data. "
        "Includes entity schemas, network message definitions, game events, "
        "console variables, and commands.\n"
    )
    lines.append("## Statistics\n")
    lines.append("| Category | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| Schema Entities | {total_entities} |")
    lines.append(f"| Proto Files | {len(protos)} |")
    lines.append(f"| Proto Messages | {total_proto_msgs} |")
    if gameevents is not None:
        lines.append(f"| Game Events | {len(gameevents)} |")
    lines.append(f"| ConVars | {len(convars)} |")
    lines.append(f"| Commands | {len(commands)} |")
    lines.append("")
    lines.append("## Quick Links\n")
    lines.append("- [Schema Entities](schemas.md) – Classes, structs, and enums from CS2's schema dump")
    lines.append("- [Protobufs](protobufs.md) – Network message and game event definitions")
    if gameevents is not None:
        lines.append("- [Game Events](gameevents.md) – Game event definitions with field schemas ([JSON Schema](gameevents_schema.json))")
    lines.append("- [ConVars](convars.md) – Console variable reference with flags and defaults")
    lines.append("- [Commands](commands.md) – Console command reference")
    lines.append("- [Entity Hierarchy Diagram](diagrams/server_hierarchy.md) – UML inheritance diagram for server & client entities")
    lines.append("")
    lines.append("## Schema Modules\n")
    module_list = "  ".join(
        f"[{mod}](schemas/{mod}.md) ({len(ents)})"
        for mod, ents in sorted(by_module.items())
    )
    lines.append(module_list)
    lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_global_diagram_md(entities: dict[str, dict], out_dir: Path) -> None:
    """Generate diagrams/server_hierarchy.md – full server/client hierarchy."""
    lines_d: list[str] = []
    seen_edges: set[tuple[str, str]] = set()

    for e in entities.values():
        if e["module"] not in ("server", "client"):
            continue
        if not e.get("bases"):
            continue
        child = _mermaid_safe(e["name"])
        for base in e["bases"]:
            parent = _mermaid_safe(base)
            edge = (base, e["name"])
            if edge not in seen_edges:
                lines_d.append(f"    {parent} <|-- {child}")
                seen_edges.add(edge)

    if not lines_d:
        return

    lines_d = list(dict.fromkeys(lines_d))

    (out_dir / "diagrams").mkdir(exist_ok=True)
    md_lines: list[str] = []
    md_lines.append(_md_front_matter(
        layout="default",
        title="Entity Hierarchy",
        parent="Schemas",
        nav_exclude="true",
    ))
    md_lines.append("# Entity Hierarchy Diagram\n")
    md_lines.append(
        "Inheritance relationships between server and client entities "
        "(capped at 300 edges for readability).\n"
    )
    md_lines.append("```mermaid")
    md_lines.append("classDiagram")
    md_lines.extend(lines_d[:300])
    md_lines.append("```\n")

    (out_dir / "diagrams" / "server_hierarchy.md").write_text(
        "\n".join(md_lines), encoding="utf-8"
    )


def generate_jekyll_config(out_dir: Path) -> None:
    """Write docs/_config.yml for Jekyll / GitHub Pages with just-the-docs remote theme."""
    config = """\
title: CS2 Reference
description: Auto-generated CS2 game documentation – schema entities, protobufs, convars, and commands.
remote_theme: just-the-docs/just-the-docs

plugins:
  - jekyll-remote-theme

url: "https://sid2934.github.io"
baseurl: "/CS2-OpenDevDocs"

# Dark color scheme (follows the just-the-docs built-in dark theme)
color_scheme: dark

# Enable Mermaid diagrams via just-the-docs
mermaid:
  version: "10.9.0"

# Search – split on spaces, hyphens, underscores, and dots so that e.g.
# "roundtime" matches the convar "mp_roundtime".
search_enabled: true
search:
  heading_level: 2
  previews: 3
  preview_words_before: 5
  preview_words_after: 10
  tokenizer_separator: /[\\s\\-_\\.]+/

# Copy button on fenced code blocks
enable_copy_code_button: true

# Back-to-top link
back_to_top: true
back_to_top_text: "Back to top"

# Footer
footer_content: "Auto-generated from <a href='https://github.com/sid2934/CS2-OpenDevDocs'>CS2-OpenDevDocs</a>."

# Exclude generator scripts, overlays, and JSON artefacts from Jekyll processing
exclude:
  - generate_docs.py
  - generate_proto_md.py
  - overlays/
  - gameevents_schema.json
"""
    (out_dir / "_config.yml").write_text(config, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate CS2 Jekyll/Markdown documentation.")
    parser.add_argument("--repo-root", default=".", help="Path to the repository root")
    parser.add_argument(
        "--data-root",
        default=None,
        help=(
            "Path to the CS2-OpenDevDocs data tree (contains DumpSource2/ and "
            "Protobufs/).  Defaults to --repo-root.  Override when running from a "
            "standalone documentation repository that tracks game data in a "
            "submodule or sibling checkout."
        ),
    )
    parser.add_argument("--output", default="docs/output", help="Output directory for generated Markdown")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    data_root = Path(args.data_root).resolve() if args.data_root else repo_root
    out_dir = Path(args.output).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    overlays_dir = repo_root / "docs" / "overlays"

    print("Loading overlays…")
    if not HAS_YAML:
        print("  WARNING: PyYAML not found – overlay annotations will be skipped.")
        print("  Install with: pip install pyyaml")
    overlays = load_overlays(overlays_dir)
    print(f"  Loaded {len(overlays)} overlay file(s).")

    schemas_root = data_root / "DumpSource2" / "schemas"
    print("Parsing schema files…")
    entities = parse_all_schemas(schemas_root)
    print(f"  Parsed {len(entities)} entities across "
          f"{len({e['module'] for e in entities.values()})} modules.")

    protobufs_root = data_root / "Protobufs"
    print("Parsing proto files…")
    protos = []
    for proto_file in sorted(protobufs_root.glob("*.proto")):
        result = parse_proto_file(proto_file)
        if result:
            protos.append(result)
    print(f"  Parsed {len(protos)} proto files.")

    dump_dir = data_root / "DumpSource2"
    print("Parsing convars and commands…")
    convars = parse_convars(dump_dir / "convars.txt")
    commands = parse_commands(dump_dir / "commands.txt")
    print(f"  {len(convars)} convars, {len(commands)} commands.")

    print("Parsing game events…")
    gameevents = parse_all_gameevents(data_root)
    print(f"  Parsed {len(gameevents)} game events.")

    print("Generating Jekyll config…")
    generate_jekyll_config(out_dir)

    print("Generating Markdown UML diagram pages…")
    uml_md = generate_module_uml_md(entities, out_dir)
    generate_global_diagram_md(entities, out_dir)
    print(f"  Generated {len(uml_md)} module UML Markdown pages.")

    print("Generating Markdown schema pages (with embedded entity details)…")
    generate_schemas_index_md(entities, overlays, out_dir, diagram_modules=uml_md)
    print(f"  Generated {len({e['module'] for e in entities.values()})} module pages "
          f"covering {len(entities)} entities.")

    print("Generating Markdown protobuf pages…")
    generate_protobufs_md_page(protos, overlays, out_dir)

    print("Generating Markdown convar and command pages…")
    generate_convars_md_page(convars, out_dir)
    generate_commands_md_page(commands, out_dir)

    print("Generating game events documentation…")
    generate_gameevents_md_page(gameevents, overlays, out_dir)
    generate_gameevents_json_schema(gameevents, overlays, out_dir)

    print("Generating Markdown home page…")
    generate_index_md(entities, protos, convars, commands, out_dir, gameevents=gameevents)

    print(f"\nDone!  Documentation written to: {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
