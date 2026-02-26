"""Read file tool — reads file contents with line numbers."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class ReadFileTool(BaseTool):
    """Read the contents of a file with line numbers.

    Returns file content prefixed with line numbers for precise reference.
    Handles file-not-found, binary files, and encoding errors.
    """

    @property
    def name(self) -> str:
        return "read_file"

    @property
    def description(self) -> str:
        return (
            "Read the contents of a file. Returns the file content with line numbers. "
            "Use this to understand code, find bugs, or gather context."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read (relative to project root).",
                },
                "start_line": {
                    "type": "integer",
                    "description": "Starting line number (1-indexed). Optional.",
                },
                "end_line": {
                    "type": "integer",
                    "description": "Ending line number (inclusive). Optional.",
                },
            },
            "required": ["file_path"],
        }

    async def execute(self, **kwargs: Any) -> str:
        """Read file contents with line numbers."""
        # TODO: Implement in Step 2
        raise NotImplementedError("ReadFileTool coming in Step 2")
