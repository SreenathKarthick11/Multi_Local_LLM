from llm import structured_llm,llm
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

def critique_b(state: DebateState):

    prompt = f"""
            You are Debater B.

            Question:
            {state["question"]}

            Your Answer:
            {state["answer_b"].answer}

            Opponent Answer:
            {state["answer_a"].answer}

            Opponent Reasoning:
            {state["answer_a"].reasoning}

            Find weaknesses in the opponent's answer.
            """

    response = llm.invoke(prompt)

    return {
        "critique_b": response.content
    }

def revise_b(state:DebateState):

    prompt = f"""
        You are Debater B.

        Original Answer:
        {state["answer_b"].answer}

        Opponent Critique:
        {state["critique_a"]}

        Revise your answer if necessary.

        Return:
        - answer
        - confidence
        - reasoning
        """

    response = structured_llm.invoke(prompt)

    return {
        "revised_answer_b": response
    }