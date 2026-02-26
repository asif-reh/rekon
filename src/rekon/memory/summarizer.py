"""SessionSummarizer — extracts lasting facts from session events using LLM.

At session end, the LLM reads raw session events and extracts:
    - Key decisions and their reasoning
    - Project conventions discovered
    - Error patterns and their solutions
    - Architecture insights

This is meta-cognition — the agent learning from its own experience.
"""

from __future__ import annotations


class SessionSummarizer:
    """Summarizes sessions and extracts semantic facts using the LLM.

    Called on graceful shutdown (Ctrl+C or 'exit').
    """

    # TODO: Implement in Step 11
