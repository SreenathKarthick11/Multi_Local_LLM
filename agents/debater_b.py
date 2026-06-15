from llm import structured_llm
from state import DebateState

def debater_b(state: DebateState) -> DebateState:

    prompt = f"""
            You are Debater B.
            Try to consider alternative possibilities.
            Question:
            {state['question']}
            """

    response = structured_llm.invoke(prompt)

    return { "answer_b": response }