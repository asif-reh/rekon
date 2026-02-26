"""Git operations tool — status, diff, log, commit, branch, stash."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class GitOpsTool(BaseTool):
    """Git operations for version control interaction.

    Read operations (status, diff, log) don't need permission.
    Write operations (commit, stash) require user approval.
    """

    @property
    def name(self) -> str:
        return "git_ops"

    @property
    def description(self) -> str:
        return (
            "Perform git operations: status, diff, log, commit, branch, stash. "
            "Use for understanding changes, committing work, and managing branches."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "enum": ["status", "diff", "log", "commit", "branch", "stash"],
                    "description": "The git operation to perform.",
                },
                "args": {
                    "type": "string",
                    "description": "Additional arguments (e.g., commit message, branch name).",
                },
            },
            "required": ["operation"],
        }

    @property
    def requires_permission(self) -> bool:
        return True  # Permission checked dynamically based on operation

    async def execute(self, **kwargs: Any) -> str:
        """Execute a git operation."""
        # TODO: Implement in Step 5
        raise NotImplementedError("GitOpsTool coming in Step 5")
