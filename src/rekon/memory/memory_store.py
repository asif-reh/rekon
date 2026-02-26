"""MemoryStore — SQLite + FTS5 persistent memory database.

3-layer architecture:
    1. Episodic memories — "what happened" (session events with timestamps)
    2. Semantic facts — "what we know" (extracted project knowledge)
    3. Session summaries — compressed narrative of entire sessions
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class EpisodicMemory:
    """A specific event from a session."""

    id: int | None = None
    session_id: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    event_type: str = ""  # tool_call, decision, error, test_result
    content: str = ""
    tool_name: str = ""
    file_path: str = ""
    importance: int = 1  # 1-5 scale


@dataclass
class SemanticFact:
    """An extracted piece of project knowledge."""

    id: int | None = None
    category: str = ""  # architecture, convention, decision, pattern
    key: str = ""
    value: str = ""
    confidence: float = 0.0  # 0.0-1.0
    source_session: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    last_accessed: datetime = field(default_factory=datetime.now)


@dataclass
class SessionSummary:
    """Compressed summary of an entire session."""

    id: int | None = None
    session_id: str = ""
    project_path: str = ""
    summary: str = ""
    key_decisions: str = ""  # JSON list
    files_modified: str = ""  # JSON list
    started_at: datetime = field(default_factory=datetime.now)
    ended_at: datetime = field(default_factory=datetime.now)


class MemoryStore:
    """SQLite-backed persistent memory with FTS5 full-text search.

    Storage: ~/.rekon/memory.db
    """

    # TODO: Implement in Steps 9-11
