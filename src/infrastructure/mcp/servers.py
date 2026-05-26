from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Mapping


MCP_BRASIL_ENV_VARS = (
    "TRANSPARENCIA_API_KEY",
    "DATAJUD_API_KEY",
    "META_ACCESS_TOKEN",
    "MCP_BRASIL_TOOL_SEARCH",
    "MCP_BRASIL_HTTP_TIMEOUT",
    "MCP_BRASIL_HTTP_MAX_RETRIES",
    "MCP_BRASIL_DATASETS",
    "MCP_BRASIL_DATASET_CACHE_DIR",
    "MCP_BRASIL_DATASET_REFRESH",
    "MCP_BRASIL_DATASET_TIMEOUT",
    "MCP_BRASIL_LGPD_ALLOW_PII",
)


@dataclass(frozen=True)
class McpServerConfig:
    name: str
    command: str
    args: tuple[str, ...]
    env: Mapping[str, str] = field(default_factory=dict)

    def as_client_config(self) -> dict[str, object]:
        config: dict[str, object] = {
            "command": self.command,
            "args": list(self.args),
        }
        if self.env:
            config["env"] = dict(self.env)

        return config


def build_mcp_brasil_server() -> McpServerConfig:
    return McpServerConfig(
        name="mcp-brasil",
        command=os.getenv("MCP_BRASIL_COMMAND", "uvx"),
        args=(
            "--from",
            "mcp-brasil",
            "python",
            "-m",
            "mcp_brasil.server",
        ),
        env=_read_optional_env(MCP_BRASIL_ENV_VARS),
    )


def _read_optional_env(names: tuple[str, ...]) -> dict[str, str]:
    values: dict[str, str] = {}
    for name in names:
        value = os.getenv(name)
        if value:
            values[name] = value

    return values


MCP_BRASIL_SERVER = build_mcp_brasil_server()
MCP_SERVERS = {MCP_BRASIL_SERVER.name: MCP_BRASIL_SERVER}
