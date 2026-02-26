# REKON.md — Project Configuration

This file tells the Rekon agent about your project. Place it in your project root.

## Project Overview
Rekon is a CLI coding agent built from scratch in Python.

## Architecture
- `src/rekon/agent.py` — Core ReAct agent loop
- `src/rekon/tools/` — 8 integrated tools
- `src/rekon/memory/` — MemoryEngine (3-layer persistent memory)
- `src/rekon/pitstop/` — PitStop (intelligent checkpoints)

## Conventions
- All code uses type hints and dataclasses
- Async/await for all I/O operations
- Every module has a docstring explaining its purpose

## Test Commands
```bash
pytest                          # Run all tests
pytest --cov=rekon              # Run with coverage
ruff check src/                 # Lint
mypy src/rekon/                 # Type check
```

## Important Notes
- Never use `shell=True` in subprocess calls
- All write operations require user permission
- Memory database is at `~/.rekon/memory.db`
