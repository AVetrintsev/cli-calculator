# Localized unit symbols

These files are specification assets for localized unit notation. The current subset contains fourteen units: seven metric length units approved through expression-language round 13, all six fixed-duration units agreed in round 12, and the previously approved kilogram. The complete product unit inventory remains to be specified.

The approved metric length symbols are nm/нм, um/мкм, mm/мм, cm/см, dm/дм, m/м, and km/км. The Latin spelling um is the product's keyboard-friendly notation; this approval does not add alternative spellings containing a micro sign. Powered-unit completion display and insertion are still proposals in round 13; no display or insertion contract is implied by these symbol dictionaries.

The user requested a separate review of abbreviations by unit group. Fixed durations are now approved: ms/мс, s/с, min/мин, h/ч, d/сут, wk/нед. Other proposed spellings are recorded in the expression-language decision before being added here. Approval of a unit category alone does not approve every abbreviation or alias for it. The minute symbol min and the built-in function min still require an explicit syntax-disambiguation rule; this dictionary does not implement one.

- [catalog.json](catalog.json) maps stable unit IDs to the always-available Latin symbol in `text` and English descriptions of its meaning, execution context, location, and element type. `unit_symbol` identifies a mathematical token rather than an interface command or sentence.
- [en.json](en.json) maps the same IDs to English symbols, currently identical to the Latin symbols in the catalog.
- [ru.json](ru.json) maps the same IDs to Russian symbols.

Each locale file supplies one local symbol per unit ID. A unit keeps its identity across all spellings. These files contain no conversion factors, dimensional definitions, or translated function names. They are stored alongside the interface translations in their own directory because a unit symbol participates in expression parsing.

## Accepted language sets

The recognized unit vocabulary combines the catalog's Latin symbols with the interface language's unit symbols. Do not combine all installed locale files. An identical Latin and local spelling for the same unit represents one token, not a collision or a third language variant.

For example, with the Russian unit locale active, `m` and `м` both refer to `length.metre`. With the English unit locale active, `м` is not supplied as a unit token by this configuration. This does not define how an independently declared user identifier with the same spelling is handled; identifier conflicts remain a separate language and data-lifecycle decision.

After an explicit conversion with `::` or `to`, the result uses the target symbol supplied by the user. Without an explicit target, the result uses the interface language's unit symbol. Saved expressions remain usable after an interface-language change: their previously localized unit symbols are displayed in the new language, while Latin symbols are retained. User-defined names and comments retain their original text. The persistence format and treatment of unfinished input are still open decisions; these files do not implement those behaviors. Never silently enable an unrelated locale to resolve an unknown symbol.

## Adding a locale

1. Read the English metadata for every unit and create a sibling locale file with the same stable IDs.
2. Translate the local symbol value only. Keep the catalog's Latin baseline and stable IDs unchanged.
3. Check that values are nonempty and that the active locale plus the Latin baseline does not map the same exact symbol to two different unit IDs. Such a conflict must be resolved in the configuration rather than guessed while evaluating a formula.
4. Check examples containing simple and compound units. A structural check does not certify a full conversion table or a complete parser.

Extend the catalog and all complete locale files together when more units are selected. Interface messages continue to use the separate parent-directory catalog and language files. User-defined names and comments are not translated through the unit-symbol dictionaries.

Product decision: [Expression language and calculation rules](../../issues/04-expression-language.md).
