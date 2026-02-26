"""Write file tool — create or overwrite files with permission."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class WriteFileTool(BaseTool):
    """Create or overwrite a file. Requires user permission."""

    @property
    def name(self) -> str:
        return "write_file"

    @property
    def description(self) -> str:
        return "Create a new file or overwrite an existing file with the provided content."

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write.",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file.",
                },
            },
            "required": ["file_path", "content"],
        }

    @property
    def requires_permission(self) -> bool:
        return True

    async def execute(self, **kwargs: Any) -> str:
        """Write content to a file."""
        # TODO: Implement in Step 4
        raise NotImplementedError("WriteFileTool coming in Step 4")
