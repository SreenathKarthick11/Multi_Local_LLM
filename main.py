# main.py
import threading
import time

from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from ui.console import console
from ui.renderer import Renderer
from ui.emitter import emit
from ui.events import QuestionEvent
from ui.clock import start as start_clock
from ui.keyboard import init as kb_init, restore as kb_restore, read_key

from graph import graph


def run_debate(initial_state):
    graph.invoke(initial_state)


def build_initial_state(question):
    return {
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


def question_prompt_panel(buffer: str) -> Panel:
    return Panel(
        Text.assemble(
            ("Question: ", "bold white"),
            (buffer, "white"),
            ("▍", "bold white"),
        ),
        title="Type your question and press Enter",
        border_style="white",
    )


def main():
    renderer = Renderer()
    layout = renderer.get_layout()

    old_settings = kb_init()

    try:
        with Live(
            layout,
            console=console,
            refresh_per_second=20,
            screen=True,
        ):
            # -----------------------------------------------
            # Phase 1: collect the question inline
            # -----------------------------------------------
            buffer = ""
            layout["header"].update(question_prompt_panel(buffer))

            question = None

            while question is None:
                key = read_key()

                if key == "ENTER":
                    if buffer.strip():
                        question = buffer.strip()

                elif key == "BACKSPACE":
                    buffer = buffer[:-1]
                    layout["header"].update(question_prompt_panel(buffer))

                elif key is not None:
                    buffer += key
                    layout["header"].update(question_prompt_panel(buffer))

                time.sleep(0.02)

            # -----------------------------------------------
            # Phase 2: run the debate
            # -----------------------------------------------
            emit(QuestionEvent(question=question))
            start_clock()
            renderer.refresh()

            initial_state = build_initial_state(question)

            worker = threading.Thread(
                target=run_debate,
                args=(initial_state,),
                daemon=True,
            )
            worker.start()

            while worker.is_alive():
                renderer.process_events()
                time.sleep(0.05)

            for _ in range(20):
                renderer.process_events()
                time.sleep(0.05)

            layout["footer"].update(
                Text(
                    "Debate finished — press Ctrl+C to exit",
                    justify="center",
                    style="bold green",
                )
            )

            while True:
                renderer.process_events()   # harmless if queue stays empty
                time.sleep(0.1)

    finally:
        kb_restore(old_settings)

    console.print("[bold cyan]Debate finished.[/bold cyan]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[bold green]Goodbye![/bold green]")