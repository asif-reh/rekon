# 🔍 Rekon

**A production-grade CLI coding agent with persistent memory and intelligent checkpoints.**

Built from scratch in Python — no AI frameworks. Just the Anthropic SDK, clean architecture, and two features no other CLI agent has.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/code-asif/rekon/actions/workflows/ci.yml/badge.svg)](https://github.com/code-asif/rekon/actions)

## Features

### Core Agent
- **ReAct Pattern** — Reason → Act → Observe loop (same architecture as Claude Code, Codex, Gemini CLI)
- **8 Integrated Tools** — read_file, write_file, edit_file, bash, search_files, list_dir, git_ops, think
- **Real-Time Streaming** — Token-by-token output with Rich terminal UI
- **Context Management** — Auto-compaction at 80% token usage, REKON.md project config
- **Permission System** — Human-in-the-loop approval for all write operations

### 🧠 MemoryEngine (Killer Feature)
3-layer persistent memory that survives across sessions:
- **Episodic** — "What happened" (session events with timestamps)
- **Semantic** — "What we know" (extracted project knowledge)
- **Session Summaries** — Compressed narratives of past sessions

Powered by SQLite + FTS5 for sub-millisecond search. No external database needed.

### 🏁 PitStop (Novel Feature)
Intelligent checkpoints with rollback:
- Auto-checkpoints at natural breakpoints (plan complete, file complete, before destructive actions)
- Token budget alerts at 25%, 50%, 75% usage
- One-command rollback to any checkpoint — zero tokens wasted
- Confidence detection triggers checkpoints when the agent is uncertain

### Multi-Agent Orchestration
- **Researcher** — Explores codebase, returns architecture summary (read-only)
- **Coder** — Implements code from a plan (all tools)
- **Reviewer** — Reviews changes for bugs, style, tests (read-only + reasoning)

### MCP Protocol
- **Client** — Connect to external MCP servers (GitHub, databases, etc.)
- **Server** — Expose Rekon's tools to Claude Desktop, Cursor, and other MCP clients

## Quick Start

```bash
# Install from PyPI
pip install rekon

# Or install from source
git clone https://github.com/code-asif/rekon.git
cd rekon
pip install -e ".[dev]"

# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-key-here"

# Start coding
rekon chat
```

## Usage

```bash
# Interactive coding session
rekon chat

# Memory management
rekon memory show          # View memory contents
rekon memory search        # Search across memories
rekon memory sessions      # List past sessions

# Checkpoint management
rekon pitstop list         # List all checkpoints
rekon pitstop rollback ID  # Rollback to a checkpoint

# MCP server mode
rekon serve                # Expose tools via MCP

# Project config
rekon init                 # Create REKON.md template
```

## Architecture

```
rekon/
├── src/rekon/
│   ├── agent.py           # Core ReAct loop
│   ├── streaming.py       # Real-time streaming handler
│   ├── context.py         # Context window management
│   ├── permissions.py     # Human-in-the-loop approval
│   ├── config.py          # REKON.md + rekon.toml loader
│   ├── cli.py             # Click CLI
│   ├── tools/             # 8 integrated tools
│   │   ├── base.py        # BaseTool ABC
│   │   ├── registry.py    # Tool registry + dispatch
│   │   ├── read_file.py   # Read with line numbers
│   │   ├── write_file.py  # Create/overwrite (permission)
│   │   ├── edit_file.py   # Find-replace with diff (permission)
│   │   ├── bash.py        # Safe shell execution (permission)
│   │   ├── search_files.py # Ripgrep-powered search
│   │   ├── git_ops.py     # Git operations
│   │   └── think.py       # Reasoning scratchpad
│   ├── memory/            # MemoryEngine
│   │   ├── memory_store.py # SQLite + FTS5 database
│   │   ├── auto_capture.py # Event auto-capture hooks
│   │   └── summarizer.py  # LLM-powered fact extraction
│   ├── pitstop/           # PitStop checkpoints
│   │   ├── checkpoint.py  # Checkpoint save/restore
│   │   ├── rollback.py    # Git-stash rollback
│   │   └── progress.py    # Trigger detection
│   ├── agents/            # Sub-agent orchestration
│   │   ├── researcher.py  # Read-only codebase explorer
│   │   ├── coder.py       # Implementation agent
│   │   └── reviewer.py    # Code review agent
│   ├── mcp/               # MCP protocol
│   │   ├── client.py      # Connect to external servers
│   │   └── server.py      # Expose tools as MCP server
│   └── ui/                # Terminal UI
│       ├── terminal.py    # Rich rendering
│       └── themes.py      # Color themes
├── tests/                 # pytest + 80% coverage target
├── pyproject.toml         # PEP 621 packaging
├── Dockerfile             # Multi-stage Docker build
└── REKON.md               # Project config template
```

## Tech Stack

- **Python 3.11+** — async/await, type hints, dataclasses
- **Anthropic Claude API** — LLM backbone (anthropic SDK)
- **Rich** — Terminal UI with syntax highlighting
- **Click** — CLI framework
- **SQLite + FTS5** — Persistent memory (zero dependencies)
- **gitpython** — Programmatic git operations
- **MCP SDK** — Model Context Protocol client/server
- **pytest** — Testing with 80%+ coverage target
- **ruff + mypy** — Linting and type checking
- **GitHub Actions** — CI/CD pipeline

## License

MIT — see [LICENSE](LICENSE) for details.

## Author

**Asif** — MSc AI, Dublin City University
