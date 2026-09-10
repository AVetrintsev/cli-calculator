# Operator precedence

Draft for review. Conversion examples are agreed; the complete table and the whitespace rule below are proposals awaiting confirmation.

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

## Proposed complete order

Higher rows bind first. The complete order below still requires confirmation; agreed examples above remain the reference for conversion behavior.

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

Examples of the proposed placement of `::` after power and unary signs: `2^3::bin = 0b1000` and `-10::hex = -0xA`.

## Proposed whitespace rule

Proposed: the operator token determines precedence, regardless of spaces around it. `2+3::hex` and `2 + 3 :: hex` both produce `5`; `2+3 to hex` produces `0x5`. Spaces can still separate tokens or group decimal digits; this is not a rule that all spaces everywhere may be removed.

`=` defines a name; it is not an equality comparison. Evaluate its right-hand expression using the operator order. Use `==` for equality checks.
