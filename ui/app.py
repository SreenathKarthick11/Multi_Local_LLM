from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from time import sleep

from ui.console import console
from ui.layout import build_layout


def build_demo_resources():

    table = Table.grid(padding=1)

    table.add_row(
        "[bold yellow]Router[/]",
        "[green]✓[/] RAG"
    )

    table.add_row(
        "",
        "[red]✗[/] Web"
    )

    table.add_row(
        "",
        "[red]✗[/] Python"
    )

    table.add_row(
        "",
        ""
    )

    table.add_row(
        "[bold green]Retrieved[/]",
        "3 document chunks"
    )

    return Panel(
        table,
        title="Resources",
        border_style="green",
    )


def build_demo_debate():

    table = Table.grid(expand=True)

    table.add_column(ratio=1)
    table.add_column(ratio=1)

    table.add_row(
        "[bold blue]Agent A[/]\n"
        "Rome is the capital of Italy.",

        "[bold magenta]Agent B[/]\n"
        "I agree. Rome is correct."
    )

    return Panel(
        table,
        title="Debate",
        border_style="cyan",
    )


def build_demo_critique(title, colour):

    return Panel(

        "[green]✓[/] No hallucinations\n"
        "[green]✓[/] Good reasoning\n"
        "[yellow]![/] Could provide citations",

        title=title,
        border_style=colour,

    )


def build_demo_judge():

    return Panel(

        Align.center(

            "[bold green]Winner[/]\n\n"

            "Agent A\n\n"

            "Confidence : 0.95"

        ),

        title="Judge",
        border_style="red",

    )


def build_demo_stats():

    table = Table.grid(padding=1)

    table.add_row("Round", "2 / 3")
    table.add_row("Resources", "RAG")
    table.add_row("Runtime", "1.82 s")
    table.add_row("Search", "No")
    table.add_row("RAG", "Yes")

    return Panel(
        table,
        title="Runtime",
        border_style="bright_blue",
    )


def main():

    layout = build_layout()

    with Live(
        layout,
        console=console,
        screen=True,
        refresh_per_second=10,
    ):

        sleep(1)

        layout["resources"].update(
            build_demo_resources()
        )

        sleep(1)

        layout["debate"].update(
            build_demo_debate()
        )

        sleep(1)

        layout["critique_a"].update(
            build_demo_critique(
                "Critique A",
                "blue",
            )
        )

        layout["critique_b"].update(
            build_demo_critique(
                "Critique B",
                "magenta",
            )
        )

        sleep(1)

        layout["judge"].update(
            build_demo_judge()
        )

        layout["stats"].update(
            build_demo_stats()
        )

        while True:
            sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[green]Exited.[/green]")