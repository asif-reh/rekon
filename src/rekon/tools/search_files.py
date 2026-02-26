"""Search files tool — ripgrep-powered regex search across codebase."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class SearchFilesTool(BaseTool):
    """Search for patterns across the codebase using ripgrep.

    Falls back to Python re + os.walk if ripgrep is not installed.
    Returns file:line:match format, max 50 results.
    """

    @property
    def name(self) -> str:
        return "search_files"

    @property
    def description(self) -> str:
        return (
            "Search for a regex pattern across files in the codebase. "
            "Returns matching lines with file paths and line numbers."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string",
                    "description": "Regex pattern to search for.",
                },
                "path": {
                    "type": "string",
                    "description": "Directory to search in. Defaults to project root.",
                },
                "file_glob": {
                    "type": "string",
                    "description": "File pattern to filter (e.g., '*.py'). Optional.",
                },
            },
            "required": ["pattern"],
        }

    async def execute(self, **kwargs: Any) -> str:
        """Search for a pattern across files."""
        # TODO: Implement in Step 5
        raise NotImplementedError("SearchFilesTool coming in Step 5")
