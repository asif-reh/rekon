"""Entry point for `python -m rekon`."""

from rekon.cli import cli


def main() -> None:
    """Run the Rekon CLI."""
    cli()


if __name__ == "__main__":
    main()
