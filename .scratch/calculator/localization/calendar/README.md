# Calendar locale patterns

[catalog.json](catalog.json) supplies English text, meaning, execution context, location and element type. [en.json](en.json) is the always-active YYYY-MM-DD input baseline. [ru.json](ru.json) adds DD.MM.YYYY only when ru is active; it does not remove the baseline.

Y/M/D are fixed pattern metacharacters, not characters typed into a date and not freely translated words. Four year digits and two month/day digits are required. Future locale patterns must be validated against the expression grammar before registration. Output remains YYYY-MM-DD for every locale. These files specify formats; they do not implement recognition or recovery from partial input.

Time input uses common 24-hour notation, optional seconds and one to three fractional-second digits after either decimal separator. Date-time accepts a space or T. Those rules are in the [calendar contract](../../language/calendar.json). Dynamic value names are in the [value catalog](../values/README.md); explanatory text and diagnostics are in the [main catalog](../catalog.json) and adjacent en/ru files. Calendar month/year and fixed-offset spellings remain pending in the [calendar decision](../../issues/19-calendar-and-clock.md).
