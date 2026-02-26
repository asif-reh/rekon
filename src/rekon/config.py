"""Configuration loader for REKON.md and rekon.toml.

Loads project-specific config (REKON.md) and tool settings (rekon.toml)
from the current working directory. Falls back to sensible defaults.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RekonConfig:
    """Loaded configuration for a Rekon session."""

    project_root: Path = field(default_factory=Path.cwd)
    project_context: str = ""  # Contents of REKON.md
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 8192
    bash_timeout: int = 30
    max_iterations: int = 25
    mcp_servers: list[dict[str, str]] = field(default_factory=list)


def load_config(project_root: Path | None = None) -> RekonConfig:
    """Load configuration from REKON.md and rekon.toml.

    Args:
        project_root: Path to the project root. Defaults to cwd.

    Returns:
        Loaded RekonConfig with project context and settings.
    """
    # TODO: Implement in Step 7
    root = project_root or Path.cwd()
    return RekonConfig(project_root=root)
