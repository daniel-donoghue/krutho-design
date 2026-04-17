// Krutho Tokens Import
// Reads a figma-plugin.json payload at runtime and materialises variable
// collections, modes, variables, and aliases into the current file.

figma.showUI(__html__, { width: 460, height: 360 });

figma.ui.onmessage = async (msg) => {
  try {
    if (msg.type === "analyse") {
      const data = parsePayload(msg.payload);
      const conflicts = await findConflicts(data);
      figma.ui.postMessage({ type: "analysis", conflicts, collectionCount: data.collections.length });
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
  if (!data || !Array.isArray(data.collections)) {
    throw new Error("JSON missing 'collections' array.");
  }
  return data;
}

async function findConflicts(data) {
  const existing = await figma.variables.getLocalVariableCollectionsAsync();
  const existingSet = new Set(existing.map((c) => c.name));
  return data.collections.map((c) => c.name).filter((name) => existingSet.has(name));
}

async function runImport(data) {
  const existing = await figma.variables.getLocalVariableCollectionsAsync();
  const existingByName = new Map();
  for (const coll of existing) existingByName.set(coll.name, coll);

  const varByKey = new Map();

  // Pre-populate with variables from existing collections so aliases from
  // this payload can target collections imported in a prior run.
  const conflictSet = new Set(data.collections.map((c) => c.name));
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

  for (const collSpec of data.collections) {
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

  figma.ui.postMessage({
    type: "done",
    message: `Imported ${totalVars} variables across ${data.collections.length} collections.`,
  });
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
