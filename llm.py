from langchain_ollama import ChatOllama
from models import AgentResponse

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)

structured_llm = llm.with_structured_output(AgentResponse)