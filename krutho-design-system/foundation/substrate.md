# Substrate

## Medium

The medium is screen. The unit is the CSS logical pixel (1/96 inch at arm's length viewing distance).

Print surfaces use the point (pt). 1pt = 1/72 inch. The arithmetic is identical.

## Substrate value

The substrate is **2px**.

Conformance test: `value mod 2 = 0`.

2px is the smallest value that satisfies three conditions:

- Stable rendering across display densities (1px may round to 0 or 2px on non-integer-scaled displays).
- Halves to integers, supporting recursive halving and sub-grid construction downstream.
- Admits the typographic range 10, 12, 14, 16, 18, 20px.

## Production context

A surface declares its production context (screen or print). That declaration determines the unit and conformance test.