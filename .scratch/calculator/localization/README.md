# Interface text and translations

This directory is a specification asset. It contains candidate copy for the currently identified product surfaces; there is no application implementation yet. A catalog entry does not approve a feature, a default setting, a keyboard binding, or a window layout. Entries whose context describes an undecided flow must be reviewed when that product decision is resolved.

The catalog and both language files are siblings:

- [catalog.json](catalog.json): the English source text and English translation guidance for every message.
- [en.json](en.json): the English message values, indexed by stable message keys.
- [ru.json](ru.json): the Russian message values, indexed by the same keys.

Localized mathematical unit symbols have their own sibling [unit-symbol catalog and locale files](units/README.md). Their active vocabulary contains only the Latin baseline plus one selected local language. They are parsed tokens with stable unit identities; ordinary interface messages remain in the files above.

## Catalog structure

The catalog has a schema version, a source language, a draft status, a coverage note, and a `messages` object. Each property in `messages` is a stable, descriptive key such as `copy.success`.

Each message has five required fields, all written in English:

| Field | Purpose |
| --- | --- |
| `text` | The full English source text, including named placeholders. |
| `meaning` | What the text communicates to the user; disambiguates short or repeated phrases. |
| `context` | The state, event, or user action that makes the message relevant. Unresolved behavior is identified explicitly. |
| `location` | The semantic region in which the text appears or is announced. Exact geometry is not assumed before the interface prototype is agreed. |
| `elementType` | The kind of element that uses the text, including text that is only available to assistive technology. |

Messages with inserted values also have a `placeholders` object. It describes each named value in English. These descriptions are translation guidance, not text displayed to the user.

Current element types: `input_placeholder`, `accessible_name`, `field_label`, `result_value`, `status_message`, `command_label`, `input_hint`, `error_message`, `section_heading`, `empty_state`, `dialog_title`, `select_option`, `description`, `menu_item`, and `button`.

## Consistency rules

1. The catalog and each complete language file must contain exactly the same message keys. Keys remain stable when wording changes.
2. Each `en.json` value must equal its catalog entry's `text` exactly. Update them together; the catalog is the authoring reference for English wording and translation context.
3. Each translation must be a nonempty string and retain the same named placeholders. A translator can reorder complete placeholders to fit the target language.
4. A translated sentence must be stored as a whole. Do not assemble user-facing sentences from independently translated fragments or add hard-coded English punctuation at call sites.
5. User-entered expressions, variable names, saved constant and function names or bodies, template names, file contents, and calculated values are data, not interface text. Do not translate or rewrite them through this catalog. Numeric formatting and the reduced opacity of fractional digits belong to result presentation, not translation strings.
6. Keyboard combinations are supplied in their platform-specific form through `{shortcut}`. Do not bake a Windows modifier into wording shared with macOS.
7. Use separate keys when identical English words have different meanings or translation requirements. Reuse a key only when its meaning and context are also shared.
8. A new label, placeholder, error, hint, menu item, dialog message, or accessible name must be added to the catalog and both initial language files before that application text is implemented.

## Adding another language

1. Read the full catalog so that meaning, execution context, location, and element type inform the translation.
2. Generate a sibling language JSON file, such as `de.json`, containing the same flat mapping from message keys to translated strings.
3. Preserve the keys and placeholder names. Translate values only; do not copy the metadata into the language file.
4. Validate key coverage, nonempty strings, and placeholder parity against the catalog. Preserve UTF-8 encoding.
5. Review meaning and terminology, then check the translation in the actual interface for clipping, text expansion, keyboard access, and screen-reader announcements.

Generation from the catalog provides a translation draft. Structural validation cannot certify its linguistic quality or visual fit.

## Coverage and remaining decisions

The initial catalog covers quick input, live results and diagnostics, history, calculation sheets, commands for saving user constants and functions, templates, settings, local data transfer, application menu commands, and shared dialog actions. Candidate text for optional interactions is marked as such in each message's context. There are no visible standard window controls added to the quick calculator by this catalog. The former calculation-wait message was removed after the long-running calculation flow was excluded.

Installer and updater wording, additional mathematical diagnostics, new built-in templates, and the final texts for unresolved interaction flows must be added as those parts of the specification become concrete. System-owned dialog text is supplied by the operating system; application-supplied titles or messages still belong in the catalog.

Numeral-system conversion targets bin, oct, dec and hex are invariant language tokens, not physical units or translated labels. Their completion descriptions belong to this interface catalog. Suggestions open immediately after a complete :: or to operator. Integer values without a unit are offered numeral-system targets; quantities with units are offered compatible units. Both operators support the same conversion kinds but have different precedence: :: binds before multiplication and addition, while to applies after arithmetic. The source operand used to select suggestions must follow that grouping. Diagnostics cover fractional nondecimal conversion, incompatible unit-bearing values, invalid prefixed digits and the shared integer-magnitude limit. An incomplete prefix retains the agreed empty-result behavior. Decimal precision and integer magnitude use distinct diagnostics: more than 30 binary digits is not itself an error. Only decimal digits are grouped with spaces; other bases remain contiguous in input and displayed results.

Operator-help fragments use stable help.precedence.* keys with English meaning, context, location and element-type guidance. The [help materials](../help/README.md) define their order and generate the English and Russian Markdown previews from these locale values. The full precedence table and whitespace rule were approved in expression-language round 20; separate operand and boundary-case contracts remain open. Help content uses help_heading, help_paragraph and help_table_row element types in addition to the UI types above.

The runtime localization library, initial language selection, fallback policy, language switching behavior, numeric/date formatting, plural handling, and right-to-left layout remain decisions for the expression-language and settings questions. `{name}` is a placeholder notation for these assets, not a choice of runtime interpolation library. Count-based messages must not be introduced with English-only plural assumptions.

Product decision: [Product scope and usage model](../issues/01-product-scope.md).
