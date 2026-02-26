"""Rekon CLI — Command-line interface for the Rekon coding agent."""

import click

from rekon import __version__


@click.group()
@click.version_option(version=__version__, prog_name="rekon")
def cli() -> None:
    """Rekon — AI coding agent with persistent memory and intelligent checkpoints."""


@cli.command()
def chat() -> None:
    """Start an interactive coding session with Rekon."""
    click.echo("🔍 Rekon v{} — Starting interactive session...".format(__version__))
    click.echo("   Type your prompt and press Enter. Ctrl+C to exit.")
    click.echo("   (Agent loop not yet implemented — coming in Step 3)")


@cli.command()
def version() -> None:
    """Show Rekon version."""
    click.echo(f"rekon {__version__}")


@cli.command()
def init() -> None:
    """Create a REKON.md config file in the current directory."""
    click.echo("📝 Creating REKON.md template... (coming in Step 7)")


@cli.group()
def memory() -> None:
    """Manage Rekon's persistent memory."""


@memory.command()
def show() -> None:
    """Show memory contents."""
    click.echo("🧠 Memory viewer (coming in Step 9-11)")


@memory.command()
def search() -> None:
    """Search memory."""
    click.echo("🔎 Memory search (coming in Step 10)")


@memory.command()
def sessions() -> None:
    """List past sessions."""
    click.echo("📋 Session history (coming in Step 11)")


@memory.command()
def clear() -> None:
    """Clear all memory."""
    click.echo("🗑️  Memory clear (coming in Step 9)")


@cli.group()
def pitstop() -> None:
    """Manage PitStop checkpoints."""


@pitstop.command(name="list")
def pitstop_list() -> None:
    """List all checkpoints."""
    click.echo("🏁 Checkpoint list (coming in Step 12)")


@pitstop.command()
@click.argument("checkpoint_id")
def rollback(checkpoint_id: str) -> None:
    """Rollback to a checkpoint."""
    click.echo(f"⏪ Rolling back to {checkpoint_id}... (coming in Step 13)")


@cli.command()
def serve() -> None:
    """Start Rekon as an MCP server."""
    click.echo("🌐 MCP server mode (coming in Step 15)")
