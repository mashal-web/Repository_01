# Phase 1 formulas

## Rectangular concrete elements

For a rectangular slab, beam, or column:

\[
V = L \times B \times H
\]

Where:
- \(V\) = geometric volume (m³)
- \(L\) = length or height (m)
- \(B\) = width (m)
- \(H\) = thickness or depth (m)

The toolkit's slab, beam, and column functions use this geometric formula with dimensions supplied in metres.

## Optional volume allowance

\[
V_e = V \left(1 + \frac{p}{100}\right)
\]

Where:
- \(V_e\) = volume after allowance (m³)
- \(V\) = geometric volume (m³)
- \(p\) = user-selected allowance percentage

The allowance is an estimate entered by the user. It is not a universal prescribed value.

## Scope

These functions calculate geometry and an optional quantity allowance only. They do not determine structural adequacy, reinforcement, mix design, durability, or code compliance.
