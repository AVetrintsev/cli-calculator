# Localized unit symbols

These files are specification assets for localized unit notation. The registry contains fifty-two unit identities: eleven length units, six fixed-duration units, seven mass units, two area units, four volume units, three temperature scales, the radian, and eighteen information units. Metre and minute intentionally share lowercase m and its localized spelling through a declared contextual symbol. The complete inventory, inference rules and compound-duration grammar remain under discussion.

The metric length symbols are nm/нм, um/мкм, mm/мм, cm/см, dm/дм, m/м, and km/км. Lowercase m/м now uses lazy resolution between metre and minute rather than being an unambiguous metre token. The Latin um remains the keyboard-friendly micrometre spelling; additional micro-sign spellings are not approved.

Round 13 also approved hectare ha/га, international acre acre/акр, litre L/л, millilitre mL/мл, microgram ug/мкг, milligram mg/мг, gram g/г, kilogram kg/кг, and metric tonne t/т. The Latin L is uppercase; lowercase litre alternatives are not included. The Latin spelling ug is the selected keyboard-friendly notation, with no additional micro-sign spelling.

Round 14 approved international inch in/дюйм, foot ft/фут, yard yd/ярд, mile mi/миля, ordinary ounce of mass oz/унц, pound lb/фунт, US liquid gallon gal_us/гал_сша, and British imperial gallon gal_uk/гал_брит. Gallon descriptions explicitly identify the system. Additional inflections and abbreviations are not included.

In round 15 the user selected the same uppercase Latin temperature symbols C, F, and K for both en and ru. Only the explanatory descriptions are translated. Proposed degC/degF and Russian word or Cyrillic-letter alternatives were not accepted. Current temperature examples use 20 C::F. Ordinary trigonometric input uses degrees without a suffix, such as sin(30). The user separately reconfirmed explicit radian input, such as sin(pi/2 rad). The Latin spelling rad is supplied in both locales; its descriptive label is translated. The proposed Russian angle symbols and standalone degree sign were not added to these dictionaries.

Round 16 selected b for bits and B for bytes in every language. Decimal multiples are kb/Mb/Gb/Tb and kB/MB/GB/TB; binary multiples are Kib/Mib/Gib/Tib and KiB/MiB/GiB/TiB. Every symbol retains its exact Latin spelling and case in all present and future locales. The earlier bit/бит and Russian-prefixed spellings were replaced by this decision. Descriptive labels remain translatable.

Square and cubic unit completions retain superscript digits and Tab inserts the displayed spelling. Lowercase m2/м2 and m3/м3 now automatically display as m²/м² and m³/м³ and always identify square/cubic metres, never minutes. The caret ^ instead raises a complete quantity to a power: 2m2 denotes two square metres; 2m^2 denotes four square metres if m has been resolved as a metre. General duration powers, automatic replacement for other units and editor boundary cases remain open. The menu must not treat a caret expression as a duplicate spelling of a superscript unit. Descriptions remain in the parent interface-text catalog.

The selected primary duration symbols are w/н, d/д, h/ч, m/м, s/с and ms/мс. The user omitted the Russian hour from the latest list; the previously accepted ч is retained. A day remains 24 hours and a week seven days: Jira-like notation does not import another application's scheduling configuration. Earlier wk/нед, сут and min/мин are no longer primary symbols. Retaining any as extra aliases is a separate decision. Grammar for a sequence such as 1h 30m is being clarified.

## Contextual symbols

[contextual.json](contextual.json) declares lowercase m as a shared symbol for the existing metre and minute identities. Each candidate has notationPolicy: contextual and contextualSymbolId: unit.metreOrMinute in the unit catalog. Locale spellings are read from the existing locale files using localeSymbolsFromUnitId, so translators do not maintain a separate embedded set of translations. Both candidates must use the same symbol in each locale. The user calls the behavior lazy unit resolution: inspect inner expressions and use constraints from outer operations as they become available. When context is insufficient, preserve the symbol in the result, as in 2m * 2 = 4m. Independent occurrences may have different meanings. Exact operation constraints, additional explicit aliases and persistence remain open in [Contextual unit resolution and automatic unit powers](../../issues/16-contextual-units.md). This is a specification record, not an implemented resolver.

The registry allows a shared spelling only for exactly the candidates of an explicitly declared contextual symbol. All other duplicate spellings remain invalid. A known neighboring unit is not an approved universal way to determine a candidate: division may combine different dimensions. A visible unresolved symbol must not silently become a metre or minute in stored data.

- [catalog.json](catalog.json) maps stable unit IDs to the Latin symbol in text and English descriptions of meaning, execution context, location, and element type. A contextual symbol names candidates rather than a single certain meaning. unit_symbol identifies a parsed mathematical token.
- [en.json](en.json) maps the same IDs to English symbols, currently identical to the Latin symbols in the catalog.
- [ru.json](ru.json) maps the same IDs to Russian symbols.

Each locale file supplies one local symbol per unit ID. A unit keeps its identity across spellings. The metre and minute entries intentionally share a symbol and must retain their contextual declaration. These files contain no conversion factors, dimensional definitions or translated function names. Mathematical shorthand powers are specified using the selected base symbol, not new translated function names.

An optional catalog field `localizationPolicy: "invariant"` marks a symbol that must be copied verbatim from `text` into every locale. It is set on all information units following the user's explicit all-language decision. Entries without this marker follow the individual approved notation and the active-locale rules below. This field constrains symbol translation, not the translation of the associated completion description.

## Accepted language sets

The recognized unit vocabulary combines the catalog's Latin symbols with the interface language's unit symbols. Do not combine all installed locale files. An identical Latin and local spelling for the same unit represents one token, not a collision or a third language variant.

For example, with the Russian unit locale active, `km` and `км` both refer to `length.kilometre`. With the English unit locale active, `км` is not supplied as a unit token by this configuration. This does not define how an independently declared user identifier with the same spelling is handled; identifier conflicts remain a separate language and data-lifecycle decision.

After an explicit conversion with `::` or `to`, the result uses the target symbol supplied by the user. Without an explicit target, the result uses the interface language's unit symbol. Saved expressions remain usable after an interface-language change: their previously localized unit symbols are displayed in the new language, while Latin symbols are retained. User-defined names and comments retain their original text. The persistence format and treatment of unfinished input are still open decisions; these files do not implement those behaviors. Never silently enable an unrelated locale to resolve an unknown symbol.

## Adding a locale

1. Read the English metadata for every unit and create a sibling locale file with the same stable IDs.
2. Translate the local symbol value only. Keep the catalog's Latin baseline and stable IDs unchanged. If the catalog entry has `localizationPolicy: "invariant"`, copy `text` exactly instead of translating the symbol; verify this equality for every locale.
3. Check that values are nonempty. A shared exact spelling in the active locale plus Latin baseline is allowed only when all mapped unit IDs belong to the same contextual declaration, and all candidates use the same localized symbol. Reject other collisions, including a new locale symbol conflicting with an unrelated Latin symbol. Do not infer a contextual group from an accidental duplicate.
4. Check examples containing simple and compound units. A structural check does not certify a full conversion table or a complete parser.

Extend the catalog and all complete locale files together when more units are selected. Interface messages continue to use the separate parent-directory catalog and language files. User-defined names and comments are not translated through the unit-symbol dictionaries.

Product decision: [Expression language and calculation rules](../../issues/04-expression-language.md).
