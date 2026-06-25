from llm import evaluation_llm


def evaluate_answer(question: str,expected: str,predicted: str):
    
    prompt = f"""
        You are evaluating an AI answer.

        Question:
        {question}

        Expected Answer:
        {expected}

        Predicted Answer:
        {predicted}

        Judge semantic correctness.

        The answer is correct if:

        - meaning matches
        - wording differs but meaning is equivalent
        - answer is more detailed but still correct

        The answer is incorrect if:

        - key facts are wrong
        - important information is missing
        - answer contradicts expected answer

        Return:

        - correct
        - score (1-10)
        - reasoning
        """

    return evaluation_llm.invoke(prompt)