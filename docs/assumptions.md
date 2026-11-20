# Assumptions and limitations

## General
- This toolkit is educational, not a substitute for project specifications, applicable standards, field measurements or qualified engineering judgment.
- Input validation does not establish engineering suitability. No calculator certifies structural adequacy, safety or code compliance.

## Concrete
- Slabs, beams and columns are rectangular prisms. Openings, intersections, haunches, embedded items and reinforcement displacement are not modeled.
- Dimensions are metres and volumes m³. Allowance is user-entered, not prescribed.

## Materials
- Brickwork is a rectangular wall with uniform mortar joints.
- Brick count divides wall volume by modular brick volume (brick dimensions plus one joint allowance in each direction). Bond pattern, cut bricks, corners, openings and coursing are not modeled.
- Wastage percentage applies to procurement count only; mortar is based on theoretical wall and brick solids.
- Mortar is wall volume less theoretical brick solid volume. Dry-volume factor converts wet mortar volume to assumed dry ingredient volume.
- Cement:sand ratio is by loose volume. Cement mass uses an assumed bulk density; bag count uses an assumed bag mass. Defaults 1:6, 1.33, 1440 kg/m³ and 50 kg are configurable estimates, not mandatory standards.
- Sand moisture/bulking, aggregate, water, admixtures, handling, workmanship, compaction, supply variation and local specifications are not modeled. Actual site quantities may differ.

## Steel
- d²/162 × L gives approximate theoretical mass for nominal diameter and length.
- Rolling tolerances, grade, coatings, couplers, bends, hooks, laps, cutting waste and bar scheduling are excluded. This is not a procurement or bar-bending schedule.

## Surveying
- Calculations are planar and use metres and degrees.
- Vertical angle is measured from horizontal; positive is upward and negative downward.
- Azimuth is clockwise from north in [0°,360°). Quadrant bearing is N/S, 0°–90°, E/W.
- Leveling uses the height-of-instrument method. Curvature/refraction, collimation, staff/instrument errors, datum and traverse/network adjustments are excluded.
- Coordinate distance assumes both points share a planar coordinate system and units.

## Engineering mathematics
- Matrix operations use floating-point arithmetic and are intended for small educational matrices. Ill-conditioned matrices can be inaccurate even when not exactly singular.
- Quadratic roots may be complex. A linear equation with zero leading coefficient is rejected because it has no unique solution.
- Tangent is rejected where undefined. Unit conversions are limited to supported units within one unit family.
- This is not symbolic algebra or a general-purpose numerical analysis package.

## Soil mechanics
- Phase relationships assume consistent mass/weight and volume units and idealized soil phases.
- Porosity requires void volume ≤ total volume; saturation requires water volume ≤ void volume; saturation is 0–100%.
- No soil classification, compaction interpretation, permeability, consolidation, shear strength, bearing capacity or settlement analysis is included.

## Intended use
Use results for learning and preliminary checking only. Confirm dimensions, material properties, construction methods, measurement conventions and applicable requirements before relying on quantities or calculations on site.
