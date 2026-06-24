import json
from graph import graph
import pandas as pd
from agents.evaluator import evaluate_answer

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

        winner = result["judge_result"].winner.lower()

        if "a" in winner:
            predicted = result["history_a"][-1].answer
        else:
            predicted = result["history_b"][-1].answer

        evaluation = evaluate_answer(
            question=sample["question"],
            expected=sample["answer"],
            predicted=predicted
        )

        results.append({
            "question": sample["question"],
            "search_used_a": result["search_used_a"],
            "search_used_b": result["search_used_b"],
            "expected": sample["answer"],

            "winner": winner,
            "predicted": predicted,

            "correct": evaluation.correct,
            "score": evaluation.score,

            "judge_reasoning":
                result["judge_result"].reasoning,

            "evaluation_reasoning":
                evaluation.reasoning
        })

    df = pd.DataFrame(results)

    accuracy = df["correct"].mean()
    average_score = df["score"].mean()

    print()
    print("=" * 50)
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Average Score: {average_score:.2f}")
    print("=" * 50)

    output_file = (path.split("/")[-1].replace(".json", "_results.csv"))

    df.to_csv(f"evaluation/results/{output_file}",index=False)

    return results


