import os
import json

def call_llm(system_prompt: str, user_prompt: str):
    """
    Fallback LLM implementation.
    Returns a static plan when OpenAI quota is unavailable.
    """

    # Simple rule-based fallback
    if "weather" in user_prompt.lower():
        return json.dumps({
            "steps": [
                {
                    "tool": "weather",
                    "input": "Delhi"
                }
            ]
        })

    return json.dumps({
        "steps": []
    })
