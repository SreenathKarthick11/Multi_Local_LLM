from graph import graph
from pprint import pprint

initial_state = {
    "question": input("Question: "),
    "answer_a": None,
    "answer_b": None,
    "final_answer": ""
}


# print(graph.get_graph().draw_ascii())

result = graph.invoke(initial_state)
print("\n===== FINAL STATE =====\n")
pprint(result)