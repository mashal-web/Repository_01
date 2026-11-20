"""Command-line interface for the initial concrete calculator."""

import argparse

from civil_toolkit.calculators.concrete import slab_volume, volume_with_allowance


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="civil-toolkit",
        description="Civil Engineering Toolkit — student quantity calculations.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    slab = subparsers.add_parser("slab", help="Calculate rectangular slab volume.")
    slab.add_argument("--length", type=float, required=True, help="Length in metres.")
    slab.add_argument("--width", type=float, required=True, help="Width in metres.")
    slab.add_argument("--thickness", type=float, required=True, help="Thickness in metres.")
    slab.add_argument(
        "--allowance",
        type=float,
        default=0.0,
        help="Optional percentage allowance (default: 0).",
    )
    return parser


def run_cli(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "slab":
            geometric = slab_volume(args.length, args.width, args.thickness)
            estimated = volume_with_allowance(geometric, args.allowance)
            print(f"Geometric concrete volume: {geometric:.3f} m³")
            print(f"Volume including allowance: {estimated:.3f} m³")
            return 0
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))

    return 0
