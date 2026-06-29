from pprint import pprint

from graph import graph


def main():

    initial_state = {
        "question": input("Question: "),

        "round_number": 1,
        "max_rounds": 3,

        "search_used_a": False,
        "search_used_b": False,

        "resource_bank_a": [],
        "resource_bank_b": [],

        "history_a": [],
        "history_b": [],

        "critique_a": None,
        "critique_b": None,

        "judge_result": None,

        "stop_reason": None,
    }

    # Uncomment to visualize the graph
    # print(graph.get_graph().draw_ascii())

    result = graph.invoke(initial_state)

    print("\n===== FINAL STATE =====\n")
    pprint(result)


if __name__ == "__main__":
    main()