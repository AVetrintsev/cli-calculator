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
| 1 | Parentheses, function calls, `√`, values with units (including compound durations) |
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

Lowercase m can mean a metre or a minute; the active Russian spelling м follows the same rule. Lazy resolution uses the whole formula, including outer parentheses. If multiple interpretations remain valid, show all distinct visible answers: 10m / 2s gives 5m/s or the unitless 300. Identical-looking answers appear once: 2m * 2 displays one 4m. Answers have no interpretation captions and remain in one row with horizontal scrolling when needed. Grouping the display does not discard original meanings or exact values. Explicit metre and min select a unit directly; the Russian equivalents are метр and мин. Ordering and copy selection remain open.

Short duration symbols are w, d, h, m, s and ms. Russian symbols are н, д, ч, м, с and мс. Days remain 24 hours and weeks remain seven days. Adjacent duration components add, with or without spaces: 1h30m and 1h 30m both equal 90 minutes. Components may appear in any order and repeat: 30m1h equals 90 minutes; 1h30m15m equals 105 minutes. Use an explicit * to multiply adjacent duration quantities. With only ambiguous m symbols, retain both valid readings: 1m30m and 1m 30m give 31 minutes as a duration sum and 30 square metres as a length product. This does not introduce addition of adjacent lengths. A compound duration is one value for surrounding operators: 1h30m * 2 equals 180 minutes, and -1h30m equals minus 90 minutes. An incomplete final component such as 1h30 keeps the result blank until its unit is entered. An explicit operator is required before a following quantity of a clearly different dimension: 1h30m2km reports a missing operator; write 1h30m / 2km to calculate pace. This boundary does not remove the two accepted readings of 1m30m or other accepted forms of implicit multiplication.

## Minutes and the min function

The min function takes at least two arguments separated by semicolons. One complete expression in the following parentheses denotes minutes multiplied by that expression: 2min(2+4) equals 12 minutes. With no coefficient, one minute is implied: min(2+4) = 1min(2+4), or 6 minutes. Two or more arguments denote the function: 2 min(2;4) = 2 * min(2;4) = 4, without a unit. Spaces before min do not change the meaning. Count arguments at the current parentheses level: 2min(max(2;4)) has one outer argument and equals 8 minutes. While 2min(2; is incomplete, the result stays blank. Closing it as 2min(2;) produces a missing-argument error, without reinterpreting the list as minutes. The max function also requires at least two arguments. Other malformed argument lists are still being specified.

## Unit powers and quantity powers

Typing m2 or m3 automatically displays m² or m³; the active Russian equivalents are м2/м3 and м²/м³. These symbols always mean square or cubic metres, never minutes. The caret ^ raises the entire quantity to a power: 2m2 denotes two square metres; 2m^2 leaves the supported answer 4m², discarding the squared-minutes interpretation. Unit support is checked after final cancellation. Editing boundaries for automatic superscripts are still being specified.

Supported compound units are speed (length/time, for example km/h), pace (time/length, min/km) and information-transfer rate (information/time, MB/s). Area and volume remain supported. Check support after final cancellation: (2s * 3s) / 1s = 6s is valid. Final units such as kg*m, s² and m/s² are excluded. Discard interpretations with unsupported final units and show the remaining valid answers; show the short unsupported-unit diagnostic only if no valid supported answer remains. Policies for other errors are still being specified. Temperature retains its separate conversion-only rule.

## Spaces around operators

The operator determines precedence, regardless of spaces around it. `2+3::hex` and `2 + 3 :: hex` both produce `5`; `2+3 to hex` produces `0x5`. Spaces can still separate tokens or group decimal digits; they cannot be removed arbitrarily from every expression.

`=` defines a name; it is not an equality comparison. Evaluate its right-hand expression using the operator order. Use `==` for equality checks.
