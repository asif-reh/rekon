"""Rollback system — restore agent to a previous checkpoint.

Pops git stash, restores conversation state, and continues
the agent loop from the checkpoint point.
"""

from __future__ import annotations


class RollbackManager:
    """Handles rollback to previous checkpoints.

    rollback_to() — restore file state + conversation state
    discard_after() — remove checkpoints after a given one
    """

    # TODO: Implement in Step 13
