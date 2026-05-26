import os
import unittest
from unittest.mock import patch

from src.infrastructure.mcp.registry import MCP_SERVERS
from src.infrastructure.mcp.servers import MCP_BRASIL_SERVER, build_mcp_brasil_server


class McpBrasilConfigTests(unittest.TestCase):
    def test_registry_exposes_mcp_brasil_server(self):
        self.assertIs(MCP_SERVERS["mcp-brasil"], MCP_BRASIL_SERVER)
        self.assertEqual(MCP_BRASIL_SERVER.command, "uvx")
        self.assertEqual(
            MCP_BRASIL_SERVER.args,
            ("--from", "mcp-brasil", "python", "-m", "mcp_brasil.server"),
        )

    def test_mcp_brasil_server_keeps_only_configured_env_values(self):
        with patch.dict(
            os.environ,
            {
                "TRANSPARENCIA_API_KEY": "transparencia-token",
                "MCP_BRASIL_DATASETS": "tse_candidatos,tse_bens",
            },
            clear=False,
        ):
            server = build_mcp_brasil_server()

        self.assertEqual(server.env["TRANSPARENCIA_API_KEY"], "transparencia-token")
        self.assertEqual(server.env["MCP_BRASIL_DATASETS"], "tse_candidatos,tse_bens")
        self.assertNotIn("DATAJUD_API_KEY", server.env)

    def test_client_config_omits_empty_env(self):
        with patch.dict(os.environ, {}, clear=True):
            server = build_mcp_brasil_server()

        self.assertEqual(
            server.as_client_config(),
            {
                "command": "uvx",
                "args": ["--from", "mcp-brasil", "python", "-m", "mcp_brasil.server"],
            },
        )


if __name__ == "__main__":
    unittest.main()
