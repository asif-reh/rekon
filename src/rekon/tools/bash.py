"""Bash tool — safe shell command execution."""

from __future__ import annotations

from typing import Any

from rekon.tools.base import BaseTool


class BashTool(BaseTool):
    """Execute shell commands safely with timeout and output capture.

    Uses asyncio.create_subprocess_exec (NOT shell=True) for security.
    Read-only commands (ls, cat, grep) don't need permission.
    Write commands require user approval.
    """

    # Commands that are considered read-only (no permission needed)
    READ_ONLY_PREFIXES = ("ls", "cat", "echo", "grep", "find", "which", "pwd", "env", "head", "tail", "wc")

    @property
    def name(self) -> str:
        return "bash"

    @property
    def description(self) -> str:
        return (
            "Execute a shell command and return its output. "
            "Use for running tests, checking versions, inspecting system state, etc."
        )

    @property
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The shell command to execute.",
                },
                "timeout": {
                    "type": "integer",
                    "description": "Timeout in seconds. Default is 30.",
                },
            },
            "required": ["command"],
        }

    @property
    def requires_permission(self) -> bool:
        return True  # Permission checked dynamically based on command

    async def execute(self, **kwargs: Any) -> str:
        """Execute a shell command."""
        # TODO: Implement in Step 5
        raise NotImplementedError("BashTool coming in Step 5")
