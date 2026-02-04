# AI Operations Assistant (GenAI Intern Assignment)

This project is a local AI Operations Assistant that takes a natural language task, plans steps using an LLM, executes tools via real APIs, and verifies the final output using a multi-agent architecture.

---

## Architecture Overview

The system follows a multi-agent design:

### Planner Agent
- Converts user input into a structured execution plan (JSON)
- Uses an LLM to decide which tools are required

### Executor Agent
- Executes each step from the plan
- Calls real third-party APIs

### Verifier Agent
- Validates executor output
- Fixes missing or partial results
- Produces the final clean response

---

## Project Structure

ai_ops_assistant/
│
├── agents/
│ ├── planner.py
│ ├── executor.py
│ └── verifier.py
│
├── tools/
│ └── weather_tool.py
│
├── llm/
│ └── openai_client.py
│
├── main.py
├── requirements.txt
├── .env.example
├── README.md


---

## Integrated APIs

1. OpenAI API  
   - Used by Planner and Verifier agents for reasoning

2. OpenWeatherMap API  
   - Used by Weather tool to fetch real-time weather data

---

## Setup Instructions (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai_ops_assistant.git
cd ai_ops_assistant


**2. Create and activate virtual environment**
       python -m venv venv
venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt


**4. Setup environment variables**

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key


**5. Run the project**
python main.py

**Example Prompts**

Try the following inputs:

Tell me the weather in Delhi

What is the weather in Mumbai?

Get current temperature for Bangalore

Check weather in New York

**Known Limitations / Tradeoffs**

Currently supports limited tools (weather only)

CLI-based interface (no UI)

LLM calls depend on API quota availability

Tool execution is sequential

**One Command Run**
python main.py


Author

Developed as part of GenAI Intern assignment submission.


---
