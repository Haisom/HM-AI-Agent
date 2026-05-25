from src.agent.core import run_agent

if __name__ == "__main__":
    while True:
        user_input = input("> ")
        result = run_agent(user_input)