import json
from llm.openai_client import call_llm

def create_plan(task: str):
    system_prompt = (
        "You are a Planner Agent. "
        "Your job is to break the user task into clear steps and choose tools."
    )

    user_prompt = f"""
Return ONLY valid JSON in this exact format:

{{
  "steps": [
    {{
      "tool": "weather",
      "input": "Delhi"
    }}
  ]
}}

Task: {task}
"""

    response = call_llm(system_prompt, user_prompt)
    return json.loads(response)
