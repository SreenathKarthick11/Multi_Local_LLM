from llm import judge_llm
from state import DebateState

def judge(state:DebateState):

    prompt = f"""
        Question:
        {state["question"]}

        Answer A:
        {state["revised_answer_a"].answer}

        Reasoning A:
        {state["revised_answer_a"].reasoning}

        Answer B:
        {state["revised_answer_b"].answer}

        Reasoning B:
        {state["revised_answer_b"].reasoning}

        Choose the better answer.

        Explain why.
        Be concise.
        """

    response = judge_llm.invoke(prompt)

    return {
        "final_answer": response.content
    }