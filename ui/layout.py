from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align


def make_placeholder(title: str):
    return Panel(
        Align.center(
            "[grey62]Waiting...[/grey62]",
            vertical="middle",
        ),
        title=title,
        border_style="grey42",
    )


def build_layout():

    layout = Layout(name="root")

    # -------------------------------------------------------
    # Entire screen
    # -------------------------------------------------------

    layout.split_column(

        Layout(name="header", size=3),

        Layout(name="body"),

        Layout(name="footer", size=1),

    )

    # -------------------------------------------------------
    # Body
    # -------------------------------------------------------

    layout["body"].split_column(

        Layout(name="top", ratio=3),

        Layout(name="middle", ratio=2),

        Layout(name="bottom", ratio=1),

    )

    # -------------------------------------------------------
    # TOP
    #
    # Resources | Debate
    # -------------------------------------------------------

    layout["top"].split_row(

        Layout(name="resources", ratio=1),

        Layout(name="debate", ratio=2),

    )

    # -------------------------------------------------------
    # MIDDLE
    #
    # Critique A | Critique B
    # -------------------------------------------------------

    layout["middle"].split_row(

        Layout(name="critique_a"),

        Layout(name="critique_b"),

    )

    # -------------------------------------------------------
    # Bottom
    #
    # Judge | Stats
    # -------------------------------------------------------

    layout["bottom"].split_row(

        Layout(name="judge"),

        Layout(name="stats"),

    )

    # -------------------------------------------------------
    # Header
    # -------------------------------------------------------

    layout["header"].update(

        Panel(
            Align.center(
                "[bold cyan]Local LLM Multi-Agent Debate[/bold cyan]\n"
                "[grey62]Routing • RAG • Web • Tools • Debate[/grey62]"
            ),
            border_style="cyan",
        )

    )

    # -------------------------------------------------------
    # Footer
    # -------------------------------------------------------

    layout["footer"].update(

        Align.center(
            "[grey62]"
            "Press Ctrl+C to exit"
            "[/grey62]"
        )

    )

    # -------------------------------------------------------
    # Placeholders
    # -------------------------------------------------------

    layout["resources"].update(
        make_placeholder("Resources")
    )

    layout["debate"].update(
        make_placeholder("Debate")
    )

    layout["critique_a"].update(
        make_placeholder("Critique A")
    )

    layout["critique_b"].update(
        make_placeholder("Critique B")
    )

    layout["judge"].update(
        make_placeholder("Judge")
    )

    layout["stats"].update(
        make_placeholder("Stats")
    )

    return layout