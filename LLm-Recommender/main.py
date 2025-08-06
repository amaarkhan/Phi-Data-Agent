from agent import get_llm_recommendation
from schema import UseCaseInput
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🤖 Welcome to the LLM Recommendation Agent!")
    use_case = input("Enter your use case (e.g., chat support, coding assistant, legal research): ")

    try:
        user_input = UseCaseInput(use_case=use_case)
    except Exception as e:
        print("❌ Invalid input:", e)
        return

    print("\n🔍 Finding the best LLMs for your use case...\n")

    recommendations = get_llm_recommendation(user_input.use_case)
    for i, model in enumerate(recommendations, 1):
        print(f"{i}. 🤖 {model.model_name}")
        print(f"   🏢 Provider: {model.provider}")
        print(f"   📄 Description: {model.description}\n")

if __name__ == "__main__":
    main()
