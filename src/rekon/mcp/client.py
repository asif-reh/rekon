"""MCP client — connects to external MCP servers.

Discovers tools from external servers (GitHub, databases, Sentry)
and makes them available to the Rekon agent. Configured via rekon.toml.
"""

from __future__ import annotations


class MCPClient:
    """Connects to external MCP servers and discovers their tools."""

    # TODO: Implement in Step 15
