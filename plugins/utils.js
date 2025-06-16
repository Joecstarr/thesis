import { normalizeLabel } from 'myst-common';

export function classDirectiveOption(nodeType = 'node') {
  return {
    class: {
      type: String,
      doc: `Annotate the ${nodeType} with a set of space-delimited class names.`,
    },
  };
}

export function labelDirectiveOption(nodeType = 'node') {
  return {
    label: {
      type: String,
      alias: ['name'],
      doc: `Label the ${nodeType} to be cross-referenced or explicitly linked to.`,
    },
  };
}

export function enumerationDirectiveOptions(nodeType = 'node') {
  return {
    enumerated: {
      type: Boolean,
      alias: ['numbered'],
      doc: `Turn on/off the numbering for the specific ${nodeType}`,
    },
    enumerator: {
      type: String,
      alias: ['number'],
      doc: `Explicitly set the ${nodeType} number`,
    },
  };
}

/**
 * Adds `class`, `label`, `enumerated`, and `enumerator`.
 */
export function commonDirectiveOptions(nodeType = 'node') {
  return {
    ...classDirectiveOption(nodeType),
    ...labelDirectiveOption(nodeType),
    ...enumerationDirectiveOptions(nodeType),
  };
}

export function addClassOptions(data, node) {
  if (typeof data.options?.class === 'string') {
    node.class = data.options.class;
  }
  return node;
}

export function addLabelOptions(data, node) {
  const { label, identifier } = normalizeLabel(data.options?.label) || {};
  if (label) node.label = label;
  if (identifier) node.identifier = identifier;
  return node;
}

export function addEnumerationOptions(data, node) {
  if (typeof data.options?.enumerated === 'boolean') {
    node.enumerated = data.options.enumerated;
  }
  if (data.options?.enumerator) {
    node.enumerator = data.options.enumerator;
  }
  return node;
}

export function addCommonDirectiveOptions(data, node) {
  addClassOptions(data, node);
  addLabelOptions(data, node);
  addEnumerationOptions(data, node);
  return node;
}
