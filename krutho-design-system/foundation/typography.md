# Typography

## Conformance test

A type size is valid if and only if `value mod 2 = 0`. Typography admits the substrate directly.

## Scale

The interval between consecutive tokens widens as size grows. A 2px difference at body size reads as clear hierarchy; at display size it falls below perceptual threshold. The token set spaces each step at a perceptually meaningful interval.

Sizes outside the token set remain valid where they satisfy the conformance test.

## Typefaces

| Style   | Default                                       |
|---------|-----------------------------------------------|
| sans    | `Aeonik Pro VF, system-ui, sans-serif`        |
| mono    | `Aeonik Mono Pro VF, ui-monospace, monospace` |
| display | `Aeonik Fono Pro VF, system-ui, sans-serif`   |

Each default names a specific typeface with a fallback to the platform's native typeface in the named style. Surfaces tailor usage per case.

## Weights

Four weights admitted across the system.

| Weight   | Value |
|----------|-------|
| Regular  | 400   |
| Medium   | 500   |
| Semibold | 600   |
| Bold     | 700   |

A surface selects which weights it uses, which slots they apply to, and the function each weight serves.

## Line height

Line height derives from type size using three ratios:

- **Tight** at 1.2: minimum ratio at which descender clearance is reliably maintained across typefaces.
- **Default** at 1.4: comfortable sustained reading; accommodates x-height variation across typefaces.
- **Loose** at 1.6: completes a three-step set at a consistent 0.2 interval.

Rounding: ceiling to the nearest even integer.

`lh = ⌈(size × ratio) / 2⌉ × 2`

Line heights satisfy the conformance test.

## Type tokens

| Token    | Size  |
|----------|-------|
| type-10  | 10px  |
| type-12  | 12px  |
| type-14  | 14px  |
| type-16  | 16px  |
| type-18  | 18px  |
| type-20  | 20px  |
| type-24  | 24px  |
| type-28  | 28px  |
| type-32  | 32px  |
| type-40  | 40px  |
| type-48  | 48px  |
| type-64  | 64px  |
| type-80  | 80px  |
| type-96  | 96px  |
| type-128 | 128px |
| type-192 | 192px |

## Line height tokens

Tokens are named `lh-{size}-{variant}`, where `{variant}` is `tight`, `default`, or `loose` (e.g. `lh-16-default` is 24px). Values derive from the table below.

| Type token | Tight (×1.2) | Default (×1.4) | Loose (×1.6) |
|------------|--------------|----------------|--------------|
| type-10    | 12px         | 14px           | 16px         |
| type-12    | 16px         | 18px           | 20px         |
| type-14    | 18px         | 20px           | 24px         |
| type-16    | 20px         | 24px           | 26px         |
| type-18    | 22px         | 26px           | 30px         |
| type-20    | 24px         | 28px           | 32px         |
| type-24    | 30px         | 34px           | 40px         |
| type-28    | 34px         | 40px           | 46px         |
| type-32    | 40px         | 46px           | 52px         |
| type-40    | 48px         | 56px           | 64px         |
| type-48    | 58px         | 68px           | 78px         |
| type-64    | 78px         | 90px           | 104px        |
| type-80    | 96px         | 112px          | 128px        |
| type-96    | 116px        | 136px          | 154px        |
| type-128   | 154px        | 180px          | 206px        |
| type-192   | 232px        | 270px          | 308px        |