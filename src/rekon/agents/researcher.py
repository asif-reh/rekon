"""Researcher sub-agent — explores codebase and returns architecture summary.

Runs in its own context window (isolated from main agent).
Tools: read_file, search_files, list_dir only (read-only).
"""

from __future__ import annotations


class ResearcherAgent:
    """Explores a codebase and returns a structured architecture summary."""

    # TODO: Implement in Step 14
