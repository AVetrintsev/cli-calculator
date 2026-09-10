# Operator help specification

These help materials record the conversion examples, complete precedence table, whitespace rule, comparison chains and distinction between unit powers and quantity powers accepted through expression-language round 21, with lowercase lazy units, unresolved-symbol results and metre square/cube notation from contextual-units round 1. They are documentation assets; the calculator has not been implemented. Separate contracts for operand types and boundary cases remain open, including operation constraints for lazy m/м, adjacent duration components and editor boundaries for automatic metre square/cube display.

- [Russian preview](operators.ru.md)
- [English preview](operators.en.md)
- [Expression language and calculation rules](../issues/04-expression-language.md)
- [Contextual unit resolution and automatic unit powers](../issues/16-contextual-units.md)
- [Fragment order](operator-help.json)
- [English text and translation guidance](../localization/catalog.json)
- [English locale](../localization/en.json) and [Russian locale](../localization/ru.json)

The `help.precedence.*` messages are the authoring source. Each fragment has English text, meaning, execution context, location and element type, with corresponding `en` and `ru` values. Mathematical expressions are preserved as data while explanatory prose is translated. The fragment index defines the order once for both languages; do not independently edit the generated Markdown previews.

After changing accepted decisions or translations, regenerate the previews from the repository root:

```text
python .scratch/calculator/help/render.py
```

The renderer joins consecutive `help_table_row` fragments with a single newline so that Markdown tables remain intact; other fragments are separated by a blank line. It writes only the two local Markdown previews. It is a documentation helper, not application implementation. A future application help entry point and its keyboard shortcut remain part of the interface specification.

When a later decision changes an operator rule, update the relevant source fragments and metadata, then regenerate both languages. Keep settled precedence distinct from still-open operator contracts. The approved difference between `::` and `to` must not be replaced with a claim that arbitrary expressions using them are interchangeable.
