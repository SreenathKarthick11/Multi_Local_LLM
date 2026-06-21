from evaluation.dataset import QUESTIONS
from evaluation.evaluator import single_agent_answer,debate_answer, is_correct

single_correct = 0
debate_correct = 0

for item in QUESTIONS:

    question = item["question"]
    expected = item["answer"]

    single = single_agent_answer(question)

    debate = debate_answer(question)

    if is_correct(single.answer, expected):
        single_correct += 1

    if is_correct(debate, expected):
        debate_correct += 1

    print()
    print("=" * 50)
    print(question)
    print()
    print("Expected:", expected)
    print("Single:", single.answer)
    print("Debate:", debate)

print()
print("Single Accuracy:",
      single_correct / len(QUESTIONS))

print("Debate Accuracy:",
      debate_correct / len(QUESTIONS))