"""Terminal UI — Rich-powered rendering for streaming, tools, and errors.

Provides professional terminal output with syntax highlighting,
markdown rendering, progress spinners, and colored indicators.
"""

from __future__ import annotations


class TerminalUI:
    """Rich-powered terminal UI for Rekon.

    Methods:
        render_streaming_text(delta) — real-time text output
        render_tool_call(name, params) — blue tool execution indicator
        render_tool_result(name, result) — syntax-highlighted results
        render_error(msg) — red error display
        render_markdown(text) — markdown rendering
    """

    # TODO: Implement in Step 6
