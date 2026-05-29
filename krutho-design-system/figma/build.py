"""Compile Figma plugin payloads from foundation and surface specs.

The spec docs in foundation/ and surfaces/ are the source of truth. This
script parses the markdown tables and emits importable JSON for the Figma
plugin. Editing a spec doc and re-running this script propagates the change
to the Figma output without any duplication in code.

Foundation emits variable collections (primitives, semantic, spacing, grid,
typography). The website surface emits text styles and grid styles, one
set per breakpoint.

Usage:
  python build.py                     Build foundation + all surfaces
  python build.py foundation          Build foundation only
  python build.py surface website     Build the website surface only
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Paths and names
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

PRIMITIVES_COLLECTION = "Colour Primitives"
SEMANTIC_COLLECTION = "Colour Semantic"
SPACING_COLLECTION = "Spacing"
GRID_COLLECTION = "Grid"
TYPOGRAPHY_COLLECTION = "Typography"

WEBSITE_STYLE_PREFIX = "Website"

# Mid-dot used in token references: `ramp · stop`, `semantic · state`.
DOT = "·"

RAMP_HEADINGS = ("Neutral", "Accent", "Error", "Success", "Warning")
FEEDBACK_STATES = ("error", "warning", "success", "info")
LH_VARIANTS = ("tight", "default", "loose")


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def read_md(rel: str) -> str:
    return (ROOT / rel).read_text()


def find_section(md: str, heading: str, level: int | None = None) -> str:
    """Return the body of a section named `heading`.

    Body runs from after the heading to the next heading at the same or
    shallower level. If `level` is given, the heading must be at that level.
    """
    level_pat = f"{{{level}}}" if level else "{1,6}"
    pat = re.compile(rf"^(#{level_pat})\s+{re.escape(heading)}\s*$", re.MULTILINE)
    m = pat.search(md)
    if not m:
        raise KeyError(f"Section not found: {heading!r}")
    found = len(m.group(1))
    body_start = m.end()
    end_pat = re.compile(rf"^#{{1,{found}}}\s+", re.MULTILINE)
    em = end_pat.search(md, body_start)
    return md[body_start : em.start() if em else len(md)]


def parse_tables(section: str) -> list[list[dict[str, str]]]:
    """Return every markdown table in `section` as a list of row dicts."""
    tables: list[list[dict[str, str]]] = []
    current: list[str] = []
    for line in section.split("\n"):
        if line.lstrip().startswith("|"):
            current.append(line)
        else:
            if len(current) >= 2:
                tables.append(_rows(current))
            current = []
    if len(current) >= 2:
        tables.append(_rows(current))
    return tables


def first_table(section: str) -> list[dict[str, str]]:
    tables = parse_tables(section)
    if not tables:
        raise ValueError("No tables found in section")
    return tables[0]


def _rows(lines: list[str]) -> list[dict[str, str]]:
    header = _cells(lines[0])
    out: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = _cells(line)
        if len(cells) == len(header):
            out.append(dict(zip(header, cells)))
    return out


def _cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _int_px(s: str) -> int:
    m = re.search(r"(\d+)", s)
    if not m:
        raise ValueError(f"No integer in {s!r}")
    return int(m.group(1))


# ---------------------------------------------------------------------------
# Reference parsing
# ---------------------------------------------------------------------------

def parse_ref(value: str) -> dict:
    """Parse a single reference cell into a tagged dict."""
    s = value.strip()
    if s == "transparent":
        return {"kind": "transparent"}
    if s == "derived":
        return {"kind": "derived"}
    if s == "inherits":
        return {"kind": "inherits"}
    if s.startswith("#"):
        return {"kind": "hex", "hex": s}
    if DOT in s:
        parts = [p.strip() for p in s.split(DOT)]
        if len(parts) == 2:
            head, tail = parts
            if head == "semantic":
                return {"kind": "semantic", "state": tail}
            return {"kind": "primitive", "ramp": head, "stop": tail}
    raise ValueError(f"Unrecognised reference: {s!r}")


def parse_value_cell(cell: str) -> tuple[dict, dict]:
    """Parse a single cell that may contain `light / dark` or one value for both."""
    s = cell.strip()
    if "/" in s and DOT in s:
        parts = [p.strip() for p in s.split("/")]
        if len(parts) == 2:
            return parse_ref(parts[0]), parse_ref(parts[1])
    r = parse_ref(s)
    return r, r


# ---------------------------------------------------------------------------
# Colour parsing
# ---------------------------------------------------------------------------

def parse_ramps(md: str) -> dict[str, dict[str, str]]:
    """{ramp_name: {stop: hex}} for each primitive ramp."""
    section = find_section(md, "Primitive scales", level=2)
    out: dict[str, dict[str, str]] = {}
    for name in RAMP_HEADINGS:
        body = find_section(section, name, level=3)
        out[name.lower()] = {row["Stop"]: row["Hex"] for row in first_table(body)}
    return out


def parse_sources(md: str) -> dict[str, tuple[dict, dict]]:
    """{state: (light_ref, dark_ref)} for each semantic source token."""
    section = find_section(md, "Source tokens", level=3)
    out: dict[str, tuple[dict, dict]] = {}
    for row in first_table(section):
        m = re.match(r"--color-semantic-(\w+)", row["Token"])
        if m:
            out[m.group(1)] = (parse_ref(row["Light"]), parse_ref(row["Dark"]))
    return out


def parse_derived(md: str) -> dict[str, str]:
    """{state: derived_dark_hex} from the dark feedback surface derivation table."""
    section = find_section(md, "Dark feedback surface derivation", level=3)
    tables = parse_tables(section)
    if not tables:
        return {}
    out: dict[str, str] = {}
    for row in tables[0]:
        m = re.match(r"--color-feedback-(\w+)-surface\s+dark", row["Token"])
        if m:
            out[m.group(1)] = row["Derived dark value"].strip()
    return out


def parse_components(md: str) -> list[tuple[str, str, dict, dict]]:
    """[(category, name, light_ref, dark_ref), ...] in document order."""
    section = find_section(md, "Component tokens", level=2)
    out: list[tuple[str, str, dict, dict]] = []
    for tbl in parse_tables(section):
        if not tbl:
            continue
        cols = list(tbl[0].keys())
        for row in tbl:
            m = re.match(r"--color-([\w-]+?)-(.+)", row["Token"])
            if not m:
                continue
            category = m.group(1)
            name = m.group(2)
            if "Light" in cols and "Dark" in cols:
                light = parse_ref(row["Light"])
                dark = parse_ref(row["Dark"])
            elif "Value" in cols:
                light, dark = parse_value_cell(row["Value"])
            else:
                continue
            out.append((category, name, light, dark))
    return out


# ---------------------------------------------------------------------------
# Spacing, grid, typography parsing
# ---------------------------------------------------------------------------

def parse_spacing(md: str) -> list[int]:
    tbl = first_table(find_section(md, "Token set", level=2))
    return [_int_px(row["Value"]) for row in tbl]


def parse_grid(md: str) -> list[int]:
    tbl = first_table(find_section(md, "Admitted values", level=2))
    return [_int_px(row["Value"]) for row in tbl]


def parse_type_sizes(md: str) -> list[int]:
    tbl = first_table(find_section(md, "Type tokens", level=2))
    return [_int_px(row["Size"]) for row in tbl]


def parse_weights(md: str) -> dict[str, int]:
    """{weight_name: weight_value}."""
    tbl = first_table(find_section(md, "Weights", level=2))
    return {row["Weight"]: int(row["Value"]) for row in tbl}


def parse_typefaces(md: str) -> dict[str, str]:
    """{slot: family}. Slot resolves to the leading family in the foundation default stack."""
    tbl = first_table(find_section(md, "Typefaces", level=2))
    out: dict[str, str] = {}
    for row in tbl:
        slot = row["Style"].strip().lower()
        stack = row["Default"].strip().strip("`")
        out[slot] = stack.split(",")[0].strip()
    return out


def parse_lh_tokens(md: str) -> dict[int, dict[str, int]]:
    """{size: {variant: line_height}}. Values read directly from the doc table."""
    tbl = first_table(find_section(md, "Line height tokens", level=2))
    out: dict[int, dict[str, int]] = {}
    for row in tbl:
        size = int(row["Type token"].split("-")[1])
        # Header cells include the ratio in parentheses, e.g. "Tight (×1.2)".
        # Match by leading variant name (case-insensitive).
        variants: dict[str, int] = {}
        for header, value in row.items():
            for variant in LH_VARIANTS:
                if header.lower().startswith(variant):
                    variants[variant] = _int_px(value)
                    break
        out[size] = variants
    return out


# ---------------------------------------------------------------------------
# Website surface parsing
# ---------------------------------------------------------------------------

def parse_breakpoints(md: str) -> list[tuple[str, str]]:
    """[(bp_key, bp_label), ...]. Label includes the viewport range."""
    tbl = first_table(find_section(md, "Breakpoint system", level=2))
    out: list[tuple[str, str]] = []
    for row in tbl:
        key = row["Breakpoint"]
        rng = row["Viewport range"]
        if "above" in rng:
            n = re.search(r"(\d+)", rng).group(1)
            label_range = f"{n}+"
        else:
            m = re.match(r"(\d+)\s+to\s+(\d+)", rng)
            label_range = f"{m.group(1)}-{m.group(2)}" if m else rng
        out.append((key, f"{key} ({label_range})"))
    return out


def parse_grid_structure(md: str) -> dict[str, tuple[int, int, int]]:
    """{bp_key: (cols, margin, gutter)}."""
    tbl = first_table(find_section(md, "Grid structure", level=2))
    out: dict[str, tuple[int, int, int]] = {}
    for row in tbl:
        out[row["Breakpoint"]] = (int(row["Cols"]), int(row["Margin"]), int(row["Gutter"]))
    return out


def parse_roles(md: str) -> list[tuple[str, str, int]]:
    """[(role, style_slot, weight_value), ...] in document order."""
    tbl = first_table(find_section(md, "Type role set", level=2))
    out: list[tuple[str, str, int]] = []
    for row in tbl:
        wm = re.search(r"(\d+)", row["Weight"])
        if wm:
            out.append((row["Role"], row["Style"].strip().lower(), int(wm.group(1))))
    return out


def parse_role_sizes(md: str) -> dict[str, dict[str, int]]:
    """{role: {bp_key: size}}."""
    tbl = first_table(find_section(md, "Type role size assignment", level=2))
    out: dict[str, dict[str, int]] = {}
    for row in tbl:
        out[row["Role"]] = {k: int(v) for k, v in row.items() if k != "Role"}
    return out


def parse_lh_assignment(md: str) -> dict[str, str]:
    """{role: variant}."""
    tbl = first_table(find_section(md, "Line height assignment", level=2))
    return {row["Role"]: row["Variant"].lower() for row in tbl}


def parse_role_attribute(md: str, heading: str, column: str) -> dict[str, str]:
    """{role: value}. Used for case and tracking. Includes the 'All others' fallback.

    Returns {} when the surface omits the section, so callers fall back to
    their defaults (Original case, 0 tracking)."""
    try:
        section = find_section(md, heading, level=2)
    except KeyError:
        return {}
    return {row["Role"]: row[column] for row in first_table(section)}


# ---------------------------------------------------------------------------
# Resolver: refs to Figma variable values
# ---------------------------------------------------------------------------

def hex_to_rgba(h: str) -> dict[str, float]:
    h = h.lstrip("#")
    r = int(h[0:2], 16) / 255
    g = int(h[2:4], 16) / 255
    b = int(h[4:6], 16) / 255
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return {"r": round(r, 8), "g": round(g, 8), "b": round(b, 8), "a": round(a, 8)}


def make_resolver(derived: dict[str, str]):
    """Returns a function that resolves a ref dict to a Figma variable value."""
    def resolve(ref: dict, ctx_state: str | None = None, paired: dict | None = None) -> dict:
        kind = ref["kind"]
        if kind == "hex":
            return {"color": hex_to_rgba(ref["hex"])}
        if kind == "transparent":
            return {"color": {"r": 0.0, "g": 0.0, "b": 0.0, "a": 0.0}}
        if kind == "primitive":
            return {"alias": f"{PRIMITIVES_COLLECTION}.{ref['ramp']}/{ref['stop']}"}
        if kind == "semantic":
            return {"alias": f"{SEMANTIC_COLLECTION}.source/{ref['state']}"}
        if kind == "derived":
            if ctx_state is None or ctx_state not in derived:
                raise ValueError(f"Cannot resolve 'derived' without a known state (got {ctx_state!r})")
            return {"color": hex_to_rgba(derived[ctx_state])}
        if kind == "inherits":
            if paired is None:
                raise ValueError("Cannot resolve 'inherits' without a paired ref")
            return resolve(paired, ctx_state=ctx_state)
        raise ValueError(f"Unknown ref kind: {kind}")
    return resolve


def state_for(name: str) -> str | None:
    """Extract a semantic state name (error/warning/success/info) from a token name."""
    for state in FEEDBACK_STATES:
        if state in name:
            return state
    return None


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def build_foundation() -> dict:
    colour_md = read_md("foundation/colour.md")
    spacing_md = read_md("foundation/spacing.md")
    grid_md = read_md("foundation/grid.md")
    typo_md = read_md("foundation/typography.md")

    ramps = parse_ramps(colour_md)
    sources = parse_sources(colour_md)
    derived = parse_derived(colour_md)
    components = parse_components(colour_md)
    resolve = make_resolver(derived)

    collections: list[dict] = []

    # Primitives
    p_vars: list[dict] = []
    for ramp_name, stops in ramps.items():
        for stop, hex_val in stops.items():
            p_vars.append({
                "path": f"{ramp_name}/{stop}",
                "type": "COLOR",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"color": hex_to_rgba(hex_val)}},
            })
    collections.append({"name": PRIMITIVES_COLLECTION, "modes": ["Default"], "variables": p_vars})

    # Semantic collection: applied component tokens lead, in document order
    # (text, surface, border, icon, action). The source tokens are emitted
    # just before feedback, their only consumer, so feedback aliases resolve
    # without the sources sitting at the head of the collection.
    s_vars: list[dict] = []

    def emit_component(category, name, light, dark):
        ctx = state_for(name)
        s_vars.append({
            "path": f"{category}/{name}",
            "type": "COLOR",
            "scopes": ["ALL_SCOPES"],
            "values": {
                "Light": resolve(light, ctx_state=ctx, paired=dark),
                "Dark": resolve(dark, ctx_state=ctx, paired=light),
            },
        })

    for category, name, light, dark in components:
        if category != "feedback":
            emit_component(category, name, light, dark)

    for state, (light, dark) in sources.items():
        s_vars.append({
            "path": f"source/{state}",
            "type": "COLOR",
            "scopes": ["ALL_SCOPES"],
            "values": {"Light": resolve(light), "Dark": resolve(dark)},
        })

    for category, name, light, dark in components:
        if category == "feedback":
            emit_component(category, name, light, dark)

    collections.append({"name": SEMANTIC_COLLECTION, "modes": ["Light", "Dark"], "variables": s_vars})

    # Spacing
    sp_vars = [{
        "path": f"space-{px}",
        "type": "FLOAT",
        "scopes": ["ALL_SCOPES"],
        "values": {"Default": {"number": px}},
    } for px in parse_spacing(spacing_md)]
    collections.append({"name": SPACING_COLLECTION, "modes": ["Default"], "variables": sp_vars})

    # Grid
    g_vars = [{
        "path": f"grid-{px}",
        "type": "FLOAT",
        "scopes": ["ALL_SCOPES"],
        "values": {"Default": {"number": px}},
    } for px in parse_grid(grid_md)]
    collections.append({"name": GRID_COLLECTION, "modes": ["Default"], "variables": g_vars})

    # Typography
    type_sizes = parse_type_sizes(typo_md)
    lh_tokens = parse_lh_tokens(typo_md)
    t_vars: list[dict] = []
    for size in type_sizes:
        t_vars.append({
            "path": f"type-{size}/size",
            "type": "FLOAT",
            "scopes": ["ALL_SCOPES"],
            "values": {"Default": {"number": size}},
        })
        for variant in LH_VARIANTS:
            t_vars.append({
                "path": f"type-{size}/lh-{variant}",
                "type": "FLOAT",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"number": lh_tokens[size][variant]}},
            })
    collections.append({"name": TYPOGRAPHY_COLLECTION, "modes": ["Default"], "variables": t_vars})

    return {"version": 1, "collections": collections}


# Map a parsed weight name to the Figma fontStyle convention.
FIGMA_FONT_STYLE = {"Semibold": "SemiBold"}


def build_surface_website() -> dict:
    typo_md = read_md("foundation/typography.md")
    website_md = read_md("surfaces/website.md")

    weights = parse_weights(typo_md)
    weight_to_style = {v: FIGMA_FONT_STYLE.get(k, k) for k, v in weights.items()}
    lh_tokens = parse_lh_tokens(typo_md)
    typefaces = parse_typefaces(typo_md)

    breakpoints = parse_breakpoints(website_md)
    grid_struct = parse_grid_structure(website_md)
    roles = parse_roles(website_md)
    role_sizes = parse_role_sizes(website_md)
    lh_assign = parse_lh_assignment(website_md)
    case_assign = parse_role_attribute(website_md, "Case assignment", "Case")
    track_assign = parse_role_attribute(website_md, "Tracking assignment", "Tracking")

    def case_for(role: str) -> str:
        return case_assign.get(role, case_assign.get("All others", "Original"))

    def tracking_for(role: str) -> float:
        raw = track_assign.get(role, track_assign.get("All others", "0"))
        m = re.search(r"([+-]?\d+(?:\.\d+)?)", raw)
        return float(m.group(1)) if m else 0.0

    text_styles: list[dict] = []
    grid_styles: list[dict] = []
    # Emit breakpoints largest viewport first (Display-LG down to SM): styles
    # list large to small, matching a large-to-small design pass.
    for bp_key, bp_label in reversed(breakpoints):
        for role, slot, weight in roles:
            size = role_sizes[role][bp_key]
            variant = lh_assign[role]
            lh = lh_tokens[size][variant]
            style: dict = {
                "name": f"{WEBSITE_STYLE_PREFIX}/{bp_label}/{role}",
                "fontFamily": typefaces[slot],
                "fontStyle": weight_to_style[weight],
                "fontSize": size,
                "lineHeight": lh,
            }
            case = case_for(role).strip().upper()
            if case != "ORIGINAL":
                style["textCase"] = case
            tracking = tracking_for(role)
            if tracking != 0:
                style["letterSpacingPercent"] = tracking
            text_styles.append(style)

        cols, margin, gutter = grid_struct[bp_key]
        grid_styles.append({
            "name": f"{WEBSITE_STYLE_PREFIX}/{bp_label}",
            "layoutGrids": [{
                "pattern": "COLUMNS",
                "alignment": "STRETCH",
                "count": cols,
                "offset": margin,
                "gutterSize": gutter,
            }],
        })

    return {
        "version": 1,
        "collections": [],
        "textStyles": text_styles,
        "gridStyles": grid_styles,
    }


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_payload(filename: str, payload: dict) -> None:
    out_path = Path(__file__).parent / filename
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    collections = payload.get("collections", [])
    text_styles = payload.get("textStyles", [])
    grid_styles = payload.get("gridStyles", [])
    n_vars = sum(len(c["variables"]) for c in collections)
    parts: list[str] = []
    if n_vars:
        parts.append(f"{n_vars} variables across {len(collections)} collections")
    if text_styles:
        parts.append(f"{len(text_styles)} text styles")
    if grid_styles:
        parts.append(f"{len(grid_styles)} grid styles")
    print(f"  {filename}: {', '.join(parts) if parts else 'empty payload'}")


SURFACES = {
    "website": ("surface-website.json", build_surface_website),
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]

    if not args:
        write_payload("foundation.json", build_foundation())
        for filename, builder in SURFACES.values():
            write_payload(filename, builder())
        return

    target = args[0]
    if target == "foundation":
        write_payload("foundation.json", build_foundation())
    elif target == "surface":
        if len(args) < 2:
            print(f"Available surfaces: {', '.join(SURFACES)}")
            sys.exit(1)
        name = args[1]
        if name not in SURFACES:
            print(f"Unknown surface: {name}. Available: {', '.join(SURFACES)}")
            sys.exit(1)
        filename, builder = SURFACES[name]
        write_payload(filename, builder())
    else:
        print("Usage: python build.py [foundation | surface <name>]")
        sys.exit(1)


if __name__ == "__main__":
    main()
