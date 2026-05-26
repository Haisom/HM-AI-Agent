from src.infrastructure.mcp.servers import MCP_SERVERS
from src.infrastructure.tools.system_time import run as system_time

TOOLS = {
    "system_time": system_time
}

__all__ = ["MCP_SERVERS", "TOOLS"]
