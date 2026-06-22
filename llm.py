from langchain_ollama import ChatOllama
from models import AgentResponse, CritiqueResponse,SearchDecision

# Base debate model
debate_base_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7,
)

debate_llm = debate_base_llm.with_structured_output(AgentResponse)

# Base critique model
critique_base_llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.3,
)

critique_llm = critique_base_llm.with_structured_output(CritiqueResponse)

# Judge remains normal text output
judge_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.2,
)

search_decision_llm = debate_base_llm.with_structured_output(
    SearchDecision
)