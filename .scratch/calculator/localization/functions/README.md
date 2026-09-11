# Financial notation catalog

This is specification material, not an implemented evaluator. Round 22 of [Financial calculations](../../issues/12-financial-calculations.md) approves 16 function names and 2 timing symbols.

- [catalog.json](catalog.json) contains stable semantic IDs and English text, meaning, execution context, placement and element type.
- [en.json](en.json) supplies the always-active Latin spellings. [ru.json](ru.json) adds Russian spellings only when Russian is the active interface locale. A future locale adds one corresponding file; inactive locale spellings are not implicitly enabled.
- [The signature contract](../../language/financial-functions.json) binds those IDs to positional parameters, defaults, result kinds and model identities. [The verified financial report](../../research/financial-models.md) supplies the formulas and reference values.
- Parameter labels and completion descriptions live in the [main English metadata catalog](../catalog.json) with matching [English](../en.json) and [Russian](../ru.json) text. Labels describe positions; they are not named arguments or inserted placeholder variables. The question mark denotes optional parameters in help only.

Names are case-sensitive. No additional short names, spreadsheet aliases, accented variants or numeric timing aliases are approved. The monetary-interest functions return an amount; ROI and annual-rate conversion functions return a percentage. Copying 30% uses 0.3 or 0,3 according to number-format locale. General use of timing values and precision when copying a long rounded percentage remain open in round 23.

Inline completion retains the approved shared layout: name and parenthesized signature use the same font, size and style; the description follows after a gap, at the same size with lighter weight and reduced opacity. Display no more than seven rows. Typing the name prefix does not add a second menu or new captions.
