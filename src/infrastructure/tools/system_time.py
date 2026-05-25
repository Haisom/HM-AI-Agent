from datetime import datetime

def run(_input: dict):
    now = datetime.now().strftime("%H:%M:%S")
    return {"result": now}