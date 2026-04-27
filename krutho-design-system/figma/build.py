"""Generate Krutho Figma plugin payloads from foundation and surface specs.

Emits separate files so foundation can be imported into all Figma files
and surfaces added individually where needed.

Foundation emits variable collections only. Surfaces emit variable
collections and/or text styles. Text styles are a surface-layer concept:
they bundle typography variables into role-specific applicable styles
(h1, body, button, etc.) and inherit the typographic rules declared by
the surface specification.

Usage:
  python build.py                          Build foundation + all surfaces
  python build.py foundation               Build foundation only
  python build.py surface diagrams         Build diagrams surface only
  python build.py surface website          Build website surface only

Output files:
  foundation.json                Colour primitives, colour semantic, spacing,
                                 grid, and typography collections.
  surface-diagrams.json          Diagram colour collection.
  surface-website.json           Website text styles and grid styles, one set
                                 per breakpoint.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Data: Foundation
# ---------------------------------------------------------------------------

# Primitive colour ramps. Source: foundation/colour.md
PRIMITIVES: dict[str, dict] = {
    "neutral": {
        0: "#FFFFFF", 50: "#FAFAFA", 100: "#F2F2F2", 200: "#E6E6E6",
        300: "#D6D6D6", 400: "#C4C4C4", 450: "#AFAFAF", 500: "#9A9A9A",
        600: "#707070", 700: "#505050", 800: "#343434", 825: "#2A2A2A",
        850: "#202020", 900: "#181818", 950: "#0A0A0A",
    },
    "signal-blue": {
        50: "#EBF3FF", 100: "#C5DBFF", 200: "#94BBFF", 300: "#5C9AFF",
        400: "#3D85FF", 500: "#1A6FFF", 600: "#0055DD", 700: "#0044BB",
        800: "#003399", 900: "#001F6B", 950: "#000E40",
    },
    "secondary-signal": {
        50: "#EEEEFF", 100: "#D0D2F8", 200: "#B0B3F0", 300: "#9092E8",
        400: "#7476DC", 500: "#5C60D6", 600: "#4448BF", 700: "#3234A8",
        800: "#20228A", 900: "#10126A", 950: "#06084A",
    },
    "teal": {
        50: "#E0F4FA", 100: "#B0E0EF", 200: "#7DCAE3", 300: "#40B0D4",
        400: "#1A96BE", 500: "#0A7CA4", 600: "#086688", 700: "#004964",
        800: "#003550", 900: "#00203A", 950: "#000E22",
    },
    "amber": {
        50: "#FFF5E6", 100: "#FFDFB0", 200: "#F5C478", 300: "#E8A840",
        400: "#D68E22", 500: "#C47B1A", 600: "#A86210", 700: "#8A4C08",
        800: "#6C3804", 900: "#4E2602", 950: "#301600",
    },
    "error": {
        50: "#FEF2F2", 100: "#FFCFCF", 200: "#FFAAAA", 300: "#FF7A7A",
        400: "#F04848", 500: "#E02828", 600: "#C0251D", 700: "#9B1C1C",
        800: "#7B1414", 900: "#5A0C0C", 950: "#380606",
    },
    "success": {
        50: "#F0FDF4", 100: "#CBFADE", 200: "#9AEEC0", 300: "#5EDE9A",
        400: "#30C478", 500: "#18A85A", 600: "#128C46", 700: "#166534",
        800: "#0F4826", 900: "#083018", 950: "#03160C",
    },
    "warning": {
        50: "#FFFBEB", 100: "#FDEFC8", 200: "#FAD88E", 300: "#F5BC50",
        400: "#E89A20", 500: "#CC7A0A", 600: "#AA5E08", 700: "#92400E",
        800: "#7A2E08", 900: "#5A1E04", 950: "#3A1002",
    },
    "deep-base": {
        "a": "#000035",
        "b": "#010364",
    },
}

# Semantic colour tokens. Tuple = (light, dark).
SEMANTIC: dict[str, tuple[str, str]] = {
    "source/error": ("error.600", "error.200"),
    "source/success": ("success.700", "success.200"),
    "source/warning": ("warning.700", "warning.300"),
    "source/info": ("signal-blue.500", "signal-blue.300"),

    "surface/overlay": ("neutral.0", "neutral.800"),
    "surface/raised": ("neutral.50", "neutral.850"),
    "surface/base": ("neutral.100", "neutral.900"),
    "surface/sunken": ("neutral.200", "neutral.950"),
    "surface/inverse": ("neutral.900", "neutral.200"),
    "surface/error": ("error.50", "#2C1A19"),
    "surface/warning": ("warning.50", "#271D17"),
    "surface/success": ("success.50", "#18211B"),
    "surface/info": ("signal-blue.50", "#182234"),

    "text/strong": ("neutral.900", "neutral.50"),
    "text/default": ("neutral.800", "neutral.200"),
    "text/subtle": ("neutral.600", "neutral.500"),
    "text/faint": ("neutral.500", "neutral.600"),
    "text/disabled": ("neutral.400", "neutral.700"),
    "text/placeholder": ("neutral.450", "neutral.700"),
    "text/inverse": ("neutral.100", "neutral.900"),
    "text/on-accent": ("neutral.0", "neutral.0"),
    "text/link": ("signal-blue.500", "signal-blue.300"),
    "text/error": ("error.600", "error.200"),
    "text/success": ("success.700", "success.200"),
    "text/warning": ("warning.700", "warning.300"),
    "text/info": ("signal-blue.500", "signal-blue.300"),

    "border/strong": ("neutral.600", "neutral.500"),
    "border/default": ("neutral.300", "neutral.800"),
    "border/subtle": ("neutral.200", "neutral.825"),
    "border/focus": ("signal-blue.500", "signal-blue.500"),
    "border/inverse": ("neutral.800", "neutral.300"),
    "border/error": ("error.600", "error.200"),
    "border/success": ("success.700", "success.200"),
    "border/warning": ("warning.700", "warning.300"),
    "border/info": ("signal-blue.500", "signal-blue.300"),

    "icon/strong": ("neutral.900", "neutral.50"),
    "icon/default": ("neutral.800", "neutral.200"),
    "icon/subtle": ("neutral.600", "neutral.500"),
    "icon/faint": ("neutral.500", "neutral.600"),
    "icon/disabled": ("neutral.400", "neutral.700"),
    "icon/inverse": ("neutral.100", "neutral.900"),
    "icon/on-accent": ("neutral.0", "neutral.0"),
    "icon/link": ("signal-blue.500", "signal-blue.300"),
    "icon/error": ("error.600", "error.200"),
    "icon/success": ("success.700", "success.200"),
    "icon/warning": ("warning.700", "warning.300"),
    "icon/info": ("signal-blue.500", "signal-blue.300"),

    "action/primary": ("signal-blue.500", "signal-blue.500"),
    "action/primary-hover": ("signal-blue.600", "signal-blue.400"),
    "action/primary-active": ("signal-blue.700", "signal-blue.300"),
    "action/primary-text": ("neutral.0", "neutral.0"),
    "action/secondary": ("transparent", "transparent"),
    "action/secondary-hover": ("neutral.100", "neutral.850"),
    "action/secondary-active": ("neutral.200", "neutral.825"),
    "action/secondary-border": ("neutral.300", "neutral.800"),
    "action/secondary-border-hover": ("neutral.500", "neutral.500"),
    "action/secondary-border-active": ("neutral.800", "neutral.200"),
    "action/secondary-text": ("neutral.900", "neutral.200"),
    "action/ghost": ("transparent", "transparent"),
    "action/ghost-hover": ("neutral.100", "neutral.850"),
    "action/ghost-active": ("neutral.200", "neutral.825"),
    "action/ghost-text": ("neutral.900", "neutral.200"),
    "action/destructive": ("error.600", "error.600"),
    "action/destructive-hover": ("error.700", "error.400"),
    "action/destructive-active": ("error.800", "error.200"),
    "action/destructive-text": ("neutral.0", "neutral.0"),
    "action/disabled": ("neutral.200", "neutral.825"),
    "action/disabled-text": ("neutral.500", "neutral.700"),

    "feedback/error-surface": ("error.50", "#2C1A19"),
    "feedback/error-text": ("error.600", "error.200"),
    "feedback/error-border": ("error.600", "error.200"),
    "feedback/error-icon": ("error.600", "error.200"),
    "feedback/warning-surface": ("warning.50", "#271D17"),
    "feedback/warning-text": ("warning.700", "warning.300"),
    "feedback/warning-border": ("warning.700", "warning.300"),
    "feedback/warning-icon": ("warning.700", "warning.300"),
    "feedback/success-surface": ("success.50", "#18211B"),
    "feedback/success-text": ("success.700", "success.200"),
    "feedback/success-border": ("success.700", "success.200"),
    "feedback/success-icon": ("success.700", "success.200"),
    "feedback/info-surface": ("signal-blue.50", "#182234"),
    "feedback/info-text": ("signal-blue.500", "signal-blue.300"),
    "feedback/info-border": ("signal-blue.500", "signal-blue.300"),
    "feedback/info-icon": ("signal-blue.500", "signal-blue.300"),
}

SPACING: list[int] = [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128, 160, 192]
GRID: list[int] = [4, 8, 16, 32, 64]

# Type token set. Source: foundation/typography.md
TYPE_SIZES: list[int] = [10, 12, 14, 16, 18, 20, 24, 28, 32, 40, 48, 64, 80, 96, 128, 192]

# Line height variants. Ratio and rounding: lh = ceil(size * ratio / 2) * 2
LH_RATIOS: dict[str, float] = {"tight": 1.2, "default": 1.4, "loose": 1.6}

# Typeface tier to family. Source: foundation/typography.md.
TIER_TYPEFACE: dict[int, str] = {
    1: "Spline Sans",
    2: "Spline Sans Mono",
    3: "Enra",
}

# Weight to Figma font-style name.
WEIGHT_STYLE: dict[int, str] = {
    400: "Regular",
    500: "Medium",
    600: "SemiBold",
}


# ---------------------------------------------------------------------------
# Data: Surfaces
# ---------------------------------------------------------------------------

# Website text roles. Source: surfaces/website.md.
# Each entry: (role-name, tier, weight, {breakpoint-key: size}, lh-variant,
# text-case, tracking-percent).
# Breakpoint keys match WEBSITE_BREAKPOINTS. The lh-variant is a key into
# LH_RATIOS: "tight" for Display and Structural categories, "default" for
# Continuous reading and Tier 2. The text-case value matches the Figma
# TextStyle.textCase enum: "ORIGINAL" (default), "UPPER", "LOWER", "TITLE".
# The tracking-percent value is applied as Figma letterSpacing with unit
# PERCENT; 0 is Normal (no emitted field).
WEBSITE_BREAKPOINTS: tuple[tuple[str, str], ...] = (
    ("SM",         "SM (320-575)"),
    ("MD",         "MD (576-1087)"),
    ("LG",         "LG (1088-1343)"),
    ("Display-SM", "Display-SM (1344-1599)"),
    ("Display-MD", "Display-MD (1600-1855)"),
    ("Display-LG", "Display-LG (1856+)"),
)

WEBSITE_ROLES: list[tuple] = [
    ("Display 1", 1, 500, {"SM": 48, "MD": 48, "LG": 48, "Display-SM": 64, "Display-MD": 80, "Display-LG": 96}, "tight",   "ORIGINAL", 0),
    ("Display 2", 1, 500, {"SM": 40, "MD": 40, "LG": 40, "Display-SM": 48, "Display-MD": 64, "Display-LG": 80}, "tight",   "ORIGINAL", 0),
    ("Heading 1", 1, 600, {"SM": 32, "MD": 32, "LG": 32, "Display-SM": 40, "Display-MD": 48, "Display-LG": 64}, "tight",   "ORIGINAL", 0),
    ("Heading 2", 1, 600, {"SM": 24, "MD": 24, "LG": 24, "Display-SM": 32, "Display-MD": 40, "Display-LG": 48}, "tight",   "ORIGINAL", 0),
    ("Heading 3", 1, 600, {"SM": 20, "MD": 20, "LG": 20, "Display-SM": 24, "Display-MD": 32, "Display-LG": 40}, "tight",   "ORIGINAL", 0),
    ("Heading 4", 1, 600, {"SM": 18, "MD": 18, "LG": 18, "Display-SM": 20, "Display-MD": 24, "Display-LG": 32}, "tight",   "ORIGINAL", 0),
    ("Lead",      1, 400, {"SM": 18, "MD": 18, "LG": 18, "Display-SM": 18, "Display-MD": 18, "Display-LG": 24}, "default", "ORIGINAL", 0),
    ("Body",      1, 400, {"SM": 16, "MD": 16, "LG": 16, "Display-SM": 16, "Display-MD": 16, "Display-LG": 20}, "default", "ORIGINAL", 0),
    ("Caption",   1, 400, {"SM": 12, "MD": 12, "LG": 12, "Display-SM": 12, "Display-MD": 12, "Display-LG": 14}, "default", "ORIGINAL", 0),
    ("Code",      2, 400, {"SM": 14, "MD": 14, "LG": 14, "Display-SM": 14, "Display-MD": 14, "Display-LG": 16}, "default", "ORIGINAL", 0),
    ("Eyebrow",   2, 400, {"SM": 12, "MD": 12, "LG": 12, "Display-SM": 12, "Display-MD": 12, "Display-LG": 14}, "default", "UPPER",    5),
]

WEBSITE_STYLE_PREFIX = "Website"

# Website grid structure per breakpoint. Source: surfaces/website.md.
# (columns, margin, gutter). Applied to frames via Figma grid styles with
# STRETCH alignment, so columns fluidly fill within a breakpoint range.
# The Display-LG content lock at 1760 is a frame-level convention: apply
# the Display-LG grid to a 1760-wide content frame centred in a >=1856
# outer frame. It is not expressed as a separate grid style.
WEBSITE_GRIDS: dict[str, tuple[int, int, int]] = {
    "SM":         (2,  16, 32),
    "MD":         (8,  48, 32),
    "LG":         (16, 48, 32),
    "Display-SM": (16, 48, 32),
    "Display-MD": (16, 48, 32),
    "Display-LG": (16, 48, 32),
}


# Diagram colour tokens. Source: surfaces/diagrams.md. Tuple = (light, dark).
DIAGRAM: dict[str, tuple[str, str]] = {
    "signal/trust-fill": ("signal-blue.50", "signal-blue.900"),
    "signal/trust-border": ("signal-blue.500", "signal-blue.500"),
    "signal/trust-text": ("signal-blue.800", "signal-blue.200"),
    "signal/human-border": ("neutral.900", "neutral.50"),

    "categorical/trust-fill": ("signal-blue.50", "signal-blue.900"),
    "categorical/trust-border": ("signal-blue.500", "signal-blue.500"),
    "categorical/trust-text": ("signal-blue.800", "signal-blue.200"),
    "categorical/integration-fill": ("secondary-signal.50", "secondary-signal.900"),
    "categorical/integration-border": ("secondary-signal.500", "secondary-signal.500"),
    "categorical/integration-text": ("secondary-signal.800", "secondary-signal.200"),
    "categorical/transport-fill": ("teal.50", "teal.900"),
    "categorical/transport-border": ("teal.500", "teal.500"),
    "categorical/transport-text": ("teal.800", "teal.200"),
    "categorical/state-fill": ("amber.50", "amber.900"),
    "categorical/state-border": ("amber.500", "amber.500"),
    "categorical/state-text": ("amber.800", "amber.200"),

    "sequential/1": ("signal-blue.50", "signal-blue.50"),
    "sequential/2": ("signal-blue.200", "signal-blue.200"),
    "sequential/3": ("signal-blue.400", "signal-blue.400"),
    "sequential/4": ("signal-blue.500", "signal-blue.500"),
    "sequential/5": ("signal-blue.700", "signal-blue.700"),
    "sequential/alt-1": ("teal.50", "teal.50"),
    "sequential/alt-2": ("teal.200", "teal.200"),
    "sequential/alt-3": ("teal.400", "teal.400"),
    "sequential/alt-4": ("teal.500", "teal.500"),
    "sequential/alt-5": ("teal.700", "teal.700"),

    "diverging/negative-strong": ("amber.600", "amber.600"),
    "diverging/negative-subtle": ("amber.200", "amber.200"),
    "diverging/midpoint": ("neutral.300", "neutral.300"),
    "diverging/positive-subtle": ("signal-blue.200", "signal-blue.200"),
    "diverging/positive-strong": ("signal-blue.600", "signal-blue.600"),

    "structural/header-bg": ("deep-base.b", "deep-base.b"),
    "structural/header-text": ("neutral.0", "neutral.0"),
    "structural/node-fill": ("neutral.0", "neutral.850"),
    "structural/node-border": ("neutral.500", "neutral.600"),
    "structural/node-text": ("neutral.900", "neutral.200"),
    "structural/node-decision-border": ("neutral.500", "neutral.600"),
    "structural/annotation-fill": ("neutral.200", "neutral.825"),
    "structural/annotation-text": ("neutral.700", "neutral.400"),
    "structural/connector": ("neutral.500", "neutral.600"),
    "structural/connector-trust": ("signal-blue.500", "signal-blue.500"),
    "structural/connector-optional": ("neutral.400", "neutral.600"),
    "structural/boundary-physical": ("neutral.600", "neutral.500"),
    "structural/boundary-logical": ("neutral.400", "neutral.600"),
    "structural/lane-divider": ("neutral.200", "neutral.825"),
}


# ---------------------------------------------------------------------------
# Collection names
# ---------------------------------------------------------------------------

PRIMITIVES_COLLECTION = "Colour Primitives"
SEMANTIC_COLLECTION = "Colour Semantic"
DIAGRAM_COLLECTION = "Colour Diagram"
SPACING_COLLECTION = "Spacing"
GRID_COLLECTION = "Grid"
TYPOGRAPHY_COLLECTION = "Typography"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def derive_lh(size: int, ratio: float) -> int:
    return math.ceil(size * ratio / 2) * 2


def hex_to_rgba_floats(h: str) -> dict:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return {"r": round(r, 8), "g": round(g, 8), "b": round(b, 8), "a": round(a, 8)}


def resolve_alias(ref: str) -> tuple[str, str] | None:
    """Return (collection, var_path) if ref is a primitive alias; else None."""
    if ref == "transparent" or ref.startswith("#"):
        return None
    ramp, stop = ref.split(".", 1)
    stop_key: object = stop if not stop.isdigit() else int(stop)
    if ramp not in PRIMITIVES or stop_key not in PRIMITIVES[ramp]:
        raise KeyError(f"Unknown primitive alias: {ref}")
    return (PRIMITIVES_COLLECTION, f"{ramp}/{stop}")


def color_value(ref: str):
    if ref == "transparent":
        return {"color": {"r": 0.0, "g": 0.0, "b": 0.0, "a": 0.0}}
    if ref.startswith("#"):
        return {"color": hex_to_rgba_floats(ref)}
    target = resolve_alias(ref)
    assert target is not None
    return {"alias": f"{target[0]}.{target[1]}"}


def write_payload(filename: str, payload: dict) -> int:
    out_path = Path(__file__).parent / filename
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    collections = payload.get("collections", [])
    text_styles = payload.get("textStyles", [])
    grid_styles = payload.get("gridStyles", [])
    n_vars = sum(len(c["variables"]) for c in collections)
    n_colls = len(collections)
    n_styles = len(text_styles)
    n_grids = len(grid_styles)
    parts: list[str] = []
    if n_vars:
        parts.append(f"{n_vars} variables across {n_colls} collections")
    if n_styles:
        parts.append(f"{n_styles} text styles")
    if n_grids:
        parts.append(f"{n_grids} grid styles")
    print(f"  {filename}: {', '.join(parts) if parts else 'empty payload'}")
    return n_vars + n_styles + n_grids


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def build_foundation() -> dict:
    collections: list[dict] = []

    # Primitives
    p_vars = []
    for ramp, stops in PRIMITIVES.items():
        for stop, hex_val in stops.items():
            p_vars.append({
                "path": f"{ramp}/{stop}",
                "type": "COLOR",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"color": hex_to_rgba_floats(hex_val)}},
            })
    collections.append({"name": PRIMITIVES_COLLECTION, "modes": ["Default"], "variables": p_vars})

    # Semantic
    s_vars = [{
        "path": path,
        "type": "COLOR",
        "scopes": ["ALL_SCOPES"],
        "values": {"Light": color_value(light), "Dark": color_value(dark)},
    } for path, (light, dark) in SEMANTIC.items()]
    collections.append({"name": SEMANTIC_COLLECTION, "modes": ["Light", "Dark"], "variables": s_vars})

    # Spacing
    sp_vars = [{
        "path": f"space-{px}",
        "type": "FLOAT",
        "scopes": ["ALL_SCOPES"],
        "values": {"Default": {"number": px}},
    } for px in SPACING]
    collections.append({"name": SPACING_COLLECTION, "modes": ["Default"], "variables": sp_vars})

    # Grid
    g_vars = [{
        "path": f"grid-{px}",
        "type": "FLOAT",
        "scopes": ["ALL_SCOPES"],
        "values": {"Default": {"number": px}},
    } for px in GRID]
    collections.append({"name": GRID_COLLECTION, "modes": ["Default"], "variables": g_vars})

    # Typography
    t_vars = []
    for size in TYPE_SIZES:
        t_vars.append({
            "path": f"type-{size}/size",
            "type": "FLOAT",
            "scopes": ["ALL_SCOPES"],
            "values": {"Default": {"number": size}},
        })
        for variant, ratio in LH_RATIOS.items():
            t_vars.append({
                "path": f"type-{size}/lh-{variant}",
                "type": "FLOAT",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"number": derive_lh(size, ratio)}},
            })
    collections.append({"name": TYPOGRAPHY_COLLECTION, "modes": ["Default"], "variables": t_vars})

    return {"version": 1, "collections": collections}


def build_surface_diagrams() -> dict:
    d_vars = [{
        "path": path,
        "type": "COLOR",
        "scopes": ["ALL_SCOPES"],
        "values": {"Light": color_value(light), "Dark": color_value(dark)},
    } for path, (light, dark) in DIAGRAM.items()]

    return {"version": 1, "collections": [
        {"name": DIAGRAM_COLLECTION, "modes": ["Light", "Dark"], "variables": d_vars},
    ]}


def build_surface_website() -> dict:
    styles: list[dict] = []
    grid_styles: list[dict] = []
    for bp_key, bp_label in WEBSITE_BREAKPOINTS:
        for role_name, tier, weight, sizes, lh_variant, text_case, tracking in WEBSITE_ROLES:
            size = sizes[bp_key]
            style: dict = {
                "name": f"{WEBSITE_STYLE_PREFIX}/{bp_label}/{role_name}",
                "fontFamily": TIER_TYPEFACE[tier],
                "fontStyle": WEIGHT_STYLE[weight],
                "fontSize": size,
                "lineHeight": derive_lh(size, LH_RATIOS[lh_variant]),
            }
            if text_case != "ORIGINAL":
                style["textCase"] = text_case
            if tracking != 0:
                style["letterSpacingPercent"] = tracking
            styles.append(style)
        cols, margin, gutter = WEBSITE_GRIDS[bp_key]
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
        "textStyles": styles,
        "gridStyles": grid_styles,
    }


SURFACES = {
    "diagrams": ("surface-diagrams.json", build_surface_diagrams),
    "website": ("surface-website.json", build_surface_website),
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]

    if not args:
        # Build everything
        write_payload("foundation.json", build_foundation())
        for name, (filename, builder) in SURFACES.items():
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
        print(f"Usage: python build.py [foundation | surface <name>]")
        sys.exit(1)


if __name__ == "__main__":
    main()
