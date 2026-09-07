import warnings
warnings.filterwarnings("ignore", module="langchain_google_genai")

from agents.chatbot_agent import ChatbotAgent
from agents.onboarding_agent import OnboardingAgent
from agents.offboarding_agent import OffboardingAgent
from agents.maintenance_agent import MaintenanceAgent

AGENTS = {
    "1": ("Chatbot Agent", ChatbotAgent()),
    "2": ("Onboarding Agent", OnboardingAgent()),
    "3": ("Offboarding Agent", OffboardingAgent()),
    "4": ("Maintenance Agent", MaintenanceAgent()),
}


def main():
    print("=== HR Multi-Agent System (Milestone 1 - Foundation) ===")
    while True:
        print("\nChoose an agent:")
        for key, (name, _) in AGENTS.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("\nAgent number: ").strip()
        if choice.lower() == "q":
            break
        if choice not in AGENTS:
            print("Invalid choice, try again.")
            continue

        name, agent = AGENTS[choice]
        query = input(f"[{name}] Your query: ")
        response = agent.run(query)
        print(f"\n[{name}] {response}")


if __name__ == "__main__":
    main()
