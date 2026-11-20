# Civil Engineering Toolkit

**Developer:** Mashal Khan  
**Repository:** [mashal-web/Repository_01](https://github.com/mashal-web/Repository_01)  
**Status:** Phase 1 — foundation in progress

A modular Python toolkit for civil engineering students and beginners. The calculation engine is designed to be reusable from both a command-line interface and a future web interface.

## Current Phase 1 features

- Rectangular slab, beam, and column geometric volume calculations.
- Optional user-defined concrete volume allowance.
- Basic length and volume unit conversions.
- Command-line slab calculator.
- Input validation and automated tests.

## Requirements

- Python 3.11 or newer.

## Setup

```bash
python -m venv .venv
```

Activate the environment, then install the package and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## CLI example

```bash
civil-toolkit slab --length 5 --width 4 --thickness 0.15 --allowance 5
```

Expected values:
- Geometric volume: 3.000 m³
- Volume including 5% allowance: 3.150 m³

## Run tests

```bash
python -m pytest
```

## Project structure

```text
src/civil_toolkit/
  calculators/   Engineering calculation modules
  cli/           Command-line interface
  core/          Shared validation and unit utilities
  main.py        Application entry point
tests/           Automated tests
docs/            Formula and assumption documentation
```

## Planned modules

Concrete, construction materials, steel, surveying, mathematics, and soil mechanics. A Streamlit web interface is planned after the calculation modules and tests are established.

## Engineering disclaimer

This is an educational toolkit for learning and preliminary calculations. It is not a substitute for engineering judgment, project specifications, applicable standards, or review by a qualified professional. Do not use it as the sole basis for construction or structural design decisions.

## License

MIT
