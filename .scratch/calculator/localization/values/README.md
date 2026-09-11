# Value notation

[catalog.json](catalog.json) gives stable IDs, English text, meaning, execution context, location and element type for logical input literals. [en.json](en.json) is the always-active Latin baseline; [ru.json](ru.json) adds only the active Russian spellings. New locales add one matching file. Result labels are separate: true/false input produces localized Yes/No output through the main UI catalog. Do not register output text as an extra input alias automatically.

Round 23 approves true/false and да/нет, logical conditions without numeric coercion, and ordinary completion descriptions. Financial timing symbols stay in the [financial notation catalog](../functions/README.md); their general value behavior is now accepted. [Value semantics](../../language/value-semantics.md) records the shared contracts.

Calendar support is newly requested, but date/time spellings and dynamic-value names are still being agreed in [Dates, time and dynamic calendar values](../../issues/19-calendar-and-clock.md). This catalog does not silently register those pending proposals.
