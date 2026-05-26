# HM-AI-Agent

Study and development repo for building a personal AI agent powered by MCP
integrations.

## Project Shape

The repo is organized around clean architecture boundaries, with MCP treated as
a first-class infrastructure concern:

```text
HM-AI-Agent/
|-- pyproject.toml
|-- main.py
|-- .vscode/
|   `-- mcp.json          # Local MCP client config for VS Code/Cursor
|-- src/
|   |-- domain/              # Core business rules and models
|   |-- application/         # Use cases and orchestration
|   |-- infrastructure/      # External systems and adapters
|   |   |-- ai/              # Model providers and LLM clients
|   |   |-- github/          # GitHub adapters
|   |   |-- mcp/             # MCP client, tools, and server adapters
|   |   |-- persistence/     # Storage, memory, and state adapters
|   |   `-- tools/           # Internal utility adapters and helpers
|   |-- interfaces/          # User and system entry points
|   |   |-- cli/
|   |   |-- http/
|   |   `-- webhooks/
|   |-- agents/              # Agent roles and behaviors
|   |   |-- planner/
|   |   |-- coder/
|   |   |-- reviewer/
|   |   `-- orchestrator/
|   |-- shared/              # Shared helpers, types, and constants
|   `-- config/              # Environment, logging, and runtime settings
|-- tests/
|   |-- unit/
|   |-- integration/
|   `-- e2e/
|-- scripts/
|-- docs/
|   `-- mcp-brasil.md
|-- data/
|-- .env.example
`-- README.md
```

## Layer Guidelines

- `domain` should stay pure: no network calls, SDK clients, databases, or MCP
  imports.
- `application` coordinates use cases and depends on domain abstractions.
- `infrastructure` implements adapters for external systems, including MCP,
  model providers, GitHub, and persistence.
- `interfaces` contains ways to run the agent, such as CLI commands, HTTP
  routes, or webhook handlers.
- `agents` contains planner, coder, reviewer, and orchestrator behavior.
- `shared` is for genuinely reusable utilities. Prefer keeping code near its
  owning layer until it is clearly shared.

## MCP Brasil

The project includes a Python integration for
[Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil), an external
MCP server for Brazilian public data sources.

Install project dependencies:

```bash
uv sync
```

The MCP server is registered in `src/infrastructure/mcp/servers.py` and can be
launched by MCP clients with:

```bash
uvx --from mcp-brasil python -m mcp_brasil.server
```

VS Code/Cursor can use the checked-in `.vscode/mcp.json`. Optional API keys and
dataset settings are documented in `.env.example` and `docs/mcp-brasil.md`.

## Next Step

Build the application-level MCP client that starts configured servers, discovers
their tools, and adapts tool calls into agent use cases.
