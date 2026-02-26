"""Edit file tool — find-and-replace with diff preview."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class EditFileTool(BaseTool):
    """Edit a file using find-and-replace with diff preview. Requires user permission."""

    @property
    def name(self) -> str:
        return "edit_file"

    @property
    def description(self) -> str:
        return (
            "Edit a file by replacing a specific text section with new text. "
            "Shows a diff preview before applying. Use for precise code modifications."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to edit.",
                },
                "old_text": {
                    "type": "string",
                    "description": "Exact text to find and replace.",
                },
                "new_text": {
                    "type": "string",
                    "description": "Text to replace old_text with.",
                },
            },
            "required": ["file_path", "old_text", "new_text"],
        }

    @property
    def requires_permission(self) -> bool:
        return True

    async def execute(self, **kwargs: Any) -> str:
        """Edit file with find-and-replace."""
        # TODO: Implement in Step 4
        raise NotImplementedError("EditFileTool coming in Step 4")
