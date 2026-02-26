"""Base tool interface that all Rekon tools must implement."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """Abstract base class for all Rekon tools.

    Every tool must define:
        - name: unique identifier used in tool_use blocks
        - description: what the tool does (LLM reads this)
        - schema: JSON Schema for the tool's parameters
        - requires_permission: whether user approval is needed
        - execute(): the actual tool logic
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool name (e.g., 'read_file')."""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description of what this tool does."""
        ...

    @property
    @abstractmethod
    def schema(self) -> dict[str, Any]:
        """JSON Schema for the tool's input parameters."""
        ...

    @property
    def requires_permission(self) -> bool:
        """Whether this tool requires user permission before execution."""
        return False

    @abstractmethod
    async def execute(self, **kwargs: Any) -> str:
        """Execute the tool with the given parameters.

        Args:
            **kwargs: Tool-specific parameters matching the schema.

        Returns:
            String result to be sent back to the LLM.
        """
        ...

    def to_anthropic_tool(self) -> dict[str, Any]:
        """Convert to Anthropic API tool definition format."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.schema,
        }
