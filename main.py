# main.py
import threading
import time

from rich.live import Live

from ui.console import console
from ui.renderer import Renderer
from ui.emitter import emit
from ui.events import QuestionEvent
from ui.clock import start as start_clock

from graph import graph


def run_debate(initial_state):
    graph.invoke(initial_state)


def main():
    question = input("Question: ")

    initial_state = {
        "question": question,
        "round_number": 1,
        "max_rounds": 3,
        "search_used_a": False,
        "search_used_b": False,
        "rag_used_a": False,
        "rag_used_b": False,
        "resource_bank_a": [],
        "resource_bank_b": [],
        "history_a": [],
        "history_b": [],
        "critique_a": None,
        "critique_b": None,
        "judge_result": None,
        "stop_reason": None,
    }

    renderer = Renderer()

    emit(QuestionEvent(question=question))
    start_clock()

    worker = threading.Thread(target=run_debate, args=(initial_state,), daemon=True)

    with Live(
        renderer.get_layout(),
        console=console,
        refresh_per_second=20,
        screen=True,
    ):
        worker.start()

        while worker.is_alive():
            renderer.process_events()
            time.sleep(0.05)

        # drain any events still on the queue after the graph finishes
        for _ in range(20):
            renderer.process_events()
            time.sleep(0.05)

    console.print("[bold cyan]Debate finished.[/bold cyan]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[bold green]Goodbye![/bold green]")