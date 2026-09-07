from core.llm_client import get_llm, extract_text
from prompts.templates import OFFBOARDING_PROMPT


class OffboardingAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = OFFBOARDING_PROMPT | self.llm

    def run(self, query: str) -> str:
        response = self.chain.invoke({"query": query})
        return extract_text(response.content)
