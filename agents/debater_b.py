from llm import llm
from state import DebateState

def debater_b(state: DebateState) -> DebateState:

    prompt = f"""
            You are Debater B.
            Try to find alternative interpretations.
            compared to Debater A.
            Question:
            {state['question']}
            """

    response = llm.invoke(prompt)

    return { "answer_b": response.content}