# Phase 1 assumptions and limitations

## Implemented behavior

- Slabs, beams, and columns are modeled as rectangular prisms.
- All concrete dimensions are entered in metres; calculated volumes are in cubic metres.
- The optional allowance is a user-selected percentage applied to the geometric volume.
- Unit conversions are limited to mm-to-m, cm-to-m, m-to-mm, and m³-to-litres.
- Numeric inputs must be finite. Booleans and numeric strings are not accepted by the calculation functions.
- Concrete dimensions must be strictly positive. Unit-conversion quantities, concrete volume, and allowance may be zero but cannot be negative.

## Explicit exclusions

- No automatic dry-volume factor, mix ratio, cement quantity, aggregate quantity, or water quantity is assumed.
- No deductions are made for openings, reinforcement, embedded items, or intersections.
- No structural analysis, member sizing, reinforcement design, mix design, durability evaluation, or code-compliance conclusion is produced.
- No construction tolerance or wastage percentage is prescribed; the allowance remains a user-entered estimate.

## Intended use

The toolkit is educational and intended for learning and preliminary geometric quantity calculations. Its outputs are not construction-ready design values and must not be used as the sole basis for procurement or construction. Verify project-specific geometry, specifications, quantities, and applicable standards with qualified professionals.
