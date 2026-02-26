"""Tool registry — manages tool registration, lookup, and dispatch."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class ToolRegistry:
    """Registry for managing Rekon tools.

    Handles registration, lookup by name, tool definition generation
    (for the Anthropic API), and execution dispatch.
    """

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """Register a tool in the registry."""
        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool:
        """Look up a tool by name.

        Raises:
            KeyError: If tool not found.
        """
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not found. Available: {list(self._tools.keys())}")
        return self._tools[name]

    def get_tool_definitions(self) -> list[dict[str, Any]]:
        """Return Anthropic-format tool definitions for all registered tools."""
        return [tool.to_anthropic_tool() for tool in self._tools.values()]

    async def execute(self, name: str, **kwargs: Any) -> str:
        """Dispatch execution to the named tool.

        Args:
            name: Tool name to execute.
            **kwargs: Parameters to pass to the tool.

        Returns:
            Tool execution result as a string.
        """
        tool = self.get(name)
        return await tool.execute(**kwargs)

    @property
    def tools(self) -> dict[str, BaseTool]:
        """All registered tools."""
        return dict(self._tools)

    def __len__(self) -> int:
        return len(self._tools)

    def __contains__(self, name: str) -> bool:
        return name in self._tools
