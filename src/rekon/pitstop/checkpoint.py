"""Checkpoint system — save and restore agent state snapshots.

Uses git stash for file state and JSON serialization for conversation state.
Storage: .rekon/checkpoints/
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Checkpoint:
    """A snapshot of agent state at a point in time."""

    id: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    git_stash_ref: str = ""
    conversation_snapshot: str = ""  # JSON serialized messages
    files_changed: list[str] = field(default_factory=list)
    token_budget_used: int = 0
    description: str = ""


class CheckpointManager:
    """Manages creation, listing, and retrieval of checkpoints.

    Storage: .rekon/checkpoints/{id}.json
    """

    # TODO: Implement in Step 12
