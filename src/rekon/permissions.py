"""Human-in-the-loop permission system.

Before any dangerous operation (file write, bash command, git commit),
the agent must get explicit user approval. Supports 'always allow'
for specific tools within a session.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PermissionManager:
    """Manages user approval for dangerous tool operations.

    Tools are classified as:
        - Safe (no permission needed): read_file, list_dir, search_files, think
        - Dangerous (permission required): write_file, edit_file, bash, git commit
    """

    always_allowed: set[str] = field(default_factory=set)

    async def request_permission(
        self,
        tool_name: str,
        description: str,
        details: str = "",
    ) -> bool:
        """Request user permission for a dangerous operation.

        Args:
            tool_name: Name of the tool requesting permission.
            description: What the tool wants to do.
            details: Additional context (file path, command, etc.).

        Returns:
            True if user approves, False if denied.
        """
        # TODO: Implement in Step 4
        raise NotImplementedError("Permission system coming in Step 4")
