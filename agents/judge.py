from llm import llm
from state import DebateState

def judge(state:DebateState) -> DebateState:

    prompt = f"""
            Question:
            {state["question"]}

            Answer A:
            {state["answer_a"].answer}

            Confidence A:
            {state["answer_a"].confidence}

            Reasoning A:
            {state["answer_a"].reasoning}

            Answer B:
            {state["answer_b"].answer}

            Confidence B:
            {state["answer_b"].confidence}

            Reasoning B:
            {state["answer_b"].reasoning}

            Choose the better answer.
            """

    response = llm.invoke(prompt)

    return { "final_answer": response.content }