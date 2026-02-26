"""List directory tool — tree-formatted directory listing."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class ListDirectoryTool(BaseTool):
    """List files and directories in a tree format.

    Filters out common noise directories (.git, __pycache__, node_modules, .venv).
    Shows file sizes and entry counts.
    """

    @property
    def name(self) -> str:
        return "list_directory"

    @property
    def description(self) -> str:
        return (
            "List files and directories in a tree format. "
            "Use this to understand project structure and find relevant files."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path to list (relative to project root). Defaults to '.'",
                },
                "max_depth": {
                    "type": "integer",
                    "description": "Maximum depth to recurse. Default is 2.",
                },
            },
            "required": [],
        }

    async def execute(self, **kwargs: Any) -> str:
        """List directory contents in tree format."""
        # TODO: Implement in Step 2
        raise NotImplementedError("ListDirectoryTool coming in Step 2")
