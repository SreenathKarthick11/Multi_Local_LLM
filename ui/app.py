import time

from rich.live import Live

from ui.console import console
from ui.layout import demo_layout


def main():

    layout = demo_layout()

    with Live(
        layout,
        console=console,
        refresh_per_second=10,
        screen=True,
    ):

        while True:
            time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[green]Exited.[/green]")