"""Real-time streaming handler for Anthropic API responses.

Wraps the async streaming API to process events (text deltas,
tool_use blocks, stop events) and yield structured events to the UI.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class StreamEventType(Enum):
    """Types of events emitted during streaming."""

    TEXT_DELTA = auto()
    TOOL_USE_START = auto()
    TOOL_USE_INPUT = auto()
    TOOL_USE_END = auto()
    MESSAGE_STOP = auto()
    ERROR = auto()


@dataclass
class StreamEvent:
    """A structured event from the streaming API."""

    type: StreamEventType
    data: str = ""
    tool_name: str = ""
    tool_id: str = ""
    tool_input: dict = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.tool_input is None:
            self.tool_input = {}


class StreamHandler:
    """Processes Anthropic streaming events and yields structured StreamEvents.

    Usage:
        async with client.messages.stream(...) as stream:
            handler = StreamHandler()
            async for event in handler.process(stream):
                ui.render(event)
    """

    # TODO: Implement in Step 6
