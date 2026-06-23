from llm import evaluation_llm


def evaluate_answer(
    question: str,
    expected: str,
    predicted: str
):

    prompt = f"""
    Question:
    {question}

    Expected Answer:
    {expected}

    Predicted Answer:
    {predicted}

    Determine:

    1. Is the predicted answer correct?
    2. Give a quality score from 1-10.
    3. Explain briefly.

    Be tolerant of equivalent wording.
    """

    return evaluation_llm.invoke(prompt)