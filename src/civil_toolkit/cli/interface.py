"""Command-line interface for Phase 1 concrete quantity calculations."""

import argparse

from civil_toolkit.calculators.concrete import (
    beam_volume,
    column_volume,
    slab_volume,
    volume_with_allowance,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for the implemented concrete calculators."""
    parser = argparse.ArgumentParser(
        prog="civil-toolkit",
        description="Civil Engineering Toolkit — student quantity calculations.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name, help_text, third_dimension in (
        ("slab", "Calculate rectangular slab volume.", "thickness"),
        ("beam", "Calculate rectangular beam volume.", "depth"),
        ("column", "Calculate rectangular column volume.", "depth"),
    ):
        command = subparsers.add_parser(name, help=help_text)
        is_column = name == "column"
        command.add_argument(
            "--height" if is_column else "--length",
            dest="height" if is_column else "length",
            type=float,
            required=True,
            help="Height or length in metres.",
        )
        command.add_argument("--width", type=float, required=True, help="Width in metres.")
        command.add_argument(
            f"--{third_dimension}",
            type=float,
            required=True,
            help=f"{third_dimension.capitalize()} in metres.",
        )
        command.add_argument(
            "--allowance",
            type=float,
            default=0.0,
            help="Optional percentage allowance (default: 0).",
        )
    return parser


def run_cli(argv: list[str] | None = None) -> int:
    """Run the CLI; invalid physical values are reported without tracebacks."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "slab":
            geometric = slab_volume(args.length, args.width, args.thickness)
        elif args.command == "beam":
            geometric = beam_volume(args.length, args.width, args.depth)
        else:
            geometric = column_volume(args.height, args.width, args.depth)
        estimated = volume_with_allowance(geometric, args.allowance)
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))

    print(f"Geometric concrete volume: {geometric:.3f} m³")
    print(f"Volume including allowance: {estimated:.3f} m³")
    return 0
