from core.llm_client import get_llm, extract_text
from prompts.templates import MAINTENANCE_PROMPT


class MaintenanceAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = MAINTENANCE_PROMPT | self.llm

    def run(self, query: str) -> str:
        response = self.chain.invoke({"query": query})
        return extract_text(response.content)
