from langchain_ollama import ChatOllama
from models import AgentResponse

llm = ChatOllama(
    model="qwen2.5:3b",
    # base_url="https://unsaid-joylessly-remake.ngrok-free.dev",
    temperature=0.7
)

structured_llm = llm.with_structured_output(AgentResponse)