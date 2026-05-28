# Spacing

## Conformance test

A spacing value is valid if and only if `value mod 4 = 0`.

4px is the minimum: at 2px, a gap may round to 0 or 4 physical pixels on non-integer DPI displays. From 4px, admitting odd multiples (6, 10, 14) would place consecutive scale values 2px apart, reintroducing the unstable interval. Even multiples produce a scale whose step size matches its minimum value.

## Generative rule

`step(n) = n × 4px`, for any positive integer n.

The scale has no upper bound. A value is valid if it satisfies the conformance test.

## Token set

The interval between consecutive tokens widens as values grow. A 4px difference at small sizes reads as clear hierarchy; the same difference at 96px is below perceptual threshold. The token set spaces each step at a perceptually meaningful interval.

| Token     | Value | Step |
|-----------|-------|------|
| space-4   | 4px   | 1    |
| space-8   | 8px   | 2    |
| space-12  | 12px  | 3    |
| space-16  | 16px  | 4    |
| space-20  | 20px  | 5    |
| space-24  | 24px  | 6    |
| space-32  | 32px  | 8    |
| space-40  | 40px  | 10   |
| space-48  | 48px  | 12   |
| space-64  | 64px  | 16   |
| space-80  | 80px  | 20   |
| space-96  | 96px  | 24   |
| space-128 | 128px | 32   |
| space-160 | 160px | 40   |
| space-192 | 192px | 48   |

Values outside the token set remain valid by the generative rule. Values above space-192 are available with no upper bound.

## Density registers

Three registers define a surface's spatial character. A surface selects one register and draws spacing values from that register's designed set.

### Compact

High information density. White space separates elements and aids scanning. Examples: documentation, dense UI, mobile application.

Tight internal spacing. Component padding and element gaps use the smaller values; margins and section separation use the middle of the scale.

| Token    | Value |
|----------|-------|
| space-4  | 4px   |
| space-8  | 8px   |
| space-12 | 12px  |
| space-16 | 16px  |
| space-20 | 20px  |
| space-24 | 24px  |
| space-32 | 32px  |
| space-40 | 40px  |
| space-48 | 48px  |

### Standard

Medium information density. White space balances structural and expressive functions. Examples: web, tablet, presentation deck.

Balanced spacing. Component padding and element gaps use the smaller and middle values; section separation and layout intervals use the middle and larger values.

| Token    | Value |
|----------|-------|
| space-4  | 4px   |
| space-8  | 8px   |
| space-12 | 12px  |
| space-16 | 16px  |
| space-20 | 20px  |
| space-24 | 24px  |
| space-32 | 32px  |
| space-40 | 40px  |
| space-48 | 48px  |
| space-64 | 64px  |
| space-80 | 80px  |
| space-96 | 96px  |

### Expressive

Low information density by intent. White space is the primary structural element. Examples: large-format display, hero surfaces, brand artifacts, posters.

Generous spacing. Internal element spacing uses the middle of the scale; section separation uses the larger values; page-scale intervals may use the largest.

| Token     | Value |
|-----------|-------|
| space-16  | 16px  |
| space-24  | 24px  |
| space-32  | 32px  |
| space-40  | 40px  |
| space-48  | 48px  |
| space-64  | 64px  |
| space-80  | 80px  |
| space-96  | 96px  |
| space-128 | 128px |
| space-160 | 160px |
| space-192 | 192px |