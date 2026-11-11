# main.py
import sys
import datetime
from agent import run_autonomous_loop

def main():
    query = "Compare the weather in Seattle and Boston. Do I need an umbrella?"
    print(f"Running Agent on Task: {query}\n")
    result = run_autonomous_loop(query)
    print(f"\nFinal Result:\n{result}")
    
    # Append tracking details to ledger file
    with open("agent_log.txt", "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] Query: {query}\nResult: {result}\n{'-'*40}\n")

if __name__ == "__main__":
    main()