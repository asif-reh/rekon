"""Progress tracker — monitors tool calls and detects checkpoint triggers.

Auto-trigger rules:
    - After planning phase (before first file edit)
    - After each completed file's changes
    - Before destructive actions (delete, force push, drop)
    - At token budget thresholds (25%, 50%, 75%)
    - When confidence detection flags uncertainty
"""

from __future__ import annotations


class ProgressTracker:
    """Monitors agent progress and triggers checkpoints at natural breakpoints."""

    # TODO: Implement in Step 13
