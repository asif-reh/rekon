"""Shared fixtures for Rekon tests."""

from __future__ import annotations

import pytest

from rekon.tools.registry import ToolRegistry


@pytest.fixture
def tool_registry() -> ToolRegistry:
    """Create an empty tool registry for testing."""
    return ToolRegistry()


@pytest.fixture
def tmp_project(tmp_path):
    """Create a temporary project directory with sample files."""
    # Create a basic project structure
    src = tmp_path / "src"
    src.mkdir()

    main = src / "main.py"
    main.write_text('def hello():\n    return "Hello, World!"\n')

    readme = tmp_path / "README.md"
    readme.write_text("# Test Project\nA test project for Rekon.\n")

    return tmp_path
