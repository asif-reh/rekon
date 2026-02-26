"""Context window management — token counting, auto-compaction, summarization.

Tracks token usage across the conversation and automatically compacts
older turns when approaching the context window limit (80% threshold).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ContextManager:
    """Manages the context window for the Rekon agent.

    Tracks token usage and triggers auto-compaction when the
    conversation approaches 80% of the model's context window.

    Compaction strategy:
        - Keep last 5 turns verbatim
        - Summarize all older turns into a compact summary
        - Preserve file paths, function names, and key decisions
    """

    max_tokens: int = 200_000
    compact_threshold: float = 0.80
    messages: list[dict[str, Any]] = field(default_factory=list)
    _total_tokens: int = 0

    def token_count(self) -> int:
        """Return current token usage."""
        # TODO: Implement in Step 7
        return self._total_tokens

    def usage_percentage(self) -> float:
        """Return context usage as a percentage (0.0 to 1.0)."""
        return self._total_tokens / self.max_tokens

    def should_compact(self) -> bool:
        """Check if compaction should be triggered."""
        return self.usage_percentage() >= self.compact_threshold

    async def compact(self) -> None:
        """Compact older conversation turns into a summary."""
        # TODO: Implement in Step 7

    def usage_display(self) -> str:
        """Return a formatted usage string for the UI."""
        pct = self.usage_percentage() * 100
        return f"Context: {self._total_tokens:,}/{self.max_tokens:,} ({pct:.0f}%)"
