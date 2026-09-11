# Operator help specification

These help materials record the conversion examples, complete precedence table, whitespace rule, comparison chains and distinction between unit powers and quantity powers accepted through expression-language round 21, with lowercase lazy units, alternative answers, explicit aliases, duration sums and length-unit square/cube notation through contextual-units round 9, including grouping identical-looking answers, no result captions, horizontal overflow, the limited compound-unit families, final cancellation, filtering unsupported-unit interpretations, compact durations and argument-count disambiguation of min, its implied one-minute coefficient, the accepted incomplete/missing-argument states and the two-argument minimum for min/max, arbitrary duration-component order and repetitions, the sum/product alternatives of 1m30m, compound-duration grouping under outer operators, blank incomplete duration input and the explicit-operator boundary before another dimension, square/cube autoformatting for all known length symbols and aliases, whole-symbol boundaries, Backspace and undo, formatting of pasted formulas in one undo step and copying visible selected formula text. They are documentation assets; the calculator has not been implemented. Separate contracts for operand types and boundary cases remain open, including other error policies, other malformed argument lists, remaining duration-token boundaries and formatting for other copy commands and remaining editing boundaries for automatic length-unit square/cube display.

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

The separate help.copy.quickRule message records the requested copy shortcut and click behavior in both locales. It belongs to copying help rather than the operator-precedence preview; copying rounds 1–2 approve Ctrl+C/Cmd+C, displayed numeric values without units, preserving the open input without adding history, copying one displayed entry and prompting a choice when several exist; remaining contracts are tracked in [History, calculation confirmation and copying](../issues/06-history-and-copy.md).

The separate help.confirm.quickRule fragment records Enter confirmation accepted in copying round 3: one ready displayed answer, history, copied result and immediate empty input in the fixed field while the window stays open. Copying round 4 adds help.confirm.hideRule for Ctrl+Enter on Windows / Cmd+Enter on macOS: hide only after full success, start empty on the next invocation. Both fragments describe retaining the formula, result and open window with a brief error if history saving or copying fails. Copying round 5 adds help.confirm.retryRule: retrying incomplete confirmation of an unchanged formula and calculation does not duplicate an already saved entry; the successful retry uses the invoked command to determine whether to stay open or hide. Successful Enter collapses expanded history, and Arrow Up opens it again with the newest entry nearest the fixed input; failure does not collapse history. Operation order and recovery after restart remain architecture decisions. They use the same paired locale files. The operator preview does not duplicate interaction-help fragments; [History, calculation confirmation and copying](../issues/06-history-and-copy.md) holds the remaining command and failure contracts.

The separate help.confirm.multipleRule fragment documents keyboard selection accepted in copying round 6. Initial Enter or modified-Enter only focuses the existing result row; Left/Right choose, and a later confirmation command records and copies the chosen answer with the corresponding open/hide transition. Escape restores the formula cursor; clicks remain copy-only. Platform shortcuts are parameters in both locale files. This interaction-help fragment is not added to the operator-precedence preview, and it does not define the stored history record.
