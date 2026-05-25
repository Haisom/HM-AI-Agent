# Architecture

This project uses a layered structure so agent behavior, use cases, external
services, and entry points can evolve independently.

## Dependency Direction

```text
interfaces -> application -> domain
agents     -> application -> domain
infrastructure -> application/domain abstractions
```

The `domain` layer should not import from any other project layer.

## MCP Placement

MCP belongs in `src/infrastructure/mcp` because it connects the agent to
external tools and servers. Application use cases should talk to MCP through
small interfaces or service abstractions rather than importing SDK clients
directly.

Typical MCP responsibilities:

- Load MCP server configuration.
- Start or connect to MCP servers.
- Discover tools and resources.
- Adapt MCP tool calls into application-level services.
- Normalize MCP errors and responses.

## Agent Roles

- `planner`: breaks user goals into steps.
- `coder`: applies code changes or creates artifacts.
- `reviewer`: checks quality, risks, and missing tests.
- `orchestrator`: coordinates agent roles, tools, memory, and user-facing flow.

## Testing Strategy

- Unit tests cover domain rules and application use cases.
- Integration tests cover adapters such as MCP, GitHub, AI providers, and
  persistence with controlled fixtures or test doubles.
- End-to-end tests cover realistic agent workflows from an interface entry
  point.
