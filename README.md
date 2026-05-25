# HM-AI-Agent

Study and development repo for building a personal AI agent powered by MCP
integrations.

## Project Shape

The repo is organized around clean architecture boundaries, with MCP treated as
a first-class infrastructure concern:

```text
HM-AI-Agent/
|-- src/
|   |-- domain/              # Core business rules and models
|   |-- application/         # Use cases and orchestration
|   |-- infrastructure/      # External systems and adapters
|   |   |-- ai/              # Model providers and LLM clients
|   |   |-- github/          # GitHub adapters
|   |   |-- mcp/             # MCP client, tools, and server adapters
|   |   `-- persistence/     # Storage, memory, and state adapters
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

## Next Step

Choose the implementation stack before adding package metadata:

- Python: add `pyproject.toml` and package code under `src/`.
- TypeScript/Node: add `package.json` and keep app code under `src/`.
