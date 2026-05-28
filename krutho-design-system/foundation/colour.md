# Colour

## Architecture

Colour is structured in three layers:

**Primitive scales.** Raw colour ramps. Hex values exist only here.

**Semantic layer.** Source tokens that name colours by function (error, success, warning, info). Light and dark mode resolution is handled at this layer.

**Component tokens.** Named values applied at the component level (surface, text, border, icon, action, feedback). Each references a primitive stop or a semantic source token.

Component tokens never reference primitives by hex value. They reference by stop name (`ramp · stop`), which makes any token traceable back to its primitive.

---

## Ramp construction

Primitive ramps are curated values, not algorithmically derived. Each ramp is a hand-tuned set of 11 standard stops (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950). Off-standard stops in neutral (0, 450, 825, 850) sit outside the standard set and exist for specific UI functions documented inline with each.

A new ramp (for a brand-specific accent, additional functional state, or extended brand palette) is constructed as follows:

1. **Pick a starting palette or anchor colour.** Tailwind CSS, Radix Colors, Open Color, or a defined brand colour are reasonable starting points.
2. **Decide the anchor stop.** The canonical brand value for the ramp. Typical anchors: 500 for brand-primary, 600 for error, 700 for success and warning.
3. **Distribute the remaining stops** so adjacent stops read as distinct perceptual steps. As a soft guide, OKLCH lightness across the standard stops falls roughly within: 50 ≈ 0.97, 100 ≈ 0.89, 200 ≈ 0.81, 300 ≈ 0.73, 400 ≈ 0.64, 500 ≈ 0.57, 600 ≈ 0.50, 700 ≈ 0.43, 800 ≈ 0.36, 900 ≈ 0.28, 950 ≈ 0.20.
4. **Verify contrast pairings** used by the system: stop 50 fill against stop 600+ text, stop 100 against stop 700, dark mode stop 50 surface over neutral 900.
5. **Hand-tune.** Saturation at light stops, hue drift across the ramp where it serves the brand, deep stops for richness.

The result is the curated set. Stops are documented at their registered hex values.

---

## Primitive scales

### Neutral

Pure achromatic scale. No warm or cool undertone. Powers surface, text, border, and icon tokens in both light and dark modes.

| Stop | Hex     |
|------|---------|
| 0    | #FFFFFF |
| 50   | #FAFAFA |
| 100  | #F2F2F2 |
| 200  | #E6E6E6 |
| 300  | #D6D6D6 |
| 400  | #C4C4C4 |
| 450  | #AFAFAF |
| 500  | #9A9A9A |
| 600  | #707070 |
| 700  | #505050 |
| 800  | #343434 |
| 825  | #2A2A2A |
| 850  | #202020 |
| 900  | #181818 |
| 950  | #0A0A0A |

Off-standard stops:

- **0 (#FFFFFF).** Pure white. Required for label text on saturated fills and icon-on-accent. The 50 stop is not sufficient: the contrast difference between #FAFAFA and a saturated fill is not equivalent to white.
- **450 (#AFAFAF).** Arithmetic midpoint of 400 (#C4C4C4) and 500 (#9A9A9A). Required for placeholder text, which must be perceptibly lighter than disabled text (400) and darker than faint text (500).
- **825 (#2A2A2A) and 850 (#202020).** Additional dark backgrounds. The dark mode surface hierarchy requires four distinct dark values (#343434, #2A2A2A, #202020, #181818); only 800 and 900 have natural positions on the standard scale.

### Accent

Anchored at 500. Powers action-primary, text-link, border-focus, and semantic-info. Defaults to neutral palette values. A brand layer overrides with brand-specific accent values.

| Stop | Hex     |
|------|---------|
| 50   | #FAFAFA |
| 100  | #F2F2F2 |
| 200  | #E6E6E6 |
| 300  | #D6D6D6 |
| 400  | #C4C4C4 |
| 500  | #9A9A9A |
| 600  | #707070 |
| 700  | #505050 |
| 800  | #343434 |
| 900  | #181818 |
| 950  | #0A0A0A |

### Error

Functional state colour for errors, destructive actions, and invalid validation. Anchored at 600 for the semantic source.

| Stop | Hex     |
|------|---------|
| 50   | #FEF2F2 |
| 100  | #FFCFCF |
| 200  | #FFAAAA |
| 300  | #FF7A7A |
| 400  | #F04848 |
| 500  | #E02828 |
| 600  | #C0251D |
| 700  | #9B1C1C |
| 800  | #7B1414 |
| 900  | #5A0C0C |
| 950  | #380606 |

### Success

Functional state colour for success confirmations and positive states. Anchored at 700 for the semantic source.

| Stop | Hex     |
|------|---------|
| 50   | #F0FDF4 |
| 100  | #CBFADE |
| 200  | #9AEEC0 |
| 300  | #5EDE9A |
| 400  | #30C478 |
| 500  | #18A85A |
| 600  | #128C46 |
| 700  | #166534 |
| 800  | #0F4826 |
| 900  | #083018 |
| 950  | #03160C |

### Warning

Functional state colour for cautionary states and non-blocking alerts. Anchored at 700 for the semantic source.

| Stop | Hex     |
|------|---------|
| 50   | #FFFBEB |
| 100  | #FDEFC8 |
| 200  | #FAD88E |
| 300  | #F5BC50 |
| 400  | #E89A20 |
| 500  | #CC7A0A |
| 600  | #AA5E08 |
| 700  | #92400E |
| 800  | #7A2E08 |
| 900  | #5A1E04 |
| 950  | #3A1002 |

---

## Semantic layer

### Source tokens

Source tokens define the single resolved value for each functional state. All downstream tokens reference these using `var()` rather than restating primitive references. Light and dark mode resolution is handled here.

To update how a state appears throughout the system, update this layer only.

| Token                    | Light          | Dark           |
|--------------------------|----------------|----------------|
| --color-semantic-error   | error · 600    | error · 200    |
| --color-semantic-success | success · 700  | success · 200  |
| --color-semantic-warning | warning · 700  | warning · 300  |
| --color-semantic-info    | accent · 500   | accent · 300   |

Info reuses the accent ramp. No separate info primitive ramp is required.

### Dark feedback surface derivation

Dark feedback surfaces are derived by compositing the semantic source stop over neutral-900 at 12% opacity.

`dark-surface = neutral-900 + semantic-source-stop at 12% opacity`

RGB calculation: `each channel = round(base + (source - base) × 0.12)` where `base = neutral-900 = rgb(24, 24, 24)`.

| Token                        | Source stop             | Source RGB        | Derived dark value |
|------------------------------|-------------------------|-------------------|--------------------|
| --color-surface-error dark   | error · 600 (#C0251D)   | rgb(192, 37, 29)  | #2C1A19            |
| --color-surface-warning dark | warning · 700 (#92400E) | rgb(146, 64, 14)  | #271D17            |
| --color-surface-success dark | success · 700 (#166534) | rgb(22, 101, 52)  | #18211B            |
| --color-surface-info dark    | accent · 500 (#1A6FFF)  | rgb(26, 111, 255) | #182234            |

The same derivation applies to `--color-feedback-[state]-surface` dark values.

The 12% value: above 15%, the surface begins to compete with node-level colour; below 8%, the tint falls below perceptual threshold at typical viewing distances. 12% is the midpoint of the viable range.

---

## Component tokens

### Surface

Surface tokens use an elevation metaphor: overlay floats above all other surfaces, raised floats above page, base is the page, sunken recedes below.

| Token                   | Light            | Dark          |
|-------------------------|------------------|---------------|
| --color-surface-overlay | neutral · 0      | neutral · 800 |
| --color-surface-raised  | neutral · 50     | neutral · 850 |
| --color-surface-base    | neutral · 100    | neutral · 900 |
| --color-surface-sunken  | neutral · 200    | neutral · 950 |
| --color-surface-inverse | neutral · 900    | neutral · 200 |
| --color-surface-error   | error · 50       | derived       |
| --color-surface-warning | warning · 50     | derived       |
| --color-surface-success | success · 50     | derived       |
| --color-surface-info    | accent · 50      | derived       |

"Derived" indicates the dark feedback surface formula applies.

### Text

#### Hierarchy

| Token                | Light         | Dark          |
|----------------------|---------------|---------------|
| --color-text-strong  | neutral · 900 | neutral · 50  |
| --color-text-default | neutral · 800 | neutral · 200 |
| --color-text-subtle  | neutral · 600 | neutral · 500 |
| --color-text-faint   | neutral · 500 | neutral · 600 |

#### Functional states

| Token                    | Light         | Dark          |
|--------------------------|---------------|---------------|
| --color-text-disabled    | neutral · 400 | neutral · 700 |
| --color-text-placeholder | neutral · 450 | neutral · 700 |

#### Inverse

| Token                  | Light         | Dark          |
|------------------------|---------------|---------------|
| --color-text-inverse   | neutral · 100 | neutral · 900 |
| --color-text-on-accent | neutral · 0   | neutral · 0   |

#### Semantic

Values reference the semantic source layer.

| Token                | Value                       |
|----------------------|-----------------------------|
| --color-text-link    | accent · 500 / accent · 300 |
| --color-text-error   | semantic · error            |
| --color-text-success | semantic · success          |
| --color-text-warning | semantic · warning          |
| --color-text-info    | semantic · info             |

### Border

#### Weight scale

| Token                  | Light         | Dark          |
|------------------------|---------------|---------------|
| --color-border-strong  | neutral · 600 | neutral · 500 |
| --color-border-default | neutral · 300 | neutral · 800 |
| --color-border-subtle  | neutral · 200 | neutral · 825 |

#### Functional

| Token                  | Light         | Dark          |
|------------------------|---------------|---------------|
| --color-border-focus   | accent · 500  | accent · 500  |
| --color-border-inverse | neutral · 800 | neutral · 300 |

#### Semantic

| Token                  | Value              |
|------------------------|--------------------|
| --color-border-error   | semantic · error   |
| --color-border-success | semantic · success |
| --color-border-warning | semantic · warning |
| --color-border-info    | semantic · info    |

### Icon

Icon tokens mirror the text hierarchy directly. An icon paired with a text token uses the corresponding icon token: icon-strong pairs with text-strong, icon-subtle pairs with text-subtle.

#### Hierarchy

| Token                | Light         | Dark          |
|----------------------|---------------|---------------|
| --color-icon-strong  | neutral · 900 | neutral · 50  |
| --color-icon-default | neutral · 800 | neutral · 200 |
| --color-icon-subtle  | neutral · 600 | neutral · 500 |
| --color-icon-faint   | neutral · 500 | neutral · 600 |

#### Functional states

| Token                 | Light         | Dark          |
|-----------------------|---------------|---------------|
| --color-icon-disabled | neutral · 400 | neutral · 700 |

#### Inverse

| Token                  | Light         | Dark          |
|------------------------|---------------|---------------|
| --color-icon-inverse   | neutral · 100 | neutral · 900 |
| --color-icon-on-accent | neutral · 0   | neutral · 0   |

#### Semantic

| Token                | Value                       |
|----------------------|-----------------------------|
| --color-icon-link    | accent · 500 / accent · 300 |
| --color-icon-error   | semantic · error            |
| --color-icon-success | semantic · success          |
| --color-icon-warning | semantic · warning          |
| --color-icon-info    | semantic · info             |

### Action

#### Primary (filled)

| Token                         | Light        | Dark         |
|-------------------------------|--------------|--------------|
| --color-action-primary        | accent · 500 | accent · 500 |
| --color-action-primary-hover  | accent · 600 | accent · 400 |
| --color-action-primary-active | accent · 700 | accent · 300 |
| --color-action-primary-text   | neutral · 0  | neutral · 0  |

#### Secondary (outlined)

| Token                                  | Light         | Dark          |
|----------------------------------------|---------------|---------------|
| --color-action-secondary               | transparent   | transparent   |
| --color-action-secondary-hover         | neutral · 100 | neutral · 850 |
| --color-action-secondary-active        | neutral · 200 | neutral · 825 |
| --color-action-secondary-border        | neutral · 300 | neutral · 800 |
| --color-action-secondary-border-hover  | neutral · 500 | neutral · 500 |
| --color-action-secondary-border-active | neutral · 800 | neutral · 200 |
| --color-action-secondary-text          | neutral · 900 | neutral · 200 |

#### Ghost

| Token                       | Light         | Dark          |
|-----------------------------|---------------|---------------|
| --color-action-ghost        | transparent   | transparent   |
| --color-action-ghost-hover  | neutral · 100 | neutral · 850 |
| --color-action-ghost-active | neutral · 200 | neutral · 825 |
| --color-action-ghost-text   | neutral · 900 | neutral · 200 |

#### Destructive

| Token                             | Light       | Dark        |
|-----------------------------------|-------------|-------------|
| --color-action-destructive        | error · 600 | error · 600 |
| --color-action-destructive-hover  | error · 700 | error · 400 |
| --color-action-destructive-active | error · 800 | error · 200 |
| --color-action-destructive-text   | neutral · 0 | neutral · 0 |

#### Disabled

| Token                        | Light         | Dark          |
|------------------------------|---------------|---------------|
| --color-action-disabled      | neutral · 200 | neutral · 825 |
| --color-action-disabled-text | neutral · 500 | neutral · 700 |

### Feedback

Surfaces use the dark feedback surface derivation formula for dark values. Text, border, and icon tokens reference the semantic source layer; "inherits" denotes the source token carries its own dark value.

#### Error

| Token                          | Light            | Dark     |
|--------------------------------|------------------|----------|
| --color-feedback-error-surface | error · 50       | derived  |
| --color-feedback-error-text    | semantic · error | inherits |
| --color-feedback-error-border  | semantic · error | inherits |
| --color-feedback-error-icon    | semantic · error | inherits |

#### Warning

| Token                            | Light              | Dark     |
|----------------------------------|--------------------|----------|
| --color-feedback-warning-surface | warning · 50       | derived  |
| --color-feedback-warning-text    | semantic · warning | inherits |
| --color-feedback-warning-border  | semantic · warning | inherits |
| --color-feedback-warning-icon    | semantic · warning | inherits |

#### Success

| Token                            | Light              | Dark     |
|----------------------------------|--------------------|----------|
| --color-feedback-success-surface | success · 50       | derived  |
| --color-feedback-success-text    | semantic · success | inherits |
| --color-feedback-success-border  | semantic · success | inherits |
| --color-feedback-success-icon    | semantic · success | inherits |

#### Info

| Token                         | Light           | Dark     |
|-------------------------------|-----------------|----------|
| --color-feedback-info-surface | accent · 50     | derived  |
| --color-feedback-info-text    | semantic · info | inherits |
| --color-feedback-info-border  | semantic · info | inherits |
| --color-feedback-info-icon    | semantic · info | inherits |