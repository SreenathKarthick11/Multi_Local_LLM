from llm import structured_llm
from state import DebateState

def debater_a(state: DebateState):

    prompt = f"""
                You are Debater A.
                Answer the question carefully.

                Question:
                {state['question']}
            """

    response = structured_llm.invoke(prompt)

    return { "answer_a": response }