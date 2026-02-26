"""Reviewer sub-agent — reviews code changes for bugs, style, and tests.

Runs in its own context window (isolated from main agent).
Tools: read_file, search_files, list_dir, think (read-only + reasoning).
"""

from __future__ import annotations


class ReviewerAgent:
    """Reviews code changes and returns structured feedback."""

    # TODO: Implement in Step 14
