"""Application entry point."""

from civil_toolkit.cli.interface import run_cli


def main() -> int:
    return run_cli()


if __name__ == "__main__":
    raise SystemExit(main())
