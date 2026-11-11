# agent.py
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import get_temperature_f, tool_definitions

load_dotenv()

# Point the client to GitHub's free models server
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
)

def run_autonomous_loop(query):
    messages = [
        {"role": "system", "content": "You are an action-oriented agent. Solve the task step-by-step using tools."},
        {"role": "user", "content": query}
    ]
    
    for step in range(3): 
        print(f"--- Agent Execution Loop Step {step+1} ---")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tool_definitions,
            tool_choice="auto"
        )
        message = response.choices[0].message
        messages.append(message)
        
        if message.tool_calls:
            for tool_call in message.tool_calls:
                args = json.loads(tool_call.function.arguments)
                tool_name = tool_call.function.name
                print(f"Executing local function: {tool_name} with {args}")
                
                if tool_name == "get_temperature_f":
                    observation = get_temperature_f(args.get("city"))
                    print(f"Tool Observation output: {observation}")
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_name,
                        "content": str(observation)
                    })
        else:
            return message.content
    return "Error: Max loops reached without output."