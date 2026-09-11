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

Operator-help fragments use stable help.precedence.* keys with English meaning, context, location and element-type guidance. The [help materials](../help/README.md) define their order and generate the English and Russian Markdown previews from these locale values. The full precedence table and whitespace rule were approved in expression-language round 20; round 21 adds comparison chains and distinguishes superscript unit notation from caret exponentiation of a quantity. Separate operand and boundary-case contracts remain open. Contextual lowercase m/м is declared separately in the [unit-symbol specification](units/README.md); the user selected showing all valid answers when an expression has multiple interpretations and unambiguous metre square/cube shorthand. Explicit metre/min aliases and duration sums are approved. Square/cube shorthand formatting now applies to all known length symbols and explicit length aliases in the Latin baseline and active locale. Only whole symbols are formatted: m20/m2rate are not rewritten by prefix, and continuing a word removes superscript formatting. Backspace after m² deletes its exponent; formatting adds no separate undo step. Pasted formulas receive the same formatting in one undo step; selected formula text copies the visible superscript characters. Quick numeric result copy preserves displayed numeric text without its unit; other copy commands and persistence remain open. Identical-looking formatted answers are displayed once, retaining their underlying meanings and exact values. The updated variant A has a shared horizontal row with thin vertical dividers, horizontal overflow and no interpretation captions. The result.alternative.interpretation message was removed; descriptions in autocomplete remain. Simple compound units are limited to speed, pace and information-transfer rate, while area and volume remain supported. Support is checked after final unit cancellation; interpretations with unsupported final units are discarded while remaining valid answers are shown. Compact durations such as 1h30m are accepted. Components may be reordered and repeated: 30m1h gives 90 minutes, and 1h30m15m gives 105 minutes. The ambiguous 1m30m / 1m 30m retains two readings, a duration sum of 31 minutes and a length product of 30 square metres; this does not approve addition of adjacent lengths. Compound durations form one value under surrounding operators; 1h30m * 2 gives 180 minutes and -1h30m gives minus 90 minutes. An incomplete 1h30 has no result. A following quantity of a clearly different dimension requires an operator; 1h30m2km uses the candidate error.missingOperator text. This does not prohibit other accepted implicit multiplication. The min and max functions require two or more arguments. The min spelling followed by one complete parenthesized expression denotes minutes multiplied by that expression; without a coefficient, one minute is implied. Nested separators do not count as outer arguments. The incomplete 2min(2; has a blank result; the closed 2min(2;) uses error.missingArgument and cannot become a minute product. Other malformed lists, other error policies, copy selection and remaining editing behavior stay open. Help content uses help_heading, help_paragraph and help_table_row element types in addition to the UI types above.

The runtime localization library, initial language selection, fallback policy, language switching behavior, numeric/date formatting, plural handling, and right-to-left layout remain decisions for the expression-language and settings questions. `{name}` is a placeholder notation for these assets, not a choice of runtime interpolation library. Count-based messages must not be introduced with English-only plural assumptions.

Product decision: [Product scope and usage model](../issues/01-product-scope.md).

The user requested quick result copy: Ctrl+C in the editor with no selection and a single ready displayed result entry, plus clicking the target result. Text selection retains ordinary text copying. The help.copy.quickRule fragment uses {shortcut}: Ctrl+C on Windows and Cmd+C on macOS are accepted. Copy success/error messages must reflect the actual clipboard outcome. Quick numeric copy omits units while preserving displayed numeric rounding, grouping and numeral-system notation; formula selections retain unit text. It keeps the window and input, restores input focus after a click and does not add history. A single displayed entry permits shortcut copy without choosing a hidden interpretation. Multiple entries without selection preserve the clipboard and show copy.chooseResult. Keyboard choice and other remaining rules are tracked in the [copying question](../issues/06-history-and-copy.md). This does not add result captions or a new settings toggle.

The accepted default Enter confirmation in quick mode has its own help.confirm.quickRule fragment, separate from help.copy.quickRule. With one ready displayed result, confirmation records history, copies according to the same payload rules and immediately focuses a new empty input in the same location while keeping the window open. Ordinary quick-copy shortcuts and clicks keep the current formula and create no history entry. Confirmation success must not be inferred merely from a successful clipboard write; recovery from partial failure and modified-Enter behavior remain open. These messages add no visible calculator buttons.
