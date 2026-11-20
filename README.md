# Civil Engineering Toolkit

**Developer:** Mashal Khan  
**Repository:** [mashal-web/Repository_01](https://github.com/mashal-web/Repository_01)  
**Status:** Phase 1.1 complete — foundational concrete quantity tools

A modular Python toolkit for civil engineering students and beginners. The Phase 1 calculation engine is shared by the command-line interface and is structured for future interfaces.

## Implemented features

- Rectangular slab, beam, and column geometric concrete-volume calculations.
- Optional user-defined concrete volume allowance.
- Validated conversions: mm to m, cm to m, m to mm, and m³ to litres.
- CLI subcommands for slab, beam, and column calculations.
- Shared finite-number and physical-quantity validation.
- Automated tests for calculations, conversions, validation, and CLI behavior.

## Planned features — not implemented

- Construction materials and steel calculators.
- Surveying calculators.
- Engineering mathematics and soil mechanics modules.
- Streamlit web interface and visualizations.

## Requirements and installation

- Python 3.11 or newer.

```bash
python -m venv .venv
```

Activate the virtual environment, then install the package and test dependencies:

```bash
python -m pip install -e ".[dev]"
```

## CLI examples

```bash
civil-toolkit slab --length 5 --width 4 --thickness 0.15 --allowance 5
civil-toolkit beam --length 6 --width 0.3 --depth 0.5
civil-toolkit column --height 3 --width 0.3 --depth 0.3
```

Dimensions are in metres. Volumes are reported in cubic metres (m³). The optional allowance is a percentage and defaults to zero.

## Validation rules

- Inputs must be Python numeric values; booleans and numeric strings are not accepted by the calculation API.
- NaN and positive/negative infinity are rejected.
- Concrete element dimensions must be strictly greater than zero.
- Unit conversions accept zero but reject negative lengths or volumes.
- Concrete volume and allowance inputs accept zero but reject negative values.
- Arithmetic results that overflow to a non-finite value are rejected.
- The CLI reports invalid arguments through standard argument-parser errors and exits with status 2 rather than exposing a traceback.

## Run tests

```bash
python -m pytest
```

## Project structure

```text
src/civil_toolkit/
  calculators/   Concrete calculation engine
  cli/           Command-line interface
  core/          Shared validation and unit conversions
  main.py        Application entry point
tests/           Automated tests
docs/            Formula and assumption documentation
```

## Engineering disclaimer

This toolkit is educational and supports preliminary geometric quantity calculations only. It does not perform structural design, reinforcement design, mix design, durability assessment, or code-compliance checks. Outputs must not be treated as construction-ready design values. Confirm project-specific requirements with qualified professionals and applicable standards.

## License

MIT
