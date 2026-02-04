from agents.planner import create_plan
from agents.executor import execute
from agents.verifier import verify

def main():
    print("=== AI Operations Assistant ===")
    task = input("Enter your task: ")

    plan = create_plan(task)
    print("\n[Planner Output]")
    print(plan)

    result = execute(plan)
    print("\n[Executor Output]")
    print(result)

    final = verify(result)
    print("\n[Final Verified Output]")
    print(final)

if __name__ == "__main__":
    main()
