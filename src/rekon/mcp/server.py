"""MCP server — exposes Rekon's tools via Model Context Protocol.

Other tools (Claude Desktop, Cursor) can connect to Rekon as an MCP
server and use its 8 tools + memory search. Stdio transport.
"""

from __future__ import annotations


class MCPServer:
    """Exposes Rekon's tools as an MCP server."""

    # TODO: Implement in Step 15
