"""Coder sub-agent — takes an implementation plan and writes code.

Runs in its own context window (isolated from main agent).
Tools: all 8 tools.
"""

from __future__ import annotations


class CoderAgent:
    """Implements code based on a plan and codebase context."""

    # TODO: Implement in Step 14
