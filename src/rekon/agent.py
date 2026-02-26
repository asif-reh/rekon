"""Core ReAct agent loop — Reason → Act → Observe.

This is the heartbeat of Rekon. The agent receives a user message,
reasons about what to do, picks a tool, executes it, observes the
result, and loops until it has a final answer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentConfig:
    """Configuration for the Rekon agent."""

    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 8192
    max_iterations: int = 25
    system_prompt: str = ""


@dataclass
class Agent:
    """The core Rekon agent implementing the ReAct pattern.

    ReAct loop:
        1. Append user message to conversation
        2. Call LLM with messages + tool definitions
        3. If tool_use → execute tool → append result → loop
        4. If end_turn → return text response
        5. Safety: max_iterations guard
    """

    config: AgentConfig = field(default_factory=AgentConfig)
    messages: list[dict[str, Any]] = field(default_factory=list)

    async def run(self, user_message: str) -> str:
        """Run the agent loop for a user message.

        Args:
            user_message: The user's prompt.

        Returns:
            The agent's final text response.
        """
        # TODO: Implement in Step 3
        raise NotImplementedError("Agent loop coming in Step 3")

    def _build_system_prompt(self) -> str:
        """Build the system prompt with injected context."""
        # TODO: Implement in Step 3
        return ""

    def _format_tool_result(self, tool_name: str, result: str) -> dict[str, Any]:
        """Format a tool result for the messages array."""
        # TODO: Implement in Step 3
        return {}
