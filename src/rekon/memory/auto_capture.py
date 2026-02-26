"""AutoCapture — automatically records agent actions into episodic memory.

Hooks into the agent's tool execution pipeline to capture file changes,
bash errors, test results, git commits, and search queries.
"""

from __future__ import annotations


class AutoCapture:
    """Automatically captures agent events into episodic memory.

    Hooks:
        on_tool_call() — fires after every tool execution
        on_agent_decision() — captures reasoning from think tool
    """

    # TODO: Implement in Step 11
