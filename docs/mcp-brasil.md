# MCP Brasil Integration

This project integrates
[Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) as an
external MCP server. The upstream package exposes public Brazilian data sources
through MCP tools, resources, and prompts.

## Runtime

The project keeps the upstream server as a dependency instead of vendoring its
source code:

```bash
uv sync
```

For MCP clients that can launch stdio servers, use:

```bash
uvx --from mcp-brasil python -m mcp_brasil.server
```

The checked-in VS Code/Cursor config at `.vscode/mcp.json` uses the same
command.

## Optional Environment

Most upstream APIs work without keys. Configure optional credentials and runtime
settings in `.env` when needed:

```bash
TRANSPARENCIA_API_KEY=
DATAJUD_API_KEY=
META_ACCESS_TOKEN=
MCP_BRASIL_COMMAND=uvx
MCP_BRASIL_TOOL_SEARCH=bm25
MCP_BRASIL_DATASETS=
MCP_BRASIL_DATASET_CACHE_DIR=
```

Large local datasets are opt-in through `MCP_BRASIL_DATASETS` and should keep
their cache outside git, usually under `~/.cache/mcp-brasil` or a local
untracked data directory.

Before commercial, journalistic, or decision-making usage, review the upstream
license, source list, and acceptable use policy:

- [License](https://github.com/Mcp-Brasil/mcp-brasil/blob/main/LICENSE)
- [Sources](https://github.com/Mcp-Brasil/mcp-brasil/blob/main/SOURCES.md)
- [Acceptable Use](https://github.com/Mcp-Brasil/mcp-brasil/blob/main/ACCEPTABLE_USE.md)
