from graph import graph

initial_state = {
    "question": input("Question: "),
    "answer_a": "",
    "answer_b": "",
    "final_answer": ""
}


# print(graph.get_graph().draw_ascii())

result = graph.invoke(initial_state)
print("\n===== FINAL STATE =====\n")

print(result)