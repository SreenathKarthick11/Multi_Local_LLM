import time

from rich.live import Live

from ui.console import console
from ui.renderer import Renderer


def main():

    renderer = Renderer()

    with Live(
        renderer.get_layout(),
        console=console,
        refresh_per_second=20,
        screen=True,
    ):

        while True:

            renderer.process_events()

            time.sleep(0.05)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        console.clear()

        console.print(
            "[bold green]Goodbye![/bold green]"
        )