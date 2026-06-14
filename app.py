from typing import TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph,START, END


class DebateState(TypedDict):
    question: str
    answer: str


llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)


def answer_node(state: DebateState) -> DebateState:
    response = llm.invoke(state["question"])
    state["answer"] = response.content

    return state


graph_builder = StateGraph(DebateState)

graph_builder.add_node("answer_node",answer_node)

graph_builder.add_edge(START,"answer_node")

graph_builder.add_edge("answer_node",END)

graph = graph_builder.compile()


result = graph.invoke(
    {
        "question": "What is the capital of France?"
    }
)

print(result)

print(graph.get_graph().draw_ascii())