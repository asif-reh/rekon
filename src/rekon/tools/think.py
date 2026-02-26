"""Think tool — reasoning scratchpad for the agent."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class ThinkTool(BaseTool):
    """A reasoning scratchpad for the agent to think without acting.

    The agent uses this to plan, reason, and organize thoughts before
    making decisions. Does nothing — just returns the thought.
    """

    @property
    def name(self) -> str:
        return "think"

    @property
    def description(self) -> str:
        return (
            "Use this tool to think through a problem step by step before acting. "
            "Your thoughts are recorded but no action is taken."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "thought": {
                    "type": "string",
                    "description": "Your reasoning, plan, or analysis.",
                },
            },
            "required": ["thought"],
        }

    async def execute(self, **kwargs: Any) -> str:
        """Record a thought. No side effects."""
        # TODO: Implement in Step 5
        raise NotImplementedError("ThinkTool coming in Step 5")
