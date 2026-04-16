"""Generate Figma variable JSON from Krutho foundation specs.

Emits in this directory:
  dtcg/<Collection>.<Mode>.tokens.json
                         DTCG with com.figma.* extensions, matches Figma's
                         built-in Variables import / export. One file per
                         (collection, mode). This is the recommended path.
  variables.rest.json    POST payload for Figma REST API /v1/files/:key/variables
                         (Enterprise plan only).
  variables.plugin.json  Generic plugin-import shape used by community plugins.

Re-run after changes to the foundation markdown specs.
"""

from __future__ import annotations

import json
from pathlib import Path


# Primitive colour ramps. Source: foundation/krutho-colour-system.md
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
# Each value is "ramp.stop" (alias to a primitive), a hex literal, or "transparent".
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


# Diagram colour tokens. Tuple = (light, dark).
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


SPACING: list[int] = [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128, 160, 192]
GRID: list[int] = [4, 8, 16, 32, 64]


# Type registers: each role = (size_px, line_height_px).
# Roles where surface declares lh (Expressive display/hero/statement) are omitted.
TYPE_REGISTERS: dict[str, list[tuple[str, int, int]]] = {
    "Compact": [
        ("caption", 12, 18),
        ("secondary", 14, 20),
        ("body", 16, 24),
        ("lead", 18, 26),
        ("heading-sm", 20, 28),
        ("heading-md", 24, 36),
        ("heading-lg", 32, 48),
        ("display", 40, 56),
    ],
    "Standard": [
        ("caption", 12, 18),
        ("secondary", 14, 20),
        ("body", 16, 24),
        ("lead", 20, 28),
        ("heading-sm", 24, 36),
        ("heading-md", 32, 48),
        ("heading-lg", 48, 64),
        ("display", 64, 80),
        ("hero", 80, 96),
    ],
    "Expressive": [
        ("caption", 14, 20),
        ("body", 16, 24),
        ("lead", 20, 28),
        ("heading-sm", 28, 40),
        ("heading-md", 40, 56),
        ("heading-lg", 48, 64),
        ("heading-xl", 64, 80),
    ],
}


def hex_to_rgba(h: str) -> dict:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return {"r": round(r / 255, 6), "g": round(g / 255, 6), "b": round(b / 255, 6), "a": round(a, 6)}


TRANSPARENT_RGBA = {"r": 0.0, "g": 0.0, "b": 0.0, "a": 0.0}

PRIMITIVES_COLLECTION = "Colour Primitives"
SEMANTIC_COLLECTION = "Colour Semantic"
DIAGRAM_COLLECTION = "Colour Diagram"
SPACING_COLLECTION = "Spacing"
GRID_COLLECTION = "Grid"


def primitive_path(ramp: str, stop) -> str:
    return f"{ramp}/{stop}"


def resolve_alias(ref: str) -> tuple[str, str] | None:
    """Return (collection, var_path) if ref is a primitive alias; else None."""
    if ref == "transparent":
        return None
    if ref.startswith("#"):
        return None
    ramp, stop = ref.split(".", 1)
    stop_key: object = stop if not stop.isdigit() else int(stop)
    if ramp not in PRIMITIVES or stop_key not in PRIMITIVES[ramp]:
        raise KeyError(f"Unknown primitive alias: {ref}")
    return (PRIMITIVES_COLLECTION, primitive_path(ramp, stop))


# REST API POST payload builder

def temp_coll_id(name: str) -> str:
    return f"tempColl:{name}"


def temp_mode_id(coll: str, mode: str) -> str:
    return f"tempMode:{coll}/{mode}"


def temp_var_id(coll: str, path: str) -> str:
    return f"tempVar:{coll}/{path}"


def build_rest_payload() -> dict:
    collections: list[dict] = []
    modes: list[dict] = []
    variables: list[dict] = []
    values: list[dict] = []

    def add_collection(name: str, mode_names: list[str]) -> None:
        initial_mode = mode_names[0]
        collections.append({
            "action": "CREATE",
            "id": temp_coll_id(name),
            "name": name,
            "initialModeId": temp_mode_id(name, initial_mode),
        })
        modes.append({
            "action": "UPDATE",
            "id": temp_mode_id(name, initial_mode),
            "variableCollectionId": temp_coll_id(name),
            "name": initial_mode,
        })
        for extra in mode_names[1:]:
            modes.append({
                "action": "CREATE",
                "id": temp_mode_id(name, extra),
                "variableCollectionId": temp_coll_id(name),
                "name": extra,
            })

    def add_variable(coll: str, path: str, resolved_type: str, scopes: list[str] | None = None) -> str:
        var_id = temp_var_id(coll, path)
        entry = {
            "action": "CREATE",
            "id": var_id,
            "name": path,
            "variableCollectionId": temp_coll_id(coll),
            "resolvedType": resolved_type,
        }
        if scopes is not None:
            entry["scopes"] = scopes
        variables.append(entry)
        return var_id

    def add_value(var_id: str, mode_id: str, value: object) -> None:
        values.append({
            "variableId": var_id,
            "modeId": mode_id,
            "value": value,
        })

    def colour_value(ref: str) -> object:
        if ref == "transparent":
            return TRANSPARENT_RGBA
        if ref.startswith("#"):
            return hex_to_rgba(ref)
        target = resolve_alias(ref)
        assert target is not None
        return {"type": "VARIABLE_ALIAS", "id": temp_var_id(target[0], target[1])}

    # Primitives (single mode "Default")
    add_collection(PRIMITIVES_COLLECTION, ["Default"])
    default_mode = temp_mode_id(PRIMITIVES_COLLECTION, "Default")
    for ramp, stops in PRIMITIVES.items():
        for stop, hex_val in stops.items():
            path = primitive_path(ramp, stop)
            vid = add_variable(PRIMITIVES_COLLECTION, path, "COLOR")
            add_value(vid, default_mode, hex_to_rgba(hex_val))

    # Semantic (Light + Dark)
    add_collection(SEMANTIC_COLLECTION, ["Light", "Dark"])
    light_mode = temp_mode_id(SEMANTIC_COLLECTION, "Light")
    dark_mode = temp_mode_id(SEMANTIC_COLLECTION, "Dark")
    for path, (light, dark) in SEMANTIC.items():
        vid = add_variable(SEMANTIC_COLLECTION, path, "COLOR")
        add_value(vid, light_mode, colour_value(light))
        add_value(vid, dark_mode, colour_value(dark))

    # Diagram (Light + Dark)
    add_collection(DIAGRAM_COLLECTION, ["Light", "Dark"])
    d_light = temp_mode_id(DIAGRAM_COLLECTION, "Light")
    d_dark = temp_mode_id(DIAGRAM_COLLECTION, "Dark")
    for path, (light, dark) in DIAGRAM.items():
        vid = add_variable(DIAGRAM_COLLECTION, path, "COLOR")
        add_value(vid, d_light, colour_value(light))
        add_value(vid, d_dark, colour_value(dark))

    # Spacing
    add_collection(SPACING_COLLECTION, ["Default"])
    s_mode = temp_mode_id(SPACING_COLLECTION, "Default")
    for px in SPACING:
        vid = add_variable(SPACING_COLLECTION, f"space-{px}", "FLOAT", scopes=["ALL_SCOPES"])
        add_value(vid, s_mode, float(px))

    # Grid
    add_collection(GRID_COLLECTION, ["Default"])
    g_mode = temp_mode_id(GRID_COLLECTION, "Default")
    for px in GRID:
        vid = add_variable(GRID_COLLECTION, f"grid-{px}", "FLOAT", scopes=["ALL_SCOPES"])
        add_value(vid, g_mode, float(px))

    # Typography (one collection per register; each role emits size + line-height)
    for register, roles in TYPE_REGISTERS.items():
        coll = f"Typography {register}"
        add_collection(coll, ["Default"])
        mode_id = temp_mode_id(coll, "Default")
        for role, size_px, lh_px in roles:
            sid = add_variable(coll, f"{role}/size", "FLOAT", scopes=["ALL_SCOPES"])
            lid = add_variable(coll, f"{role}/line-height", "FLOAT", scopes=["ALL_SCOPES"])
            add_value(sid, mode_id, float(size_px))
            add_value(lid, mode_id, float(lh_px))

    return {
        "variableCollections": collections,
        "variableModes": modes,
        "variables": variables,
        "variableModeValues": values,
    }


# Plugin-import payload builder
# Shape: { collection: { modes: [...], variables: { path: { type, valuesByMode } } } }
# Aliases use the string syntax "{Collection.path}".

def build_plugin_payload() -> dict:
    out: dict = {}

    def colour_value(ref: str) -> object:
        if ref == "transparent":
            return "transparent"
        if ref.startswith("#"):
            return ref
        target = resolve_alias(ref)
        assert target is not None
        return f"{{{target[0]}.{target[1]}}}"

    out[PRIMITIVES_COLLECTION] = {"modes": ["Default"], "variables": {}}
    for ramp, stops in PRIMITIVES.items():
        for stop, hex_val in stops.items():
            out[PRIMITIVES_COLLECTION]["variables"][primitive_path(ramp, stop)] = {
                "type": "color",
                "valuesByMode": {"Default": hex_val},
            }

    out[SEMANTIC_COLLECTION] = {"modes": ["Light", "Dark"], "variables": {}}
    for path, (light, dark) in SEMANTIC.items():
        out[SEMANTIC_COLLECTION]["variables"][path] = {
            "type": "color",
            "valuesByMode": {"Light": colour_value(light), "Dark": colour_value(dark)},
        }

    out[DIAGRAM_COLLECTION] = {"modes": ["Light", "Dark"], "variables": {}}
    for path, (light, dark) in DIAGRAM.items():
        out[DIAGRAM_COLLECTION]["variables"][path] = {
            "type": "color",
            "valuesByMode": {"Light": colour_value(light), "Dark": colour_value(dark)},
        }

    out[SPACING_COLLECTION] = {"modes": ["Default"], "variables": {}}
    for px in SPACING:
        out[SPACING_COLLECTION]["variables"][f"space-{px}"] = {
            "type": "number",
            "valuesByMode": {"Default": px},
            "scopes": ["ALL_SCOPES"],
        }

    out[GRID_COLLECTION] = {"modes": ["Default"], "variables": {}}
    for px in GRID:
        out[GRID_COLLECTION]["variables"][f"grid-{px}"] = {
            "type": "number",
            "valuesByMode": {"Default": px},
            "scopes": ["ALL_SCOPES"],
        }

    for register, roles in TYPE_REGISTERS.items():
        coll = f"Typography {register}"
        out[coll] = {"modes": ["Default"], "variables": {}}
        for role, size_px, lh_px in roles:
            out[coll]["variables"][f"{role}/size"] = {
                "type": "number",
                "valuesByMode": {"Default": size_px},
                "scopes": ["ALL_SCOPES"],
            }
            out[coll]["variables"][f"{role}/line-height"] = {
                "type": "number",
                "valuesByMode": {"Default": lh_px},
                "scopes": ["ALL_SCOPES"],
            }

    return {"collections": out}


# DTCG payload builder — one file per (collection, mode), matches Figma's
# native Variables export. Color $value uses {colorSpace, components, alpha,
# hex}; aliases use the DTCG curly-brace ref "{Collection.path.to.token}".

def hex_to_components(h: str) -> dict:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    norm = "#" + "".join(f"{int(round(c * 255)):02X}" for c in (r, g, b))
    return {
        "colorSpace": "srgb",
        "components": [round(r, 8), round(g, 8), round(b, 8)],
        "alpha": round(a, 8),
        "hex": norm,
    }


# Transparent in Figma's exported convention: white components, alpha 0.
TRANSPARENT_DTCG = {
    "colorSpace": "srgb",
    "components": [1.0, 1.0, 1.0],
    "alpha": 0,
    "hex": "#FFFFFF",
}


def insert_at_path(root: dict, path_segments: list[str], leaf: dict) -> None:
    cursor = root
    for seg in path_segments[:-1]:
        cursor = cursor.setdefault(seg, {})
        if "$type" in cursor:
            raise ValueError(f"Path collision at segment '{seg}'")
    cursor[path_segments[-1]] = leaf


def dtcg_alias(target_collection: str, target_path: str) -> str:
    dotted = target_path.replace("/", ".")
    return f"{{{target_collection}.{dotted}}}"


def colour_dtcg_value(ref: str) -> tuple[str, object]:
    """Return ('value' | 'alias', payload). Payload is the $value content."""
    if ref == "transparent":
        return ("value", TRANSPARENT_DTCG)
    if ref.startswith("#"):
        return ("value", hex_to_components(ref))
    target = resolve_alias(ref)
    assert target is not None
    return ("alias", dtcg_alias(target[0], target[1]))


def make_color_leaf(ref: str, scopes: list[str]) -> dict:
    kind, payload = colour_dtcg_value(ref)
    return {
        "$type": "color",
        "$value": payload,
        "$extensions": {"com.figma.scopes": scopes},
    }


def make_color_leaf_literal(hex_val: str, scopes: list[str]) -> dict:
    return {
        "$type": "color",
        "$value": hex_to_components(hex_val),
        "$extensions": {"com.figma.scopes": scopes},
    }


def make_number_leaf(value: float, scopes: list[str]) -> dict:
    numeric: int | float = int(value) if float(value).is_integer() else value
    return {
        "$type": "number",
        "$value": numeric,
        "$extensions": {"com.figma.scopes": scopes},
    }


def build_dtcg_files() -> dict[str, dict]:
    """Return mapping of filename → DTCG payload."""
    files: dict[str, dict] = {}

    def file_for(collection: str, mode: str) -> dict:
        key = f"{collection}.{mode}.tokens.json"
        if key not in files:
            files[key] = {"$extensions": {"com.figma.modeName": mode}}
        return files[key]

    all_scopes = ["ALL_SCOPES"]

    # Primitives — single mode "Default"
    payload = file_for(PRIMITIVES_COLLECTION, "Default")
    for ramp, stops in PRIMITIVES.items():
        for stop, hex_val in stops.items():
            insert_at_path(
                payload,
                [ramp, str(stop)],
                make_color_leaf_literal(hex_val, all_scopes),
            )

    # Semantic — Light + Dark
    for mode_name, idx in (("Light", 0), ("Dark", 1)):
        payload = file_for(SEMANTIC_COLLECTION, mode_name)
        for path, refs in SEMANTIC.items():
            insert_at_path(
                payload,
                path.split("/"),
                make_color_leaf(refs[idx], all_scopes),
            )

    # Diagram — Light + Dark, combined file plus per-subgroup files for
    # diagnostic import. Subgroup file mode name = "Light" / "Dark" so they
    # all merge into the same collection × mode in Figma.
    for mode_name, idx in (("Light", 0), ("Dark", 1)):
        payload = file_for(DIAGRAM_COLLECTION, mode_name)
        for path, refs in DIAGRAM.items():
            insert_at_path(
                payload,
                path.split("/"),
                make_color_leaf(refs[idx], all_scopes),
            )

    # Per-subgroup diagram files (signal / categorical / sequential / diverging / structural).
    subgroups: dict[str, list[tuple[str, tuple[str, str]]]] = {}
    for path, refs in DIAGRAM.items():
        head = path.split("/", 1)[0]
        subgroups.setdefault(head, []).append((path, refs))

    for sub, entries in subgroups.items():
        for mode_name, idx in (("Light", 0), ("Dark", 1)):
            key = f"Colour Diagram {sub}.{mode_name}.tokens.json"
            files[key] = {"$extensions": {"com.figma.modeName": mode_name}}
            for path, refs in entries:
                insert_at_path(
                    files[key],
                    path.split("/"),
                    make_color_leaf(refs[idx], all_scopes),
                )

    # Flat (no-alias) diagram files — all values resolved to literal hex.
    # Used to test whether the DTCG import error is alias-related.
    def resolve_to_hex(ref: str) -> str:
        if ref == "transparent":
            return "#00000000"
        if ref.startswith("#"):
            return ref
        ramp, stop = ref.split(".", 1)
        stop_key: object = stop if not stop.isdigit() else int(stop)
        return PRIMITIVES[ramp][stop_key]

    for mode_name, idx in (("Light", 0), ("Dark", 1)):
        key = f"Colour Diagram (flat).{mode_name}.tokens.json"
        files[key] = {"$extensions": {"com.figma.modeName": mode_name}}
        for path, refs in DIAGRAM.items():
            insert_at_path(
                files[key],
                path.split("/"),
                make_color_leaf_literal(resolve_to_hex(refs[idx]), all_scopes),
            )

    # Spacing
    payload = file_for(SPACING_COLLECTION, "Default")
    for px in SPACING:
        insert_at_path(
            payload,
            [f"space-{px}"],
            make_number_leaf(float(px), ["ALL_SCOPES"]),
        )

    # Grid
    payload = file_for(GRID_COLLECTION, "Default")
    for px in GRID:
        insert_at_path(
            payload,
            [f"grid-{px}"],
            make_number_leaf(float(px), ["ALL_SCOPES"]),
        )

    # Typography — one file per register
    for register, roles in TYPE_REGISTERS.items():
        coll = f"Typography {register}"
        payload = file_for(coll, "Default")
        for role, size_px, lh_px in roles:
            insert_at_path(payload, [role, "size"], make_number_leaf(float(size_px), ["ALL_SCOPES"]))
            insert_at_path(payload, [role, "line-height"], make_number_leaf(float(lh_px), ["ALL_SCOPES"]))

    return files


# Krutho plugin payload: single self-contained JSON the companion Figma
# plugin consumes at runtime. Collections are emitted in dependency order
# (Primitives before anything that aliases it).

def hex_to_rgba_floats(h: str) -> dict:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return {"r": round(r, 8), "g": round(g, 8), "b": round(b, 8), "a": round(a, 8)}


def build_krutho_plugin_payload() -> dict:
    def color_value(ref: str):
        if ref == "transparent":
            return {"color": {"r": 0.0, "g": 0.0, "b": 0.0, "a": 0.0}}
        if ref.startswith("#"):
            return {"color": hex_to_rgba_floats(ref)}
        target = resolve_alias(ref)
        assert target is not None
        return {"alias": f"{target[0]}.{target[1]}"}

    collections: list[dict] = []

    # Primitives
    pvars = []
    for ramp, stops in PRIMITIVES.items():
        for stop, hex_val in stops.items():
            pvars.append({
                "path": f"{ramp}/{stop}",
                "type": "COLOR",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"color": hex_to_rgba_floats(hex_val)}},
            })
    collections.append({
        "name": PRIMITIVES_COLLECTION,
        "modes": ["Default"],
        "variables": pvars,
    })

    # Semantic
    svars = []
    for path, (light, dark) in SEMANTIC.items():
        svars.append({
            "path": path,
            "type": "COLOR",
            "scopes": ["ALL_SCOPES"],
            "values": {"Light": color_value(light), "Dark": color_value(dark)},
        })
    collections.append({
        "name": SEMANTIC_COLLECTION,
        "modes": ["Light", "Dark"],
        "variables": svars,
    })

    # Diagram
    dvars = []
    for path, (light, dark) in DIAGRAM.items():
        dvars.append({
            "path": path,
            "type": "COLOR",
            "scopes": ["ALL_SCOPES"],
            "values": {"Light": color_value(light), "Dark": color_value(dark)},
        })
    collections.append({
        "name": DIAGRAM_COLLECTION,
        "modes": ["Light", "Dark"],
        "variables": dvars,
    })

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

    # Typography per register
    for register, roles in TYPE_REGISTERS.items():
        t_vars = []
        for role, size_px, lh_px in roles:
            t_vars.append({
                "path": f"{role}/size",
                "type": "FLOAT",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"number": size_px}},
            })
            t_vars.append({
                "path": f"{role}/line-height",
                "type": "FLOAT",
                "scopes": ["ALL_SCOPES"],
                "values": {"Default": {"number": lh_px}},
            })
        collections.append({
            "name": f"Typography {register}",
            "modes": ["Default"],
            "variables": t_vars,
        })

    return {"version": 1, "collections": collections}


def main() -> None:
    out_dir = Path(__file__).parent
    rest = build_rest_payload()
    plugin = build_plugin_payload()
    dtcg = build_dtcg_files()
    krutho = build_krutho_plugin_payload()

    (out_dir / "variables.rest.json").write_text(json.dumps(rest, indent=2) + "\n")
    (out_dir / "variables.plugin.json").write_text(json.dumps(plugin, indent=2) + "\n")
    (out_dir / "figma-plugin.json").write_text(json.dumps(krutho, indent=2) + "\n")

    dtcg_dir = out_dir / "dtcg"
    dtcg_dir.mkdir(exist_ok=True)
    for name, payload in dtcg.items():
        (dtcg_dir / name).write_text(json.dumps(payload, indent=2) + "\n")

    n_vars = len(rest["variables"])
    n_colls = len(rest["variableCollections"])
    print(f"Wrote {n_vars} variables across {n_colls} collections.")
    print(f"DTCG files: {len(dtcg)}")
    print(f"Plugin payload: figma-plugin.json ({n_vars} variables)")


if __name__ == "__main__":
    main()
