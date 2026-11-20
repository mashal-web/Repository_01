# Implemented Phase 1 formulas

All concrete dimensions are entered in metres (m), and geometric volumes are returned in cubic metres (m³).

## Rectangular slab, beam, and column volume

\[
V = L \times B \times H
\]

Where:
- \(V\) = geometric volume (m³)
- \(L\) = element length or column height (m)
- \(B\) = width (m)
- \(H\) = slab thickness or beam/column depth (m)

The implementation models each element as a rectangular prism. It does not subtract openings or account for intersections, haunches, non-rectangular geometry, or reinforcement displacement.

## Optional volume allowance

\[
V_e = V \left(1 + \frac{p}{100}\right)
\]

Where:
- \(V_e\) = volume after allowance (m³)
- \(V\) = geometric volume (m³)
- \(p\) = user-selected allowance (percent)

The percentage is user-supplied. It is not a prescribed or universally applicable construction factor.

## Implemented unit conversions

| Conversion | Formula |
|---|---|
| Millimetres to metres | \(m = mm / 1000\) |
| Centimetres to metres | \(m = cm / 100\) |
| Metres to millimetres | \(mm = m \times 1000\) |
| Cubic metres to litres | \(L = m^3 \times 1000\) |

## Validation and numerical behavior

Calculation inputs must be finite numeric values. Concrete dimensions must be greater than zero. Unit-conversion inputs may be zero but cannot be negative. The volume and allowance inputs may be zero but cannot be negative. Non-finite arithmetic results are rejected.

## Scope

These functions calculate geometry and an optional quantity allowance only. They do not determine structural adequacy, reinforcement, mix proportions, durability, or compliance with any engineering standard.
