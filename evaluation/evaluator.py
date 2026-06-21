from llm import structured_llm
from graph import graph

def single_agent_answer(question):

    prompt = f"""
    Answer the question.

    Question:
    {question}
    """

    return structured_llm.invoke(prompt)

def debate_answer(question):

    initial_state = {
        "question": question,

        "answer_a": None,
        "answer_b": None,

        "critique_a": None,
        "critique_b": None,

        "revised_answer_a": None,
        "revised_answer_b": None,

        "final_answer": ""
    }

    result = graph.invoke(initial_state)

    return result["final_answer"]

def is_correct(prediction, ground_truth):

    prediction = prediction.lower()
    ground_truth = ground_truth.lower()

    return ground_truth in prediction