from graph import graph
from pprint import pprint

initial_state = {
    "question": input("Question: "),

    "round_number": 1,
    "max_rounds": 3,

    "evidence_a": "",
    "evidence_b": "",

    # "answer_a": None,
    # "answer_b": None,

    "critique_a": None,
    "critique_b": None,

    # "revised_answer_a": None,
    # "revised_answer_b": None,

    "final_answer": ""
}


# print(graph.get_graph().draw_ascii())

result = graph.invoke(initial_state)
print("\n===== FINAL STATE =====\n")
pprint(result)