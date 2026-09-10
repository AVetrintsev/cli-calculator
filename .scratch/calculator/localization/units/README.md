# Localized unit symbols

These files are specification assets for localized unit notation. The direct registry contains fifty-two unit identities: eleven length units, six fixed-duration units, seven mass units, two area units, four volume units, three temperature scales, the radian, and eighteen information units. The metre and minute spelling records are under revision following the new contextual M requirement; retaining their former direct spellings is being clarified. The complete product unit inventory remains to be verified as language decisions are refined.

The previously approved metric length symbols are nm/нм, um/мкм, mm/мм, cm/см, dm/дм, m/м, and km/км; retention of the explicit metre spelling is now under discussion. The Latin spelling um is the product's keyboard-friendly notation; this approval does not add alternative spellings containing a micro sign.

Round 13 also approved hectare ha/га, international acre acre/акр, litre L/л, millilitre mL/мл, microgram ug/мкг, milligram mg/мг, gram g/г, kilogram kg/кг, and metric tonne t/т. The Latin L is uppercase; lowercase litre alternatives are not included. The Latin spelling ug is the selected keyboard-friendly notation, with no additional micro-sign spelling.

Round 14 approved international inch in/дюйм, foot ft/фут, yard yd/ярд, mile mi/миля, ordinary ounce of mass oz/унц, pound lb/фунт, US liquid gallon gal_us/гал_сша, and British imperial gallon gal_uk/гал_брит. Gallon descriptions explicitly identify the system. Additional inflections and abbreviations are not included.

In round 15 the user selected the same uppercase Latin temperature symbols C, F, and K for both en and ru. Only the explanatory descriptions are translated. Proposed degC/degF and Russian word or Cyrillic-letter alternatives were not accepted. Current temperature examples use 20 C::F. Ordinary trigonometric input uses degrees without a suffix, such as sin(30). The user separately reconfirmed explicit radian input, such as sin(pi/2 rad). The Latin spelling rad is supplied in both locales; its descriptive label is translated. The proposed Russian angle symbols and standalone degree sign were not added to these dictionaries.

Round 16 selected b for bits and B for bytes in every language. Decimal multiples are kb/Mb/Gb/Tb and kB/MB/GB/TB; binary multiples are Kib/Mib/Gib/Tib and KiB/MiB/GiB/TiB. Every symbol retains its exact Latin spelling and case in all present and future locales. The earlier bit/бит and Russian-prefixed spellings were replaced by this decision. Descriptive labels remain translatable.

Square and cubic unit completions retain superscript digits, such as m² and см³, and Tab inserts the displayed spelling. Expression-language round 21 changed the former caret equivalence: ^ is an exponentiation operator on the complete quantity, not an alternative unit spelling after a coefficient. The user selected automatic M2-to-M² display. In a length context, 2 M2 denotes two square metres, while 2 M^2 denotes the square of two metres. Extension to other abbreviations, cubes and editing edge cases is still under discussion. The menu must not treat a caret expression as a duplicate spelling of a superscript unit. Unit descriptions remain in the parent interface-text catalog.

The user requested a separate review of abbreviations by unit group. Direct duration spellings ms/мс, s/с, h/ч, d/сут and wk/нед remain selected. The earlier min/мин spelling is retained here as an under-revision record pending the exact contextual-M and explicit-input policy; do not read it as a resolution of the new request. Other proposed spellings are recorded in the language decision before becoming final. Approval of a unit category alone does not approve every abbreviation or alias for it.

## Contextual symbols

[contextual.json](contextual.json) records the new M requirement separately from the direct one-symbol-to-one-unit registry. Its candidates are the existing metre and minute identities. Resolve such an occurrence using constraints from the whole expression, including outer operations; do not select a candidate merely by looking at the nearest unit. Exact case and locale spellings, behavior with zero or multiple valid interpretations, and interaction with saved names remain open in [Contextual unit resolution and automatic unit powers](../../issues/16-contextual-units.md). This is a specification record, not an implemented resolver.

The direct registry's uniqueness rule still prevents accidental conflicts. Intentional contextual candidates must be declared explicitly in the separate model; the new feature is not permission to accept arbitrary duplicate locale spellings. Entries marked `notationStatus: "under_revision"` retain earlier direct notation for traceability while a replacement or explicit fallback is being chosen.

- [catalog.json](catalog.json) maps stable unit IDs to the always-available Latin symbol in `text` and English descriptions of its meaning, execution context, location, and element type. `unit_symbol` identifies a mathematical token rather than an interface command or sentence.
- [en.json](en.json) maps the same IDs to English symbols, currently identical to the Latin symbols in the catalog.
- [ru.json](ru.json) maps the same IDs to Russian symbols.

Each locale file supplies one local symbol per unit ID. A unit keeps its identity across all spellings. These files contain no conversion factors, dimensional definitions, or translated function names. They are stored alongside the interface translations in their own directory because a unit symbol participates in expression parsing.

An optional catalog field `localizationPolicy: "invariant"` marks a symbol that must be copied verbatim from `text` into every locale. It is set on all information units following the user's explicit all-language decision. Entries without this marker follow the individual approved notation and the active-locale rules below. This field constrains symbol translation, not the translation of the associated completion description.

## Accepted language sets

The recognized unit vocabulary combines the catalog's Latin symbols with the interface language's unit symbols. Do not combine all installed locale files. An identical Latin and local spelling for the same unit represents one token, not a collision or a third language variant.

For example, with the Russian unit locale active, `km` and `км` both refer to `length.kilometre`. With the English unit locale active, `км` is not supplied as a unit token by this configuration. This does not define how an independently declared user identifier with the same spelling is handled; identifier conflicts remain a separate language and data-lifecycle decision.

After an explicit conversion with `::` or `to`, the result uses the target symbol supplied by the user. Without an explicit target, the result uses the interface language's unit symbol. Saved expressions remain usable after an interface-language change: their previously localized unit symbols are displayed in the new language, while Latin symbols are retained. User-defined names and comments retain their original text. The persistence format and treatment of unfinished input are still open decisions; these files do not implement those behaviors. Never silently enable an unrelated locale to resolve an unknown symbol.

## Adding a locale

1. Read the English metadata for every unit and create a sibling locale file with the same stable IDs.
2. Translate the local symbol value only. Keep the catalog's Latin baseline and stable IDs unchanged. If the catalog entry has `localizationPolicy: "invariant"`, copy `text` exactly instead of translating the symbol; verify this equality for every locale.
3. Check that values are nonempty and that the active locale plus the Latin baseline does not map the same exact symbol to two different unit IDs. Such a conflict must be resolved in the configuration rather than guessed while evaluating a formula.
4. Check examples containing simple and compound units. A structural check does not certify a full conversion table or a complete parser.

Extend the catalog and all complete locale files together when more units are selected. Interface messages continue to use the separate parent-directory catalog and language files. User-defined names and comments are not translated through the unit-symbol dictionaries.

Product decision: [Expression language and calculation rules](../../issues/04-expression-language.md).
