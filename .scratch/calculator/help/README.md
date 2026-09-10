# Operator help specification

These are reviewable help materials, not an implemented calculator or a final language contract. The examples accepted through expression-language round 19 are separated from the complete precedence table and whitespace rule proposed in round 20.

- [Russian preview](operators.ru.md)
- [English preview](operators.en.md)
- [Expression language and calculation rules](../issues/04-expression-language.md)
- [Fragment order](operator-help.json)
- [English text and translation guidance](../localization/catalog.json)
- [English locale](../localization/en.json) and [Russian locale](../localization/ru.json)

The `help.precedence.*` messages are the authoring source. Each fragment has English text, meaning, execution context, location and element type, with corresponding `en` and `ru` values. Mathematical expressions are preserved as data while explanatory prose is translated. The fragment index defines the order once for both languages; do not independently edit the generated Markdown previews.

After changing accepted decisions or translations, regenerate the previews from the repository root:

```text
python .scratch/calculator/help/render.py
```

The renderer joins consecutive `help_table_row` fragments with a single newline so that Markdown tables remain intact; other fragments are separated by a blank line. It writes only the two local Markdown previews. It is a documentation helper, not application implementation. A future application help entry point and its keyboard shortcut remain part of the interface specification.

Before calling the table final, resolve the pending questions in the linked language decision, update the relevant fragment text and metadata, and regenerate both languages. The approved difference between `::` and `to` must not be replaced with a claim that arbitrary expressions using them are interchangeable.
