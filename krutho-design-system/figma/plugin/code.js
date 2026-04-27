// Krutho Tokens Import
// Reads a payload JSON at runtime and materialises variable collections,
// modes, variables, aliases, and text styles into the current file.

figma.showUI(__html__, { width: 460, height: 360 });

figma.ui.onmessage = async (msg) => {
  try {
    if (msg.type === "analyse") {
      const data = parsePayload(msg.payload);
      const conflicts = await findConflicts(data);
      figma.ui.postMessage({
        type: "analysis",
        conflicts,
        collectionCount: data.collections.length,
        textStyleCount: data.textStyles.length,
        gridStyleCount: data.gridStyles.length,
      });
    } else if (msg.type === "import") {
      const data = parsePayload(msg.payload);
      await runImport(data);
    } else if (msg.type === "close") {
      figma.closePlugin();
    }
  } catch (err) {
    figma.ui.postMessage({ type: "error", error: err && err.message ? err.message : String(err) });
  }
};

function parsePayload(text) {
  let data;
  try {
    data = JSON.parse(text);
  } catch (e) {
    throw new Error("File is not valid JSON.");
  }
  const hasCollections = data && Array.isArray(data.collections);
  const hasTextStyles = data && Array.isArray(data.textStyles);
  const hasGridStyles = data && Array.isArray(data.gridStyles);
  if (!hasCollections && !hasTextStyles && !hasGridStyles) {
    throw new Error("JSON missing 'collections', 'textStyles', or 'gridStyles' array.");
  }
  if (!hasCollections) data.collections = [];
  if (!hasTextStyles) data.textStyles = [];
  if (!hasGridStyles) data.gridStyles = [];
  return data;
}

async function findConflicts(data) {
  const conflicts = { collections: [], textStyles: [], gridStyles: [] };
  if (data.collections.length > 0) {
    const existing = await figma.variables.getLocalVariableCollectionsAsync();
    const set = new Set(existing.map((c) => c.name));
    conflicts.collections = data.collections.map((c) => c.name).filter((n) => set.has(n));
  }
  if (data.textStyles.length > 0) {
    const existing = await figma.getLocalTextStylesAsync();
    const set = new Set(existing.map((s) => s.name));
    conflicts.textStyles = data.textStyles.map((s) => s.name).filter((n) => set.has(n));
  }
  if (data.gridStyles.length > 0) {
    const existing = await figma.getLocalGridStylesAsync();
    const set = new Set(existing.map((s) => s.name));
    conflicts.gridStyles = data.gridStyles.map((s) => s.name).filter((n) => set.has(n));
  }
  return conflicts;
}

async function runImport(data) {
  let totalVars = 0;
  if (data.collections.length > 0) {
    totalVars = await importCollections(data.collections);
  }

  let totalStyles = 0;
  if (data.textStyles.length > 0) {
    totalStyles = await importTextStyles(data.textStyles);
  }

  let totalGrids = 0;
  if (data.gridStyles.length > 0) {
    totalGrids = await importGridStyles(data.gridStyles);
  }

  const summary = [];
  if (totalVars > 0) summary.push(`${totalVars} variables across ${data.collections.length} collections`);
  if (totalStyles > 0) summary.push(`${totalStyles} text styles`);
  if (totalGrids > 0) summary.push(`${totalGrids} grid styles`);
  figma.ui.postMessage({
    type: "done",
    message: summary.length > 0 ? `Imported ${summary.join(", ")}.` : "Nothing to import.",
  });
}

async function importCollections(collectionSpecs) {
  const existing = await figma.variables.getLocalVariableCollectionsAsync();
  const existingByName = new Map();
  for (const coll of existing) existingByName.set(coll.name, coll);

  const varByKey = new Map();

  // Pre-populate with variables from existing collections so aliases from
  // this payload can target collections imported in a prior run.
  const conflictSet = new Set(collectionSpecs.map((c) => c.name));
  for (const coll of existing) {
    if (conflictSet.has(coll.name)) continue;
    for (const varId of coll.variableIds) {
      const variable = await figma.variables.getVariableByIdAsync(varId);
      if (variable) varByKey.set(`${coll.name}.${variable.name}`, variable);
    }
  }

  const conflicts = [...conflictSet].filter((n) => existingByName.has(n));
  if (conflicts.length > 0) {
    for (const name of conflicts) {
      existingByName.get(name).remove();
    }
    figma.ui.postMessage({ type: "progress", message: `Deleted ${conflicts.length} existing collection(s).` });
  }

  let totalVars = 0;

  for (const collSpec of collectionSpecs) {
    figma.ui.postMessage({ type: "progress", message: `Creating "${collSpec.name}"...` });

    const coll = figma.variables.createVariableCollection(collSpec.name);

    const modeIdByName = new Map();
    const defaultMode = coll.modes[0];
    coll.renameMode(defaultMode.modeId, collSpec.modes[0]);
    modeIdByName.set(collSpec.modes[0], defaultMode.modeId);
    for (let i = 1; i < collSpec.modes.length; i++) {
      const modeId = coll.addMode(collSpec.modes[i]);
      modeIdByName.set(collSpec.modes[i], modeId);
    }

    for (const v of collSpec.variables) {
      const variable = figma.variables.createVariable(v.path, coll, v.type);
      if (Array.isArray(v.scopes)) variable.scopes = v.scopes;

      for (const [modeName, valueSpec] of Object.entries(v.values)) {
        const modeId = modeIdByName.get(modeName);
        if (modeId === undefined) {
          throw new Error(`Mode "${modeName}" not declared on collection "${collSpec.name}".`);
        }
        variable.setValueForMode(modeId, toFigmaValue(v.type, valueSpec, varByKey, collSpec.name, v.path));
      }

      varByKey.set(`${collSpec.name}.${v.path}`, variable);
      totalVars++;
    }
  }

  return totalVars;
}

async function importTextStyles(styleSpecs) {
  // Delete existing text styles whose names collide with incoming ones.
  // Unlike variables, text styles are not auto-remapped by name on
  // re-creation. Text nodes previously bound to a deleted style retain
  // their last-resolved values and must be re-applied to pick up the new
  // style. The UI warns the user about this before import.
  const existing = await figma.getLocalTextStylesAsync();
  const incomingNames = new Set(styleSpecs.map((s) => s.name));
  let deleted = 0;
  for (const s of existing) {
    if (incomingNames.has(s.name)) { s.remove(); deleted++; }
  }
  if (deleted > 0) {
    figma.ui.postMessage({ type: "progress", message: `Deleted ${deleted} existing text style(s).` });
  }

  // Collect unique (family, style) pairs and try to load each. Setting
  // fontName on a TextStyle requires the font to be loaded first even
  // though the style stores only a reference.
  const fontPairs = new Map();
  for (const s of styleSpecs) {
    const key = `${s.fontFamily}__${s.fontStyle}`;
    if (!fontPairs.has(key)) fontPairs.set(key, { family: s.fontFamily, style: s.fontStyle });
  }
  figma.ui.postMessage({ type: "progress", message: `Loading ${fontPairs.size} font(s)...` });

  const loadedKeys = new Set();
  const failedFonts = [];
  await Promise.all([...fontPairs.entries()].map(async ([key, font]) => {
    try {
      await figma.loadFontAsync(font);
      loadedKeys.add(key);
    } catch (err) {
      failedFonts.push(font);
    }
  }));

  if (failedFonts.length > 0) {
    const list = failedFonts.map((f) => `${f.family} ${f.style}`).join(", ");
    figma.ui.postMessage({ type: "progress", message: `Skipping styles using unavailable fonts: ${list}.` });
  }

  figma.ui.postMessage({ type: "progress", message: `Creating text style(s)...` });
  let created = 0;
  for (const spec of styleSpecs) {
    const key = `${spec.fontFamily}__${spec.fontStyle}`;
    if (!loadedKeys.has(key)) continue;
    const style = figma.createTextStyle();
    style.name = spec.name;
    style.fontName = { family: spec.fontFamily, style: spec.fontStyle };
    style.fontSize = spec.fontSize;
    if (typeof spec.lineHeight === "number") {
      style.lineHeight = { unit: "PIXELS", value: spec.lineHeight };
    }
    if (typeof spec.textCase === "string") {
      style.textCase = spec.textCase;
    }
    if (typeof spec.letterSpacingPercent === "number") {
      style.letterSpacing = { unit: "PERCENT", value: spec.letterSpacingPercent };
    }
    created++;
  }

  return created;
}

async function importGridStyles(specs) {
  // Delete existing grid styles whose names collide with incoming ones.
  // Like text styles, grid styles are not auto-remapped on re-creation:
  // frames previously bound to a deleted grid style retain their last
  // layout grids but lose the style link. The UI warns before import.
  const existing = await figma.getLocalGridStylesAsync();
  const incomingNames = new Set(specs.map((s) => s.name));
  let deleted = 0;
  for (const s of existing) {
    if (incomingNames.has(s.name)) { s.remove(); deleted++; }
  }
  if (deleted > 0) {
    figma.ui.postMessage({ type: "progress", message: `Deleted ${deleted} existing grid style(s).` });
  }

  figma.ui.postMessage({ type: "progress", message: `Creating grid style(s)...` });
  let created = 0;
  for (const spec of specs) {
    const style = figma.createGridStyle();
    style.name = spec.name;
    style.layoutGrids = spec.layoutGrids.map((g) => toFigmaLayoutGrid(g, spec.name));
    created++;
  }
  return created;
}

function toFigmaLayoutGrid(g, ownerName) {
  if (g.pattern !== "COLUMNS") {
    throw new Error(`Unsupported layout grid pattern "${g.pattern}" on ${ownerName}`);
  }
  return {
    pattern: "COLUMNS",
    alignment: g.alignment,
    count: g.count,
    gutterSize: g.gutterSize,
    offset: g.offset,
    visible: true,
    color: { r: 1, g: 0, b: 0, a: 0.1 },
  };
}

function toFigmaValue(type, spec, varByKey, ownerColl, ownerPath) {
  if (spec && typeof spec === "object" && "alias" in spec) {
    const target = varByKey.get(spec.alias);
    if (!target) {
      throw new Error(
        `Alias target not found: ${spec.alias} (referenced by ${ownerColl}.${ownerPath})`
      );
    }
    return figma.variables.createVariableAlias(target);
  }
  if (type === "COLOR") {
    if (!spec || !spec.color) {
      throw new Error(`Invalid COLOR value for ${ownerColl}.${ownerPath}`);
    }
    const { r, g, b, a } = spec.color;
    return { r, g, b, a: a === undefined ? 1 : a };
  }
  if (type === "FLOAT") {
    if (!spec || typeof spec.number !== "number") {
      throw new Error(`Invalid FLOAT value for ${ownerColl}.${ownerPath}`);
    }
    return spec.number;
  }
  throw new Error(`Unsupported variable type: ${type}`);
}
