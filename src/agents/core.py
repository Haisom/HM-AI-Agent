from src.infrastructure.mcp.registry import TOOLS

def run_agent(user_input: str):
    if "time" in user_input.lower():
        tool = TOOLS["system_time"]
        return tool({})

    return {"error": "no tool matched"}
