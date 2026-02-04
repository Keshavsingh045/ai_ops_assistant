# AI Operations Assistant (GenAI Intern Assignment)

This project is a local AI Operations Assistant that takes a natural language task, plans steps using an LLM, executes tools via real APIs, and verifies the final output using a multi-agent architecture.

---

## Architecture Overview

The system follows a multi-agent design:

- **Planner Agent**
  - Converts user input into a structured execution plan (JSON)
  - Uses an LLM to decide which tools are required

- **Executor Agent**
  - Executes each step from the plan
  - Calls real third-party APIs (Weather API, OpenAI)

- **Verifier Agent**
  - Validates the executor output
  - Fixes missing or partial results
  - Provides a clean final response

---

## Integrated APIs

1. **OpenAI API**
   - Used by the Planner and Verifier agents for reasoning

2. **OpenWeatherMap API**
   - Used by the Weather tool to fetch real-time weather data

---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd ai_ops_assistant
