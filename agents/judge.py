from llm import llm
from state import DebateState

def judge(state:DebateState) -> DebateState:

    prompt = f"""
                Question:
                {state['question']}

                Answer A:
                {state['answer_a']}

                Answer B:
                {state['answer_b']}

                Choose the better answer.

                Explain your reasoning.
                """

    response = llm.invoke(prompt)

    return { "final_answer": response.content }