# Civil Engineering Toolkit

**Developer:** Mashal Khan  
**Repository:** https://github.com/mashal-web/Repository_01  
**Status:** Phase 2 — educational engineering calculators

A modular, dependency-free Python toolkit. Calculation modules are independent of the CLI and can be reused by other interfaces.

## Implemented modules

- **Concrete:** rectangular slab, beam and column volumes; optional user-selected allowance.
- **Materials:** rectangular wall brick count, custom brick dimensions and mortar joints, wastage, mortar volume, cement and sand estimates from configurable cement:sand volume ratios.
- **Steel:** approximate theoretical reinforcing-bar weight using d²/162 × L; individual and multiple bar sizes/counts.
- **Surveying:** slope-distance components, coordinate distance, quadrant bearing/azimuth conversion, and height-of-instrument leveling.
- **Engineering mathematics:** linear and quadratic equations, matrix addition/multiplication/inversion, trigonometry, percentages, ratios and selected engineering unit conversions.
- **Soil mechanics:** water content, void ratio, porosity, degree of saturation, bulk/dry unit weight and phase relationships.

## Requirements and installation

Python 3.11 or newer. No runtime dependencies; pytest is used for development tests.

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m pytest
```

## CLI examples

Concrete dimensions are metres:

```bash
civil-toolkit slab --length 5 --width 4 --thickness 0.15 --allowance 5
civil-toolkit beam --length 6 --width 0.3 --depth 0.5
civil-toolkit column --height 3 --width 0.3 --depth 0.3
```

Materials: wall dimensions in metres; brick and joint dimensions in millimetres:

```bash
civil-toolkit brickwork --length 4 --height 3 --thickness 0.1 --wastage 5 --cement-parts 1 --sand-parts 6
```

Steel: diameter in mm, length in metres:

```bash
civil-toolkit steel --diameter 12 --length 12 --count 5
```

Surveying: angles in degrees; azimuth clockwise from north:

```bash
civil-toolkit survey-horizontal --slope-distance 10 --angle 30
civil-toolkit survey-coordinate --easting1 0 --northing1 0 --easting2 3 --northing2 4
civil-toolkit survey-bearing --ns N --angle 30 --ew W
civil-toolkit survey-level --rl 100 --bs 1.5 --fs 1.2
```

Mathematics:

```bash
civil-toolkit math-linear --a 2 --b -6
civil-toolkit math-quadratic --a 1 --b -5 --c 6
civil-toolkit math-trig --value 30 --function sin --unit degrees
civil-toolkit math-convert --value 2 --from-unit MPa --to-unit kPa
```

Soil mechanics:

```bash
civil-toolkit soil-water --water-mass 20 --dry-soil-mass 100
civil-toolkit soil-phase --gs 2.65 --void-ratio 0.65 --saturation 50
```

Use civil-toolkit --help for all commands.

## Units, validation and limitations

- Numeric inputs must be finite. Booleans and numeric strings are not accepted by calculation functions.
- Physical dimensions, masses, volumes and mix components are checked for valid signs and non-zero denominators.
- Survey angles use degrees. Azimuth is [0, 360), clockwise from north; quadrant bearings use N/S, 0–90°, E/W.
- Steel output is approximate theoretical weight, not a bar-bending schedule or procurement weight.
- Matrix inversion rejects singular matrices. Tangent rejects angles where it is undefined.
- CLI validation failures are reported through argparse and exit with status 2.

Materials outputs are preliminary theoretical estimates. The masonry model assumes a rectangular wall and uniform joints, uses modular brick dimensions (brick plus joint) for count, and estimates mortar from wall volume less theoretical brick solids. Defaults of 1.33 dry-volume factor, cement bulk density 1440 kg/m³, 50 kg bag mass, and 1:6 cement:sand ratio are assumptions, not prescribed values. Bond, openings, corners, workmanship, moisture, sand bulking, compaction and supplier bag sizes can change actual quantities.

Steel estimates exclude rolling tolerances, coatings, couplers, bends, laps, cutting waste and grade. Surveying functions are elementary planar calculations and do not apply curvature/refraction, instrument corrections, traverse adjustment, datum transformations or geodetic projections. Engineering mathematics uses floating-point arithmetic and is intended for educational calculations, not high-precision numerical solvers. Soil relationships are idealized phase calculations and do not classify soil or determine bearing capacity, settlement, permeability or design parameters.

This toolkit is educational and supports preliminary calculations only. It is not a structural design system, code-compliance checker, mix-design tool, laboratory interpretation system or substitute for qualified engineering review and project specifications.

## Project structure

```text
src/civil_toolkit/
  calculators/   concrete, materials, steel, surveying, mathematics, soil mechanics
  cli/           command-line interface
  core/          shared validation and unit conversions
  main.py        application entry point
tests/           automated tests
docs/            formulas and assumptions
```

## License

MIT
