# Operator precedence

The order below applies to mathematical expressions. Use parentheses to group a calculation explicitly.

## Two conversion operators

`::` and `to` support the same conversions but apply to different parts of an expression. `::` binds before multiplication and addition. `to` applies after the arithmetic expression to its left.

| Input | Grouping | Result |
| --- | --- | --- |
| `2+3::hex` | `2+(3::hex)` | `5` |
| `2+3 to hex` | `(2+3) to hex` | `0x5` |
| `(2+3)::hex` | Convert the parenthesized sum | `0x5` |

To continue arithmetic after `to`, use parentheses: `(2 to hex) + 3 = 5`. The intermediate representation does not change the number. `2 to hex + 3` asks for parentheses; `2::hex+3` is valid and produces `5`.

## Conversion chains

Consecutive conversions run from left to right, including mixed operators: `255 to hex::bin = 0b11111111`; `1 km to m::cm = 100 000 cm`. Each target names a conversion destination. The next conversion uses the preceding value, not the target name. The last target sets the final representation or unit. Rounded intermediate display text is never reused for calculation.

## Order of operations

Higher rows bind first. Operators within an expression use this order unless parentheses explicitly change the grouping.

| Priority | Operation |
| ---: | --- |
| 1 | Parentheses, function calls, `√`, values with units |
| 2 | Postfix percent `%` |
| 3 | Power `^` |
| 4 | Unary signs `+` and `-` |
| 5 | Conversion `::` |
| 6 | Multiplication (including implicit multiplication) and division |
| 7 | Addition and subtraction |
| 8 | Comparisons `==`, `!=`, `<`, `<=`, `>`, `>=` |
| 9 | Logical `not` |
| 10 | Logical `and` |
| 11 | Logical `or` |
| 12 | Conversion `to` |

Already agreed: powers associate left to right, so `2^3^2 = (2^3)^2 = 64`. Power precedes unary minus: `-2^2 = -4`. Multiplication, implicit multiplication and division have equal priority and run left to right: `6/2(1+2) = 9`.

A chain such as `1 < x < 10` compares neighboring values and requires every comparison to hold. It means `1 < x and x < 10`. Stop at the first false comparison; do not compare a Boolean intermediate result with the next number.

Power and unary signs bind before `::`: `2^3::bin = 0b1000` and `-10::hex = -0xA`.

## Lazy unit resolution

Lowercase m can mean a metre or a minute; the active Russian spelling м follows the same rule. Determine its meaning from the expression, including outer parentheses. When context is insufficient, preserve the symbol: 2m * 2 = 4m. Different occurrences can have different meanings. The constraints supplied by multiplication, division and other operations are still being specified.

Short duration symbols are w, d, h, m, s and ms. Russian symbols are н, д, ч, м, с and мс; the existing hour symbol ч is retained. Days remain 24 hours and weeks remain seven days. The minute symbols m and м are contextual. Grammar for adjacent duration components is still being agreed.

## Unit powers and quantity powers

Typing m2 or m3 automatically displays m² or m³; the active Russian equivalents are м2/м3 and м²/м³. These symbols always mean square or cubic metres, never minutes. The caret ^ instead raises the entire quantity to a power: 2m2 denotes two square metres; 2m^2 denotes four square metres if m has been resolved as a metre. Powers of resolved durations and automatic replacement for other units are still being specified.

## Spaces around operators

The operator determines precedence, regardless of spaces around it. `2+3::hex` and `2 + 3 :: hex` both produce `5`; `2+3 to hex` produces `0x5`. Spaces can still separate tokens or group decimal digits; they cannot be removed arbitrarily from every expression.

`=` defines a name; it is not an equality comparison. Evaluate its right-hand expression using the operator order. Use `==` for equality checks.
