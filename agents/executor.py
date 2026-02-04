from tools.weather_tool import get_weather

def execute(plan: dict):
    results = []

    steps = plan.get("steps", [])
    for step in steps:
        tool = step.get("tool")
        user_input = step.get("input")

        if tool == "weather":
            weather_result = get_weather(user_input)
            results.append(weather_result)
        else:
            results.append({
                "error": f"Unknown tool: {tool}"
            })

    return results
