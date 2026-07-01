import time

from rich.live import Live

from ui.console import console
from ui.renderer import Renderer

from core.debate_runner import start_debate


def main():

    renderer = Renderer()

    question = console.input(
        "\n[bold cyan]Question > [/bold cyan]"
    )

    worker = start_debate(question)

    with Live(
        renderer.get_layout(),
        console=console,
        refresh_per_second=20,
        screen=True,
    ):

        while worker.is_alive():

            renderer.process_events()

            time.sleep(0.05)

        # Flush remaining events

        renderer.process_events()

        time.sleep(0.2)

    console.print()

    console.print(
        "[bold green]Debate Finished.[/bold green]"
    )


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        console.clear()

        console.print(
            "[bold green]Goodbye![/bold green]"
        )