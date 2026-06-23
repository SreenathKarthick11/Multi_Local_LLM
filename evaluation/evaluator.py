import json
from graph import graph
import pandas as pd

def run_dataset(path):

    with open(path) as f:
        dataset = json.load(f)

    results = []

    for sample in dataset:

        print(f"Running: {sample['question']}")

        state = {
            "question": sample["question"],
            "round_number": 1,
            "max_rounds": 3,

            "history_a": [],
            "history_b": [],

            "evidence_a": "",
            "evidence_b": "",

            "critique_a": None,
            "critique_b": None,

            "final_answer": None,
            "judge_result": None,
        }

        result = graph.invoke(state)

        results.append({
            "question": sample["question"],
            "expected": sample["answer"],
            "winner": result["judge_result"].winner,
            "judge_reasoning": result["judge_result"].reasoning,
            "answer_a": result["history_a"][-1].answer,
            "answer_b": result["history_b"][-1].answer,
        })

    df = pd.DataFrame(results)

    output_file = (
        path.split("/")[-1]
        .replace(".json", "_results.csv")
    )

    df.to_csv(
        f"evaluation/results/{output_file}",
        index=False
    )

    return results


