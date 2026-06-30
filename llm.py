from langchain_ollama import ChatOllama
from models import AgentResponse, CritiqueResponse, JudgeResponse
from models import EvaluationResponse, ResourceRoute

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
judge_base_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.2,
)

judge_llm = judge_base_llm.with_structured_output(JudgeResponse)

evaluation_llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
).with_structured_output(EvaluationResponse)


resource_router_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
).with_structured_output(ResourceRoute)