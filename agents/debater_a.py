from llm import structured_llm,critique_llm
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

def critique_a(state: DebateState):

    prompt = f"""
            You are Debater A.

            Question:
            {state["question"]}

            Your Answer:
            {state["answer_a"].answer}

            Opponent Answer:
            {state["answer_b"].answer}

            Opponent Reasoning:
            {state["answer_b"].reasoning}

            Find weaknesses in the opponent's answer.

            Focus on:
            - factual errors
            - unsupported claims
            - weak reasoning

            Return concise issues.
            """

    response = critique_llm.invoke(prompt)

    return {
        "critique_a": response
    }

def revise_a(state:DebateState):

    prompt = f"""
        You are Debater A.

        Original Answer:
        {state["answer_a"].answer}

        Opponent Critique:
        - {"\n- ".join(state["critique_b"].issues)}

        Revise your answer if necessary.

        Return:
        - answer
        - confidence
        - reasoning
        """

    response = structured_llm.invoke(prompt)

    return {
        "revised_answer_a": response
    }