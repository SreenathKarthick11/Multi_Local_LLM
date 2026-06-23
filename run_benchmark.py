from evaluation.evaluate import run_dataset

datasets = [
    "evaluation/dataset/factual.json",
    "evaluation/dataset/reasoning.json",
    "evaluation/dataset/ambiguity.json",
]

for dataset in datasets:
    print(f"\nRunning {dataset}\n")
    run_dataset(dataset)