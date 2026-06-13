from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)

test_questions=[
    "What is the capital of France?",
    "Who discovered penicillin?",
    "What is the largest planet in our solar system?",
    "When was IIT Palakkad established?"
    ]


for q in test_questions:
    print(f"\nQuestion: {q}")

    response = llm.invoke([
        SystemMessage(
            content="You are a careful fact-checking assistant. If unsure, say you are unsure."
        ),
        HumanMessage(content=q)
    ])

    print("\nAnswer:")
    print(response.content)

