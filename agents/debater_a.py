from llm import llm
from state import DebateState

def debater_a(state: DebateState):

    prompt = f"""
                You are Debater A.
                Answer the question carefully.

                Question:
                {state['question']}
            """

    response = llm.invoke(prompt)
    
    return { "answer_a": response.content}